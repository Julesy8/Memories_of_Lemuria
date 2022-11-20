from __future__ import annotations

from components.inventory import Inventory
from components.consumables import GunMagFed, GunIntegratedMag, ComponentPart, Usable
from entity import Item


class Parts:

    parent: Usable

    def __init__(self):
        self.part_list = []
        self.update_partlist()

    def update_partlist(self):
        all_attributes = self.__dict__.values()

        for attribute in all_attributes:
            if isinstance(attribute, Item):
                if isinstance(attribute.usable_properties, ComponentPart):
                    self.part_list.append(attribute)

        self.update_gun_properties()

    def update_gun_properties(self):

        prefixes = ''
        suffixes = ''

        total_weight = 0  # total weight of all parts

        for part in self.part_list:

            item = self.parent.parent

            item.weight += part.weight

            if isinstance(self.parent, GunMagFed):
                if hasattr(part.usable_properties, 'compatible_bullet_type') and hasattr(part.usable_properties,
                                                                                         'mag_capacity'):
                    self.parent = GunIntegratedMag(parts=self,
                                                   velocity_modifier=self.parent.velocity_modifier,
                                                   muzzle_break_efficiency=self.parent.muzzle_break_efficiency,
                                                   compatible_bullet_type=part.compatible_bullet_type,
                                                   current_fire_mode=self.parent.current_fire_mode,
                                                   equip_time=self.parent.equip_time,
                                                   mag_capacity=part.usable_properties.mag_capacity,
                                                   fire_modes=self.parent.fire_modes,
                                                   keep_round_chambered=self.parent.keep_round_chambered,
                                                   chambered_bullet=None,
                                                   enemy_attack_range=self.parent.enemy_attack_range,
                                                   fire_rate_modifier=self.parent.fire_rate_modifier,
                                                   load_time_modifier=self.parent.load_time_modifier,
                                                   felt_recoil=self.parent.felt_recoil,
                                                   barrel_length=self.parent.barrel_length,
                                                   sight_height_above_bore=self.parent.sight_height_above_bore,
                                                   sound_modifier=self.parent.sound_modifier,
                                                   zero_range=self.parent.zero_range
                                                   )

                    self.parent.parent = item
                    item.usable_properties = self.parent

            elif isinstance(self.parent, GunIntegratedMag):
                if hasattr(part.usable_properties, 'compatible_magazine_type'):
                    self.parent = GunMagFed(parts=self,
                                            velocity_modifier=self.parent.velocity_modifier,
                                            muzzle_break_efficiency=self.parent.muzzle_break_efficiency,
                                            current_fire_mode=self.parent.current_fire_mode,
                                            equip_time=self.parent.equip_time,
                                            fire_modes=self.parent.fire_modes,
                                            keep_round_chambered=self.parent.keep_round_chambered,
                                            compatible_magazine_type=part.usable_properties.compatible_magazine_type,
                                            chambered_bullet=None,
                                            enemy_attack_range=self.parent.enemy_attack_range,
                                            compatible_bullet_type=self.parent.compatible_bullet_type,
                                            fire_rate_modifier=self.parent.fire_rate_modifier,
                                            load_time_modifier=self.parent.load_time_modifier,
                                            felt_recoil=self.parent.felt_recoil,
                                            barrel_length=self.parent.barrel_length,
                                            sight_height_above_bore=self.parent.sight_height_above_bore,
                                            sound_modifier=self.parent.sound_modifier,
                                            zero_range=self.parent.zero_range
                                            )

                    self.parent.parent = item
                    item.usable_properties = self.parent

            part_properties = part.usable_properties.__dict__

            # adds prefixes and suffixes
            if hasattr(part.usable_properties, 'prefix'):
                prefixes += f"{part.usable_properties.prefix}"
            if hasattr(part.usable_properties, 'suffix'):
                suffixes += f"{part.usable_properties.suffix}"

            # alters propeties of the item according to part properties
            for property_str in part_properties.keys():
                if hasattr(self.parent, property_str):

                    # TODO: make sure working as intended
                    non_multiplicative_properties = ["barrel_length", "zero_range", "sight_height_above_bore"]

                    additive_properties = ["sight_height_above_bore",]

                    if part_properties[property_str] in non_multiplicative_properties:
                        if part_properties[property_str] in additive_properties:
                            gun_property = getattr(self.parent, property_str)
                            setattr(self.parent, property_str, (part_properties[property_str] + gun_property))
                        else:
                            setattr(self.parent, property_str, part_properties[property_str])

                    elif type(part_properties[property_str]) is float:
                        gun_property = getattr(self.parent, property_str)
                        if type(gun_property) is int:
                            setattr(self.parent, property_str, round((part_properties[property_str] * gun_property), 2))
                        else:
                            setattr(self.parent, property_str, (part_properties[property_str] * gun_property))

                    elif type(part_properties[property_str]) in (None, str, int):
                        setattr(self.parent, property_str, part_properties[property_str])

                    elif type(part_properties[property_str]) is dict:
                        new_dict = {**getattr(self.parent, property_str), **part_properties[property_str]}
                        setattr(self.parent, property_str, new_dict)

        # gives item suitable prefixes and suffixes
        if not prefixes == '':
            self.parent.parent.name = f"{prefixes} {self.parent.parent.name}"
        if not suffixes == '':
            self.parent.parent.name = f"{self.parent.parent.name} {suffixes}"

    def disassemble(self, entity):

        gun_component = self.parent
        gun_item = gun_component.parent
        inventory = entity.inventory

        if isinstance(inventory, Inventory):
            if gun_item in inventory.items:
                for part in self.part_list:
                    inventory.items.append(part)

                if isinstance(gun_item.usable_properties, GunMagFed):
                    if gun_item.usable_properties.loaded_magazine is not None:
                        gun_item.usable_properties.unload_gun()

                elif isinstance(gun_item.usable_properties, GunIntegratedMag):
                    gun_item.usable_properties.unload_magazine()

                inventory.items.remove(gun_item)
