from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from exceptions import Impossible

from copy import deepcopy
from pydantic.utils import deep_update

import actions
import colour
import components.inventory
from components.npc_templates import BaseComponent
if TYPE_CHECKING:
    from components.gunparts import Parts
    from entity import Item, Actor
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
                 base_meat_damage,
                 base_armour_damage,
                 maximum_range: int,
                 base_accuracy: float,
                 equip_time: int,
                 range_accuracy_dropoff: Optional[float],
                 ranged: bool = False,
                 ):

        self.base_meat_damage = base_meat_damage
        self.base_armour_damage = base_armour_damage
        self.ranged = ranged  # if true, weapon has range (non-melee)
        self.maximum_range = maximum_range  # determines how far away the weapon can deal damage
        self.base_accuracy = base_accuracy  # decimal value, modifies base_chance_to_hit for a limb
        self.equip_time = equip_time
        self.range_accuracy_dropoff = range_accuracy_dropoff  # the range up to which the weapon is accurate

        if not self.ranged:
            self.maximum_range = 1

    def activate(self, action: actions.ItemAction):
        return NotImplementedError

    def attack(self, distance: int, target: Actor, attacker: Actor, part_index: int, hitchance: int):

        weapon_accuracy_type = attacker.fighter.melee_accuracy

        if self.ranged:
            weapon_accuracy_type = attacker.fighter.ranged_accuracy

        # successful hit
        if hitchance <= (float(target.bodyparts[part_index].base_chance_to_hit) * self.base_accuracy
                         * weapon_accuracy_type):

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

            if inventory.parent == self.engine.player:
                for i in range(self.equip_time):
                    self.engine.handle_enemy_turns()

            inventory.items.remove(entity)
            inventory.held = entity

    def unequip(self) -> None:

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):
            inventory.held = None
            inventory.items.append(entity)


class Bullet(Usable):

    def __init__(self,
                 parts,
                 bullet_type: str,
                 meat_damage: int,
                 armour_damage: int,
                 accuracy_factor: float,
                 recoil_modifier: float,  # reduces accuracy of followup automatic shots
                 sound_modifier: float,  # alters amount of noise the gun makes
                 ):

        self.parts = parts
        self.bullet_type = bullet_type
        self.meat_damage = meat_damage
        self.armour_damage = armour_damage
        self.accuracy_factor = accuracy_factor
        self.recoil_modifier = recoil_modifier
        self.sound_modifier = sound_modifier

    def activate(self, action: actions.ItemAction):
        return NotImplementedError


class Magazine(Usable):

    def __init__(self,
                 magazine_type: str,  # type of weapon this magazine works with i.e. glock 9mm
                 compatible_bullet_type: str,  # compatible bullet i.e. 9mm
                 mag_capacity: int,
                 magazine_size: str,  # small, medium or large
                 turns_to_load: int,  # amount of turns it takes to load magazine into gun
                 base_accuracy: float = 1.0,
                 ):
        self.magazine_type = magazine_type
        self.compatible_bullet_type = compatible_bullet_type
        self.mag_capacity = mag_capacity
        self.magazine_size = magazine_size
        self.turns_to_load = turns_to_load
        self.magazine = []
        self.base_accuracy = base_accuracy

    def activate(self, action: actions.ItemAction):
        return NotImplementedError

    def load_magazine(self, ammo, load_amount) -> None:
        # loads bullets into magazine

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if load_amount > ammo.stacking.stack_size or load_amount < 1:
                raise Impossible("Invalid entry.")

            # amount to be loaded is greater than no. of rounds available
            if load_amount > ammo.stacking.stack_size:
                load_amount = ammo.stacking.stack_size

            # amount to be loaded is greater than the magazine capacity
            if load_amount > self.mag_capacity - len(self.magazine):
                load_amount = self.mag_capacity - len(self.magazine)

            # 1 or more stack left in inventory after loading
            if ammo.stacking.stack_size - load_amount > 1:
                ammo.stacking.stack_size -= load_amount

            # no stacks left after loading
            elif ammo.stacking.stack_size - load_amount <= 0:
                if self.engine.player == entity:
                    inventory.items.remove(ammo)

            single_round = deepcopy(ammo)
            single_round.stacking.stack_size = 1

            for i in range(load_amount):
                self.magazine.append(single_round)
                if len(self.magazine) == \
                        self.mag_capacity:
                    break

            if self.engine.player == inventory.parent:
                for i in range(round(load_amount / 5)):
                    self.engine.handle_enemy_turns()

            if isinstance(self, GunIntegratedMag):
                self.chamber_round()

    def unload_magazine(self) -> None:
        # unloads bullets from magazine

        bullets_unloaded = []

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if isinstance(self, GunIntegratedMag):
                if not self.keep_round_chambered:
                    self.magazine.append(self.chambered_bullet)
                    setattr(self, "chambered_bullet", None)

            if len(self.magazine) > 0:
                for bullet in self.magazine:

                    if bullet not in bullets_unloaded:
                        bullets_unloaded.append(bullet)
                        bullet_counter = 0
                        for i in self.magazine:
                            if i.name == bullet.name:
                                bullet_counter += 1

                        bullet.stacking.stack_size = bullet_counter

                        actions.AddToInventory(item=bullet, amount=bullet_counter, entity=inventory.parent).perform()
                self.magazine = []

            else:
                return self.engine.message_log.add_message(f"{entity.name} is already empty", colour.RED)


