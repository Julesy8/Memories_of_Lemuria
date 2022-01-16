from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING
from random import randint
from copy import deepcopy

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


class TakeStairsAction(Action):
    def perform(self) -> None:
        """
        Take the stairs, if any exist at the entity's location.
        """
        if (self.entity.x, self.entity.y) == self.engine.game_map.downstairs_location:
            self.engine.game_map.generate_level()
        else:
            raise exceptions.Impossible("There is no way down from here")


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
            # hit
            if self.hitchance <= float(self.targeted_actor.bodyparts[self.part_index].base_chance_to_hit) * \
                    self.entity.fighter.melee_accuracy:

                self.targeted_actor.bodyparts[self.part_index].deal_damage(
                    meat_damage=self.entity.fighter.unarmed_meat_damage,
                    armour_damage=self.entity.fighter.unarmed_armour_damage,
                    attacker=self.entity)

            # miss
            else:
                if self.entity.player:
                    return self.engine.message_log.add_message("You miss the attack", colour.YELLOW)

                else:
                    return self.engine.message_log.add_message(f"{self.entity.name}'s attack misses", colour.LIGHT_BLUE)


class WeaponAttackAction(AttackAction):
    def __init__(self, distance: int, item: Optional[Item], entity: Actor, targeted_actor: Actor,
                 targeted_bodypart: Optional[Bodypart]):
        super().__init__(distance, entity, targeted_actor, targeted_bodypart)
        self.item = item

    def attack(self) -> None:
        self.perform()
        self.item.usable_properties.attack(distance=self.distance, target=self.targeted_actor, attacker=self.entity,
                                           part_index=self.part_index, hitchance=self.hitchance)


class MovementAction(ActionWithDirection):
    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            # Destination is out of bounds.
            raise exceptions.Impossible("Silent")

        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # Destination is blocked by a tile.
            raise exceptions.Impossible("Silent")

        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            # Destination is blocked by an entity.
            raise exceptions.Impossible("Silent")

        self.entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    def perform(self) -> None:
        if self.blocking_entity:

            item_held = self.engine.player.inventory.held

            if item_held is not None:
                return WeaponAttackAction(distance=1, item=item_held, entity=self.entity,
                                          targeted_actor=self.target_actor,
                                          targeted_bodypart=self.target_actor.bodyparts[0]).attack()

            else:
                return UnarmedAttackAction(distance=1, entity=self.entity, targeted_actor=self.target_actor,
                                           targeted_bodypart=self.target_actor.bodyparts[0]).attack()

        else:
            if self.entity.turn_counter >= self.entity.last_move_turn + self.entity.move_interval:
                self.entity.turn_counter += 1
                self.entity.last_move_turn = self.entity.turn_counter
                return MovementAction(self.entity, self.dx, self.dy).perform()
            else:
                self.entity.turn_counter += 1
                return WaitAction(self.entity).perform()


class PickupAction(Action):
    """Pickup an item and add it to the inventory, if there is room for it."""

    def __init__(self, entity: Actor, item: Item, pickup_amount: int):
        super().__init__(entity)
        self.item = item
        self.pickup_amount = pickup_amount

    def perform(self) -> None:

        stack_amount = 1

        item_copy = deepcopy(self.item)
        
        if self.item.stacking:
            if 0 < self.pickup_amount <= self.item.stacking.stack_size:
                stack_amount = self.pickup_amount
            else:
                stack_amount = self.item.stacking.stack_size

            item_copy.stacking.stack_size = stack_amount

        # weight check
        if self.entity.inventory.current_item_weight() + self.item.weight * stack_amount > \
                self.entity.inventory.capacity:
            raise exceptions.Impossible("Your inventory is full.")

        if self.item.stacking:

            # if item of this type already in inventory, tries to add it to existing stack
            try:
                for i in self.entity.inventory.items:
                    if i.name == self.item.name:
                        repeat_item_index = self.entity.inventory.items.index(i)
                self.entity.inventory.items[repeat_item_index].stacking.stack_size += item_copy.stacking.stack_size

            # item of this type not already present in inventory
            except UnboundLocalError:
                self.entity.inventory.items.append(item_copy)

            # removes item from map / reduces item on map stack size
            if self.item.stacking.stack_size - stack_amount > 0:
                self.item.stacking.stack_size -= stack_amount
            else:
                self.engine.game_map.entities.remove(self.item)

        # item not stacking
        else:
            self.entity.inventory.items.append(item_copy)
            self.engine.game_map.entities.remove(self.item)

        item_copy.parent = self.entity.inventory


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
        if self.item.usable_properties:  # test
            self.item.usable_properties.activate(self)
