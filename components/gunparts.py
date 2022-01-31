from __future__ import annotations

from components.inventory import Inventory
from components.consumables import Gun, GunMagFed, GunIntegratedMag, GunComponent
from entity import Item


class GunParts:

    parent: Gun

    def __init__(self):

        self.part_list = []

    def update_partlist(self):
        all_attributes = self.__dict__.values()

        for attribute in all_attributes:
            if isinstance(attribute, Item):
                if isinstance(attribute.usable_properties, GunComponent):
                    self.part_list.append(attribute)

        self.update_gun_properties()

    def update_gun_properties(self):
        for part in self.part_list:

            if isinstance(self.parent, GunMagFed):

                if part.usable_properties.compatible_bullet_type is not None and part.usable_properties.mag_capacity\
                        is not None:

                    self.parent = GunIntegratedMag(parts=self,
                                                   base_meat_damage=self.parent.base_meat_damage,
                                                   base_armour_damage=self.parent.base_armour_damage,
                                                   base_accuracy=self.parent.base_accuracy,
                                                   compatible_bullet_type=part.compatible_bullet_type,
                                                   current_fire_mode=self.parent.current_fire_mode,
                                                   equip_time=self.parent.equip_time,
                                                   mag_capacity=part.mag_capacity,
                                                   fire_modes=self.parent.fire_modes,
                                                   keep_round_chambered=self.parent.keep_round_chambered,
                                                   range_accuracy_dropoff=self.parent.range_accuracy_dropoff,
                                                   chambered_bullet=None,
                                                   )

            elif isinstance(self.parent, GunIntegratedMag):

                if part.usable_properties.compatible_magazine_type is not None:
                    self.parent = GunMagFed(parts=self,
                                            base_meat_damage=self.parent.base_meat_damage,
                                            base_armour_damage=self.parent.base_armour_damage,
                                            base_accuracy=self.parent.base_accuracy,
                                            current_fire_mode=self.parent.current_fire_mode,
                                            equip_time=self.parent.equip_time,
                                            fire_modes=self.parent.fire_modes,
                                            keep_round_chambered=self.parent.keep_round_chambered,
                                            range_accuracy_dropoff=self.parent.range_accuracy_dropoff,
                                            compatible_magazine_type=part.compatible_magazine_type,
                                            chambered_bullet=None
                                            )

            part_properties = part.__dict__

            for property_str in part_properties.keys():
                if hasattr(self.parent, property_str):
                    if type(part_properties[property_str]) is float:
                        gun_property = getattr(self.parent, property_str)
                        setattr(self.parent, property_str, part_properties[property_str] * gun_property)
                    elif type(part_properties[property_str]) is str or type(part_properties[property_str]) is dict:
                        setattr(self.parent, property_str, part_properties[property_str])

    def disassemble(self):

        gun_component = self.parent
        entity = gun_component.parent
        inventory = entity.parent

        if isinstance(inventory, Inventory):
            if entity in inventory.items:
                for part in self.part_list:
                    inventory.items.append(part)
                inventory.items.remove(entity)