class Gun(Weapon):
    def __init__(self,
                 parts: Parts,
                 base_meat_damage: float,
                 base_armour_damage: float,
                 base_accuracy: float,
                 range_accuracy_dropoff: float,
                 equip_time: int,
                 fire_modes: dict,  # fire rates in rpm
                 possible_parts: dict,
                 current_fire_mode: str,
                 keep_round_chambered: bool,
                 enemy_attack_range: int,  # range at which AI enemies will try to attack when using this weapon
                 sound_radius: float,  # radius at which enemies can 'hear' the shot
                 close_range_accuracy: float,
                 recoil: float,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 chambered_bullet=None,
                 ):

        self.parts = parts
        self.parts.parent = self
        self.possible_parts = possible_parts  # dict containing possible part options the gun is able to spawn with

        self.recoil = recoil
        self.chambered_bullet = chambered_bullet
        self.keep_round_chambered = keep_round_chambered
        self.fire_modes = fire_modes
        self.current_fire_mode = current_fire_mode
        self.enemy_attack_range = enemy_attack_range
        self.sound_radius = sound_radius
        self.fire_rate_modifier = fire_rate_modifier
        self.load_time_modifier = load_time_modifier
        self.close_range_accuracy = close_range_accuracy

        super().__init__(
            base_meat_damage=base_meat_damage,
            base_armour_damage=base_armour_damage,
            maximum_range=100,
            base_accuracy=base_accuracy,
            ranged=True,
            range_accuracy_dropoff=range_accuracy_dropoff,
            equip_time=equip_time
        )

    def attack(self, distance: int, target: Actor, attacker: Actor, part_index: int, hitchance: int):

        rounds_to_fire = round(self.fire_modes[self.current_fire_mode] / 60 * self.fire_rate_modifier)

        recoil_penalty = 0

        range_penalty = 0

        magazine_accuracy_factor = 1.0

        if isinstance(self, GunMagFed):
            if self.loaded_magazine is not None:
                magazine_accuracy_factor = self.loaded_magazine.usable_properties.base_accuracy

        # long range accuracy penalty
        if distance > self.range_accuracy_dropoff:
            range_penalty = distance - self.range_accuracy_dropoff

        # close range accuracy penalty
        functional_accuracy = self.base_accuracy
        if distance < 7:
            functional_accuracy = self.base_accuracy * self.close_range_accuracy

        # fires rounds
        while rounds_to_fire > 0:
            if self.chambered_bullet is not None:

                # successful hit
                if hitchance <= (float(target.bodyparts[part_index].base_chance_to_hit) * functional_accuracy *
                                 magazine_accuracy_factor *
                                 self.chambered_bullet.usable_properties.accuracy_factor
                                 * attacker.fighter.ranged_accuracy) - range_penalty - recoil_penalty:

                    # does damage to given bodypart
                    target.bodyparts[part_index].deal_damage(
                        meat_damage=self.base_meat_damage
                                    * self.chambered_bullet.usable_properties.meat_damage,
                        armour_damage=self.base_armour_damage
                                      * self.chambered_bullet.usable_properties.armour_damage,
                        attacker=attacker, item=self.parent)

                # miss
                else:
                    if attacker.player:
                        self.engine.message_log.add_message("Your shot misses.", colour.YELLOW)

                    else:
                        self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.LIGHT_BLUE)

                self.chambered_bullet = None

                self.chamber_round()

                rounds_to_fire -= 1

                if self.chambered_bullet is not None:
                    recoil_penalty += self.chambered_bullet.usable_properties.recoil_modifier

            else:
                if attacker.player:
                    self.engine.message_log.add_message(f"Out of ammo.", colour.RED)
                break

    def chamber_round(self):
        return NotImplementedError


