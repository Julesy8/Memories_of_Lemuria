from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING
from random import randint

import colour
import exceptions

if TYPE_CHECKING:
    from engine import Engine
    from entity import Actor, Entity, Item
    from components.bodyparts import Bodypart


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


class AttackAction(Action):

    def __init__(self, distance: int, entity: Actor, targeted_actor: Actor, targeted_bodypart: Optional[Bodypart]):
        super().__init__(entity)

        self.targeted_actor = targeted_actor
        self.targeted_bodypart = targeted_bodypart
        self.distance = distance
        self.attack_colour = colour.LIGHT_RED
        self.hitchance = randint(0, 100)

        if self.targeted_bodypart:
            self.part_index = self.targeted_actor.bodyparts.index(self.targeted_bodypart)

        else:  # if no bodypart selected (should only be when entity is not player), sets value later
            self.part_index = None

    def perform(self) -> None:
        target = self.targeted_actor
        if not target:
            raise exceptions.Impossible("Nothing to attack.")

        if self.entity.player:
            self.attack_colour = colour.LIGHT_GREEN

        if not self.targeted_bodypart:
            self.part_index = randint(0, len(target.bodyparts) - 1)
            self.targeted_bodypart = target.bodyparts[self.part_index]

    def attack(self) -> None:
        # attack method to be replaced by specific attack methods
        raise NotImplementedError()


class UnarmedAttackAction(AttackAction):  # entity attacking without a weapon

    def attack(self) -> None:
        self.perform()

        if self.distance > 1:
            raise exceptions.Impossible("Enemy out of range")

        else:
            if self.hitchance <= float(self.targeted_actor.bodyparts[self.part_index].base_chance_to_hit) * \
                    self.entity.fighter.melee_accuracy:

                # if armour on the given part, value set for armour protection
                armour_protection = 0
                if self.targeted_actor.bodyparts[self.part_index].equipped:
                    armour_protection = self.targeted_actor.bodyparts[self.part_index].equipped.wearable.protection

                # calculates damage (system right now is placeholder) if successfully hits
                damage = self.entity.fighter.power - self.targeted_actor.bodyparts[self.part_index].defence - \
                         armour_protection

                # hit and did damage
                if damage > 0:
                    # result printed to console
                    self.engine.message_log.add_message(f"{self.entity.name} strikes {self.targeted_actor.name} on the "
                                                        f"{self.targeted_bodypart.name} for {str(damage)} points!",
                                                        self.attack_colour)
                    self.targeted_actor.bodyparts[self.part_index].hp -= damage

                # hit but dealt no damage
                else:
                    self.engine.message_log.add_message(f"{self.entity.name} strikes {self.targeted_actor.name} on the "
                                                        f"{self.targeted_bodypart.name} but does no damage!",
                                                        self.attack_colour)

            # miss
            else:
                self.engine.message_log.add_message(f"{self.entity.name} tries to strike {self.targeted_actor.name}"
                                                    f", but misses!", self.attack_colour)


