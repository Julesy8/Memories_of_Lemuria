from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from exceptions import Impossible

from copy import deepcopy

from random import randint
import actions
import colour
import components.inventory
from components.npc_templates import BaseComponent
if TYPE_CHECKING:
    from entity import Actor, Item
    from input_handlers import ActionOrHandler


class Usable(BaseComponent):

    parent: Item

    def get_action(self, user: Actor) -> Optional[ActionOrHandler]:
        """Try to return the action for this item."""
        return actions.ItemAction(user, self.parent)

    def activate(self, action: actions.ItemAction) -> None:
        """Invoke this items ability.

        `action` is the context for this activation.
        """
        raise NotImplementedError()

    def consume(self) -> None:
        """Remove the consumed item from its containing inventory."""
        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.remove(entity)


class HealingConsumable(Usable):

    def __init__(self, amount: int):
        self.amount = amount

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity

        for bodypart in consumer.bodyparts:
            bodypart.heal(self.amount)

        self.engine.message_log.add_message(
            f"You use the {self.parent.name}",
            colour.GREEN,
        )
        self.parent.stacking.stack_size -= 1
        if self.parent.stacking.stack_size <= 0:
            self.consume()


class Weapon(Usable):

    def __init__(self,
                 base_meat_damage: int,
                 base_armour_damage: int,
                 maximum_range: int,
                 base_accuracy: float,
                 range_accuracy_dropoff: Optional[int],
                 ranged: bool = False,
                 cutting: bool = False,
                 ):

        self.base_meat_damage = base_meat_damage
        self.base_armour_damage = base_armour_damage
        self.ranged = ranged  # if true, weapon has range (non-melee)
        self.maximum_range = maximum_range  # determines how far away the weapon can deal damage
        self.base_accuracy = base_accuracy  # decimal value, modifies base_chance_to_hit for a limb
        self.range_accuracy_dropoff = range_accuracy_dropoff  # the range up to which the weapon is accurate
        self.cutting = cutting  # whether the weapon can cleanly remove limbs

        if not self.ranged:
            self.maximum_range = 1

    def activate(self, action: actions.ItemAction):
        return NotImplementedError

    def attack(self, distance: int, target: Actor, attacker: Actor, part_index: int, hitchance: int):

        # successful hit
        if hitchance <= (float(target.bodyparts[part_index].base_chance_to_hit) * self.base_accuracy):

            # does damage to given bodypart
            target.bodyparts[part_index].deal_damage(
                meat_damage=self.base_meat_damage,
                armour_damage=self.base_armour_damage,
                attacker=attacker, item=self.parent)

        # miss
        else:
            if attacker.player:
                return self.engine.message_log.add_message("You miss", colour.YELLOW)

            else:
                return self.engine.message_log.add_message(f"{attacker.name} misses", colour.LIGHT_BLUE)

    def equip(self) -> None:

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.remove(entity)
            inventory.held = entity

    def unequip(self) -> None:

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.append(inventory.held)
            inventory.held = None


class Bullet(Usable):

    def __init__(self,
                 bullet_type: str,
                 meat_damage_factor: float,
                 armour_damage_factor: float,
                 accuracy_factor: float,
                 ):

        self.bullet_type = bullet_type
        self.meat_damage_factor = meat_damage_factor
        self.armour_damage_factor = armour_damage_factor
        self.accuracy_factor = accuracy_factor

    def activate(self, action: actions.ItemAction):
        return NotImplementedError


class Magazine(Usable):

    def __init__(self,
                 magazine_type: str,
                 compatible_bullet_type: str,
                 mag_capacity: int,
                 ):
        self.magazine_type = magazine_type
        self.compatible_bullet_type = compatible_bullet_type
        self.mag_capacity = mag_capacity
        self.magazine = []

    def activate(self, action: actions.ItemAction):
        return NotImplementedError

    def load_magazine(self, ammo, load_amount) -> None:
        # loads bullets into magazine

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if load_amount > ammo.stacking.stack_size:
                raise Impossible("Invalid entry.")

            # 1 or more stack left in inventory after loading
            elif ammo.stacking.stack_size - load_amount > 1:
                if ammo in inventory.items:
                    ammo.stacking.stack_size -= load_amount

            # no stacks left after loading
            elif ammo.stacking.stack_size - load_amount <= 0:
                if ammo in self.engine.player.inventory.items:
                    inventory.items.remove(ammo)

            rounds_loaded = 0

            single_round = deepcopy(ammo)
            single_round.stacking.stack_size = 1

            while rounds_loaded < load_amount:
                self.magazine.append(single_round)
                rounds_loaded += 1
                if len(self.magazine) == \
                        self.mag_capacity:
                    break

    def unload_magazine(self) -> None:
        # unloads bullets from magazine

        bullets_unloaded = []

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if len(self.magazine) > 0:
                for bullet in self.magazine:

                    if bullet in bullets_unloaded:
                        pass

                    else:
                        bullets_unloaded.append(bullet)
                        bullet_counter = 0
                        for i in self.magazine:
                            if i.name == bullet.name:
                                bullet_counter += 1

                        bullet.stacking.stack_size = bullet_counter

                        # if bullet of same type already in inventory, adds unloaded bullets to stack
                        bullet_type_in_inventory = False

                        for item in inventory.items:
                            if item.name == bullet.name:
                                item.stacking.stack_size += bullet.stacking.stack_size
                                bullet_type_in_inventory = True

                        # if no bullets of same type in inventory, adds to inventory
                        if not bullet_type_in_inventory:
                            inventory.items.append(bullet)

                self.magazine = []

            else:
                raise Impossible(f"{entity.name} is already empty")