class Wearable(Usable):
    def __init__(self, protection: int, fits_bodypart_type: str, small_mag_slots: int, medium_mag_slots: int,
                 large_mag_slots: int):
        self.protection = protection
        self.fits_bodypart = fits_bodypart_type  # bodypart types able to equip the item

        # how much of an item type the armour can carry
        self.small_mag_slots = small_mag_slots
        self.medium_mag_slots = medium_mag_slots
        self.large_mag_slots = large_mag_slots

    def activate(self, action: actions.ItemAction):
        return NotImplementedError

    def equip(self) -> None:

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):
            item_removed = False

            inventory.small_mag_capacity += self.small_mag_slots
            inventory.medium_mag_capacity += self.medium_mag_slots
            inventory.large_mag_capacity += self.large_mag_slots

            for bodypart in inventory.parent.bodyparts:
                if bodypart.part_type == self.fits_bodypart:

                    if bodypart.equipped is not None:
                        self.engine.message_log.add_message(f"You are already wearing something there.", colour.RED)

                    else:
                        if not item_removed:
                            inventory.items.remove(entity)
                            item_removed = True
                        bodypart.equipped = entity

            self.engine.handle_enemy_turns()

    def unequip(self) -> None:

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            inventory.small_mag_capacity -= self.small_mag_slots
            inventory.medium_mag_capacity -= self.medium_mag_slots
            inventory.large_mag_capacity -= self.large_mag_slots

            inventory.update_magazines()

            for bodypart in inventory.parent.bodyparts:
                if bodypart.part_type == self.fits_bodypart:
                    bodypart.equipped = None

            inventory.items.append(entity)

            self.engine.handle_enemy_turns()


class GunMagFed(Gun):
    def __init__(self,
                 parts: Parts,
                 compatible_magazine_type: str,
                 base_meat_damage: float,
                 base_armour_damage: float,
                 base_accuracy: float,
                 range_accuracy_dropoff: float,
                 equip_time: int,
                 fire_modes: dict,
                 current_fire_mode: str,
                 keep_round_chambered: bool,
                 enemy_attack_range: int,
                 sound_radius: float,
                 possible_parts: dict,
                 recoil: float,
                 close_range_accuracy: float,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 chambered_bullet=None,
                 loaded_magazine=None,
                 ):
        self.compatible_magazine_type = compatible_magazine_type
        self.loaded_magazine = loaded_magazine

        # for AIs to know what type of magazine to reload
        self.previously_loaded_magazine = loaded_magazine

        super().__init__(
            parts=parts,
            base_meat_damage=base_meat_damage,
            base_armour_damage=base_armour_damage,
            base_accuracy=base_accuracy,
            range_accuracy_dropoff=range_accuracy_dropoff,
            equip_time=equip_time,
            fire_modes=fire_modes,
            current_fire_mode=current_fire_mode,
            keep_round_chambered=keep_round_chambered,
            chambered_bullet=chambered_bullet,
            enemy_attack_range=enemy_attack_range,
            possible_parts=possible_parts,
            sound_radius=sound_radius,
            fire_rate_modifier=fire_rate_modifier,
            load_time_modifier=load_time_modifier,
            recoil=recoil,
            close_range_accuracy=close_range_accuracy,
        )

    def load_gun(self, magazine):

        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, components.inventory.Inventory):
            if self.loaded_magazine is not None:

                if not self.keep_round_chambered:
                    self.loaded_magazine.append(self.chambered_bullet)
                    self.chambered_bullet = None

                if inventory.parent == self.engine.player:
                    inventory.items.append(self.loaded_magazine)

                self.loaded_magazine = deepcopy(magazine)

            else:
                self.loaded_magazine = deepcopy(magazine)

            if inventory.parent == self.engine.player:
                inventory.items.remove(magazine)

            if len(self.loaded_magazine.usable_properties.magazine) > 0:
                if self.chambered_bullet is None:
                    self.chambered_bullet = self.loaded_magazine.usable_properties.magazine.pop()

            # takes appropriate amount of turns to load magazine into gun
            for i in range(round(magazine.usable_properties.turns_to_load * self.load_time_modifier)):
                self.engine.handle_enemy_turns()

    def unload_gun(self):

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if self.loaded_magazine is not None:

                if not self.keep_round_chambered:
                    self.loaded_magazine.append(self.chambered_bullet)
                    self.chambered_bullet = None

                inventory.items.append(self.loaded_magazine)
                self.loaded_magazine = None

            else:
                self.engine.message_log.add_message(f"{entity.name} has no magazine loaded", colour.RED)

    def unequip(self) -> None:
        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if self.loaded_magazine is not None:
                self.engine.player.inventory.remove_from_magazines(self.loaded_magazine)

            inventory.items.append(inventory.held)
            inventory.held = None

    def chamber_round(self):
        if self.loaded_magazine is not None:
            if len(self.loaded_magazine.usable_properties.magazine) > 0:
                self.chambered_bullet = self.loaded_magazine.usable_properties.magazine.pop()


