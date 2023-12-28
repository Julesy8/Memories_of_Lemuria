from __future__ import annotations

from components.inventory import Inventory
from components.consumables import GunMagFed, GunIntegratedMag, Usable, GunComponent
from entity import Item


class Parts:

    parent: Usable

    def __init__(self):
        self.part_list = []
        self.attachment_dict = {}

        # I don't think below line does anything important - commented out for now
        # self.update_partlist(attachment_dict={})

        self.non_multiplicative_properties = ["barrel_length", "zero_range", "sight_height_above_bore",
                                              "receiver_height_above_bore", "muzzle_break_efficiency",
                                              "sight_spread_modifier"]

        self.additive_properties = ["receiver_height_above_bore"]

    def update_partlist(self, attachment_dict: dict):
        all_attributes = self.__dict__.values()
        self.attachment_dict = attachment_dict

        for attribute in all_attributes:
            if isinstance(attribute, Item):
                if isinstance(attribute.usable_properties, GunComponent):
                    self.part_list.append(attribute)

        self.update_gun_properties()

    def update_gun_properties(self):

        prefixes = ''
        suffixes = ''

        total_weight = 0

        grip_properties = None  # secondary weapon grip part GunComponent i.e. handguard, vertical grip
        optic_properties = None

        for part in self.part_list:

            # changes condition of the gun to reflect average of condition of the parts
            if part.usable_properties.functional_part:
                self.parent.condition_function = (part.usable_properties.condition_function +
                                                  self.parent.condition_function) / 2

            if part.usable_properties.accuracy_part:
                self.parent.condition_accuracy = (part.usable_properties.condition_accuracy +
                                                  self.parent.condition_function) / 2

            item = self.parent.parent

            total_weight += part.weight

            if isinstance(self.parent, GunMagFed):
                if hasattr(part.usable_properties, 'compatible_bullet_type') and hasattr(part.usable_properties,
                                                                                         'mag_capacity'):
                    self.parent = GunIntegratedMag(parts=self,
                                                   gun_type=self.parent.gun_type,
                                                   has_stock=self.parent.has_stock,
                                                   pdw_stock=self.parent.pdw_stock,
                                                   short_barrel=self.parent.short_barrel,
                                                   velocity_modifier=self.parent.velocity_modifier,
                                                   muzzle_break_efficiency=self.parent.muzzle_break_efficiency,
                                                   compatible_bullet_type=part.compatible_bullet_type,
                                                   current_fire_mode=self.parent.current_fire_mode,
                                                   ap_to_equip=self.parent.ap_to_equip,
                                                   mag_capacity=part.usable_properties.mag_capacity,
                                                   fire_modes=self.parent.fire_modes,
                                                   keep_round_chambered=self.parent.keep_round_chambered,
                                                   chambered_bullet=None,
                                                   fire_rate_modifier=self.parent.fire_rate_modifier,
                                                   load_time_modifier=self.parent.load_time_modifier,
                                                   felt_recoil=self.parent.felt_recoil,
                                                   sight_height_above_bore=self.parent.sight_height_above_bore,
                                                   sound_modifier=self.parent.sound_modifier,
                                                   zero_range=self.parent.zero_range,
                                                   ap_distance_cost_modifier=self.parent.ap_distance_cost_modifier,
                                                   receiver_height_above_bore=self.parent.receiver_height_above_bore,
                                                   sight_spread_modifier=self.parent.sight_spread_modifier,
                                                   handling_spread_modifier=self.parent.handling_spread_modifier,
                                                   projectile_spread_modifier=self.parent.projectile_spread_modifier,
                                                   target_acquisition_ap=self.parent.target_acquisition_ap,
                                                   firing_ap_cost=self.parent.firing_ap_cost,
                                                   condition_accuracy=self.parent.condition_accuracy,
                                                   condition_function=self.parent.condition_function,
                                                   compatible_clip=self.parent.compatible_clip,
                                                   barrel_length=self.parent.barrel_length
                                                   )

                    self.parent.parent = item
                    item.usable_properties = self.parent

            elif isinstance(self.parent, GunIntegratedMag):
                if hasattr(part.usable_properties, 'compatible_magazine_type'):
                    self.parent = GunMagFed(parts=self,
                                            gun_type=self.parent.gun_type,
                                            has_stock=self.parent.has_stock,
                                            pdw_stock=self.parent.pdw_stock,
                                            short_barrel=self.parent.short_barrel,
                                            velocity_modifier=self.parent.velocity_modifier,
                                            muzzle_break_efficiency=self.parent.muzzle_break_efficiency,
                                            current_fire_mode=self.parent.current_fire_mode,
                                            ap_to_equip=self.parent.ap_to_equip,
                                            fire_modes=self.parent.fire_modes,
                                            keep_round_chambered=self.parent.keep_round_chambered,
                                            compatible_magazine_type=part.usable_properties.compatible_magazine_type,
                                            chambered_bullet=None,
                                            compatible_bullet_type=self.parent.compatible_bullet_type,
                                            fire_rate_modifier=self.parent.fire_rate_modifier,
                                            load_time_modifier=self.parent.load_time_modifier,
                                            felt_recoil=self.parent.felt_recoil,
                                            sight_height_above_bore=self.parent.sight_height_above_bore,
                                            sound_modifier=self.parent.sound_modifier,
                                            zero_range=self.parent.zero_range,
                                            ap_distance_cost_modifier=self.parent.ap_distance_cost_modifier,
                                            receiver_height_above_bore=self.parent.receiver_height_above_bore,
                                            sight_spread_modifier=self.parent.sight_spread_modifier,
                                            handling_spread_modifier=self.parent.handling_spread_modifier,
                                            projectile_spread_modifier=self.parent.projectile_spread_modifier,
                                            target_acquisition_ap=self.parent.target_acquisition_ap,
                                            firing_ap_cost=self.parent.firing_ap_cost,
                                            condition_accuracy=self.parent.condition_accuracy,
                                            condition_function=self.parent.condition_function,
                                            compatible_clip=self.parent.compatible_clip,
                                            barrel_length=self.parent.barrel_length
                                            )

                    self.parent.parent = item
                    item.usable_properties = self.parent

            # updates the item weight to be the total weight of all parts added so far
            item.weight = total_weight
            
            if hasattr(part.usable_properties, 'weight_reduction'):
                total_weight -= part.usable_properties.weight_reduction

            # adds prefixes and suffixes
            if hasattr(part.usable_properties, 'prefix'):
                prefixes += f"{part.usable_properties.prefix}"
            if hasattr(part.usable_properties, 'suffix'):
                suffixes += f"{part.usable_properties.suffix}"

            # updates description
            if hasattr(part.usable_properties, 'description'):
                item.description = part.usable_properties.description

            # true if part is secondary gripping surface e.g. vertical grip or handguard
            if hasattr(part.usable_properties, 'grip_properties'):
                grip_properties = part.usable_properties.grip_properties

            if hasattr(part.usable_properties, 'optic_properties'):
                optic_properties = part.usable_properties.optic_properties

            # if current part is an optic, iterates through part list to find the part to which the optic is
            # currently attached. If found, updates the gun properties with that of the optic mount.
            if part.usable_properties.part_type == 'Optic':
                for x in self.part_list:
                    if hasattr(x.usable_properties, 'is_attachment_point_types'):

                        try:
                            if part in self.attachment_dict[x.name].values():
                                if hasattr(x.usable_properties, 'optic_mount_properties'):
                                    self.set_property(part_properties=x.usable_properties.optic_mount_properties)
                        except KeyError:
                            pass

            # if current part is an attachment adapter, finds out if optic attached and then iterates through part list
            # to find what it is currently attached to. If found, updates the gun properties with that of the optic
            # mount to which the adapter is attached
            if part.usable_properties.part_type == 'Attachment Adapter':
                optic_attached = False

                try:
                    for x in self.attachment_dict[part.name].values():
                        if x.usable_properties.part_type == 'Optic':
                            optic_attached = True
                            break

                except KeyError:
                    pass

                if optic_attached:
                    for x in self.part_list:
                        if hasattr(x.usable_properties, 'is_attachment_point_types'):

                            try:
                                if part in self.attachment_dict[x.name].values():
                                    if hasattr(x.usable_properties, 'optic_mount_properties'):
                                        self.set_property(part_properties=x.usable_properties.optic_mount_properties)
                            except KeyError:
                                pass

            # gives additional mag capacity if conferred by parts
            if (isinstance(self.parent, GunIntegratedMag) and
                    hasattr(part.usable_properties, 'additional_magazine_capacity')):
                self.parent.mag_capacity += part.usable_properties.additional_magazine_capacity

            # updates gun properties with that of the current part
            self.set_property(part_properties=part.usable_properties.__dict__)

        # gives item suitable prefixes and suffixes
        if not prefixes == '':
            self.parent.parent.name = f"{prefixes} {self.parent.parent.name}"
        if not suffixes == '':
            self.parent.parent.name = f"{self.parent.parent.name} {suffixes}"

        # sets appropriate properties given the weapon secondary grip
        if grip_properties is not None:
            self.set_property(part_properties=grip_properties)

        if optic_properties is not None:
            self.set_property(part_properties=optic_properties)

        # assigns type to weapon

        # if a gun was previously classified as a rifle, but now has a short barrel and PDW type stock, is now a PDW
        if self.parent.gun_type == 'rifle':
            if self.parent.short_barrel and self.parent.pdw_stock:
                self.parent.gun_type = 'pdw'

        elif self.parent.gun_type == 'pdw':
            # if gun was a PDW but now has a long barrel and stock, is now a rifle
            if not self.parent.short_barrel and not self.parent.pdw_stock:
                self.parent.gun_type = 'rifle'
            # if gun was a PDW but has a short barrel and no stock, is now a pistol
            if self.parent.short_barrel and not self.parent.has_stock:
                self.parent.gun_type = 'pistol'

        elif self.parent.gun_type == 'pistol':
            # if pistol has a stock is now a PDW
            if self.parent.has_stock:
                self.parent.gun_type = 'pdw'
            # if pistol has a long barrel is now a rifle
            if not self.parent.short_barrel:
                self.parent.gun_type = 'rifle'

    def set_property(self, part_properties: dict) -> None:

        # alters properties of the item according to part properties
        for property_str in part_properties.keys():
            if hasattr(self.parent, property_str):

                if property_str in self.non_multiplicative_properties:
                    # property is additive
                    if property_str in self.additive_properties:
                        gun_property = getattr(self.parent, property_str)
                        setattr(self.parent, property_str, (part_properties[property_str] + gun_property))
                    # property not additive but also not multiplicative, sets gun value to part value
                    else:
                        setattr(self.parent, property_str, part_properties[property_str])

                elif type(part_properties[property_str]) is float:
                    gun_property = getattr(self.parent, property_str)

                    if property_str == "velocity_modifier" or property_str == "projectile_spread_modifier":
                        gun_property['single projectile'] = (gun_property['single projectile'] *
                                                             part_properties[property_str])

                    else:

                        if type(gun_property) is int:
                            setattr(self.parent, property_str, round((part_properties[property_str] * gun_property), 2))
                        else:
                            setattr(self.parent, property_str, (part_properties[property_str] * gun_property))

                elif type(part_properties[property_str]) in (None, str, int, bool, tuple):
                    setattr(self.parent, property_str, part_properties[property_str])

                elif type(part_properties[property_str]) is dict:

                    if property_str == "velocity_modifier" or property_str == "projectile_spread_modifier":
                        gun_property = getattr(self.parent, property_str)

                        for round_type in part_properties[property_str].keys():
                            if round_type in gun_property:
                                gun_property[round_type] = gun_property[round_type] * \
                                                           part_properties[property_str][round_type]
                            else:
                                gun_property[round_type] = part_properties[property_str][round_type]

                    else:
                        new_dict = {**getattr(self.parent, property_str), **part_properties[property_str]}
                        setattr(self.parent, property_str, new_dict)

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
                    gun_item.usable_properties.unload_magazine(entity=entity)

                inventory.items.remove(gun_item)
