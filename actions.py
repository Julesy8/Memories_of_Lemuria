from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING
from random import randint

import colour
import exceptions

if TYPE_CHECKING:
    from engine import Engine
    from entity import Actor, Entity, Item


class Action:
    def __init__(self, entity: Actor) -> None:
        super().__init__()
        self.entity = entity

    @property
    def engine(self) -> Engine:
        """Return the engine this action belongs to."""
        return self.entity.gamemap.engine

    def perform(self) -> None:
        """Perform this action with the objects needed to determine its scope.

        `self.engine` is the scope this action is being performed in.

        `self.entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()


class WaitAction(Action):
    def perform(self) -> None:
        pass


class ChangeTarget(Action):
    # cycles through which body part is targeted by the player to attack
    def perform(self) -> None:
        index = self.entity.targeting.index(self.entity.selected_target)
        if index >= 3:
            self.entity.selected_target = self.entity.targeting[0]
        else:
            self.entity.selected_target = self.entity.targeting[index + 1]

        print('now targeting', self.entity.selected_target.lower())


class ActionWithDirection(Action):
    def __init__(self, entity: Actor, dx: int, dy: int):
        super().__init__(entity)

        self.dx = dx
        self.dy = dy

    @property
    def dest_xy(self) -> Tuple[int, int]:
        """Returns this actions destination."""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self) -> Optional[Entity]:
        """Return the blocking entity at this actions destination.."""
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination."""
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)

    def perform(self) -> None:
        raise NotImplementedError()


class MeleeAction(ActionWithDirection):
    def perform(self) -> None:
        target = self.target_actor
        if not target:
            raise exceptions.Impossible("Nothing to attack.")

        # body part selected by the entity
        targeted_bodypart = self.entity.selected_target

        # list of body parts able to be attacked by the entity
        targetable_bodyparts = []

        # if the entity attacking is has AI, randomly selects a bodypart to be targeted
        if not self.entity.player:
            targeted_by_enemy = randint(1, 10)
            if targeted_by_enemy <= 5:
                self.entity.selected_target = "Body"
            elif 5 < targeted_by_enemy <= 8:
                self.entity.selected_target = "Head"
            elif targeted_by_enemy == 9:
                self.entity.selected_target = "Arms"
            elif targeted_by_enemy == 10:
                self.entity.selected_target = "Legs"

        # finds viable bodyparts of the type specified by targeted_bodypart and appends them to targetable_bodyparts
        for bodypart in target.bodyparts:
            if bodypart.type == targeted_bodypart:
                targetable_bodyparts.append(bodypart)

        # if there are no viable bodyparts of this type, default to the body of the entity
        if len(targetable_bodyparts) == 0:
            for bodypart in target.bodyparts:
                if bodypart.type == "Body":
                    targetable_bodyparts.append(bodypart)

        # of the viable bodyparts in targetable_bodyparts, randomly selects one of them
        selected_bodypart = randint(0, len(targetable_bodyparts) - 1)
        part = targetable_bodyparts[selected_bodypart]
        part_index = target.bodyparts.index(targetable_bodyparts[selected_bodypart])

        if self.entity.player:
            attack_colour = colour.LIGHT_GREEN
        else:
            attack_colour = colour.LIGHT_RED

        # chance to hit calculation
        hitchance = randint(0, 100)
        if hitchance <= float(target.bodyparts[part_index].base_chance_to_hit) * self.entity.fighter.melee_accuracy:

            # calculates damage (system right now is placeholder) if successfully hits
            damage = self.entity.fighter.power - target.bodyparts[part_index].defence
            if damage > 0:
                # result printed to console
                self.engine.message_log.add_message(f"{self.entity.name} strikes {target.name} on the "
                                                    f"{part.name} for {str(damage)} points!", attack_colour)
                target.bodyparts[part_index].hp -= damage
            else:
                self.engine.message_log.add_message(f"{self.entity.name} strikes {target.name} on the "
                                                    f"{part.name} but does no damage!", attack_colour)

        # miss
        else:
            self.engine.message_log.add_message(f"{self.entity.name} tries to strike {target.name} on the "
                                                f"{part.name}, but misses!", attack_colour)


class MovementAction(ActionWithDirection):
    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            # Destination is out of bounds.
            raise exceptions.Impossible("That way is blocked.")

        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # Destination is blocked by a tile.
            raise exceptions.Impossible("That way is blocked.")

        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            # Destination is blocked by an entity.
            raise exceptions.Impossible("That way is blocked.")

        self.entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    def perform(self) -> None:
        if self.blocking_entity:
            return MeleeAction(self.entity, self.dx, self.dy).perform()

        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()


class PickupAction(Action):
    """Pickup an item and add it to the inventory, if there is room for it."""

    def __init__(self, entity: Actor):
        super().__init__(entity)

    def perform(self) -> None:
        actor_location_x = self.entity.x
        actor_location_y = self.entity.y
        inventory = self.entity.inventory

        for item in self.engine.game_map.items:
            if actor_location_x == item.x and actor_location_y == item.y:
                if len(inventory.items) >= inventory.capacity:
                    raise exceptions.Impossible("Your inventory is full.")

                self.engine.game_map.entities.remove(item)
                item.parent = self.entity.inventory
                inventory.items.append(item)

                self.engine.message_log.add_message(f"You picked up the {item.name}!")
                return

        raise exceptions.Impossible("There is nothing here to pick up.")


class ItemAction(Action):
    def __init__(
            self, entity: Actor, item: Item, target_xy: Optional[Tuple[int, int]] = None
    ):
        super().__init__(entity)
        self.item = item
        if not target_xy:
            target_xy = entity.x, entity.y
        self.target_xy = target_xy

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination."""
        return self.engine.game_map.get_actor_at_location(*self.target_xy)

    def perform(self) -> None:
        """Invoke the items ability, this action will be given to provide context."""
        self.item.consumable.activate(self)


class DropItem(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.drop(self.item)


class EquipWeapon(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.equip_weapon(self.item)


class UnequipWeapon(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.unequip_weapon(self.item)