class Gun(Weapon):

    def __init__(self,
                 compatible_magazine_type: str,
                 base_meat_damage: int,
                 base_armour_damage: int,
                 base_accuracy: float,
                 range_accuracy_dropoff: int,
                 chambered_bullet=None,
                 loaded_magazine=None,
                 ):

        self.compatible_magazine_type = compatible_magazine_type
        self.chambered_bullet = chambered_bullet
        self.loaded_magazine = loaded_magazine

        super().__init__(
            base_meat_damage=base_meat_damage,
            base_armour_damage=base_armour_damage,
            maximum_range=100,
            base_accuracy=base_accuracy,
            ranged=True,
            range_accuracy_dropoff=range_accuracy_dropoff,
        )

    def attack(self, distance: int, target: Actor, attacker: Actor, part_index: int, hitchance: int):

        if self.chambered_bullet is not None:

            range_penalty = 0

            if distance > self.range_accuracy_dropoff:
                range_penalty = distance - self.range_accuracy_dropoff

            # successful hit
            if hitchance <= (float(target.bodyparts[part_index].base_chance_to_hit) * self.base_accuracy) + \
                    range_penalty:

                # does damage to given bodypart
                target.bodyparts[part_index].deal_damage(
                    meat_damage=self.base_meat_damage,
                    armour_damage=self.base_armour_damage,
                    attacker=attacker, item=self.parent)

            # miss
            else:
                if attacker.player:
                    return self.engine.message_log.add_message("Your shot misses.", colour.YELLOW)

                else:
                    return self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.LIGHT_BLUE)

            self.chambered_bullet = None

            if self.loaded_magazine is not None:
                if len(self.loaded_magazine.usable_properties.magazine) > 0:
                    self.chambered_bullet = self.loaded_magazine.usable_properties.magazine.pop()

        else:
            return self.engine.message_log.add_message(f"Out of ammo.", colour.RED)

    def load_gun(self, magazine):

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):
            if self.loaded_magazine is not None:
                inventory.items.append(self.loaded_magazine)
                self.loaded_magazine = magazine

            else:
                self.loaded_magazine = magazine

            inventory.items.remove(magazine)

            if len(magazine.usable_properties.magazine) > 0:
                if self.chambered_bullet is None:
                    self.chambered_bullet = magazine.usable_properties.magazine.pop()

    def unload_gun(self):

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if self.loaded_magazine is not None:
                inventory.items.append(self.loaded_magazine)
                self.loaded_magazine = None

            else:
                raise Impossible(f"{entity.name} has no magazine loaded")


class Wearable(Usable):  # in future add different types of protection i.e. projectile + melee
    def __init__(self, protection: int, fits_bodypart_type: str):
        self.protection = protection
        self.fits_bodypart = fits_bodypart_type  # bodypart types able to equip the item

    def activate(self, action: actions.ItemAction):
        return NotImplementedError

    def equip(self) -> None:

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):
            item_removed = False

            for bodypart in inventory.parent.bodyparts:
                if bodypart.part_type == self.fits_bodypart:

                    if bodypart.equipped is not None:
                        raise Impossible(f"You are already wearing something there.")

                    else:
                        if not item_removed:
                            inventory.items.remove(entity)
                            item_removed = True
                        bodypart.equipped = entity

    def unequip(self) -> None:

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            for bodypart in inventory.parent.bodyparts:
                if bodypart.part_type == self.fits_bodypart:
                    bodypart.equipped = None

            if inventory.current_item_weight() + entity.weight > inventory.capacity:
                raise Impossible(f"Your inventory is full")

            else:
                inventory.items.append(entity)