class WeaponAttackAction(AttackAction):
    def __init__(self, distance: int, item: Optional[Item], entity: Actor, targeted_actor: Actor,
                 targeted_bodypart: Optional[Bodypart]):
        super().__init__(distance, entity, targeted_actor, targeted_bodypart)
        self.item = item

    def attack(self) -> None:
        self.perform()

        range_penalty = 0
        if self.item.weapon.ranged:
            # if weapon is ranged (not melee) and dist > ranged_accuracy calculates penalty
            if self.distance > self.item.weapon.ranged_accuracy:
                range_penalty = self.distance - (self.item.weapon.ranged_accuracy * 2)
        else:
            if self.distance > 1:
                raise exceptions.Impossible("Enemy out of range")

        # successful hit
        if self.hitchance <= (float(self.targeted_actor.bodyparts[self.part_index].base_chance_to_hit)
                              * self.item.weapon.base_accuracy) + range_penalty:

            # if armour on the given part, value set for armour protection
            armour_protection = 0
            if self.targeted_actor.bodyparts[self.part_index].equipped:
                armour_protection = self.targeted_actor.bodyparts[self.part_index].equipped.wearable.protection

            # calculates damage if successfully hits
            damage = self.item.weapon.power - self.targeted_actor.bodyparts[self.part_index].defence - armour_protection

            # attack dealt damage (melee)
            if not self.item.weapon.ranged and damage > 0:
                # result printed to console
                self.engine.message_log.add_message(f"{self.entity.name} strikes {self.targeted_actor.name} in the "
                                                    f"{self.targeted_bodypart.name} with the {self.item.name} for {str(damage)} "
                                                    f"points", self.attack_colour)
                self.targeted_actor.bodyparts[self.part_index].hp -= damage

            # attack dealt damage (ranged)
            elif damage > 0:
                self.engine.message_log.add_message(f"{self.item.name} projectile hits {self.targeted_actor.name} "
                                                    f"in the {self.targeted_bodypart.name} for {str(damage)} points",
                                                    self.attack_colour)
                self.targeted_actor.bodyparts[self.part_index].hp -= damage

            # attack hit but did no damage
            else:
                # ranged
                if self.item.weapon.ranged:
                    self.engine.message_log.add_message(f"{self.item.name} projectile hits {self.targeted_actor.name} "
                                                        f"in the {self.targeted_bodypart.name} but does no damage",
                                                        self.attack_colour)
                # melee
                else:
                    self.engine.message_log.add_message(f"{self.entity.name} strikes {self.targeted_actor.name} in the "
                                                        f"{self.targeted_bodypart.name} with the {self.item.name} but does no damage"
                                                        , self.attack_colour)

        # miss
        else:
            # ranged
            if self.item.weapon.ranged:
                self.engine.message_log.add_message(f"{self.entity.name} tries to shoot {self.targeted_actor.name} "
                                                    f"with {self.item.name} but misses", self.attack_colour)
            # melee
            else:
                self.engine.message_log.add_message(f"{self.entity.name} tries to strike {self.targeted_actor.name} "
                                                    f"with {self.item.name} but misses", self.attack_colour)


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
            if self.entity.inventory.held is not None and self.entity.inventory.held.weapon and not \
                    self.entity.inventory.held.weapon.ranged:
                return WeaponAttackAction(distance=1, item=self.entity.inventory.held, entity=self.entity,
                                          targeted_actor=self.target_actor,
                                          targeted_bodypart=self.target_actor.bodyparts[0]).attack()
            else:
                return UnarmedAttackAction(distance=1, entity=self.entity, targeted_actor=self.target_actor,
                                           targeted_bodypart=self.target_actor.bodyparts[0]).attack()

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
                if self.entity.inventory.current_item_weight() + item.weight > self.entity.inventory.capacity:
                    raise exceptions.Impossible("Your inventory is full.")

                self.engine.game_map.entities.remove(item)

                if item.stacking:
                    try:
                        for i in self.entity.inventory.items:
                            if i.name == item.name:
                                repeat_item_index = self.entity.inventory.items.index(i)
                        self.entity.inventory.items[repeat_item_index].stacking.stack_size += item.stacking.stack_size

                    except UnboundLocalError:
                        inventory.items.append(item)

                else:
                    inventory.items.append(item)

                item.parent = self.entity.inventory

                if item.stacking:
                    self.engine.message_log.add_message(f"You picked up the {item.name} ({item.stacking.stack_size})")
                else:
                    self.engine.message_log.add_message(f"You picked up the {item.name}")
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
        if self.item.consumable:  # test
            self.item.consumable.activate(self)
        if self.item.weapon:
            self.item.weapon.activate(self)


class DropItem(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.drop(self.item)


class EquipWeapon(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.equip_weapon(self.item)


class UnequipWeapon(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.unequip_weapon(self.item)


class EquipArmour(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.equip_armour(self.item)


class UnequipArmour(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.unequip_armour(self.item)


'''
class ShootWeapon(ItemAction):
    def perform(self) -> None:
        self.entity.inventory.held.weapon.activate
'''