class GunIntegratedMag(Gun, Magazine):
    def __init__(self,
                 parts: Parts,
                 base_meat_damage: float,
                 base_armour_damage: float,
                 base_accuracy: float,
                 range_accuracy_dropoff: float,
                 equip_time: int,
                 fire_modes: dict,
                 current_fire_mode: str,
                 compatible_bullet_type: str,
                 mag_capacity: int,
                 keep_round_chambered: bool,  # if when unloading gun the chambered round should stay
                 enemy_attack_range: int,
                 possible_parts: dict,
                 sound_radius: float,
                 recoil: float,
                 close_range_accuracy: float,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 chambered_bullet=None,
                 ):

        self.compatible_bullet_type = compatible_bullet_type
        self.mag_capacity = mag_capacity
        self.magazine = []

        self.previously_loaded_round = chambered_bullet

        super().__init__(
            parts=parts,
            base_meat_damage=base_meat_damage,
            base_armour_damage=base_armour_damage,
            base_accuracy=base_accuracy,
            range_accuracy_dropoff=range_accuracy_dropoff,
            equip_time=equip_time,
            fire_modes=fire_modes,
            current_fire_mode=current_fire_mode,
            keep_round_chambered=keep_round_chambered,
            chambered_bullet=chambered_bullet,
            enemy_attack_range=enemy_attack_range,
            possible_parts=possible_parts,
            sound_radius=sound_radius,
            fire_rate_modifier=fire_rate_modifier,
            load_time_modifier=load_time_modifier,
            recoil=recoil,
            close_range_accuracy=close_range_accuracy,
        )

    def chamber_round(self):
        if len(self.magazine) > 0:
            self.chambered_bullet = self.magazine.pop()


class ComponentPart(Usable):
    def __init__(self, part_type: str,
                 prerequisite_parts: tuple = (),
                 incompatible_parts: tuple = (),
                 compatible_items: tuple = (),
                 material: dict = None,
                 disassemblable=True,
                 **kwargs
                 ):
        self.disassemblable = disassemblable
        self.material = material
        self.part_type = part_type
        self.prerequisite_parts = prerequisite_parts
        self.incompatible_parts = incompatible_parts
        self.compatible_items = compatible_items
        self.__dict__.update(kwargs)

    def activate(self, action: actions.ItemAction):
        return NotImplementedError


class GunComponent(ComponentPart):
    def __init__(self,
                 part_type: str,
                 optics_mount_required: str = '',  # type of mount required for attachment of the optic
                 prerequisite_parts: tuple = (),
                 incompatible_parts: tuple = (),
                 compatible_items: tuple = (),
                 material: dict = None,
                 disassemblable=True,
                 prevents_suppression=False,
                 is_optic=False,
                 is_suppressor=False,
                 optics_mount_types: tuple = (),  # types of optics attachments compatible
                 accessory_attachment_underbarrel=False,  # whether the attachment is an underbarrel attachment point
                 accessory_attachment_sidemount=False,
                 is_underbarrel_attachment=False,  # whether the attachment is an underbarrel accessory
                 is_sidemount_attachment=False,
                 compatible_calibres: tuple = (),
                 **kwargs,
                 ):
        self.prevents_suppression = prevents_suppression
        self.is_optic = is_optic
        self.is_suppressor = is_suppressor
        self.accessory_attachment_underbarrel = accessory_attachment_underbarrel
        self.accessory_attachment_sidemount = accessory_attachment_sidemount
        self.is_underbarrel_attachment = is_underbarrel_attachment
        self.is_sidemount_attachment = is_sidemount_attachment
        self.compatible_calibres = compatible_calibres
        self.optics_mount_types = optics_mount_types

        if self.is_optic:
            self.optics_mount_required = optics_mount_required

        self.__dict__.update(kwargs)

        super().__init__(
            part_type=part_type,
            prerequisite_parts=prerequisite_parts,
            incompatible_parts=incompatible_parts,
            compatible_items=compatible_items,
            material=material,
            disassemblable=disassemblable
        )


class RecipeUnlock(Usable):

    def __init__(self, datapack: dict):
        self.datapack = datapack

    def activate(self, action: actions.ItemAction) -> None:

        self.engine.crafting_recipes = deep_update(self.engine.crafting_recipes, self.datapack)
        self.engine.message_log.add_message(
            f"Crafting recipes unlocked - {list(self.datapack.keys())[0]}",
            colour.GREEN,
        )

        self.consume()