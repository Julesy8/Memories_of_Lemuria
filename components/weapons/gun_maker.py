import components.weapons.glock17 as glock17
import components.weapons.ar15 as ar15
import components.weapons.kalashnikov as ak
import components.weapons.mac10 as m10
import components.weapons.sks as sks
import components.weapons.mosin as mosin
import components.weapons.m1911 as m1911
import components.weapons.m1_carbine as m1_carbine
import components.weapons.m14 as m14
import components.weapons.r870 as r870
import components.weapons.misc_guns as misc
import components.weapons.attachments as attachments
import components.weapons.gun_parts_weighted as gun_parts

import components.weapons.bullets as bullets
import components.weapons.magazines as magazines
from copy import deepcopy, copy
from random import choices, randint

from entity import Item

crafting_dict = {
    "Rifles": {
        "Mosin-Nagant 91/30": {
            "required parts": {
                "Mosin-Nagant Stock": 1,
                "Mosin-Nagant Barrel": 1,
            },
            "compatible parts": {
                "Attachment Adapter": 1,
                "Muzzle Adapter": 1,
                "Mosin-Nagant Accessory Mount": 1,
                "Muzzle Device": 1,
                "Optic": 1,
                "Side Mounted Accessory": 1,
            },
            "item": mosin.mosin_nagant
        },
        "SKS": {
            "required parts": {
                "SKS Barrel": 1,
                "SKS Stock": 1,
            },
            "compatible parts": {
                "SKS Internal Magazine": 1,
                "Attachment Adapter": 1,
                "SKS Optics Mount": 1,
                "Underbarrel Accessory": 1,
                "Side Mounted Accessory": 1,
                "Muzzle Device": 1,
                "Optic": 1
            },
            "item": sks.sks
        },
        "M1 Carbine": {
            "required parts": {
                "M1 Reciever": 1,
                "M1/M2 Stock": 1,
                "M1/M2 Barrel": 1,
            },
            "compatible parts": {
                "M1/M2 Carbine Optic Mount": 1,
                "Attachment Adapter": 1,
                "Muzzle Adapter": 1,
                "Side Mounted Accessory": 1,
                "Underbarrel Accessory": 1,
                "Muzzle Device": 1,
                "Optic": 1
            },
            "item": m1_carbine.m1_carbine
        },
        "M2 Carbine": {
            "required parts": {
                "M2 Reciever": 1,
                "M1/M2 Stock": 1,
                "M1/M2 Barrel": 1,
            },
            "compatible parts": {
                "M1/M2 Carbine Optic Mount": 1,
                "Attachment Adapter": 1,
                "Muzzle Adapter": 1,
                "Side Mounted Accessory": 1,
                "Underbarrel Accessory": 1,
                "Muzzle Device": 1,
                "Optic": 1
            },
            "item": m1_carbine.m2_carbine
        },
        "SVT-40": {
            "required parts": {
                "SVT Reciever": 1,
                "SVT Stock": 1,
            },
            "compatible parts": {
                "SVT Optics Mount": 1,
                "Optic": 1
            },
            "item": misc.svt
        },
        "M14": {
            "required parts": {
                "M14 - Reciever": 1,
                "M14/M1A Stock": 1,
                "M14/M1A Barrel": 1,
            },
            "compatible parts": {
                "M14/M1A Picatinny Rail Optic Mount": 1,
                "Attachment Adapter": 1,
                "Side Mounted Accessory": 1,
                "Underbarrel Accessory": 1,
                "Muzzle Device": 1,
                "Optic": 1
            },
            "item": m14.m14
        },
    },
    "Pistols": {
        "S&W Model 610": {
            "required parts": {
                "S&W 10mm Frame": 1,
                "S&W 10mm Frame Barrel": 1,
            },
            "compatible parts": {
                "S&W N-Frame Optic Mount": 1,
                "Optic": 1,
            },
            "item": misc.sw610
        },
        "S&W Model 629": {
            "required parts": {
                "S&W .44 Frame": 1,
                "S&W .44 Barrel": 1,
            },
            "compatible parts": {
                "S&W N-Frame Optic Mount": 1,
                "Optic": 1,
            },
            "item": misc.sw629
        },
        "TT-33": {
            "required parts": {
                "Tokarev TT Frame": 1,
                "Tokarev TT Barrel": 1,
                "Tokarev TT Slide": 1,
                "Tokarev TT-33 Grip Panels": 1,
            },
            "compatible parts": {
                "Optic": 1,
                "Muzzle Device": 1,
            },
            "item": misc.tt33
        },
        "Glock": {
            "Glock 17": {
                "required parts": {
                    "Glock Standard Frame": 1,
                    "Glock 17 Barrel": 1,
                    "G17 Slide": 1,
                },
                "compatible parts": {
                    "Glock Stock": 1,
                    "Muzzle Adapter": 1,
                    "Glock Optics Mount": 1,
                    "Glock Base Plate": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": glock17.glock_17
            },
            "Glock .40 S&W": {
                "required parts": {
                    "Glock Standard Frame": 1,
                    "Glock .40 S&W Barrel": 1,
                    "Glock .40 S&W Slide": 1,
                },
                "compatible parts": {
                    "Glock Stock": 1,
                    "Glock Optics Mount": 1,
                    "Glock Base Plate": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": glock17.glock_17
            },
            "Glock 10mm": {
                "required parts": {
                    "Glock 10mm Frame": 1,
                    "Glock 10mm Barrel": 1,
                    "Glock 10mm Slide": 1,
                },
                "compatible parts": {
                    "Muzzle Adapter": 1,
                    "Glock Base Plate": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": glock17.glock_17
            },
        },
        "M1911": {
            "required parts": {
                "M1911 Frame": 1,
                "M1911 Barrel": 1,
                "M1911 Slide": 1,
                "M1911 Grip Panels": 1,
            },
            "compatible parts": {
                "M1911 Optics Mount": 1,
                "Side Mounted Accessory": 1,
                "Underbarrel Accessory": 1,
                "Optic": 1,
                "Muzzle Device": 1,
            },
            "item": m1911.m1911
        },
        "Desert Eagle XIX": {
            "required parts": {
                "DE .44 Frame": 1,
                "DE .44 Barrel": 1,
                "DE .44 Slide": 1,
            },
            "compatible parts": {
                "Optic": 1,
                "Muzzle Device": 1,
            },
            "item": misc.de44
        },
    },
    "Submachine Guns": {
        "M3 Submachine Gun": {
            "required parts": {
                "M3 Reciever": 1,
                "M3 Barrel": 1,
            },
            "compatible parts": {
                "M3 Stock": 1,
                "Optic": 1,
                "Muzzle Device": 1,
            },
            "item": misc.m3_greasegun
        },
        "PPSh-41": {
            "required parts": {
                "PPSh Reciever": 1,
                "PPSh Barrel": 1,
                "PPSh Dust Cover": 1,
                "PPSh Stock": 1,
            },
            "compatible parts": {
                "Optic": 1
            },
            "item": misc.ppsh_41
        },
        "M10": {
            "required parts": {
                "M10 Lower": 1,
                "M10 Upper": 1,
            },
            "compatible parts": {
                "Stock Adapter M10": 1,
                "Attachment Adapter": 1,
                "Muzzle Adapter": 1,
                "M10 Stock": 1,
                "M10 Optics Mount": 1,
                "Muzzle Device": 1,
                "Accessory Adapter M10": 1,
                "Side Mounted Accessory": 1,
                "Underbarrel Accessory": 1,
                "Optic": 1
            },
            "item": m10.mac10
        },
    },
    "Assault Rifles": {
        "Kalashnikov": {
            "required parts": {
                "AK Reciever": 1,
                "AK Barrel": 1,
                "AK Handguard": 1,
                "AK Grip": 1,
            },
            "compatible parts": {
                "AK Stock": 1,
                "Attachment Adapter": 1,
                "Muzzle Adapter": 1,
                "AK Optics Mount": 1,
                "Side Mounted Accessory": 1,
                "Underbarrel Accessory": 1,
                "Muzzle Device": 1,
                "AK Magazine Adapter": 1,
                "Optic": 1
            },
            "item": ak.ak
        },
        "AR Pattern": {
            "required parts": {
                "AR Lower Receiver": 1,
                "AR Upper Receiver": 1,
                "AR Buffer Tube": 1,
                "AR Buffer": 1,
                "AR Barrel": 1,
                "AR Handguard": 1,
                "AR Grip": 1,
            },
            "compatible parts": {
                "AR Stock": 1,
                "Attachment Adapter": 1,
                "Muzzle Adapter": 1,
                "Front Sight": 1,
                "AR Optics Mount": 1,
                "Underbarrel Accessory": 1,
                "Side Mounted Accessory": 1,
                "Muzzle Device": 1,
                "Optic": 1
            },
            "item": ar15.ar15
        },
        "MCR": {
            "required parts": {
                "AR Lower Receiver": 1,
                "MCR Upper Receiver": 1,
                "AR Buffer Tube": 1,
                "AR Grip": 1,
            },
            "compatible parts": {
                "AR Stock": 1,
                "Attachment Adapter": 1,
                "Muzzle Adapter": 1,
                "Front Sight": 1,
                "Underbarrel Accessory": 1,
                "Side Mounted Accessory": 1,
                "Muzzle Device": 1,
                "Optic": 1
            },
            "item": ar15.fightlite_mcr
        },
    },
    "Shotguns": {
        "Winchester H015": {
            "required parts": {
                "H015 Reciever": 1,
                "H015 Barrel": 1,
                "H015 Stock": 1,
                "Model 870 Choke": 1,
            },
            "compatible parts": {
                "H015 Optic Mount": 1,
                "Optic": 1
            },
            "item": misc.singleshot
        },
        "Remington 870": {
            "required parts": {
                "Model 870 Reciever": 1,
                "Model 870 Barrel": 1,
                "Model 870 Stock": 1,
                "Model 870 Forend": 1,
                "Model 870 Choke": 1,
            },
            "compatible parts": {
                "Attachment Adapter": 1,
                "Model 870 Magazine Extension": 1,
                "Model 870 Optics Mount": 1,
                "Underbarrel Accessory": 1,
                "Side Mounted Accessory": 1,
                "Optic": 1
            },
            "item": r870.rem_870
        },
        "Remington 870 Super Shorty": {
            "required parts": {
                "Super Shorty Reciever": 1,
                "Model 870 Barrel": 1,
                "Model 870 Stock": 1,
                "Model 870 Choke": 1,
            },
            "compatible parts": {
                "Attachment Adapter": 1,
                "Model 870 Magazine Extension": 1,
                "Model 870 Optics Mount": 1,
                "Underbarrel Accessory": 1,
                "Side Mounted Accessory": 1,
                "Optic": 1
            },
            "item": r870.rem_870
        },
    },
}


class PremadeWeapon:
    def __init__(self, gun_item: Item, part_dict: dict, bullet, optics: dict, allowed_part_types: list,
                 magazine=None, name: str = '', clip=None):

        self.allowed_part_types = allowed_part_types
        self.gun_item = gun_item
        self.name = name
        self.part_dict = part_dict
        self.magazine = magazine
        self.optics = optics
        self.bullet = bullet
        self.clip = clip

    def update_properties(self, level: int, random_condition: bool = True) -> Item:

        optic_added = False
        prevent_suppression = False

        magazine_type = None

        compatible_parts = {}
        attachment_points = []

        # sets part values
        for part in self.part_dict.keys():

            if not part in self.allowed_part_types:
                continue

            # checks if current part selection is the same as the type as item in the prerequisite parts
            # if it is, only adds parts to options that are in prerequisites
            add_only_compatible = False
            for part_type in compatible_parts.keys():
                if part_type == part:
                    add_only_compatible = True
                    break

            # makes random part selection
            if isinstance(self.part_dict[part], dict):

                compatible_possible_parts = copy(self.part_dict[part])

                for x in self.part_dict[part]:

                    if x is None:
                        continue

                    # only prerequisite parts to be added
                    if add_only_compatible:
                        if x.name in compatible_parts[part]:
                            continue

                        has_compatible_tag = False

                        # makes list of all tags
                        tags = [x.usable_properties.part_type, ]

                        if hasattr(x.usable_properties, 'tags'):
                            tags.extend(getattr(x.usable_properties, 'tags'))

                        # checks if tags are compatible
                        for tag in tags:
                            if tag in compatible_parts[part]:
                                has_compatible_tag = True
                                break

                        if not has_compatible_tag:
                            del compatible_possible_parts[x]
                            continue

                    # checks if there is an attachment point compatible with the attachment
                    if hasattr(x.usable_properties, 'attachment_point_required'):
                        attachment_point = getattr(x.usable_properties, 'attachment_point_required')
                        if not any(item in attachment_point for item in attachment_points):
                            del compatible_possible_parts[x]
                            continue

                    # checks for incompatibilities
                    if hasattr(x.usable_properties, 'incompatibilities'):
                        all_parts = []
                        for value in self.part_dict.values():
                            if hasattr(value, 'tags'):
                                all_parts += value.tags
                        incompatibilities = getattr(x.usable_properties, 'incompatibilities')
                        for setups in incompatibilities:
                            for items in setups:
                                if all(item in all_parts for item in items):
                                    del compatible_possible_parts[x]
                                    continue

                    # checks suppressor compatibility
                    if x.usable_properties.is_suppressor:
                        if prevent_suppression:
                            del compatible_possible_parts[x]
                            continue

                # makes random selection from possible parts
                if compatible_possible_parts == {}:
                    selection = None
                else:
                    if isinstance(list(compatible_possible_parts.values())[0], tuple):
                        part_weights = []
                        for value in compatible_possible_parts.values():
                            try:
                                part_weights.append(value[level])
                            except IndexError:
                                part_weights.append(value[int(len(value + 1))])

                        selection = deepcopy(choices(population=list(compatible_possible_parts.keys()),
                                                     weights=part_weights, k=1)[0])
                    else:
                        selection = deepcopy(choices(population=list(compatible_possible_parts.keys()),
                                                     weights=list(compatible_possible_parts.values()), k=1)[0])
                if selection is not None:
                    setattr(self.gun_item.usable_properties.parts, part, selection)
                    self.part_dict[part] = selection
                else:
                    continue

            # ony one possible value for part, adds part to gun parts
            else:
                setattr(self.gun_item.usable_properties.parts, part, deepcopy(self.part_dict[part]))

            # find if part requires optic
            if not optic_added:
                if hasattr(self.part_dict[part].usable_properties, 'additional_required_parts'):
                    if 'Optic' in self.part_dict[part].usable_properties.additional_required_parts:
                        # constructs dictionary of compatible optics
                        compatible_optics = {}
                        for optic in self.optics.keys():
                            # checks if attachment point type in required attachment point
                            if any(attach_point in optic.usable_properties.attachment_point_required
                                   for attach_point in
                                   self.part_dict[part].usable_properties.is_attachment_point_types):
                                # adds to dictionary
                                compatible_optics[optic] = self.optics[optic]
                        # selects optic from dict
                        # print(compatible_optics.keys())
                        selection = choices(population=list(compatible_optics.keys()),
                                            weights=list(compatible_optics.values()), k=1)[0]
                        # sets part as optic
                        setattr(self.gun_item.usable_properties.parts, 'optic', deepcopy(selection))
                        # sets optic mount to part
                        self.gun_item.usable_properties.parts. \
                            set_property(self.part_dict[part].usable_properties.optic_mount_properties)
                        optic_added = True

            # updates the compatible parts dictionary
            if hasattr(self.part_dict[part].usable_properties, 'compatible_parts'):
                part_keys = self.part_dict[part].usable_properties.compatible_parts.keys()
                for key, value in compatible_parts.items():
                    if key in part_keys:
                        compatible_parts[key].extend(self.part_dict[part].usable_properties.compatible_parts[key])
                for key, value in self.part_dict[part].usable_properties.compatible_parts.items():
                    if key not in compatible_parts.keys():
                        compatible_parts[key] = self.part_dict[part].usable_properties.compatible_parts[key]

            # updates attachment points dictionary
            if hasattr(self.part_dict[part].usable_properties, 'is_attachment_point_types'):
                attachment_point_types = getattr(self.part_dict[part].usable_properties, 'is_attachment_point_types')
                attachment_points.extend(attachment_point_types)

            # checks if suppression prevented
            if self.part_dict[part].usable_properties.prevents_suppression:
                prevent_suppression = True

            # set parts condition
            if random_condition:
                if self.part_dict[part].usable_properties.functional_part:
                    self.part_dict[part].usable_properties.condition_function = randint(1, 5)

                if self.part_dict[part].usable_properties.accuracy_part:
                    self.part_dict[part].usable_properties.condition_accuracy = randint(1, 5)
            else:
                if self.part_dict[part].usable_properties.functional_part:
                    self.part_dict[part].usable_properties.condition_function = 5

                if self.part_dict[part].usable_properties.accuracy_part:
                    self.part_dict[part].usable_properties.condition_accuracy = 5

            # checks compatible magazine type
            if hasattr(self.part_dict[part].usable_properties, 'compatible_magazine_type'):
                magazine_type = self.part_dict[part].usable_properties.compatible_magazine_type

            # adds addition required parts to allowed_part_types
            if hasattr(self.part_dict[part].usable_properties, 'additional_required_parts'):
                for additional_part in self.part_dict[part].usable_properties.additional_required_parts:
                    if additional_part == "optic":
                        continue
                    else:
                        self.allowed_part_types.append(additional_part)

        # randomly selects magazine

        # updates gun properties
        self.gun_item.usable_properties.parts.update_partlist(attachment_dict={})

        # checks for magazine compatibility - may not be mag compatible, therefore not necessary to select

        if magazine_type is not None:

            if isinstance(self.magazine, dict):
                # constructs dictionary of compatible magazines
                compatible_magazines = copy(self.magazine)
                for magazine in self.magazine.keys():
                    if magazine.usable_properties.magazine_type not in magazine_type:
                        del compatible_magazines[magazine]

                # randomly selects magazine
                if isinstance(list(compatible_magazines.values())[0], tuple):
                    magazine_weights = []
                    for value in compatible_magazines.values():
                        try:
                            magazine_weights.append(value[level])
                        except IndexError:
                            magazine_weights.append(value[int(len(value + 1))])

                    magazine = choices(population=list(compatible_magazines.keys()),
                                       weights=magazine_weights, k=1)[0]
                    self.magazine = magazine.usable_properties

                else:
                    magazine = choices(population=list(compatible_magazines.keys()),
                                       weights=list(compatible_magazines.values()), k=1)[0]
                    self.magazine = magazine.usable_properties

            else:
                self.magazine = self.magazine.usable_properties

        else:
            self.magazine = self.gun_item.usable_properties

        # TODO - make it so can select correct bullet type given gun chambering
        if isinstance(self.bullet, dict):
            if isinstance(list(self.bullet.values())[0], tuple):
                bullet_weights = []
                for value in self.bullet.values():
                    try:
                        bullet_weights.append(value[level])
                    except IndexError:
                        bullet_weights.append(value[int(len(value + 1))])

                self.bullet = choices(population=list(self.bullet.keys()),
                                      weights=bullet_weights, k=1)[0]
            else:
                self.bullet = choices(population=list(self.bullet.keys()),
                                      weights=list(self.bullet.values()), k=1)[0]

        self.bullet.stacking.stack_size = 1

        # changes fire mode to full auto if available
        if 'automatic' in self.gun_item.usable_properties.fire_modes.keys():
            self.gun_item.usable_properties.current_fire_mode = 'automatic'

        # loads magazine with bullets
        bullets_to_load = [self.bullet.usable_properties] * self.magazine.mag_capacity
        self.magazine.magazine = bullets_to_load

        # sets magazine if gun has internal magazine
        if hasattr(self.gun_item.usable_properties, 'magazine'):
            self.gun_item.usable_properties.previously_loaded_round = deepcopy(self.bullet.usable_properties)

        # sets magazine if gun if magazine fed
        if hasattr(self.gun_item.usable_properties, 'loaded_magazine'):
            self.gun_item.usable_properties.loaded_magazine = self.magazine
            self.gun_item.usable_properties.previously_loaded_magazine = deepcopy(self.magazine)

        # sets chambered round
        self.gun_item.usable_properties.chambered_bullet = self.bullet.usable_properties

        # if not keep_round_chambered - i.e. gun is bolt action or open bolt, removes bullet from magazine
        if not self.gun_item.usable_properties.keep_round_chambered:
            self.magazine.magazine.pop()

        if self.clip is not None:
            self.gun_item.usable_properties.previously_loaded_clip = self.clip

        # sets gun name
        if not self.name == '':
            self.gun_item.name = self.name

        return self.gun_item


optics_test = {attachments.holosun503: 5, attachments.acog_ta01: 2, attachments.eotech_exps3: 3,
               attachments.aimpoint_comp: 10, attachments.kobra_ekp: 15, attachments.kobra_ekp_picrail: 15,
               attachments.amguh1: 5, attachments.compactprism: 5, attachments.pm2scope: 1, attachments.pso1: 1,
               attachments.okp7: 20, attachments.holosun_reflex: 1}

""" 
Glock
"""

g_17 = PremadeWeapon(gun_item=glock17.glock_17,
                     bullet=gun_parts.bullets_9mm_weighted,
                     optics=optics_test,
                     magazine={magazines.glock_mag_9mm: 100, magazines.glock_mag_9mm_33: 10,
                               magazines.glock_mag_9mm_50: 2, magazines.glock_mag_9mm_100: 1},
                     part_dict={
                         "Glock Standard Frame": glock17.glock17_frame,
                         "Glock 17 Barrel": {
                             glock17.glock17_barrel: 200,
                             glock17.glock17l_barrel: 10,
                             glock17.glock_9in_barrel: 3,
                             glock17.glock17_barrel_ported: 10,
                             glock17.glock17l_barrel_ported: 5,
                         },
                         "G17 Slide": {
                             glock17.glock17_slide: 100,
                             glock17.glock17l_slide: 100,
                             glock17.glock17_slide_optic: 20,
                             glock17.glock17l_slide_optic: 20,
                             glock17.glock17_slide_custom: 5,
                             glock17.glock17l_slide_custom: 5,
                         },
                         "Glock Stock": {None: 100, glock17.glock_stock: 2, glock17.glock_pistol_brace: 3},
                         "Glock Optics Mount": {None: 50, glock17.glock_pic_rail: 2},
                         "Glock Base Plate": {None: 50, glock17.glock_switch: 1},
                     },
                     allowed_part_types=['Glock Standard Frame', 'Glock 17 Barrel', 'G17 Slide', 'Glock Stock',
                                         'Muzzle Adapter', 'Glock Optics Mount', 'Glock Base Plate',
                                         'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
                     )

g_40sw = PremadeWeapon(gun_item=glock17.glock_17,
                       bullet=gun_parts.bullets_40sw_weighted,
                       optics=optics_test,
                       magazine={magazines.glock_mag_40: 100, magazines.glock_mag_40_22: 10,
                                 magazines.glock_mag_40_50: 2},
                       part_dict={
                           "Glock Standard Frame": glock17.glock17_frame,
                           "Glock .40 S&W Barrel": {
                               glock17.glock22_barrel: 100,
                               glock17.glock24_barrel: 10,
                               glock17.glock22_barrel_ported: 5,
                               glock17.glock24_barrel_ported: 2,
                           },
                           "Glock .40 S&W Slide": {
                               glock17.glock22_slide: 100,
                               glock17.glock24_barrel: 100,
                               glock17.glock22_slide_optic: 20,
                               glock17.glock24_slide_optic: 20,
                               glock17.glock22_slide_custom: 5,
                               glock17.glock24_slide_custom: 5,
                           },
                           "Glock Stock": {None: 50, glock17.glock_stock: 2, glock17.glock_pistol_brace: 3},
                           "Glock Optics Mount": {None: 50, glock17.glock_pic_rail: 2},
                           "Glock Base Plate": {None: 50, glock17.glock_switch: 1},
                       },
                       allowed_part_types=['Glock Standard Frame', 'Glock .40 S&W Barrel', 'Glock .40 S&W Slide',
                                           'Glock Stock',
                                           'Muzzle Adapter', 'Glock Optics Mount', 'Glock Base Plate',
                                           'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
                       )

g_10mm = PremadeWeapon(gun_item=glock17.glock_17,
                       bullet=gun_parts.bullets_10mm_weighted,
                       optics=optics_test,
                       magazine={magazines.glock_mag_10mm: 100, magazines.glock_mag_10mm_33: 7,
                                 magazines.glock_mag_10mm_50: 2},
                       part_dict={
                           "Glock 10mm Frame": glock17.glock17_frame,
                           "Glock 10mm Barrel": {
                               glock17.glock20_barrel: 100,
                               glock17.glock40_barrel: 10,
                               glock17.glock20_barrel_ported: 5,
                               glock17.glock40_barrel_ported: 2,
                           },
                           "Glock 10mm Slide": {
                               glock17.glock20_slide: 100,
                               glock17.glock40_slide: 100,
                               glock17.glock20_slide_optic: 20,
                               glock17.glock40_slide_optic: 20,
                               glock17.glock20_slide_custom: 5,
                               glock17.glock40_slide_custom: 5,
                           },
                           "Glock Stock": {None: 20, glock17.glock_brace_rt: 1},
                           "Glock Base Plate": {None: 50, glock17.glock_switch: 1},
                       },
                       allowed_part_types=['Glock 10mm Frame', 'Glock 10mm Barrel', 'Glock 10mm Slide',
                                           'Glock Stock',
                                           'Muzzle Adapter', 'Glock Base Plate',
                                           'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
                       )

g_50gi = PremadeWeapon(gun_item=glock17.glock_17,
                       bullet=gun_parts.bullets_50gi_weighted,
                       optics=optics_test,
                       magazine=magazines.glock_mag_50gi,
                       part_dict={
                           "Glock 10mm Frame": glock17.glock20_frame,
                           "Glock .50 GI Barrel": glock17.glock50_barrel,
                           "Glock .50 GI Slide": {
                               glock17.glock50_slide: 100,
                               glock17.glock50_slide_optic: 10,
                               glock17.glock50_slide_custom: 1,
                           },
                           "Glock Stock": {None: 20, glock17.glock_brace_rt: 1},
                           "Glock Base Plate": {None: 20, glock17.glock_switch: 1},
                       },
                       allowed_part_types=['Glock 10mm Frame', 'Glock .50 GI Barrel', 'Glock .50 GI Slide',
                                           'Glock Stock',
                                           'Muzzle Adapter', 'Glock Base Plate',
                                           'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
                       )

"""
AR
"""

ar_optics = {**optics_test, **{ar15.ar_carry_handle: 100, attachments.irons_troy_rear: 30,
                               attachments.irons_dd_rear: 20, attachments.irons_magpul_rear: 50,
                               attachments.irons_sig_rear: 10}}

ar15_weapon_300 = PremadeWeapon(gun_item=ar15.ar15,
                                bullet=gun_parts.bullets_300aac_weighted,
                                magazine={
                                    magazines.stanag_10rd: (100, 100, 0, 0, 0),
                                    magazines.stanag_20rd: (10, 10, 200, 0, 0),
                                    magazines.stanag_30rd: (5, 5, 100, 200, 200),
                                    magazines.stanag_40rd: (0, 1, 10, 10, 10),
                                    magazines.stanag_50rd: (0, 0, 3, 3, 5),
                                    magazines.stanag_60rd: (0, 0, 1, 2, 4),
                                    magazines.stanag_100rd: (0, 0, 0, 1, 2),
                                },
                                optics=ar_optics,
                                part_dict={
                                    "AR Lower Receiver": {ar15.lower_ar15: (1, 100, 10, 10, 1, 0),
                                                          ar15.lower_ar15_auto: (0, 3, 1, 3, 1, 1)},
                                    "AR Upper Receiver": {ar15.upper_ar_m16a2: 10,
                                                          ar15.upper_ar_m16a4: 1},
                                    "AR Buffer Tube": ar15.ar15_buffer_tube,
                                    "AR Buffer": {ar15.ar15_buffer: 40,
                                                  ar15.ar15_buffer_heavy: 2,
                                                  ar15.ar15_buffer_light: 1},
                                    "AR Barrel": {
                                        ar15.ar_barrel_carbine_300: 10,
                                        ar15.ar_barrel_carbine_300_carbinelen: 10,
                                        ar15.ar_barrel_pistol_300: 1,
                                        ar15.ar_barrel_pistol_300_pistollen: 1,
                                    },
                                    "AR Handguard": {
                                        ar15.ar_handguard_m16a1: 10,
                                        ar15.ar_handguard_m16a2: 100,
                                        ar15.ar_handguard_m16a2_carbine: 100,
                                        ar15.ar_handguard_magpul: 75,
                                        ar15.ar_handguard_magpul_carbine: 75,
                                        ar15.ar_handguard_aero: 25,
                                        ar15.ar_handguard_aero_carbine: 25,
                                        ar15.ar_handguard_aero_pistol: 10,
                                        ar15.ar_handguard_faxon: 15,
                                        ar15.ar_handguard_faxon_carbine: 15,
                                        ar15.ar_handguard_faxon_pistol: 5,
                                        ar15.ar_handguard_mk18: 15,
                                    },
                                    "AR Grip": {
                                        ar15.ar_grip_trybe: 15,
                                        ar15.ar_grip_moe: 90,
                                        ar15.ar_grip_hogue: 5,
                                        ar15.ar_grip_strikeforce: 10,
                                        ar15.ar_grip_a2: 100,
                                        ar15.ar_grip_stark: 15,
                                    },
                                    "AR Stock": {
                                        None: 5,
                                        ar15.ar_stock_m16a2: 100,
                                        ar15.ar_stock_moe: 90,
                                        ar15.ar_stock_ubr: 10,
                                        ar15.ar_stock_danieldefense: 15,
                                        ar15.ar_stock_prs: 5,
                                        ar15.ar_stock_maxim_cqb: 5,
                                    },
                                    "AR Optics Mount": {None: 20, ar15.carry_handle_optic_mount: 1},
                                    "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                                    attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                                    attachments.irons_sig_front: 10, },
                                    "Muzzle Device": {
                                        ar15.ar15_300_muzzle_flashhider: 100,
                                        ar15.ar15_300_muzzle_cobra: 8,
                                        ar15.ar15_300_muzzle_pegasus: 5,
                                        ar15.ar15_300_muzzle_strike: 3,
                                        attachments.suppressor_sandman: 1,
                                    },
                                    "Attachment Adapter": {None: 20,
                                                           attachments.adapter_mlok_picrail: 1,
                                                           attachments.adapter_mlok_picrail_short: 1},
                                    "Underbarrel Accessory": {
                                        None: 500,
                                        attachments.grip_hera_cqr: 3,
                                        attachments.grip_promag_vertical: 10,
                                        attachments.grip_jem_vertical: 10,
                                        attachments.grip_magpul_angled: 6,
                                        attachments.grip_magpul_mvg: 8,
                                        attachments.grip_aimtac_short: 7,
                                        attachments.grip_magpul_handstop: 6,
                                        attachments.grip_hipoint_folding: 3,
                                    },
                                },
                                allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
                                                    'AR Buffer', 'AR Barrel',
                                                    'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
                                                    'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
                                                    'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
                                                    'Optic']
                                )

ar10_weapon = PremadeWeapon(gun_item=ar15.ar15,
                            bullet=gun_parts.bullets_308_weighted,
                            magazine={
                                magazines.ar10_10rd: (100, 100, 0, 0, 0),
                                magazines.ar10_20rd: (5, 5, 100, 200, 200),
                                magazines.ar10_25rd: (0, 1, 10, 10, 10),
                                magazines.ar10_40rd: (0, 0, 1, 2, 4),
                                magazines.ar10_50rd: (0, 0, 0, 1, 2),
                            },
                            optics=ar_optics,
                            part_dict={
                                "AR Lower Receiver": {ar15.lower_ar10: (1, 100, 50, 40),
                                                      ar15.lower_ar10_auto: (0, 1, 1, 1)},
                                "AR Upper Receiver": ar15.upper_ar10,
                                "AR Buffer Tube": ar15.ar10_buffer_tube,
                                "AR Buffer": {ar15.ar10_buffer: 40,
                                              ar15.ar10_buffer_heavy: 2,
                                              ar15.ar10_buffer_light: 1},
                                "AR Barrel": {
                                    ar15.ar_barrel_standard_308: 100,
                                    ar15.ar_barrel_standard_308_midlen: 100,
                                    ar15.ar_barrel_carbine_308_midlen: 20,
                                    ar15.ar_barrel_carbine_308_carblen: 20,
                                    ar15.ar_barrel_pistol_308_carblen: 5,
                                    ar15.ar_barrel_pistol_308_pistollen: 5,
                                },
                                "AR Handguard": {
                                    ar15.ar10_handguard_a2: 100,
                                    ar15.ar10_handguard_a2_carbine: 15,
                                    ar15.ar10_handguard_wilson: 5,
                                    ar15.ar10_handguard_vseven: 2,
                                },
                                "AR Grip": {
                                    ar15.ar_grip_trybe: 15,
                                    ar15.ar_grip_moe: 90,
                                    ar15.ar_grip_hogue: 5,
                                    ar15.ar_grip_strikeforce: 10,
                                    ar15.ar_grip_a2: 100,
                                    ar15.ar_grip_stark: 15,
                                },
                                "AR Stock": {
                                    None: 5,
                                    ar15.ar_stock_m16a2: 100,
                                    ar15.ar_stock_moe: 90,
                                    ar15.ar_stock_ubr: 10,
                                    ar15.ar_stock_danieldefense: 15,
                                    ar15.ar_stock_prs: 5,
                                    ar15.ar_stock_maxim_cqb: 5,
                                },
                                "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                                attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                                attachments.irons_sig_front: 10, },
                                "Muzzle Device": {
                                    ar15.ar15_300_muzzle_flashhider: 100,
                                    ar15.ar15_300_muzzle_cobra: 8,
                                    ar15.ar15_300_muzzle_pegasus: 5,
                                    ar15.ar15_300_muzzle_strike: 3,
                                    attachments.suppressor_sandman: 1,
                                },
                                "Attachment Adapter": {None: 20,
                                                       attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 500,
                                    attachments.grip_hera_cqr: 3,
                                    attachments.grip_promag_vertical: 10,
                                    attachments.grip_jem_vertical: 10,
                                    attachments.grip_magpul_angled: 6,
                                    attachments.grip_magpul_mvg: 8,
                                    attachments.grip_aimtac_short: 7,
                                    attachments.grip_magpul_handstop: 6,
                                    attachments.grip_hipoint_folding: 3,
                                },
                            },
                            allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
                                                'AR Buffer', 'AR Barrel',
                                                'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
                                                'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
                                                'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
                                                'Optic']
                            )

mcr_weapon = PremadeWeapon(gun_item=ar15.fightlite_mcr,
                           bullet=gun_parts.bullets_556_weighted,
                           magazine=magazines.mcr_100rd,
                           optics=ar_optics,
                           part_dict={
                               "AR Lower Receiver": {ar15.lower_ar15: 3, ar15.lower_ar15_auto: 1},
                               "MCR Upper Receiver": ar15.upper_mcr,
                               "AR Grip": {
                                   ar15.ar_grip_trybe: 15,
                                   ar15.ar_grip_moe: 90,
                                   ar15.ar_grip_hogue: 5,
                                   ar15.ar_grip_strikeforce: 10,
                                   ar15.ar_grip_a2: 100,
                                   ar15.ar_grip_stark: 15,
                               },
                               "AR Stock": {
                                   ar15.ar_stock_m16a2: 100,
                                   ar15.ar_stock_moe: 90,
                                   ar15.ar_stock_ubr: 10,
                                   ar15.ar_stock_danieldefense: 15,
                                   ar15.ar_stock_prs: 5,
                                   ar15.ar_stock_maxim_cqb: 5,
                               },
                               "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                               attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                               attachments.irons_sig_front: 10, },
                               "Muzzle Device": {
                                   ar15.ar15_muzzle_flashhider: 200,
                                   ar15.ar15_muzzle_st6012: 16,
                                   ar15.ar15_muzzle_mi_mb4: 10,
                                   ar15.ar15_muzzle_cobra: 2,
                                   attachments.suppressor_wolfman_9mm: 1,
                                   attachments.suppressor_obsidian_45: 1,
                               },
                               "Attachment Adapter": {None: 20,
                                                      attachments.adapter_mlok_picrail: 1,
                                                      attachments.adapter_mlok_picrail_short: 1},
                               "Underbarrel Accessory": {
                                   None: 500,
                                   attachments.grip_hera_cqr: 3,
                                   attachments.grip_promag_vertical: 10,
                                   attachments.grip_jem_vertical: 10,
                                   attachments.grip_magpul_angled: 6,
                                   attachments.grip_magpul_mvg: 8,
                                   attachments.grip_aimtac_short: 7,
                                   attachments.grip_magpul_handstop: 6,
                                   attachments.grip_hipoint_folding: 3,
                               },
                           },
                           allowed_part_types=['AR Lower Receiver', "MCR Upper Receiver", 'AR Buffer Tube',
                                               'AR Grip', 'AR Stock', 'Attachment Adapter',
                                               'Muzzle Adapter', 'Front Sight',
                                               'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
                                               'Optic']
                           )

ar15_weapon = PremadeWeapon(gun_item=ar15.ar15,
                            bullet=gun_parts.bullets_556_weighted,
                            magazine={
                                magazines.stanag_10rd: (100, 100, 0, 0, 0),
                                magazines.stanag_20rd: (10, 10, 200, 0, 0),
                                magazines.stanag_30rd: (5, 5, 100, 200, 200),
                                magazines.stanag_40rd: (0, 1, 10, 10, 10),
                                magazines.stanag_50rd: (0, 0, 3, 3, 5),
                                magazines.stanag_60rd: (0, 0, 1, 2, 4),
                                magazines.stanag_100rd: (0, 0, 0, 1, 2),
                            },
                            optics=ar_optics,
                            part_dict={
                                "AR Lower Receiver": {ar15.lower_ar15: (1, 100, 10, 10, 1, 0),
                                                      ar15.lower_ar15_auto: (0, 3, 1, 3, 1, 1)},
                                "AR Upper Receiver": {ar15.upper_ar_m16a2: 10,
                                                      ar15.upper_ar_m16a4: 1},
                                "AR Buffer Tube": ar15.ar15_buffer_tube,
                                "AR Buffer": {ar15.ar15_buffer: 40,
                                              ar15.ar15_buffer_heavy: 2,
                                              ar15.ar15_buffer_light: 1},
                                "AR Barrel": {
                                    ar15.ar_barrel_standard_556: 100,
                                    ar15.ar_barrel_standard_556_midlen: 100,
                                    ar15.ar_barrel_carbine_556: 20,
                                    ar15.ar_barrel_carbine_556_carblen: 20,
                                    ar15.ar_barrel_pistol_556: 5,
                                    ar15.ar_barrel_pistol_556_pistollen: 5,
                                },
                                "AR Handguard": {
                                    ar15.ar_handguard_m16a1: 10,
                                    ar15.ar_handguard_m16a2: 100,
                                    ar15.ar_handguard_m16a2_carbine: 100,
                                    ar15.ar_handguard_magpul: 75,
                                    ar15.ar_handguard_magpul_carbine: 75,
                                    ar15.ar_handguard_aero: 25,
                                    ar15.ar_handguard_aero_carbine: 25,
                                    ar15.ar_handguard_aero_pistol: 10,
                                    ar15.ar_handguard_faxon: 15,
                                    ar15.ar_handguard_faxon_carbine: 15,
                                    ar15.ar_handguard_faxon_pistol: 5,
                                    ar15.ar_handguard_mk18: 15,
                                },
                                "AR Grip": {
                                    ar15.ar_grip_trybe: 15,
                                    ar15.ar_grip_moe: 90,
                                    ar15.ar_grip_hogue: 5,
                                    ar15.ar_grip_strikeforce: 10,
                                    ar15.ar_grip_a2: 100,
                                    ar15.ar_grip_stark: 15,
                                },
                                "AR Stock": {
                                    None: 5,
                                    ar15.ar_stock_m16a2: 100,
                                    ar15.ar_stock_moe: 90,
                                    ar15.ar_stock_ubr: 10,
                                    ar15.ar_stock_danieldefense: 15,
                                    ar15.ar_stock_prs: 5,
                                    ar15.ar_stock_maxim_cqb: 5,
                                },
                                "AR Optics Mount": {None: 20, ar15.carry_handle_optic_mount: 1},
                                "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                                attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                                attachments.irons_sig_front: 10, },
                                "Muzzle Device": {
                                    ar15.ar15_muzzle_flashhider: 200,
                                    ar15.ar15_muzzle_st6012: 16,
                                    ar15.ar15_muzzle_mi_mb4: 10,
                                    ar15.ar15_muzzle_cobra: 2,
                                    attachments.suppressor_wolfman_9mm: 1,
                                    attachments.suppressor_obsidian_45: 1,
                                },
                                "Attachment Adapter": {None: 20,
                                                       attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 500,
                                    attachments.grip_hera_cqr: 3,
                                    attachments.grip_promag_vertical: 10,
                                    attachments.grip_jem_vertical: 10,
                                    attachments.grip_magpul_angled: 6,
                                    attachments.grip_magpul_mvg: 8,
                                    attachments.grip_aimtac_short: 7,
                                    attachments.grip_magpul_handstop: 6,
                                    attachments.grip_hipoint_folding: 3,
                                },
                            },
                            allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', "AR Buffer Tube",
                                                'AR Buffer', 'AR Barrel',
                                                'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
                                                'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
                                                'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
                                                'Optic']
                            )

ar_9mm = PremadeWeapon(gun_item=ar15.ar15,
                       bullet=gun_parts.bullets_9mm_weighted,
                       magazine={
                           magazines.glock_mag_9mm: (100, 100, 0, 0, 0),
                           magazines.glock_mag_9mm_33: (10, 10, 100, 100, 100),
                           magazines.glock_mag_9mm_50: (0, 0, 3, 3, 5),
                           magazines.glock_mag_9mm_100: (0, 0, 0, 1, 2),
                       },
                       optics=ar_optics,
                       part_dict={
                           "AR Lower Receiver": {ar15.lower_ar_9mm: (1, 100, 10, 10, 1, 0),
                                                 ar15.lower_ar_9mm_auto: (0, 3, 1, 3, 1, 1)},
                           "AR Upper Receiver": ar15.upper_ar_9mm,
                           "AR Buffer Tube": ar15.ar15_buffer_tube,
                           "AR Buffer": {ar15.ar15_buffer: 40,
                                         ar15.ar15_buffer_heavy: 2,
                                         ar15.ar15_buffer_light: 1},
                           "AR Barrel": {
                               ar15.ar_barrel_9mm_11in: 100,
                               ar15.ar_barrel_9mm_16in: 10,
                               ar15.ar_barrel_9mm_4in: 5,
                           },
                           "AR Handguard": {
                               ar15.ar_handguard_m16a1: 10,
                               ar15.ar_handguard_m16a2: 100,
                               ar15.ar_handguard_m16a2_carbine: 100,
                               ar15.ar_handguard_magpul: 75,
                               ar15.ar_handguard_magpul_carbine: 75,
                               ar15.ar_handguard_aero: 25,
                               ar15.ar_handguard_aero_carbine: 25,
                               ar15.ar_handguard_aero_pistol: 10,
                               ar15.ar_handguard_faxon: 15,
                               ar15.ar_handguard_faxon_carbine: 15,
                               ar15.ar_handguard_faxon_pistol: 5,
                               ar15.ar_handguard_mk18: 15,
                           },
                           "AR Grip": {
                               ar15.ar_grip_trybe: 15,
                               ar15.ar_grip_moe: 90,
                               ar15.ar_grip_hogue: 5,
                               ar15.ar_grip_strikeforce: 10,
                               ar15.ar_grip_a2: 100,
                               ar15.ar_grip_stark: 15,
                           },
                           "AR Stock": {
                               None: 100,
                               ar15.ar_stock_m16a2: 100,
                               ar15.ar_stock_moe: 90,
                               ar15.ar_stock_ubr: 10,
                               ar15.ar_stock_danieldefense: 15,
                               ar15.ar_stock_prs: 5,
                               ar15.ar_stock_maxim_cqb: 5,
                           },
                           "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                           attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                           attachments.irons_sig_front: 10, },
                           "Muzzle Device": {
                               None: 50,
                               ar15.ar15_muzzle_flashhider: 200,
                               ar15.ar15_muzzle_st6012: 16,
                               ar15.ar15_muzzle_mi_mb4: 10,
                               ar15.ar15_muzzle_cobra: 2,
                               attachments.suppressor_wolfman_9mm: 3,
                               attachments.suppressor_obsidian_9: 2,
                           },
                           "Attachment Adapter": {None: 20,
                                                  attachments.adapter_mlok_picrail: 1,
                                                  attachments.adapter_mlok_picrail_short: 1},
                           "Underbarrel Accessory": {
                               None: 500,
                               attachments.grip_hera_cqr: 3,
                               attachments.grip_promag_vertical: 10,
                               attachments.grip_jem_vertical: 10,
                               attachments.grip_magpul_angled: 6,
                               attachments.grip_magpul_mvg: 8,
                               attachments.grip_aimtac_short: 7,
                               attachments.grip_magpul_handstop: 6,
                               attachments.grip_hipoint_folding: 3,
                           },
                       },
                       allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
                                           'AR Buffer', 'AR Barrel',
                                           'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
                                           'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
                                           'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
                                           'Optic']
                       )

ar_40sw = PremadeWeapon(gun_item=ar15.ar15,
                        bullet=gun_parts.bullets_40sw_weighted,
                        magazine={
                            magazines.glock_mag_40: (100, 100, 0, 0, 0),
                            magazines.glock_mag_40_22: (10, 10, 100, 100, 100),
                            magazines.glock_mag_40_50: (0, 0, 3, 3, 5),
                        },
                        optics=ar_optics,
                        part_dict={
                            "AR Lower Receiver": {ar15.lower_ar_9mm: (1, 100, 10, 10, 1, 0),
                                                  ar15.lower_ar_9mm_auto: (0, 3, 1, 3, 1, 1)},
                            "AR Upper Receiver": ar15.upper_ar_9mm,
                            "AR Buffer Tube": ar15.ar15_buffer_tube,
                            "AR Buffer": {ar15.ar15_buffer: 40,
                                          ar15.ar15_buffer_heavy: 2,
                                          ar15.ar15_buffer_light: 1},
                            "AR Barrel": {
                                ar15.ar_barrel_40_12in: 100,
                                ar15.ar_barrel_40_16in: 10,
                                ar15.ar_barrel_40_4in: 5,
                            },
                            "AR Handguard": {
                                ar15.ar_handguard_m16a1: 10,
                                ar15.ar_handguard_m16a2: 100,
                                ar15.ar_handguard_m16a2_carbine: 100,
                                ar15.ar_handguard_magpul: 75,
                                ar15.ar_handguard_magpul_carbine: 75,
                                ar15.ar_handguard_aero: 25,
                                ar15.ar_handguard_aero_carbine: 25,
                                ar15.ar_handguard_aero_pistol: 10,
                                ar15.ar_handguard_faxon: 15,
                                ar15.ar_handguard_faxon_carbine: 15,
                                ar15.ar_handguard_faxon_pistol: 5,
                                ar15.ar_handguard_mk18: 15,
                            },
                            "AR Grip": {
                                ar15.ar_grip_trybe: 15,
                                ar15.ar_grip_moe: 90,
                                ar15.ar_grip_hogue: 5,
                                ar15.ar_grip_strikeforce: 10,
                                ar15.ar_grip_a2: 100,
                                ar15.ar_grip_stark: 15,
                            },
                            "AR Stock": {
                                None: 100,
                                ar15.ar_stock_m16a2: 100,
                                ar15.ar_stock_moe: 90,
                                ar15.ar_stock_ubr: 10,
                                ar15.ar_stock_danieldefense: 15,
                                ar15.ar_stock_prs: 5,
                                ar15.ar_stock_maxim_cqb: 5,
                            },
                            "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                            attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                            attachments.irons_sig_front: 10, },
                            "Muzzle Device": {
                                None: 50,
                                attachments.muzzle_maxtac: 3,
                                attachments.suppressor_octane45: 2,
                            },
                            "Attachment Adapter": {None: 20,
                                                   attachments.adapter_mlok_picrail: 1,
                                                   attachments.adapter_mlok_picrail_short: 1},
                            "Underbarrel Accessory": {
                                None: 500,
                                attachments.grip_hera_cqr: 3,
                                attachments.grip_promag_vertical: 10,
                                attachments.grip_jem_vertical: 10,
                                attachments.grip_magpul_angled: 6,
                                attachments.grip_magpul_mvg: 8,
                                attachments.grip_aimtac_short: 7,
                                attachments.grip_magpul_handstop: 6,
                                attachments.grip_hipoint_folding: 3,
                            },
                        },
                        allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
                                            'AR Buffer', 'AR Barrel',
                                            'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
                                            'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
                                            'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
                                            'Optic']
                        )

"""
AK 7.62
"""

ak47_weapon = PremadeWeapon(gun_item=ak.ak,
                            bullet=gun_parts.bullets_752_weighted,
                            magazine={
                                magazines.ak762_10rd: (100, 100, 0, 0, 0),
                                magazines.ak762_20rd: (10, 10, 200, 0, 0),
                                magazines.ak762_30rd: (5, 5, 100, 200, 200),
                                magazines.ak762_40rd: (0, 1, 10, 10, 10),
                                magazines.ak762_60rd: (0, 0, 1, 2, 4),
                                magazines.ak762_75rd: (0, 0, 1, 1, 3),
                                magazines.ak762_100rd: (0, 0, 0, 1, 2)},
                            optics=optics_test,
                            part_dict={
                                "AK Reciever": {ak.reciever_akm: (1, 100, 10, 10, 1, 0),
                                                ak.reciever_akm_auto: (0, 3, 1, 3, 1, 1)},
                                "AK Barrel": {ak.barrel_ak762: 100, ak.barrel_rpk762: 5, ak.barrel_ak762_short: 10},
                                "Thread Adapter": {None: 20,
                                                   attachments.thread_adapter_141_24mm: 1},
                                "AK Handguard": {
                                    ak.handguard_akm: 200,
                                    ak.handguard_amd65: 15,
                                    ak.handguard_ak74: 70,
                                    ak.handguard_romanian: 10,
                                    ak.handguard_ak100: 20,
                                    ak.handguard_B10M: 5,
                                    ak.handguard_leader: 7,
                                    ak.handguard_magpul: 30,
                                },
                                "AK Grip": {
                                    ak.grip_akm: 300,
                                    ak.grip_ak12: 10,
                                    ak.grip_sniper: 15,
                                    ak.grip_moe: 50,
                                    ak.grip_rk3: 30,
                                    ak.grip_tapco: 30,
                                    ak.grip_skeletonised: 20,
                                    ak.grip_hogue: 20,
                                    ak.grip_fab: 25,
                                },
                                "AK Stock": {
                                    None: 10,
                                    ak.stock_akm: 300,
                                    ak.stock_rpk: 15,
                                    ak.stock_ak74: 100,
                                    ak.stock_ak100: 25,
                                    ak.stock_ak_underfolder: 80,
                                    ak.stock_ak_triangle: 90,
                                    ak.stock_ak12: 8,
                                    ak.stock_amd65: 40,
                                    ak.stock_pt1: 15,
                                    ak.stock_moe: 30,
                                    ak.stock_zhukov: 10,
                                },
                                "AK Optics Mount": {None: 100, ak.accessory_dustcoverrail: 2,
                                                    ak.accessory_railsidemount: 3},
                                "Muzzle Device": {
                                    ak.muzzle_ak74: 100,
                                    ak.muzzle_dtk: 15,
                                    ak.muzzle_amd65: 20,
                                    ak.muzzle_akm: 300,
                                    ak.muzzle_akml: 60,
                                    ak.muzzle_lantac: 15,
                                    ak.muzzle_pbs4: 5,
                                    ak.muzzle_pbs1: 5,
                                    ak.muzzle_dynacomp: 12,
                                },
                                "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 500,
                                    attachments.grip_hera_cqr: 3,
                                    attachments.grip_promag_vertical: 10,
                                    attachments.grip_jem_vertical: 10,
                                    attachments.grip_magpul_angled: 6,
                                    attachments.grip_magpul_mvg: 8,
                                    attachments.grip_aimtac_short: 7,
                                    attachments.grip_magpul_handstop: 6,
                                    attachments.grip_hipoint_folding: 3,
                                },
                            },
                            allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
                                                'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
                                                'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
                                                'AK Magazine Adapter', 'Optic']
                            )

ak74_weapon = PremadeWeapon(gun_item=ak.ak,
                            bullet=gun_parts.bullets_545_weighted,
                            magazine={magazines.ak545_30rd: (5, 5, 100, 200, 200),
                                      magazines.ak545_45rd: (0,  1,  10,  10, 10),
                                      magazines.ak545_60rd: (0,  0,  1,   2,  4),
                                      magazines.ak545_100rd: (0, 0,  0,   1,  2)},
                            optics=optics_test,
                            part_dict={
                                "AK Reciever": {ak.reciever_ak74: (1, 100, 10, 10, 1, 0),
                                                ak.reciever_ak74_auto: (0, 3, 1, 3, 1, 1)},
                                "AK Barrel": {ak.barrel_ak545: 100, ak.barrel_rpk545: 5, ak.barrel_ak545_short: 10},
                                "Thread Adapter": {None: 20,
                                                   attachments.thread_adapter_2415_5824: 1},
                                "AK Handguard": {
                                    ak.handguard_akm: 200,
                                    ak.handguard_amd65: 15,
                                    ak.handguard_ak74: 70,
                                    ak.handguard_romanian: 10,
                                    ak.handguard_ak100: 20,
                                    ak.handguard_B10M: 5,
                                    ak.handguard_leader: 7,
                                    ak.handguard_magpul: 30,
                                },
                                "AK Grip": {
                                    ak.grip_akm: 300,
                                    ak.grip_ak12: 10,
                                    ak.grip_sniper: 15,
                                    ak.grip_moe: 50,
                                    ak.grip_rk3: 30,
                                    ak.grip_tapco: 30,
                                    ak.grip_skeletonised: 20,
                                    ak.grip_hogue: 20,
                                    ak.grip_fab: 25,
                                },
                                "AK Stock": {
                                    None: 10,
                                    ak.stock_akm: 300,
                                    ak.stock_rpk: 15,
                                    ak.stock_ak74: 100,
                                    ak.stock_ak100: 25,
                                    ak.stock_ak_underfolder: 80,
                                    ak.stock_ak_triangle: 90,
                                    ak.stock_ak12: 8,
                                    ak.stock_amd65: 40,
                                    ak.stock_pt1: 15,
                                    ak.stock_moe: 30,
                                    ak.stock_zhukov: 10,
                                },
                                "AK Optics Mount": {None: 100, ak.accessory_dustcoverrail: 5,
                                                    ak.accessory_railsidemount: 5},
                                "Muzzle Device": {
                                    ak.muzzle_ak74: 100,
                                    ak.muzzle_dtk: 15,
                                    ak.muzzle_amd65: 20,
                                    ak.muzzle_akm: 300,
                                    ak.muzzle_akml: 60,
                                    ak.muzzle_lantac: 15,
                                    ak.muzzle_pbs4: 5,
                                    ak.muzzle_pbs1: 5,
                                    ak.muzzle_dynacomp: 12,
                                },
                                "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 500,
                                    attachments.grip_hera_cqr: 3,
                                    attachments.grip_promag_vertical: 10,
                                    attachments.grip_jem_vertical: 10,
                                    attachments.grip_magpul_angled: 6,
                                    attachments.grip_magpul_mvg: 8,
                                    attachments.grip_aimtac_short: 7,
                                    attachments.grip_magpul_handstop: 6,
                                    attachments.grip_hipoint_folding: 3,
                                },
                            },
                            allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
                                                'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
                                                'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
                                                'AK Magazine Adapter', 'Optic']
                            )

ak556_weapon = PremadeWeapon(gun_item=ak.ak,
                             bullet=gun_parts.bullets_556_weighted,
                             magazine={magazines.ak556_30rd: (1, 1, 1, 1, 1),
                                       magazines.stanag_10rd: (100, 100, 0, 0, 0),
                                       magazines.stanag_20rd: (10, 10, 200, 0, 0),
                                       magazines.stanag_30rd: (5, 5, 100, 200, 200),
                                       magazines.stanag_40rd: (0, 1, 10, 10, 10),
                                       magazines.stanag_50rd: (0, 0, 3, 3, 5),
                                       magazines.stanag_60rd: (0, 0, 1, 2, 4),
                                       magazines.stanag_100rd: (0, 0, 0, 1, 2),
                                       },
                             optics=optics_test,
                             part_dict={
                                 "AK Reciever": {ak.reciever_100556: (1, 100, 10, 10, 1, 0),
                                                 ak.reciever_100556_auto: (0, 3, 1, 3, 1, 1)},
                                 "AK Magazine Adapter": {None: 20, ak.ak_ar_mag_adapter: 1},
                                 "AK Barrel": {ak.barrel_ak556: 100, ak.barrel_ak556_short: 10},
                                 "Thread Adapter": {None: 20,
                                                    attachments.thread_adapter_2415_5824: 1},
                                 "AK Handguard": {
                                     ak.handguard_akm: 200,
                                     ak.handguard_amd65: 15,
                                     ak.handguard_ak74: 70,
                                     ak.handguard_romanian: 10,
                                     ak.handguard_ak100: 20,
                                     ak.handguard_B10M: 5,
                                     ak.handguard_leader: 7,
                                     ak.handguard_magpul: 30,
                                 },
                                 "AK Grip": {
                                     ak.grip_akm: 300,
                                     ak.grip_ak12: 10,
                                     ak.grip_sniper: 15,
                                     ak.grip_moe: 50,
                                     ak.grip_rk3: 30,
                                     ak.grip_tapco: 30,
                                     ak.grip_skeletonised: 20,
                                     ak.grip_hogue: 20,
                                     ak.grip_fab: 25,
                                 },
                                 "AK Stock": {
                                     None: 10,
                                     ak.stock_akm: 300,
                                     ak.stock_rpk: 15,
                                     ak.stock_ak74: 100,
                                     ak.stock_ak100: 25,
                                     ak.stock_ak_underfolder: 80,
                                     ak.stock_ak_triangle: 90,
                                     ak.stock_ak12: 8,
                                     ak.stock_amd65: 40,
                                     ak.stock_pt1: 15,
                                     ak.stock_moe: 30,
                                     ak.stock_zhukov: 10,
                                 },
                                 "AK Optics Mount": {None: 100, ak.accessory_dustcoverrail: 5,
                                                     ak.accessory_railsidemount: 5},
                                 "Muzzle Device": {
                                     ak.muzzle_ak74: 100,
                                     ak.muzzle_dtk: 15,
                                     ak.muzzle_amd65: 20,
                                     ak.muzzle_akm: 300,
                                     ak.muzzle_akml: 60,
                                     ak.muzzle_lantac: 15,
                                     ak.muzzle_pbs4: 5,
                                     ak.muzzle_pbs1: 5,
                                     ak.muzzle_dynacomp: 12,
                                 },
                                 "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                        attachments.adapter_mlok_picrail_short: 1},
                                 "Underbarrel Accessory": {
                                     None: 500,
                                     attachments.grip_hera_cqr: 3,
                                     attachments.grip_promag_vertical: 10,
                                     attachments.grip_jem_vertical: 10,
                                     attachments.grip_magpul_angled: 6,
                                     attachments.grip_magpul_mvg: 8,
                                     attachments.grip_aimtac_short: 7,
                                     attachments.grip_magpul_handstop: 6,
                                     attachments.grip_hipoint_folding: 3,
                                 },
                             },
                             allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
                                                 'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
                                                 'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
                                                 'AK Magazine Adapter', 'Optic']
                             )

"""
MAC 10
"""

m1045_weapon = PremadeWeapon(gun_item=m10.mac10,
                             bullet=gun_parts.bullets_45_weighted,
                             magazine={magazines.mac10_mag_45: 10, magazines.mac10_mag_45_extended: 1},
                             optics=optics_test,
                             part_dict={
                                 "M10 Lower": m10.mac1045_lower,
                                 "M10 Upper": {m10.mac1045_upper: 100,
                                               m10.mac1045_upper_tactical: 10,
                                               m10.mac1045_upper_max: 2},
                                 "M10 Barrel": {m10.mac1045_barrel: 100,
                                                m10.mac1045_max_barrel: 5,
                                                m10.mac1045_carbine_barrel: 5,
                                                },
                                 "M10/45 Carbine Handguard": {m10.mac10_carbine_handguard_m16a2: 5,
                                                              m10.mac10_carbine_handguard_picatinny: 1},
                                 "Stock Adapter M10": {None: 20,
                                                       m10.mac10_ar_stock_adapter: 1},
                                 "M10 Stock": {m10.mac1045_full_stock: 8,
                                               m10.mac1045_folding_stock: 4,
                                               m10.mac1045_stock: 100},
                                 "AR Stock": {
                                     ar15.ar_stock_m16a2: 100,
                                     ar15.ar_stock_moe: 90,
                                     ar15.ar_stock_ubr: 10,
                                     ar15.ar_stock_danieldefense: 15,
                                     ar15.ar_stock_prs: 5,
                                     ar15.ar_stock_maxim_cqb: 5,
                                 },
                                 "M10 Optics Mount": {None: 15, m10.mac10_optics_mount: 1},
                                 "Muzzle Device": {
                                     None: 50,
                                     attachments.muzzle_nullifier: 3,
                                     attachments.muzzle_kak_45: 5,
                                     attachments.muzzle_kak_a2: 50,
                                     m10.mac1045_sionics_suppressor: 1,
                                     m10.mac1045_extended_barrel: 5,
                                     attachments.suppressor_obsidian_45: 2,
                                 },
                                 "Accessory Adapter M10": {None: 20, m10.mac10_trirail: 1},
                                 "Underbarrel Accessory": {
                                     None: 500,
                                     attachments.grip_hera_cqr: 3,
                                     attachments.grip_promag_vertical: 10,
                                     attachments.grip_jem_vertical: 10,
                                     attachments.grip_magpul_angled: 6,
                                     attachments.grip_magpul_mvg: 8,
                                     attachments.grip_aimtac_short: 7,
                                     attachments.grip_magpul_handstop: 6,
                                     attachments.grip_hipoint_folding: 3,
                                 },
                             },
                             allowed_part_types=['M10 Lower', 'M10 Upper', 'Stock Adapter M10', 'Attachment Adapter',
                                                 'Muzzle Adapter', 'M10 Stock', 'M10 Optics Mount', 'Muzzle Device',
                                                 'Accessory Adapter M10', 'Side Mounted Accessory',
                                                 'Underbarrel Accessory', 'Optic']
                             )

m109_weapon = PremadeWeapon(gun_item=m10.mac10,
                            bullet=gun_parts.bullets_9mm_weighted,
                            magazine=magazines.mac10_mag_9,
                            optics=optics_test,
                            part_dict={
                                "M10 Lower": m10.mac109_lower,
                                "M10 Upper": {m10.mac109_upper: 100,
                                              m10.mac109_upper_tactical: 10,
                                              m10.mac109_upper_max: 2,
                                              m10.mac109_upper_max31: 1,
                                              m10.mac109_upper_max31k: 1,
                                              },
                                "M10 Barrel": {m10.mac109_barrel: 100,
                                               m10.mac109_max_barrel: 5,
                                               m10.mac109_carbine_barrel: 5,
                                               m10.max1031_barrel_1228: 5,
                                               m10.max1031k_barrel_1228: 5,
                                               m10.max1031_barrel_3410: 5,
                                               m10.max1031k_barrel_3410: 5,
                                               },
                                "M10/45 Carbine Handguard": {m10.mac109_carbine_handguard_m16a2: 5,
                                                             m10.mac109_carbine_handguard_picatinny: 1},
                                "Stock Adapter M10": {None: 20,
                                                      m10.mac10_ar_stock_adapter: 1},
                                "M10 Stock": {m10.mac1045_full_stock: 8,
                                              m10.mac1045_folding_stock: 4,
                                              m10.mac1045_stock: 100},
                                "AR Stock": {
                                    ar15.ar_stock_m16a2: 100,
                                    ar15.ar_stock_moe: 90,
                                    ar15.ar_stock_ubr: 10,
                                    ar15.ar_stock_danieldefense: 15,
                                    ar15.ar_stock_prs: 5,
                                    ar15.ar_stock_maxim_cqb: 5,
                                },
                                "M10 Optics Mount": {None: 15, m10.mac10_optics_mount: 1},
                                "Muzzle Device": {
                                    None: 100,
                                    m10.mac109_sionics_suppressor: 1,
                                    m10.mac109_extended_barrel: 5,
                                    attachments.suppressor_wolfman_9mm: 3,
                                    attachments.suppressor_obsidian_9: 2,
                                },
                                "Accessory Adapter M10": {None: 20, m10.mac10_trirail: 1},
                                "Underbarrel Accessory": {
                                    None: 500,
                                    attachments.grip_hera_cqr: 3,
                                    attachments.grip_promag_vertical: 10,
                                    attachments.grip_jem_vertical: 10,
                                    attachments.grip_magpul_angled: 6,
                                    attachments.grip_magpul_mvg: 8,
                                    attachments.grip_aimtac_short: 7,
                                    attachments.grip_magpul_handstop: 6,
                                    attachments.grip_hipoint_folding: 3,
                                },
                            },
                            allowed_part_types=['M10 Lower', 'M10 Upper', 'Stock Adapter M10', 'Attachment Adapter',
                                                'Muzzle Adapter', 'M10 Stock', 'M10 Optics Mount', 'Muzzle Device',
                                                'Accessory Adapter M10', 'Side Mounted Accessory',
                                                'Underbarrel Accessory', 'Optic']
                            )

"""
SKS
"""

sks_weapon = PremadeWeapon(gun_item=sks.sks,
                           bullet=gun_parts.bullets_752_weighted,
                           magazine={
                               magazines.ak762_10rd: (100, 100, 0, 0, 0),
                               magazines.ak762_20rd: (10, 10, 200, 0, 0),
                               magazines.ak762_30rd: (5, 5, 100, 200, 200),
                               magazines.ak762_40rd: (0, 1, 10, 10, 10),
                               magazines.ak762_60rd: (0, 0, 1, 2, 4),
                               magazines.ak762_75rd: (0, 0, 1, 1, 3),
                               magazines.ak762_100rd: (0, 0, 0, 1, 2),
                               magazines.sks_mag_20rd: (10, 10, 200, 0, 0),
                               magazines.sks_mag_35rd: (0, 1, 10, 10, 10),
                               magazines.sks_mag_75rd: (0, 0, 1, 1, 3)},
                           clip=magazines.sks_clip,
                           optics=optics_test,
                           part_dict={
                               "SKS Barrel": {
                                   sks.barrel_sks:                      (10, 10, 20, 40),
                                   sks.barrel_sks_shortened:            (1,  2,  4,  8),
                                   sks.barrel_sks_auto:                 (0,  0,  1,  5),
                                   sks.barrel_sks_shortened_auto:       (0,  0,  1,  3),
                                   sks.barrel_sks_akmag:                (0,  0,  2,  4),
                                   sks.barrel_sks_shortened_akmag:      (0,  0,  1,  3),
                                   sks.barrel_sks_auto_akmag:           (0,  0,  0,  2),
                                   sks.barrel_sks_shortened_auto_akmag: (0,  0,  0,  2),
                               },
                               "Thread Adapter": {None: 20,
                                                  attachments.thread_adapter_sks: 1},
                               "SKS Stock": {
                                   sks.stock_sks: 300,
                                   sks.stock_sks_tapco: 30,
                                   sks.stock_sks_dragunov: 15,
                                   sks.stock_sks_fab: 10,
                                   sks.stock_sks_sabertooth: 5,
                                   sks.stock_sks_bullpup: 3,
                               },
                               "AR Grip": {
                                   ar15.ar_grip_trybe: 15,
                                   ar15.ar_grip_moe: 90,
                                   ar15.ar_grip_hogue: 5,
                                   ar15.ar_grip_strikeforce: 10,
                                   ar15.ar_grip_a2: 100,
                                   ar15.ar_grip_stark: 15,
                               },
                               "AR Stock": {
                                   ar15.ar_stock_m16a2: 100,
                                   ar15.ar_stock_moe: 90,
                                   ar15.ar_stock_ubr: 10,
                                   ar15.ar_stock_danieldefense: 15,
                                   ar15.ar_stock_prs: 5,
                                   ar15.ar_stock_maxim_cqb: 5,
                               },
                               "SKS Internal Magazine": {sks.sks_integrated_mag: 1, None: 1},
                               "SKS Optics Mount": {None: 15, sks.sks_optics_mount: 1},
                               "Attachment Adapter": {None: 20,
                                                      attachments.adapter_mlok_picrail: 1,
                                                      attachments.adapter_mlok_picrail_short: 1},
                               "Underbarrel Accessory": {
                                   None: 500,
                                   attachments.grip_hera_cqr: 3,
                                   attachments.grip_promag_vertical: 10,
                                   attachments.grip_jem_vertical: 10,
                                   attachments.grip_magpul_angled: 6,
                                   attachments.grip_magpul_mvg: 8,
                                   attachments.grip_aimtac_short: 7,
                                   attachments.grip_magpul_handstop: 6,
                                   attachments.grip_hipoint_folding: 3,
                               },
                               "Muzzle Device": {
                                   ak.muzzle_ak74: 100,
                                   ak.muzzle_dtk: 15,
                                   ak.muzzle_amd65: 20,
                                   ak.muzzle_akm: 300,
                                   ak.muzzle_akml: 60,
                                   ak.muzzle_lantac: 15,
                                   ak.muzzle_pbs4: 5,
                                   ak.muzzle_pbs1: 5,
                                   ak.muzzle_dynacomp: 12,
                               },
                           },
                           allowed_part_types=['SKS Barrel', 'SKS Stock', 'SKS Internal Magazine', 'Attachment Adapter',
                                               'SKS Optics Mount', 'Underbarrel Accessory', 'Side Mounted Accessory',
                                               'Muzzle Device', 'Optic']
                           )

"""
Mosin Nagant
"""

mosin_weapon = PremadeWeapon(gun_item=mosin.mosin_nagant,
                             bullet=gun_parts.bullets_54r_weighted,
                             magazine=magazines.mosin_nagant,
                             clip=magazines.mosin_clip,
                             optics=optics_test,
                             part_dict={
                                 "Mosin-Nagant Stock": {
                                     mosin.mosin_stock: 300,
                                     mosin.mosin_stock_montecarlo: 10,
                                     mosin.mosin_archangel_stock: 10,
                                     mosin.mosin_carbine_stock: 50,
                                     mosin.mosin_obrez_stock: 15,
                                 },
                                 "Mosin-Nagant Barrel": {
                                     mosin.mosin_barrel: 100,
                                     mosin.mosin_carbine_barrel: 15,
                                     mosin.mosin_obrez_barrel: 500,
                                 },
                                 "Thread Adapter": {None: 20,
                                                    attachments.thread_adapter_mosin: 1},
                                 "Mosin-Nagant Accessory Mount": {mosin.mosin_pic_scope_mount: 1, None: 15},
                                 "Muzzle Device": {
                                     None: 150,
                                     mosin.mosin_suppressor: 5,
                                     mosin.mosin_muzzlebreak: 10,
                                     ar15.ar15_muzzle_flashhider: 100,
                                     ar15.ar15_muzzle_st6012: 8,
                                     ar15.ar15_muzzle_mi_mb4: 5,
                                     ar15.ar15_muzzle_cobra: 1,
                                 },
                             },
                             allowed_part_types=['Mosin-Nagant Stock', 'Mosin-Nagant Barrel', 'Attachment Adapter',
                                                 'Muzzle Adapter', 'Mosin-Nagant Accessory Mount', 'Muzzle Device',
                                                 'Optic', 'Side Mounted Accessory']
                             )

"""
1911
"""

m1911_45 = PremadeWeapon(gun_item=m1911.m1911,
                         bullet=gun_parts.bullets_45_weighted,
                         magazine={magazines.m1911_mag_45_8: (5, 5, 100, 200, 50),
                                   magazines.m1911_mag_45_10: (1, 2, 50, 200, 100),
                                   magazines.m1911_mag_45_15: (0, 1, 10, 10, 10),
                                   magazines.m1911_mag_45_40: (0, 0, 1, 2, 2)},
                         optics=optics_test,
                         part_dict={
                             "M1911 Frame": {
                                 m1911.m1911_frame_gov_ss:                         (10, 30, 50),
                                             m1911.m1911_frame_gov_alloy:          (2,  6,  30),
                                             m1911.m1911_frame_gov_ss_tac:         (1,  4,  20),
                                             m1911.m1911_frame_gov_alloy_tac:      (0,  2,  12),
                                             m1911.m1911_frame_gov_ss_auto:        (0,  1,  1),
                                             m1911.m1911_frame_gov_alloy_auto:     (0,  0,  1),
                                             m1911.m1911_frame_gov_ss_tac_auto:    (0,  0,  1),
                                             m1911.m1911_frame_gov_alloy_tac_auto: (0,  0,  1), },
                             "M1911 Barrel": {m1911.m1911_barrel_gov: 200,
                                              m1911.m1911_barrel_commander: 15,
                                              m1911.m1911_barrel_long: 5,
                                              m1911.m1911_barrel_gov_threaded: 100,
                                              m1911.m1911_barrel_commander_threaded: 7,
                                              m1911.m1911_barrel_long_threaded: 2, },
                             "M1911 Slide": {m1911.m1911_slide_gov: 400,
                                             m1911.m1911_slide_commander: 75,
                                             m1911.m1911_slide_long: 10,
                                             m1911.m1911_slide_gov_light: 50,
                                             m1911.m1911_slide_commander_light: 20,
                                             m1911.m1911_slide_long_light: 5,
                                             m1911.m1911_slide_gov_optic: 100,
                                             m1911.m1911_slide_commander_optic: 50,
                                             m1911.m1911_slide_long_optic: 8,
                                             m1911.m1911_slide_gov_light_optic: 7,
                                             m1911.m1911_slide_commander_light_optic: 4,
                                             m1911.m1911_slide_long_light_optic: 2,
                                             },
                             "M1911 Grip Panels": {m1911.m1911_grip_magpul: 200,
                                                   m1911.m1911_grip_rectac: 20,
                                                   m1911.m1911_grip_wood: 15,
                                                   m1911.m1911_grip_operator: 10,
                                                   m1911.m1911_grip_palmswell: 6,
                                                   m1911.m1911_grip_hogue: 5,
                                                   m1911.m1911_rec_stock: 2,
                                                   },
                             "M1911 Optics Mount": {None: 20, m1911.m1911_bridge_mount: 1},
                             "Muzzle Device": {None: 200, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                               m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10,
                                               attachments.suppressor_obsidian_45: 3},
                             "Underbarrel Accessory": {
                                 None: 500,
                                 attachments.grip_promag_vertical: 10,
                                 attachments.grip_jem_vertical: 10,
                                 attachments.grip_aimtac_short: 5,
                                 attachments.grip_hipoint_folding: 5,
                             },
                         },
                         allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
                                             'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
                                             'Optic', 'Muzzle Device']
                         )

m1911_9mm = PremadeWeapon(gun_item=m1911.m1911,
                          bullet=gun_parts.bullets_9mm_weighted,
                          magazine=magazines.m1911_mag_9_10,
                          optics=optics_test,
                          part_dict={
                              "M1911 Frame": {
                                  m1911.m1911_frame_gov_ss: (10, 30, 50),
                                  m1911.m1911_frame_gov_alloy: (2, 6, 30),
                                  m1911.m1911_frame_gov_ss_tac: (1, 4, 20),
                                  m1911.m1911_frame_gov_alloy_tac: (0, 2, 12),
                                  m1911.m1911_frame_gov_ss_auto: (0, 1, 1),
                                  m1911.m1911_frame_gov_alloy_auto: (0, 0, 1),
                                  m1911.m1911_frame_gov_ss_tac_auto: (0, 0, 1),
                                  m1911.m1911_frame_gov_alloy_tac_auto: (0, 0, 1), },
                              "M1911 Barrel": {m1911.m1911_barrel_gov_9mm: 200,
                                               m1911.m1911_barrel_commander_9mm: 15,
                                               m1911.m1911_barrel_long_9mm: 5,
                                               m1911.m1911_barrel_gov_threaded_9mm: 100,
                                               m1911.m1911_barrel_commander_threaded_9mm: 7,
                                               m1911.m1911_barrel_long_threaded_9mm: 2, },
                              "M1911 Slide": {m1911.m1911_slide_gov_9mm: 400,
                                              m1911.m1911_slide_commander_9mm: 75,
                                              m1911.m1911_slide_long_9mm: 10,
                                              m1911.m1911_slide_gov_light_9mm: 50,
                                              m1911.m1911_slide_commander_light_9mm: 20,
                                              m1911.m1911_slide_long_light_9mm: 5,
                                              m1911.m1911_slide_gov_9mm_optic: 100,
                                              m1911.m1911_slide_commander_9mm_optic: 50,
                                              m1911.m1911_slide_long_9mm_optic: 8,
                                              m1911.m1911_slide_gov_light_9mm_optic: 7,
                                              m1911.m1911_slide_commander_light_9mm_optic: 4,
                                              m1911.m1911_slide_long_light_9mm_optic: 2,
                                              },
                              "M1911 Grip Panels": {m1911.m1911_grip_magpul: 200,
                                                    m1911.m1911_grip_rectac: 20,
                                                    m1911.m1911_grip_wood: 15,
                                                    m1911.m1911_grip_operator: 10,
                                                    m1911.m1911_grip_palmswell: 6,
                                                    m1911.m1911_grip_hogue: 5,
                                                    m1911.m1911_rec_stock: 2,
                                                    },
                              "M1911 Optics Mount": {None: 20, m1911.m1911_bridge_mount: 1},
                              "Muzzle Device": {None: 200, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                                m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10,
                                                attachments.suppressor_wolfman_9mm: 3,
                                                attachments.suppressor_obsidian_9: 2,},
                              "Underbarrel Accessory": {
                                  None: 500,
                                  attachments.grip_promag_vertical: 10,
                                  attachments.grip_jem_vertical: 10,
                                  attachments.grip_aimtac_short: 5,
                                  attachments.grip_hipoint_folding: 5,
                              },
                          },
                          allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
                                              'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
                                              'Optic', 'Muzzle Device']
                          )

m1911_10mm = PremadeWeapon(gun_item=m1911.m1911,
                           bullet=gun_parts.bullets_10mm_weighted,
                           magazine=magazines.m1911_mag_10_8,
                           optics=optics_test,
                           part_dict={
                               "M1911 Frame": {
                                   m1911.m1911_frame_gov_ss: (10, 30, 50),
                                   m1911.m1911_frame_gov_alloy: (2, 6, 30),
                                   m1911.m1911_frame_gov_ss_tac: (1, 4, 20),
                                   m1911.m1911_frame_gov_alloy_tac: (0, 2, 12),
                                   m1911.m1911_frame_gov_ss_auto: (0, 1, 1),
                                   m1911.m1911_frame_gov_alloy_auto: (0, 0, 1),
                                   m1911.m1911_frame_gov_ss_tac_auto: (0, 0, 1),
                                   m1911.m1911_frame_gov_alloy_tac_auto: (0, 0, 1), },
                               "M1911 Barrel": {m1911.m1911_barrel_gov_10mm: 200,
                                                m1911.m1911_barrel_commander_10mm: 15,
                                                m1911.m1911_barrel_long_10mm: 5,
                                                m1911.m1911_barrel_gov_threaded_10mm: 100,
                                                m1911.m1911_barrel_commander_threaded_10mm: 7,
                                                m1911.m1911_barrel_long_threaded_10mm: 2, },
                               "M1911 Slide": {m1911.m1911_slide_gov_40: 400,
                                               m1911.m1911_slide_commander_40: 75,
                                               m1911.m1911_slide_long_40: 10,
                                               m1911.m1911_slide_gov_light_40: 50,
                                               m1911.m1911_slide_commander_light_40: 20,
                                               m1911.m1911_slide_long_light_40: 5,
                                               m1911.m1911_slide_gov_40_optic: 100,
                                               m1911.m1911_slide_commander_40_optic: 50,
                                               m1911.m1911_slide_long_40_optic: 8,
                                               m1911.m1911_slide_gov_light_40_optic: 7,
                                               m1911.m1911_slide_commander_light_40_optic: 4,
                                               m1911.m1911_slide_long_light_40_optic: 2,
                                               },
                               "M1911 Grip Panels": {m1911.m1911_grip_magpul: 200,
                                                     m1911.m1911_grip_rectac: 20,
                                                     m1911.m1911_grip_wood: 15,
                                                     m1911.m1911_grip_operator: 10,
                                                     m1911.m1911_grip_palmswell: 6,
                                                     m1911.m1911_grip_hogue: 5,
                                                     m1911.m1911_rec_stock: 2,
                                                     },
                               "M1911 Optics Mount": {None: 20, m1911.m1911_bridge_mount: 1},
                               "Muzzle Device": {None: 200, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                                 m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10,
                                                 attachments.suppressor_sandman: 2},
                               "Underbarrel Accessory": {
                                   None: 500,
                                   attachments.grip_promag_vertical: 10,
                                   attachments.grip_jem_vertical: 10,
                                   attachments.grip_aimtac_short: 5,
                                   attachments.grip_hipoint_folding: 5,
                               },
                           },
                           allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
                                               'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
                                               'Optic', 'Muzzle Device']
                           )

m1911_40sw = PremadeWeapon(gun_item=m1911.m1911,
                           bullet=gun_parts.bullets_40sw_weighted,
                           magazine=magazines.m1911_mag_40sw_8,
                           optics=optics_test,
                           part_dict={
                               "M1911 Frame": {
                                   m1911.m1911_frame_gov_ss: (10, 30, 50),
                                   m1911.m1911_frame_gov_alloy: (2, 6, 30),
                                   m1911.m1911_frame_gov_ss_tac: (1, 4, 20),
                                   m1911.m1911_frame_gov_alloy_tac: (0, 2, 12),
                                   m1911.m1911_frame_gov_ss_auto: (0, 1, 1),
                                   m1911.m1911_frame_gov_alloy_auto: (0, 0, 1),
                                   m1911.m1911_frame_gov_ss_tac_auto: (0, 0, 1),
                                   m1911.m1911_frame_gov_alloy_tac_auto: (0, 0, 1), },
                               "M1911 Barrel": {m1911.m1911_barrel_gov_40sw: 200,
                                                m1911.m1911_barrel_commander_40sw: 15,
                                                m1911.m1911_barrel_long_40sw: 5,
                                                m1911.m1911_barrel_gov_threaded_40sw: 100,
                                                m1911.m1911_barrel_commander_threaded_40sw: 7,
                                                m1911.m1911_barrel_long_threaded_40sw: 2, },
                               "M1911 Slide": {m1911.m1911_slide_gov_40: 400,
                                               m1911.m1911_slide_commander_40: 75,
                                               m1911.m1911_slide_long_40: 10,
                                               m1911.m1911_slide_gov_light_40: 50,
                                               m1911.m1911_slide_commander_light_40: 20,
                                               m1911.m1911_slide_long_light_40: 5,
                                               m1911.m1911_slide_gov_40_optic: 100,
                                               m1911.m1911_slide_commander_40_optic: 50,
                                               m1911.m1911_slide_long_40_optic: 8,
                                               m1911.m1911_slide_gov_light_40_optic: 7,
                                               m1911.m1911_slide_commander_light_40_optic: 4,
                                               m1911.m1911_slide_long_light_40_optic: 2,
                                               },
                               "M1911 Grip Panels": {m1911.m1911_grip_magpul: 200,
                                                     m1911.m1911_grip_rectac: 20,
                                                     m1911.m1911_grip_wood: 15,
                                                     m1911.m1911_grip_operator: 10,
                                                     m1911.m1911_grip_palmswell: 6,
                                                     m1911.m1911_grip_hogue: 5,
                                                     m1911.m1911_rec_stock: 2,
                                                     },
                               "M1911 Optics Mount": {None: 20, m1911.m1911_bridge_mount: 1},
                               "Muzzle Device": {None: 200, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                                 m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10,
                                                 attachments.suppressor_sandman: 2},
                               "Underbarrel Accessory": {
                                   None: 500,
                                   attachments.grip_promag_vertical: 10,
                                   attachments.grip_jem_vertical: 10,
                                   attachments.grip_aimtac_short: 5,
                                   attachments.grip_hipoint_folding: 5,
                               },
                           },
                           allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
                                               'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
                                               'Optic', 'Muzzle Device']
                           )

"""
M1 Carbine
"""

m1_carbine_gun = PremadeWeapon(gun_item=m1_carbine.m1_carbine,
                               bullet={bullets.round_30carb_110_jhp: 1, bullets.round_30carb_110_fmj: 4},
                               magazine={magazines.m1_carbine_15rd: 5, magazines.m1_carbine_30rd: 1},
                               optics=optics_test,
                               part_dict={
                                   "M1 Reciever": m1_carbine.m1_reciever,
                                   "M1/M2 Stock": {
                                       m1_carbine.m1_stock: 200,
                                       m1_carbine.m1_stock_ebr: 4,
                                       m1_carbine.m1_stock_enforcer: 5,
                                       m1_carbine.m1_stock_springfield: 10
                                   },
                                   "M1/M2 Barrel": {
                                       m1_carbine.m1_barrel: 10,
                                       m1_carbine.m1_barrel_enforcer: 10,
                                       m1_carbine.m1_barrel_threaded: 1,
                                       m1_carbine.m1_barrel_enforcer_threaded: 1,
                                   },
                                   "AR Grip": {
                                       ar15.ar_grip_trybe: 15,
                                       ar15.ar_grip_moe: 90,
                                       ar15.ar_grip_hogue: 5,
                                       ar15.ar_grip_strikeforce: 10,
                                       ar15.ar_grip_a2: 100,
                                       ar15.ar_grip_stark: 15,
                                   },
                                   "AR Stock": {
                                       ar15.ar_stock_m16a2: 100,
                                       ar15.ar_stock_moe: 90,
                                       ar15.ar_stock_ubr: 10,
                                       ar15.ar_stock_danieldefense: 15,
                                       ar15.ar_stock_prs: 5,
                                       ar15.ar_stock_maxim_cqb: 5,
                                   },
                                   "M1/M2 Carbine Optic Mount": {None: 30, m1_carbine.m1_m6b_mount: 1,
                                                                 m1_carbine.m1_sk_mount: 1},
                                   "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                          attachments.adapter_mlok_picrail_short: 1},
                                   "Muzzle Device": {
                                       attachments.suppressor_obsidian_9: 1,
                                       attachments.suppressor_wolfman_9mm: 1,
                                       ar15.ar15_muzzle_flashhider: 100,
                                       ar15.ar15_muzzle_st6012: 8,
                                       ar15.ar15_muzzle_mi_mb4: 5,
                                       ar15.ar15_muzzle_cobra: 3, },
                                   "Underbarrel Accessory": {
                                       None: 500,
                                       attachments.grip_hera_cqr: 3,
                                       attachments.grip_promag_vertical: 10,
                                       attachments.grip_jem_vertical: 10,
                                       attachments.grip_magpul_angled: 6,
                                       attachments.grip_magpul_mvg: 8,
                                       attachments.grip_aimtac_short: 7,
                                       attachments.grip_magpul_handstop: 6,
                                       attachments.grip_hipoint_folding: 3,
                                   },
                               },
                               allowed_part_types=['M1 Reciever', 'M1/M2 Stock', 'M1/M2 Barrel',
                                                   'M1/M2 Carbine Optic Mount', 'Attachment Adapter',
                                                   'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
                                                   'Optic', 'Muzzle Adapter']
                               )

m2_carbine_gun = PremadeWeapon(gun_item=m1_carbine.m2_carbine,
                               bullet={bullets.round_30carb_110_jhp: 1, bullets.round_30carb_110_fmj: 4},
                               magazine={magazines.m1_carbine_15rd: 5, magazines.m1_carbine_30rd: 1},
                               optics=optics_test,
                               part_dict={
                                   "M2 Reciever": m1_carbine.m2_reciever,
                                   "M1/M2 Stock": {
                                       m1_carbine.m1_stock: 200,
                                       m1_carbine.m1_stock_ebr: 4,
                                       m1_carbine.m1_stock_enforcer: 5,
                                       m1_carbine.m1_stock_springfield: 10
                                   },
                                   "M1/M2 Barrel": {
                                       m1_carbine.m1_barrel: 10,
                                       m1_carbine.m1_barrel_enforcer: 10,
                                       m1_carbine.m1_barrel_threaded: 1,
                                       m1_carbine.m1_barrel_enforcer_threaded: 1,
                                   },
                                   "AR Grip": {
                                       ar15.ar_grip_trybe: 15,
                                       ar15.ar_grip_moe: 90,
                                       ar15.ar_grip_hogue: 5,
                                       ar15.ar_grip_strikeforce: 10,
                                       ar15.ar_grip_a2: 100,
                                       ar15.ar_grip_stark: 15,
                                   },
                                   "AR Stock": {
                                       ar15.ar_stock_m16a2: 100,
                                       ar15.ar_stock_moe: 90,
                                       ar15.ar_stock_ubr: 10,
                                       ar15.ar_stock_danieldefense: 15,
                                       ar15.ar_stock_prs: 5,
                                       ar15.ar_stock_maxim_cqb: 5,
                                   },
                                   "M1/M2 Carbine Optic Mount": {None: 30, m1_carbine.m1_m6b_mount: 1,
                                                                 m1_carbine.m1_sk_mount: 1},
                                   "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                          attachments.adapter_mlok_picrail_short: 1},
                                   "Muzzle Device": {
                                       attachments.suppressor_obsidian_9: 1,
                                       attachments.suppressor_wolfman_9mm: 1,
                                       ar15.ar15_muzzle_flashhider: 100,
                                       ar15.ar15_muzzle_st6012: 8,
                                       ar15.ar15_muzzle_mi_mb4: 5,
                                       ar15.ar15_muzzle_cobra: 3, },
                                   "Underbarrel Accessory": {
                                       None: 500,
                                       attachments.grip_hera_cqr: 3,
                                       attachments.grip_promag_vertical: 10,
                                       attachments.grip_jem_vertical: 10,
                                       attachments.grip_magpul_angled: 6,
                                       attachments.grip_magpul_mvg: 8,
                                       attachments.grip_aimtac_short: 7,
                                       attachments.grip_magpul_handstop: 6,
                                       attachments.grip_hipoint_folding: 3,
                                   },
                               },
                               allowed_part_types=['M2 Reciever', 'M1/M2 Stock', 'M1/M2 Barrel',
                                                   'M1/M2 Carbine Optic Mount', 'Attachment Adapter',
                                                   'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
                                                   'Optic', 'Muzzle Adapter']
                               )

"""
M14 / M1A
"""

m14_gun = PremadeWeapon(gun_item=m14.m14,
                        bullet=gun_parts.bullets_308_weighted,
                        magazine={magazines.m14_10rd: (1, 5, 2, 50,  0),
                                  magazines.m14_20rd: (0, 1, 1, 100, 75),
                                  magazines.m14_50rd: (0, 0, 0, 3,   3)},
                        optics=optics_test,
                        part_dict={
                            "M14 - Reciever": {m14.m14_reciever:      (1, 50, 20, 15,),
                                               m14.m14_reciever_auto: (0, 1,  1,  1,)},
                            "M14/M1A Stock": {m14.m14_stock_fiberglass: 40,
                                              m14.m14_stock_wood: 40,
                                              m14.m14_stock_archangel: 10,
                                              m14.m14_stock_bullpup: 2,
                                              m14.m14_stock_ebr: 5,
                                              m14.m14_stock_vltor: 6},
                            "M14/M1A Barrel": {m14.m14_barrel: 15, m14.m14_barrel_18in: 3, m14.m14_barrel_socom: 1},
                            "AR Grip": {
                                ar15.ar_grip_trybe: 15,
                                ar15.ar_grip_moe: 90,
                                ar15.ar_grip_hogue: 5,
                                ar15.ar_grip_strikeforce: 10,
                                ar15.ar_grip_a2: 100,
                                ar15.ar_grip_stark: 15,
                            },
                            "AR Stock": {
                                ar15.ar_stock_m16a2: 100,
                                ar15.ar_stock_moe: 90,
                                ar15.ar_stock_ubr: 10,
                                ar15.ar_stock_danieldefense: 15,
                                ar15.ar_stock_prs: 5,
                                ar15.ar_stock_maxim_cqb: 5,
                            },
                            "Thread Adapter": {None: 15,
                                               attachments.thread_adapter_m14_5824: 1},
                            "M14/M1A Picatinny Rail Optic Mount": {None: 15, m14.m14_optic_mount: 1},
                            "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                   attachments.adapter_mlok_picrail_short: 1},
                            "Underbarrel Accessory": {
                                None: 500,
                                attachments.grip_hera_cqr: 3,
                                attachments.grip_promag_vertical: 10,
                                attachments.grip_jem_vertical: 10,
                                attachments.grip_magpul_angled: 6,
                                attachments.grip_magpul_mvg: 8,
                                attachments.grip_aimtac_short: 7,
                                attachments.grip_magpul_handstop: 6,
                                attachments.grip_hipoint_folding: 3,
                            },
                            "Muzzle Device": {m14.m14_muzzle_usgi: 100,
                                              m14.m14_muzzle_uscg_brake: 3,
                                              m14.m14_muzzle_vais_brake: 8,
                                              m14.m14_muzzle_synergy_brake: 4,
                                              ar15.ar15_300_muzzle_flashhider: 100,
                                              ar15.ar15_300_muzzle_cobra: 8,
                                              ar15.ar15_300_muzzle_pegasus: 5,
                                              ar15.ar15_300_muzzle_strike: 3,
                                              },
                        },
                        allowed_part_types=['M14 - Reciever', 'M14/M1A Stock', 'M14/M1A Barrel',
                                            'M14/M1A Picatinny Rail Optic Mount', 'Attachment Adapter',
                                            'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device', 'Optic']
                        )

"""
R870
"""

r870_gun = PremadeWeapon(gun_item=r870.rem_870,
                         bullet=gun_parts.bullets_12ga_weighted,
                         magazine=magazines.r870_6rd,
                         optics=optics_test,
                         part_dict={
                             "Model 870 Reciever": {r870.reciever_r870_4rd: (10, 10, 30, 15),
                                                    r870.reciever_r870dm:   (0,  0,  1,  4),
                                                    r870.reciever_r870_6rd: (1,  2,  10, 30)},
                             "Model 870 Barrel": {r870.r870_barrel_26:       (40, 40, 20, 10),
                                                  r870.r870_barrel_18:       (2,  4,  4,  4),
                                                  r870.r870_barrel_t14:      (1,  2,  2,  2),
                                                  r870.r870_barrel_18_bead:  (2,  4,  4,  4),
                                                  r870.r870_barrel_t14_bead: (1,  2,  2,  2)},
                             "Model 870 Stock": {r870.r870_stock: 300,
                                                 r870.r870_stock_polymer: 300,
                                                 r870.r870_stock_magpul: 100,
                                                 r870.r870_stock_shockwave: 10,
                                                 r870.r870_stock_pistol: 15,
                                                 r870.r870_stock_maverick: 40,
                                                 r870.r870_stock_sterling: 35,
                                                 r870.r870_ar_stock_adapter: 10},
                             "AR Grip": {
                                 ar15.ar_grip_trybe: 15,
                                 ar15.ar_grip_moe: 90,
                                 ar15.ar_grip_hogue: 5,
                                 ar15.ar_grip_strikeforce: 10,
                                 ar15.ar_grip_a2: 100,
                                 ar15.ar_grip_stark: 15,
                             },
                             "AR Stock": {
                                 ar15.ar_stock_m16a2: 100,
                                 ar15.ar_stock_moe: 90,
                                 ar15.ar_stock_ubr: 10,
                                 ar15.ar_stock_danieldefense: 15,
                                 ar15.ar_stock_prs: 5,
                                 ar15.ar_stock_maxim_cqb: 5,
                             },
                             "Model 870 Forend": {r870.r870_forend: 100,
                                                  r870.r870_forend_polymer: 100,
                                                  r870.r870_forend_magpul: 25,
                                                  r870.r870_forend_tacstar: 15,
                                                  r870.r870_forend_voa: 10},
                             "Model 870 Choke": {
                                 r870.r870_choke_im: 15,
                                 r870.r870_choke_modified: 50,
                                 r870.r870_choke_cylinder: 300,
                                 r870.r870_choke_improved_ported: 10,
                                 r870.r870_choke_cylinder_ported: 15,
                             },
                             "Model 870 Magazine Extension": {
                                 None: 150,
                                 r870.r870_extension_2rd: 10,
                                 r870.r870_extension_4rd: 5,
                                 r870.r870_extension_6rd: 2,
                             },
                             "Model 870 Optics Mount": {
                                 None: 50,
                                 r870.r870_optic_picrail: 5,
                                 r870.r870_optic_picrail_ghost: 3,
                             },
                         },
                         allowed_part_types=['Model 870 Reciever', 'Model 870 Barrel', 'Model 870 Stock',
                                             'Model 870 Forend', 'Model 870 Choke', 'Attachment Adapter',
                                             'Model 870 Magazine Extension', 'Model 870 Optics Mount',
                                             'Underbarrel Accessory', 'Side Mounted Accessory', 'Optic']
                         )

supershorty_gun = PremadeWeapon(gun_item=r870.rem_870,
                                bullet=gun_parts.bullets_12ga_weighted,
                                magazine={},
                                optics=optics_test,
                                part_dict={
                                    "Model 870 Reciever": {r870.reciever_r870_shorty: 1},
                                    "Model 870 Barrel": {r870.r870_barrel_shorty: 1},
                                    "Model 870 Stock": {r870.r870_stock: 300,
                                                        r870.r870_stock_polymer: 300,
                                                        r870.r870_stock_magpul: 100,
                                                        r870.r870_stock_shockwave: 10,
                                                        r870.r870_stock_pistol: 15,
                                                        r870.r870_stock_maverick: 40,
                                                        r870.r870_stock_sterling: 35,
                                                        r870.r870_ar_stock_adapter: 10},
                                    "AR Grip": {
                                        ar15.ar_grip_trybe: 15,
                                        ar15.ar_grip_moe: 90,
                                        ar15.ar_grip_hogue: 5,
                                        ar15.ar_grip_strikeforce: 10,
                                        ar15.ar_grip_a2: 100,
                                        ar15.ar_grip_stark: 15,
                                    },
                                    "AR Stock": {
                                        ar15.ar_stock_m16a2: 100,
                                        ar15.ar_stock_moe: 90,
                                        ar15.ar_stock_ubr: 10,
                                        ar15.ar_stock_danieldefense: 15,
                                        ar15.ar_stock_prs: 5,
                                        ar15.ar_stock_maxim_cqb: 5,
                                    },
                                    "Model 870 Choke": {
                                        r870.r870_choke_im: 15,
                                        r870.r870_choke_modified: 50,
                                        r870.r870_choke_cylinder: 300,
                                        r870.r870_choke_improved_ported: 10,
                                        r870.r870_choke_cylinder_ported: 15,
                                    },
                                    "Model 870 Magazine Extension": {
                                        None: 150,
                                        r870.r870_extension_2rd: 10,
                                        r870.r870_extension_4rd: 5,
                                        r870.r870_extension_6rd: 2,
                                    },
                                    "Model 870 Optics Mount": {
                                        None: 50,
                                        r870.r870_optic_picrail: 5,
                                        r870.r870_optic_picrail_ghost: 3,
                                    },
                                },
                                allowed_part_types=['Super Shorty Reciever', 'Model 870 Barrel', 'Model 870 Stock',
                                                    'Model 870 Forend', 'Model 870 Choke', 'Attachment Adapter',
                                                    'Model 870 Magazine Extension', 'Model 870 Optics Mount',
                                                    'Underbarrel Accessory', 'Side Mounted Accessory', 'Optic']
                                )

"""
S&W M629
"""

m629_gun = PremadeWeapon(gun_item=misc.sw629,
                         bullet=gun_parts.bullets_44mag_weighted,
                         magazine={},
                         clip=magazines.m629_clip,
                         optics=optics_test,
                         part_dict={
                             "S&W .44 Frame": misc.sw629_frame,
                             "S&W .44 Barrel": {misc.sw629_barrel: 400,
                                                misc.sw629_barrel_stealth: 10,
                                                misc.sw629_barrel_5in: 150,
                                                misc.sw629_barrel_4in: 75,
                                                },
                             "S&W N-Frame Optic Mount": {misc.sw629_optic_pistol: 1,
                                                         misc.sw629_optic_pistol_picrail: 1,
                                                         None: 20,
                                                         },
                         },
                         allowed_part_types=['S&W .44 Frame', 'S&W .44 Barrel', 'S&W N-Frame Optic Mount', 'Optic']
                         )

"""
S&W M610
"""

m610_gun = PremadeWeapon(gun_item=misc.sw610,
                         bullet=gun_parts.bullets_10mm_40sw_weighted,
                         magazine={},
                         clip=magazines.m610_clip,
                         optics=optics_test,
                         part_dict={
                             "S&W 10mm Frame": misc.sw610_frame,
                             "S&W 10mm Barrel": {misc.sw610_barrel: 6,
                                                 misc.sw610_barrel_4in: 1,
                                                 },
                             "S&W N-Frame Optic Mount": {misc.sw629_optic_pistol: 1,
                                                         misc.sw629_optic_pistol_picrail: 1,
                                                         None: 20,
                                                         },
                         },
                         allowed_part_types=['S&W 10mm Frame', 'S&W 10mm Barrel', 'S&W N-Frame Optic Mount', 'Optic']
                         )

"""
DE XIX
"""

dexix_gun = PremadeWeapon(gun_item=misc.de44,
                          bullet=gun_parts.bullets_44mag_weighted,
                          magazine=magazines.de44_mag,
                          optics=optics_test,
                          part_dict={
                              "DE .44 Frame": misc.sw629_frame,
                              "DE .44 Barrel": {misc.de44_barrel: 400,
                                                misc.de44_barrel_imb: 20,
                                                misc.de44_barrel_10in: 15,
                                                misc.de44_barrel_10in_threaded: 8,
                                                },
                              "DE .44 Slide": misc.de44_slide,
                              "Muzzle Device": {
                                  ar15.ar15_300_muzzle_flashhider: 100,
                                  ar15.ar15_300_muzzle_cobra: 8,
                                  ar15.ar15_300_muzzle_pegasus: 5,
                                  ar15.ar15_300_muzzle_strike: 3,
                              },

                          },
                          allowed_part_types=['DE .44 Frame', 'DE .44 Barrel', 'DE .44 Slide', 'Optic',
                                              'Muzzle Device']
                          )

"""
TT33
"""

tt33_gun = PremadeWeapon(gun_item=misc.tt33,
                         bullet=gun_parts.bullets_76225_weighted,
                         magazine=magazines.tt33_magazine,
                         optics=optics_test,
                         part_dict={
                             "Tokarev TT Frame": misc.tt33_frame,
                             "Tokarev TT Barrel": misc.tt33_barrel,
                             "Tokarev TT Slide": {misc.tt33_slide: 20,
                                                  misc.tt33_slide_tactical: 1,
                                                  },
                             "Tokarev TT-33 Grip Panels": {misc.tt33_grip: 15,
                                                           misc.tt33_grip_rubberised: 1,
                                                           },
                             "Muzzle Device": {
                                 misc.tt33_compensator: 1,
                                 None: 20,
                             },

                         },
                         allowed_part_types=['Tokarev TT Frame', 'Tokarev TT Barrel', 'Tokarev TT Slide',
                                             'Tokarev TT-33 Grip Panels', 'Optic', 'Muzzle Device']
                         )

"""
H015
"""

h015_gun = PremadeWeapon(gun_item=misc.singleshot,
                         bullet=gun_parts.bullets_12ga_weighted,
                         magazine={},
                         optics=optics_test,
                         part_dict={
                             "H015 Reciever": misc.single_shot_reciever,
                             "H015 Barrel": {misc.single_shot_barrel: 10,
                                             misc.single_shot_barrel_short: 1},
                             "H015 Stock": {misc.single_shot_stock: 10,
                                            misc.h015_birdshead: 1,
                                            },
                             "Model 870 Choke": {
                                 r870.r870_choke_im: 15,
                                 r870.r870_choke_modified: 50,
                                 r870.r870_choke_cylinder: 300,
                                 r870.r870_choke_improved_ported: 10,
                                 r870.r870_choke_cylinder_ported: 40,
                             },
                             "H015 Optic Mount": {
                                 misc.h015_scope_mount: 1,
                                 None: 20,
                             },

                         },
                         allowed_part_types=['H015 Reciever', 'H015 Barrel', 'H015 Stock',
                                             'Model 870 Choke', 'H015 Optic Mount', 'Optic']
                         )

"""
M3
"""

m3_gun = PremadeWeapon(gun_item=misc.m3_greasegun,
                       bullet=gun_parts.bullets_45_weighted,
                       magazine=magazines.greasegun_mag,
                       optics=optics_test,
                       part_dict={
                           "M3 Reciever": {misc.m3_reciever: 20,
                                           misc.m3_reciever_picrail: 1},
                           "M3 Barrel": {misc.m3_barrel: 10,
                                         misc.m3_barrel_threaded: 1},
                           "M3 Stock": {misc.single_shot_stock: 10,
                                        misc.h015_birdshead: 1,
                                        },
                           "Muzzle Device": {
                               attachments.muzzle_nullifier: 3,
                               attachments.muzzle_kak_45: 5,
                               attachments.muzzle_kak_a2: 50,
                               attachments.suppressor_obsidian_45: 2,
                           },
                       },
                       allowed_part_types=['M3 Reciever', 'M3 Barrel', 'M3 Stock', 'Muzzle Device', 'Optic']
                       )

"""
PPSh
"""

ppsh_gun = PremadeWeapon(gun_item=misc.ppsh_41,
                         bullet=gun_parts.bullets_76225_weighted,
                         magazine={magazines.ppsh_mag_35rd: 20, magazines.ppsh_71rd: 1},
                         optics=optics_test,
                         part_dict={
                             "PPSh Reciever": misc.ppsh_reciever,
                             "PPSh Barrel": {misc.ppsh_barrel: 150,
                                             misc.ppsh_barrel_obrez: 5,
                                             # misc.ppsh_barrel_9mm: 10,
                                             # misc.ppsh_barrel_obrez_9mm: 1
                                             }
                             ,
                             "PPSh Dust Cover": {misc.ppsh_cover: 20,
                                                 misc.ppsh_cover_obrez: 20,
                                                 misc.ppsh_cover_tactical: 1,
                                                 misc.ppsh_cover_obrez_tactical: 1,
                                                 },
                             "PPSh Stock": {misc.ppsh_stock: 20,
                                            misc.ppsh_stock_obrez: 1,
                                            },
                         },
                         allowed_part_types=['PPSh Reciever', 'PPSh Barrel', 'PPSh Dust Cover', 'PPSh Stock', 'Optic']
                         )

"""
SVT-40
"""

svt40_gun = PremadeWeapon(gun_item=misc.svt,
                          bullet=gun_parts.bullets_54r_weighted,
                          magazine=magazines.svt_10rd,
                          clip=magazines.svt_clip,
                          optics=optics_test,
                          part_dict={
                              "SVT Reciever": {misc.svt_barrel: 29,
                                               misc.svt_barrel_auto: 1,
                                               },
                              "SVT Stock": misc.stock_svt,
                              "SVT Optics Mount": {misc.svt_pic_scope_mount: 1,
                                                   None: 15},
                          },
                          allowed_part_types=['SVT Reciever', 'SVT Stock', 'SVT Optics Mount', 'Optic']
                          )

# g_17 = PremadeWeapon(gun_item=glock17.glock_17,
#                      bullet=gun_parts.bullets_9mm_weighted,
#                      optics=optics_test,
#                      magazine={magazines.glock_mag_9mm: 1, magazines.glock_mag_9mm_33: 1,
#                                magazines.glock_mag_9mm_50: 1, magazines.glock_mag_9mm_100: 1},
#                      part_dict={
#                          "Glock Standard Frame": glock17.glock17_frame,
#                          "Glock 17 Barrel": {
#                              glock17.glock17_barrel: 1,
#                              glock17.glock17l_barrel: 1,
#                              glock17.glock_9in_barrel: 1,
#                              glock17.glock17_barrel_ported: 1,
#                              glock17.glock17l_barrel_ported: 1,
#                          },
#                          "G17 Slide": {
#                              glock17.glock17_slide: 1,
#                              glock17.glock17l_slide: 1,
#                              glock17.glock17_slide_optic: 1,
#                              glock17.glock17l_slide_optic: 1,
#                              glock17.glock17_slide_custom: 1,
#                              glock17.glock17l_slide_custom: 1,
#                          },
#                          "Glock Stock": {None: 1, glock17.glock_stock: 1, glock17.glock_pistol_brace: 1},
#                          "Glock Optics Mount": {None: 1, glock17.glock_pic_rail: 1},
#                          "Glock Base Plate": {None: 1, glock17.glock_switch: 1},
#                      },
#                      allowed_part_types=['Glock Standard Frame', 'Glock 17 Barrel', 'G17 Slide', 'Glock Stock',
#                                          'Muzzle Adapter', 'Glock Optics Mount', 'Glock Base Plate',
#                                          'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
#                      )
#
# g_40sw = PremadeWeapon(gun_item=glock17.glock_17,
#                        bullet=gun_parts.bullets_40sw_weighted,
#                        optics=optics_test,
#                        magazine={magazines.glock_mag_40: 1, magazines.glock_mag_40_22: 1,
#                                  magazines.glock_mag_40_50: 1},
#                        part_dict={
#                            "Glock Standard Frame": glock17.glock17_frame,
#                            "Glock .40 S&W Barrel": {
#                                glock17.glock22_barrel: 1,
#                                glock17.glock24_barrel: 1,
#                                glock17.glock22_barrel_ported: 1,
#                                glock17.glock24_barrel_ported: 1,
#                            },
#                            "Glock .40 S&W Slide": {
#                                glock17.glock22_slide: 1,
#                                glock17.glock24_barrel: 1,
#                                glock17.glock22_slide_optic: 1,
#                                glock17.glock24_slide_optic: 1,
#                                glock17.glock22_slide_custom: 1,
#                                glock17.glock24_slide_custom: 1,
#                            },
#                            "Glock Stock": {None: 1, glock17.glock_stock: 1, glock17.glock_pistol_brace: 1},
#                            "Glock Optics Mount": {None: 1, glock17.glock_pic_rail: 1},
#                            "Glock Base Plate": {None: 1, glock17.glock_switch: 1},
#                        },
#                        allowed_part_types=['Glock Standard Frame', 'Glock .40 S&W Barrel', 'Glock .40 S&W Slide',
#                                            'Glock Stock',
#                                            'Muzzle Adapter', 'Glock Optics Mount', 'Glock Base Plate',
#                                            'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
#                        )
#
# g_10mm = PremadeWeapon(gun_item=glock17.glock_17,
#                        bullet=gun_parts.bullets_10mm_weighted,
#                        optics=optics_test,
#                        magazine={magazines.glock_mag_10mm: 1, magazines.glock_mag_10mm_33: 1,
#                                  magazines.glock_mag_10mm_50: 1},
#                        part_dict={
#                            "Glock 10mm Frame": glock17.glock20_frame,
#                            "Glock 10mm Barrel": {
#                                glock17.glock20_barrel: 1,
#                                glock17.glock40_barrel: 1,
#                                glock17.glock20_barrel_ported: 1,
#                                glock17.glock40_barrel_ported: 1,
#                            },
#                            "Glock 10mm Slide": {
#                                glock17.glock20_slide: 1,
#                                glock17.glock40_slide: 1,
#                                glock17.glock20_slide_optic: 1,
#                                glock17.glock40_slide_optic: 1,
#                                glock17.glock20_slide_custom: 1,
#                                glock17.glock40_slide_custom: 1,
#                            },
#                            "Glock Stock": {None: 1, glock17.glock_brace_rt: 1},
#                            "Glock Base Plate": {None: 1, glock17.glock_switch: 1},
#                        },
#                        allowed_part_types=['Glock 10mm Frame', 'Glock 10mm Barrel', 'Glock 10mm Slide',
#                                            'Glock Stock',
#                                            'Muzzle Adapter', 'Glock Base Plate',
#                                            'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
#                        )
#
# g_50gi = PremadeWeapon(gun_item=glock17.glock_17,
#                        bullet=gun_parts.bullets_50gi_weighted,
#                        optics=optics_test,
#                        magazine=magazines.glock_mag_50gi,
#                        part_dict={
#                            "Glock 10mm Frame": glock17.glock20_frame,
#                            "Glock .50 GI Barrel": glock17.glock50_barrel,
#                            "Glock .50 GI Slide": {
#                                glock17.glock50_slide: 1,
#                                glock17.glock50_slide_optic: 1,
#                                glock17.glock50_slide_custom: 1,
#                            },
#                            "Glock Stock": {None: 1, glock17.glock_brace_rt: 1},
#                            "Glock Base Plate": {None: 1, glock17.glock_switch: 1},
#                        },
#                        allowed_part_types=['Glock 10mm Frame', 'Glock .50 GI Barrel', 'Glock .50 GI Slide',
#                                            'Glock Stock',
#                                            'Muzzle Adapter', 'Glock Base Plate',
#                                            'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
#                        )
#
# ar_optics = {**optics_test, **{ar15.ar_carry_handle: 1, attachments.irons_troy_rear: 1,
#                                attachments.irons_dd_rear: 1, attachments.irons_magpul_rear: 1,
#                                attachments.irons_sig_rear: 1}}
#
# ar15_weapon_300 = PremadeWeapon(gun_item=ar15.ar15,
#                                 bullet=gun_parts.bullets_300aac_weighted,
#                                 magazine={
#                                     magazines.stanag_10rd: (1, 1, 1, 1, 1),
#                                     magazines.stanag_20rd: (1, 1, 1, 1, 1),
#                                     magazines.stanag_30rd: (1, 1, 1, 1, 1),
#                                     magazines.stanag_40rd: (1, 1, 1, 1, 1),
#                                     magazines.stanag_50rd: (1, 1, 1, 1, 1),
#                                     magazines.stanag_60rd: (1, 1, 1, 1, 1),
#                                     magazines.stanag_100rd: (1, 1, 1, 1, 1),
#                                 },
#                                 optics=ar_optics,
#                                 part_dict={
#                                     "AR Lower Receiver": {ar15.lower_ar15: (1, 1, 1, 1, 1, 1),
#                                                           ar15.lower_ar15_auto: (1, 1, 1, 1, 1, 1)},
#                                     "AR Upper Receiver": {ar15.upper_ar_m16a2: 1,
#                                                           ar15.upper_ar_m16a4: 1},
#                                     "AR Buffer Tube": ar15.ar15_buffer_tube,
#                                     "AR Buffer": {ar15.ar15_buffer: 1,
#                                                   ar15.ar15_buffer_heavy: 1,
#                                                   ar15.ar15_buffer_light: 1},
#                                     "AR Barrel": {
#                                         ar15.ar_barrel_carbine_300: 1,
#                                         ar15.ar_barrel_carbine_300_carbinelen: 1,
#                                         ar15.ar_barrel_pistol_300: 1,
#                                         ar15.ar_barrel_pistol_300_pistollen: 1,
#                                     },
#                                     "AR Handguard": {
#                                         ar15.ar_handguard_m16a1: 1,
#                                         ar15.ar_handguard_m16a2: 1,
#                                         ar15.ar_handguard_m16a2_carbine: 1,
#                                         ar15.ar_handguard_magpul: 1,
#                                         ar15.ar_handguard_magpul_carbine: 1,
#                                         ar15.ar_handguard_aero: 1,
#                                         ar15.ar_handguard_aero_carbine: 1,
#                                         ar15.ar_handguard_aero_pistol: 1,
#                                         ar15.ar_handguard_faxon: 1,
#                                         ar15.ar_handguard_faxon_carbine: 1,
#                                         ar15.ar_handguard_faxon_pistol: 1,
#                                         ar15.ar_handguard_mk18: 1,
#                                     },
#                                     "AR Grip": {
#                                         ar15.ar_grip_trybe: 1,
#                                         ar15.ar_grip_moe: 1,
#                                         ar15.ar_grip_hogue: 1,
#                                         ar15.ar_grip_strikeforce: 1,
#                                         ar15.ar_grip_a2: 1,
#                                         ar15.ar_grip_stark: 1,
#                                     },
#                                     "AR Stock": {
#                                         None: 5,
#                                         ar15.ar_stock_m16a2: 1,
#                                         ar15.ar_stock_moe: 1,
#                                         ar15.ar_stock_ubr: 1,
#                                         ar15.ar_stock_danieldefense: 1,
#                                         ar15.ar_stock_prs: 1,
#                                         ar15.ar_stock_maxim_cqb: 1,
#                                     },
#                                     "AR Optics Mount": {None: 1, ar15.carry_handle_optic_mount: 1},
#                                     "Front Sight": {ar15.ar_front_sight: 1, attachments.irons_troy_front: 1,
#                                                     attachments.irons_dd_front: 1, attachments.irons_magpul_front: 1,
#                                                     attachments.irons_sig_front: 1, },
#                                     "Muzzle Device": {
#                                         ar15.ar15_300_muzzle_flashhider: 1,
#                                         ar15.ar15_300_muzzle_cobra: 1,
#                                         ar15.ar15_300_muzzle_pegasus: 1,
#                                         ar15.ar15_300_muzzle_strike: 1,
#                                         attachments.suppressor_sandman: 1,
#                                     },
#                                     "Attachment Adapter": {None: 1,
#                                                            attachments.adapter_mlok_picrail: 1,
#                                                            attachments.adapter_mlok_picrail_short: 1},
#                                     "Underbarrel Accessory": {
#                                         None: 1,
#                                         attachments.grip_hera_cqr: 1,
#                                         attachments.grip_promag_vertical: 1,
#                                         attachments.grip_jem_vertical: 1,
#                                         attachments.grip_magpul_angled: 1,
#                                         attachments.grip_magpul_mvg: 1,
#                                         attachments.grip_aimtac_short: 1,
#                                         attachments.grip_magpul_handstop: 1,
#                                         attachments.grip_hipoint_folding: 1,
#                                     },
#                                 },
#                                 allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
#                                                     'AR Buffer', 'AR Barrel',
#                                                     'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
#                                                     'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
#                                                     'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
#                                                     'Optic']
#                                 )
#
# ar10_weapon = PremadeWeapon(gun_item=ar15.ar15,
#                             bullet=gun_parts.bullets_308_weighted,
#                             magazine={
#                                 magazines.ar10_10rd: (1, 1, 1, 1, 1),
#                                 magazines.ar10_20rd: (1, 1, 1, 1, 1),
#                                 magazines.ar10_25rd: (1, 1, 1, 1, 1),
#                                 magazines.ar10_40rd: (1, 1, 1, 1, 1),
#                                 magazines.ar10_50rd: (1, 1, 1, 1, 1),
#                             },
#                             optics=ar_optics,
#                             part_dict={
#                                 "AR Lower Receiver": {ar15.lower_ar10: (1, 1, 1, 1),
#                                                       ar15.lower_ar10_auto: (1, 1, 1, 1)},
#                                 "AR Upper Receiver": ar15.upper_ar10,
#                                 "AR Buffer Tube": ar15.ar10_buffer_tube,
#                                 "AR Buffer": {ar15.ar10_buffer: 1,
#                                               ar15.ar10_buffer_heavy: 1,
#                                               ar15.ar10_buffer_light: 1},
#                                 "AR Barrel": {
#                                     ar15.ar_barrel_standard_308: 1,
#                                     ar15.ar_barrel_standard_308_midlen: 1,
#                                     ar15.ar_barrel_carbine_308_midlen: 1,
#                                     ar15.ar_barrel_carbine_308_carblen: 1,
#                                     ar15.ar_barrel_pistol_308_carblen: 1,
#                                     ar15.ar_barrel_pistol_308_pistollen: 1,
#                                 },
#                                 "AR Handguard": {
#                                     ar15.ar10_handguard_a2: 1,
#                                     ar15.ar10_handguard_a2_carbine: 1,
#                                     ar15.ar10_handguard_wilson: 1,
#                                     ar15.ar10_handguard_vseven: 1,
#                                 },
#                                 "AR Grip": {
#                                     ar15.ar_grip_trybe: 1,
#                                     ar15.ar_grip_moe: 1,
#                                     ar15.ar_grip_hogue: 1,
#                                     ar15.ar_grip_strikeforce: 1,
#                                     ar15.ar_grip_a2: 1,
#                                     ar15.ar_grip_stark: 1,
#                                 },
#                                 "AR Stock": {
#                                     None: 1,
#                                     ar15.ar_stock_m16a2: 1,
#                                     ar15.ar_stock_moe: 1,
#                                     ar15.ar_stock_ubr: 1,
#                                     ar15.ar_stock_danieldefense: 1,
#                                     ar15.ar_stock_prs: 1,
#                                     ar15.ar_stock_maxim_cqb: 1,
#                                 },
#                                 "Front Sight": {ar15.ar_front_sight: 1, attachments.irons_troy_front: 1,
#                                                 attachments.irons_dd_front: 1, attachments.irons_magpul_front: 1,
#                                                 attachments.irons_sig_front: 1, },
#                                 "Muzzle Device": {
#                                     ar15.ar15_300_muzzle_flashhider: 1,
#                                     ar15.ar15_300_muzzle_cobra: 1,
#                                     ar15.ar15_300_muzzle_pegasus: 1,
#                                     ar15.ar15_300_muzzle_strike: 1,
#                                     attachments.suppressor_sandman: 1,
#                                 },
#                                 "Attachment Adapter": {None: 1,
#                                                        attachments.adapter_mlok_picrail: 1,
#                                                        attachments.adapter_mlok_picrail_short: 1},
#                                 "Underbarrel Accessory": {
#                                     None: 1,
#                                     attachments.grip_hera_cqr: 1,
#                                     attachments.grip_promag_vertical: 1,
#                                     attachments.grip_jem_vertical: 1,
#                                     attachments.grip_magpul_angled: 1,
#                                     attachments.grip_magpul_mvg: 1,
#                                     attachments.grip_aimtac_short: 1,
#                                     attachments.grip_magpul_handstop: 1,
#                                     attachments.grip_hipoint_folding: 1,
#                                 },
#                             },
#                             allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
#                                                 'AR Buffer', 'AR Barrel',
#                                                 'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
#                                                 'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
#                                                 'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
#                                                 'Optic']
#                             )
#
# mcr_weapon = PremadeWeapon(gun_item=ar15.fightlite_mcr,
#                            bullet=gun_parts.bullets_556_weighted,
#                            magazine=magazines.mcr_100rd,
#                            optics=ar_optics,
#                            part_dict={
#                                "AR Lower Receiver": {ar15.lower_ar15: 1, ar15.lower_ar15_auto: 1},
#                                "MCR Upper Receiver": ar15.upper_mcr,
#                                "AR Grip": {
#                                    ar15.ar_grip_trybe: 1,
#                                    ar15.ar_grip_moe: 1,
#                                    ar15.ar_grip_hogue: 1,
#                                    ar15.ar_grip_strikeforce: 1,
#                                    ar15.ar_grip_a2: 1,
#                                    ar15.ar_grip_stark: 1,
#                                },
#                                "AR Stock": {
#                                    ar15.ar_stock_m16a2: 1,
#                                    ar15.ar_stock_moe: 1,
#                                    ar15.ar_stock_ubr: 1,
#                                    ar15.ar_stock_danieldefense: 1,
#                                    ar15.ar_stock_prs: 1,
#                                    ar15.ar_stock_maxim_cqb: 1,
#                                },
#                                "Front Sight": {ar15.ar_front_sight: 1, attachments.irons_troy_front: 1,
#                                                attachments.irons_dd_front: 1, attachments.irons_magpul_front: 1,
#                                                attachments.irons_sig_front: 1, },
#                                "Muzzle Device": {
#                                    ar15.ar15_muzzle_flashhider: 1,
#                                    ar15.ar15_muzzle_st6012: 1,
#                                    ar15.ar15_muzzle_mi_mb4: 1,
#                                    ar15.ar15_muzzle_cobra: 1,
#                                    attachments.suppressor_wolfman_9mm: 1,
#                                    attachments.suppressor_obsidian_45: 1,
#                                },
#                                "Attachment Adapter": {None: 1,
#                                                       attachments.adapter_mlok_picrail: 1,
#                                                       attachments.adapter_mlok_picrail_short: 1},
#                                "Underbarrel Accessory": {
#                                    None: 1,
#                                    attachments.grip_hera_cqr: 1,
#                                    attachments.grip_promag_vertical: 1,
#                                    attachments.grip_jem_vertical: 1,
#                                    attachments.grip_magpul_angled: 1,
#                                    attachments.grip_magpul_mvg: 1,
#                                    attachments.grip_aimtac_short: 1,
#                                    attachments.grip_magpul_handstop: 1,
#                                    attachments.grip_hipoint_folding: 1,
#                                },
#                            },
#                            allowed_part_types=['AR Lower Receiver', "MCR Upper Receiver", 'AR Buffer Tube',
#                                                'AR Grip', 'AR Stock', 'Attachment Adapter',
#                                                'Muzzle Adapter', 'Front Sight',
#                                                'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
#                                                'Optic']
#                            )
#
# ar15_weapon = PremadeWeapon(gun_item=ar15.ar15,
#                             bullet=gun_parts.bullets_556_weighted,
#                             magazine={
#                                 magazines.stanag_10rd: (1, 1, 1, 1, 1),
#                                 magazines.stanag_20rd: (1, 1, 1, 1, 1),
#                                 magazines.stanag_30rd: (1, 1, 1, 1, 1),
#                                 magazines.stanag_40rd: (1, 1, 1, 1, 1),
#                                 magazines.stanag_50rd: (1, 1, 1, 1, 1),
#                                 magazines.stanag_60rd: (1, 1, 1, 1, 1),
#                                 magazines.stanag_100rd: (1, 1, 1, 1, 1),
#                             },
#                             optics=ar_optics,
#                             part_dict={
#                                 "AR Lower Receiver": {ar15.lower_ar15: (1, 1, 1, 1, 1, 1),
#                                                       ar15.lower_ar15_auto: (1, 1, 1, 1, 1, 1)},
#                                 "AR Upper Receiver": {ar15.upper_ar_m16a2: 1,
#                                                       ar15.upper_ar_m16a4: 1},
#                                 "AR Buffer Tube": ar15.ar15_buffer_tube,
#                                 "AR Buffer": {ar15.ar15_buffer: 1,
#                                               ar15.ar15_buffer_heavy: 1,
#                                               ar15.ar15_buffer_light: 1},
#                                 "AR Barrel": {
#                                     ar15.ar_barrel_standard_556: 1,
#                                     ar15.ar_barrel_standard_556_midlen: 1,
#                                     ar15.ar_barrel_carbine_556: 1,
#                                     ar15.ar_barrel_carbine_556_carblen: 1,
#                                     ar15.ar_barrel_pistol_556: 1,
#                                     ar15.ar_barrel_pistol_556_pistollen: 1,
#                                 },
#                                 "AR Handguard": {
#                                     ar15.ar_handguard_m16a1: 1,
#                                     ar15.ar_handguard_m16a2: 1,
#                                     ar15.ar_handguard_m16a2_carbine: 1,
#                                     ar15.ar_handguard_magpul: 1,
#                                     ar15.ar_handguard_magpul_carbine: 1,
#                                     ar15.ar_handguard_aero: 1,
#                                     ar15.ar_handguard_aero_carbine: 1,
#                                     ar15.ar_handguard_aero_pistol: 1,
#                                     ar15.ar_handguard_faxon: 1,
#                                     ar15.ar_handguard_faxon_carbine: 1,
#                                     ar15.ar_handguard_faxon_pistol: 1,
#                                     ar15.ar_handguard_mk18: 1,
#                                 },
#                                 "AR Grip": {
#                                     ar15.ar_grip_trybe: 1,
#                                     ar15.ar_grip_moe: 1,
#                                     ar15.ar_grip_hogue: 1,
#                                     ar15.ar_grip_strikeforce: 1,
#                                     ar15.ar_grip_a2: 1,
#                                     ar15.ar_grip_stark: 1,
#                                 },
#                                 "AR Stock": {
#                                     None: 1,
#                                     ar15.ar_stock_m16a2: 1,
#                                     ar15.ar_stock_moe: 1,
#                                     ar15.ar_stock_ubr: 1,
#                                     ar15.ar_stock_danieldefense: 1,
#                                     ar15.ar_stock_prs: 1,
#                                     ar15.ar_stock_maxim_cqb: 1,
#                                 },
#                                 "AR Optics Mount": {None: 1, ar15.carry_handle_optic_mount: 1},
#                                 "Front Sight": {ar15.ar_front_sight: 1, attachments.irons_troy_front: 1,
#                                                 attachments.irons_dd_front: 1, attachments.irons_magpul_front: 1,
#                                                 attachments.irons_sig_front: 1, },
#                                 "Muzzle Device": {
#                                     ar15.ar15_muzzle_flashhider: 1,
#                                     ar15.ar15_muzzle_st6012: 1,
#                                     ar15.ar15_muzzle_mi_mb4: 1,
#                                     ar15.ar15_muzzle_cobra: 1,
#                                     attachments.suppressor_wolfman_9mm: 1,
#                                     attachments.suppressor_obsidian_45: 1,
#                                 },
#                                 "Attachment Adapter": {None: 1,
#                                                        attachments.adapter_mlok_picrail: 1,
#                                                        attachments.adapter_mlok_picrail_short: 1},
#                                 "Underbarrel Accessory": {
#                                     None: 1,
#                                     attachments.grip_hera_cqr: 1,
#                                     attachments.grip_promag_vertical: 1,
#                                     attachments.grip_jem_vertical: 1,
#                                     attachments.grip_magpul_angled: 1,
#                                     attachments.grip_magpul_mvg: 1,
#                                     attachments.grip_aimtac_short: 1,
#                                     attachments.grip_magpul_handstop: 1,
#                                     attachments.grip_hipoint_folding: 1,
#                                 },
#                             },
#                             allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', "AR Buffer Tube",
#                                                 'AR Buffer', 'AR Barrel',
#                                                 'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
#                                                 'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
#                                                 'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
#                                                 'Optic']
#                             )
#
# ar_9mm = PremadeWeapon(gun_item=ar15.ar15,
#                        bullet=gun_parts.bullets_9mm_weighted,
#                        magazine={
#                            magazines.glock_mag_9mm: (1, 1, 1, 1, 1),
#                            magazines.glock_mag_9mm_33: (1, 1, 1, 1, 1),
#                            magazines.glock_mag_9mm_50: (1, 1, 1, 1, 1),
#                            magazines.glock_mag_9mm_100: (1, 1, 1, 1, 1),
#                        },
#                        optics=ar_optics,
#                        part_dict={
#                            "AR Lower Receiver": {ar15.lower_ar_9mm: (1, 1, 1, 1, 1),
#                                                  ar15.lower_ar_9mm_auto: (1, 1, 1, 1, 1)},
#                            "AR Upper Receiver": ar15.upper_ar_9mm,
#                            "AR Buffer Tube": ar15.ar15_buffer_tube,
#                            "AR Buffer": {ar15.ar15_buffer: 1,
#                                          ar15.ar15_buffer_heavy: 1,
#                                          ar15.ar15_buffer_light: 1},
#                            "AR Barrel": {
#                                ar15.ar_barrel_9mm_11in: 1,
#                                ar15.ar_barrel_9mm_16in: 1,
#                                ar15.ar_barrel_9mm_4in: 1,
#                            },
#                            "AR Handguard": {
#                                ar15.ar_handguard_m16a1: 1,
#                                ar15.ar_handguard_m16a2: 1,
#                                ar15.ar_handguard_m16a2_carbine: 1,
#                                ar15.ar_handguard_magpul: 1,
#                                ar15.ar_handguard_magpul_carbine: 1,
#                                ar15.ar_handguard_aero: 1,
#                                ar15.ar_handguard_aero_carbine: 1,
#                                ar15.ar_handguard_aero_pistol: 1,
#                                ar15.ar_handguard_faxon: 1,
#                                ar15.ar_handguard_faxon_carbine: 1,
#                                ar15.ar_handguard_faxon_pistol: 1,
#                                ar15.ar_handguard_mk18: 1,
#                            },
#                            "AR Grip": {
#                                ar15.ar_grip_trybe: 1,
#                                ar15.ar_grip_moe: 1,
#                                ar15.ar_grip_hogue: 1,
#                                ar15.ar_grip_strikeforce: 1,
#                                ar15.ar_grip_a2: 1,
#                                ar15.ar_grip_stark: 1,
#                            },
#                            "AR Stock": {
#                                None: 1,
#                                ar15.ar_stock_m16a2: 1,
#                                ar15.ar_stock_moe: 1,
#                                ar15.ar_stock_ubr: 1,
#                                ar15.ar_stock_danieldefense: 1,
#                                ar15.ar_stock_prs: 1,
#                                ar15.ar_stock_maxim_cqb: 1,
#                            },
#                            "Front Sight": {ar15.ar_front_sight: 1, attachments.irons_troy_front: 1,
#                                            attachments.irons_dd_front: 1, attachments.irons_magpul_front: 1,
#                                            attachments.irons_sig_front: 1, },
#                            "Muzzle Device": {
#                                None: 1,
#                                ar15.ar15_muzzle_flashhider: 1,
#                                ar15.ar15_muzzle_st6012: 1,
#                                ar15.ar15_muzzle_mi_mb4: 1,
#                                ar15.ar15_muzzle_cobra: 1,
#                                attachments.suppressor_wolfman_9mm: 1,
#                                attachments.suppressor_obsidian_9: 1,
#                            },
#                            "Attachment Adapter": {None: 1,
#                                                   attachments.adapter_mlok_picrail: 1,
#                                                   attachments.adapter_mlok_picrail_short: 1},
#                            "Underbarrel Accessory": {
#                                None: 1,
#                                attachments.grip_hera_cqr: 1,
#                                attachments.grip_promag_vertical: 1,
#                                attachments.grip_jem_vertical: 1,
#                                attachments.grip_magpul_angled: 1,
#                                attachments.grip_magpul_mvg: 1,
#                                attachments.grip_aimtac_short: 1,
#                                attachments.grip_magpul_handstop: 1,
#                                attachments.grip_hipoint_folding: 1,
#                            },
#                        },
#                        allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
#                                            'AR Buffer', 'AR Barrel',
#                                            'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
#                                            'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
#                                            'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
#                                            'Optic']
#                        )
#
# ar_40sw = PremadeWeapon(gun_item=ar15.ar15,
#                         bullet=gun_parts.bullets_40sw_weighted,
#                         magazine={
#                             magazines.glock_mag_40: (1, 1, 1, 1, 1),
#                             magazines.glock_mag_40_22: (1, 1, 1, 1, 1),
#                             magazines.glock_mag_40_50: (1, 1, 1, 1, 1),
#                         },
#                         optics=ar_optics,
#                         part_dict={
#                             "AR Lower Receiver": {ar15.lower_ar_9mm: (1, 1, 1, 1, 1),
#                                                   ar15.lower_ar_9mm_auto: (1, 1, 1, 1, 1)},
#                             "AR Upper Receiver": ar15.upper_ar_9mm,
#                             "AR Buffer Tube": ar15.ar15_buffer_tube,
#                             "AR Buffer": {ar15.ar15_buffer: 1,
#                                           ar15.ar15_buffer_heavy: 1,
#                                           ar15.ar15_buffer_light: 1},
#                             "AR Barrel": {
#                                 ar15.ar_barrel_40_12in: 1,
#                                 ar15.ar_barrel_40_16in: 1,
#                                 ar15.ar_barrel_40_4in: 1,
#                             },
#                             "AR Handguard": {
#                                 ar15.ar_handguard_m16a1: 1,
#                                 ar15.ar_handguard_m16a2: 1,
#                                 ar15.ar_handguard_m16a2_carbine: 1,
#                                 ar15.ar_handguard_magpul: 1,
#                                 ar15.ar_handguard_magpul_carbine: 1,
#                                 ar15.ar_handguard_aero: 1,
#                                 ar15.ar_handguard_aero_carbine: 1,
#                                 ar15.ar_handguard_aero_pistol: 1,
#                                 ar15.ar_handguard_faxon: 1,
#                                 ar15.ar_handguard_faxon_carbine: 1,
#                                 ar15.ar_handguard_faxon_pistol: 1,
#                                 ar15.ar_handguard_mk18: 1,
#                             },
#                             "AR Grip": {
#                                 ar15.ar_grip_trybe: 1,
#                                 ar15.ar_grip_moe: 1,
#                                 ar15.ar_grip_hogue: 1,
#                                 ar15.ar_grip_strikeforce: 1,
#                                 ar15.ar_grip_a2: 1,
#                                 ar15.ar_grip_stark: 1,
#                             },
#                             "AR Stock": {
#                                 None: 1,
#                                 ar15.ar_stock_m16a2: 1,
#                                 ar15.ar_stock_moe: 1,
#                                 ar15.ar_stock_ubr: 1,
#                                 ar15.ar_stock_danieldefense: 1,
#                                 ar15.ar_stock_prs: 1,
#                                 ar15.ar_stock_maxim_cqb: 1,
#                             },
#                             "Front Sight": {ar15.ar_front_sight: 1, attachments.irons_troy_front: 1,
#                                             attachments.irons_dd_front: 1, attachments.irons_magpul_front: 1,
#                                             attachments.irons_sig_front: 1, },
#                             "Muzzle Device": {
#                                 None: 1,
#                                 attachments.muzzle_maxtac: 1,
#                                 attachments.suppressor_octane45: 1
#                             },
#                             "Attachment Adapter": {None: 1,
#                                                    attachments.adapter_mlok_picrail: 1,
#                                                    attachments.adapter_mlok_picrail_short: 1},
#                             "Underbarrel Accessory": {
#                                 None: 1,
#                                 attachments.grip_hera_cqr: 1,
#                                 attachments.grip_promag_vertical: 1,
#                                 attachments.grip_jem_vertical: 1,
#                                 attachments.grip_magpul_angled: 1,
#                                 attachments.grip_magpul_mvg: 1,
#                                 attachments.grip_aimtac_short: 1,
#                                 attachments.grip_magpul_handstop: 1,
#                                 attachments.grip_hipoint_folding: 1,
#                             },
#                         },
#                         allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer Tube',
#                                             'AR Buffer', 'AR Barrel',
#                                             'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
#                                             'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
#                                             'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
#                                             'Optic']
#                         )
#
# """
# AK 7.62
# """
#
# ak47_weapon = PremadeWeapon(gun_item=ak.ak,
#                             bullet=gun_parts.bullets_752_weighted,
#                             magazine={
#                                 magazines.ak762_10rd: (1, 1, 1, 1, 1),
#                                 magazines.ak762_20rd: (1, 1, 1, 1, 1),
#                                 magazines.ak762_30rd: (1, 1, 1, 1, 1),
#                                 magazines.ak762_40rd: (1, 1, 1, 1, 1),
#                                 magazines.ak762_60rd: (1, 1, 1, 1, 1),
#                                 magazines.ak762_75rd: (1, 1, 1, 1, 1),
#                                 magazines.ak762_100rd: (1, 1, 1, 1, 1)},
#                             optics=optics_test,
#                             part_dict={
#                                 "AK Reciever": {ak.reciever_akm: (1, 1, 1, 1, 1),
#                                                 ak.reciever_akm_auto: (1, 1, 1, 1, 1)},
#                                 "AK Barrel": {ak.barrel_ak762: 1, ak.barrel_rpk762: 1, ak.barrel_ak762_short: 1},
#                                 "Thread Adapter": {None: 1,
#                                                    attachments.thread_adapter_141_24mm: 1},
#                                 "AK Handguard": {
#                                     ak.handguard_akm: 1,
#                                     ak.handguard_amd65: 1,
#                                     ak.handguard_ak74: 1,
#                                     ak.handguard_romanian: 1,
#                                     ak.handguard_ak100: 1,
#                                     ak.handguard_B10M: 1,
#                                     ak.handguard_leader: 1,
#                                     ak.handguard_magpul: 1,
#                                 },
#                                 "AK Grip": {
#                                     ak.grip_akm: 1,
#                                     ak.grip_ak12: 1,
#                                     ak.grip_sniper: 1,
#                                     ak.grip_moe: 1,
#                                     ak.grip_rk3: 1,
#                                     ak.grip_tapco: 1,
#                                     ak.grip_skeletonised: 1,
#                                     ak.grip_hogue: 1,
#                                     ak.grip_fab: 1,
#                                 },
#                                 "AK Stock": {
#                                     None: 1,
#                                     ak.stock_akm: 1,
#                                     ak.stock_rpk: 1,
#                                     ak.stock_ak74: 1,
#                                     ak.stock_ak100: 1,
#                                     ak.stock_ak_underfolder: 1,
#                                     ak.stock_ak_triangle: 1,
#                                     ak.stock_ak12: 1,
#                                     ak.stock_amd65: 1,
#                                     ak.stock_pt1: 1,
#                                     ak.stock_moe: 1,
#                                     ak.stock_zhukov: 1,
#                                 },
#                                 "AK Optics Mount": {None: 1, ak.accessory_dustcoverrail: 1,
#                                                     ak.accessory_railsidemount: 1},
#                                 "Muzzle Device": {
#                                     ak.muzzle_ak74: 1,
#                                     ak.muzzle_dtk: 1,
#                                     ak.muzzle_amd65: 1,
#                                     ak.muzzle_akm: 1,
#                                     ak.muzzle_akml: 1,
#                                     ak.muzzle_lantac: 1,
#                                     ak.muzzle_pbs4: 1,
#                                     ak.muzzle_pbs1: 1,
#                                     ak.muzzle_dynacomp: 1,
#                                 },
#                                 "Attachment Adapter": {None: 1, attachments.adapter_mlok_picrail: 1,
#                                                        attachments.adapter_mlok_picrail_short: 1},
#                                 "Underbarrel Accessory": {
#                                     None: 1,
#                                     attachments.grip_hera_cqr: 1,
#                                     attachments.grip_promag_vertical: 1,
#                                     attachments.grip_jem_vertical: 1,
#                                     attachments.grip_magpul_angled: 1,
#                                     attachments.grip_magpul_mvg: 1,
#                                     attachments.grip_aimtac_short: 1,
#                                     attachments.grip_magpul_handstop: 1,
#                                     attachments.grip_hipoint_folding: 1,
#                                 },
#                             },
#                             allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
#                                                 'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
#                                                 'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
#                                                 'AK Magazine Adapter', 'Optic']
#                             )
#
# ak74_weapon = PremadeWeapon(gun_item=ak.ak,
#                             bullet=gun_parts.bullets_545_weighted,
#                             magazine={magazines.ak545_30rd: (1, 1, 1, 1, 1),
#                                       magazines.ak545_45rd: (1, 1, 1, 1, 1),
#                                       magazines.ak545_60rd: (1, 1, 1, 1, 1),
#                                       magazines.ak545_100rd: (1, 1, 1, 1, 1)},
#                             optics=optics_test,
#                             part_dict={
#                                 "AK Reciever": {ak.reciever_ak74: (1, 1, 1, 1, 1),
#                                                 ak.reciever_ak74_auto: (1, 1, 1, 1, 1)},
#                                 "AK Barrel": {ak.barrel_ak545: 1, ak.barrel_rpk545: 1, ak.barrel_ak545_short: 1},
#                                 "Thread Adapter": {None: 1,
#                                                    attachments.thread_adapter_2415_5824: 1},
#                                 "AK Handguard": {
#                                     ak.handguard_akm: 1,
#                                     ak.handguard_amd65: 1,
#                                     ak.handguard_ak74: 1,
#                                     ak.handguard_romanian: 1,
#                                     ak.handguard_ak100: 1,
#                                     ak.handguard_B10M: 1,
#                                     ak.handguard_leader: 1,
#                                     ak.handguard_magpul: 1,
#                                 },
#                                 "AK Grip": {
#                                     ak.grip_akm: 1,
#                                     ak.grip_ak12: 1,
#                                     ak.grip_sniper: 1,
#                                     ak.grip_moe: 1,
#                                     ak.grip_rk3: 1,
#                                     ak.grip_tapco: 1,
#                                     ak.grip_skeletonised: 1,
#                                     ak.grip_hogue: 1,
#                                     ak.grip_fab: 1,
#                                 },
#                                 "AK Stock": {
#                                     None: 1,
#                                     ak.stock_akm: 1,
#                                     ak.stock_rpk: 1,
#                                     ak.stock_ak74: 1,
#                                     ak.stock_ak100: 1,
#                                     ak.stock_ak_underfolder: 1,
#                                     ak.stock_ak_triangle: 1,
#                                     ak.stock_ak12: 1,
#                                     ak.stock_amd65: 1,
#                                     ak.stock_pt1: 1,
#                                     ak.stock_moe: 1,
#                                     ak.stock_zhukov: 1,
#                                 },
#                                 "AK Optics Mount": {None: 1, ak.accessory_dustcoverrail: 1,
#                                                     ak.accessory_railsidemount: 1},
#                                 "Muzzle Device": {
#                                     ak.muzzle_ak74: 1,
#                                     ak.muzzle_dtk: 1,
#                                     ak.muzzle_amd65: 1,
#                                     ak.muzzle_akm: 1,
#                                     ak.muzzle_akml: 1,
#                                     ak.muzzle_lantac: 1,
#                                     ak.muzzle_pbs4: 1,
#                                     ak.muzzle_pbs1: 1,
#                                     ak.muzzle_dynacomp: 1,
#                                 },
#                                 "Attachment Adapter": {None: 1, attachments.adapter_mlok_picrail: 1,
#                                                        attachments.adapter_mlok_picrail_short: 1},
#                                 "Underbarrel Accessory": {
#                                     None: 1,
#                                     attachments.grip_hera_cqr: 1,
#                                     attachments.grip_promag_vertical: 1,
#                                     attachments.grip_jem_vertical: 1,
#                                     attachments.grip_magpul_angled: 1,
#                                     attachments.grip_magpul_mvg: 1,
#                                     attachments.grip_aimtac_short: 1,
#                                     attachments.grip_magpul_handstop: 1,
#                                     attachments.grip_hipoint_folding: 1,
#                                 },
#                             },
#                             allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
#                                                 'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
#                                                 'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
#                                                 'AK Magazine Adapter', 'Optic']
#                             )
#
# ak556_weapon = PremadeWeapon(gun_item=ak.ak,
#                              bullet=gun_parts.bullets_556_weighted,
#                              magazine={magazines.ak556_30rd: (1, 1, 1, 1, 1),
#                                        magazines.stanag_10rd: (1, 1, 1, 1, 1),
#                                        magazines.stanag_20rd: (1, 1, 1, 1, 1),
#                                        magazines.stanag_30rd: (1, 1, 1, 1, 1),
#                                        magazines.stanag_40rd: (1, 1, 1, 1, 1),
#                                        magazines.stanag_50rd: (1, 1, 1, 1, 1),
#                                        magazines.stanag_60rd: (1, 1, 1, 1, 1),
#                                        magazines.stanag_100rd: (1, 1, 1, 1, 1),
#                                        },
#                              optics=optics_test,
#                              part_dict={
#                                  "AK Reciever": {ak.reciever_100556: (1, 1, 1, 1, 1),
#                                                  ak.reciever_100556_auto: (1, 1, 1, 1, 1)},
#                                  "AK Magazine Adapter": {None: 1, ak.ak_ar_mag_adapter: 1},
#                                  "AK Barrel": {ak.barrel_ak556: 1, ak.barrel_ak556_short: 1},
#                                  "Thread Adapter": {None: 1,
#                                                     attachments.thread_adapter_2415_5824: 1},
#                                  "AK Handguard": {
#                                      ak.handguard_akm: 1,
#                                      ak.handguard_amd65: 1,
#                                      ak.handguard_ak74: 1,
#                                      ak.handguard_romanian: 1,
#                                      ak.handguard_ak100: 1,
#                                      ak.handguard_B10M: 1,
#                                      ak.handguard_leader: 1,
#                                      ak.handguard_magpul: 1,
#                                  },
#                                  "AK Grip": {
#                                      ak.grip_akm: 1,
#                                      ak.grip_ak12: 1,
#                                      ak.grip_sniper: 1,
#                                      ak.grip_moe: 1,
#                                      ak.grip_rk3: 1,
#                                      ak.grip_tapco: 1,
#                                      ak.grip_skeletonised: 1,
#                                      ak.grip_hogue: 1,
#                                      ak.grip_fab: 1,
#                                  },
#                                  "AK Stock": {
#                                      None: 1,
#                                      ak.stock_akm: 1,
#                                      ak.stock_rpk: 1,
#                                      ak.stock_ak74: 1,
#                                      ak.stock_ak100: 1,
#                                      ak.stock_ak_underfolder: 1,
#                                      ak.stock_ak_triangle: 1,
#                                      ak.stock_ak12: 1,
#                                      ak.stock_amd65: 1,
#                                      ak.stock_pt1: 1,
#                                      ak.stock_moe: 1,
#                                      ak.stock_zhukov: 1,
#                                  },
#                                  "AK Optics Mount": {None: 1, ak.accessory_dustcoverrail: 1,
#                                                      ak.accessory_railsidemount: 1},
#                                  "Muzzle Device": {
#                                      ak.muzzle_ak74: 1,
#                                      ak.muzzle_dtk: 1,
#                                      ak.muzzle_amd65: 1,
#                                      ak.muzzle_akm: 1,
#                                      ak.muzzle_akml: 1,
#                                      ak.muzzle_lantac: 1,
#                                      ak.muzzle_pbs4: 1,
#                                      ak.muzzle_pbs1: 1,
#                                      ak.muzzle_dynacomp: 1,
#                                  },
#                                  "Attachment Adapter": {None: 1, attachments.adapter_mlok_picrail: 1,
#                                                         attachments.adapter_mlok_picrail_short: 1},
#                                  "Underbarrel Accessory": {
#                                      None: 1,
#                                      attachments.grip_hera_cqr: 1,
#                                      attachments.grip_promag_vertical: 1,
#                                      attachments.grip_jem_vertical: 1,
#                                      attachments.grip_magpul_angled: 1,
#                                      attachments.grip_magpul_mvg: 1,
#                                      attachments.grip_aimtac_short: 1,
#                                      attachments.grip_magpul_handstop: 1,
#                                      attachments.grip_hipoint_folding: 1,
#                                  },
#                              },
#                              allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
#                                                  'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
#                                                  'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
#                                                  'AK Magazine Adapter', 'Optic']
#                              )
#
# """
# MAC 10
# """
#
# m1045_weapon = PremadeWeapon(gun_item=m10.mac10,
#                              bullet=gun_parts.bullets_45_weighted,
#                              magazine={magazines.mac10_mag_45: 1, magazines.mac10_mag_45_extended: 1},
#                              optics=optics_test,
#                              part_dict={
#                                  "M10 Lower": m10.mac1045_lower,
#                                  "M10 Upper": {m10.mac1045_upper: 1,
#                                                m10.mac1045_upper_tactical: 1,
#                                                m10.mac1045_upper_max: 1},
#                                  "M10 Barrel": {m10.mac1045_barrel: 1,
#                                                 m10.mac1045_max_barrel: 1,
#                                                 m10.mac1045_carbine_barrel: 1,
#                                                 },
#                                  "M10/45 Carbine Handguard": {m10.mac10_carbine_handguard_m16a2: 1,
#                                                               m10.mac10_carbine_handguard_picatinny: 1},
#                                  "Stock Adapter M10": {None: 1,
#                                                        m10.mac10_ar_stock_adapter: 1},
#                                  "M10 Stock": {m10.mac1045_full_stock: 1,
#                                                m10.mac1045_folding_stock: 1,
#                                                m10.mac1045_stock: 1},
#                                  "AR Stock": {
#                                      ar15.ar_stock_m16a2: 1,
#                                      ar15.ar_stock_moe: 1,
#                                      ar15.ar_stock_ubr: 1,
#                                      ar15.ar_stock_danieldefense: 1,
#                                      ar15.ar_stock_prs: 1,
#                                      ar15.ar_stock_maxim_cqb: 1,
#                                  },
#                                  "M10 Optics Mount": {None: 1, m10.mac10_optics_mount: 1},
#                                  "Muzzle Device": {
#                                      None: 1,
#                                      attachments.muzzle_nullifier: 1,
#                                      attachments.muzzle_kak_45: 1,
#                                      attachments.muzzle_kak_a2: 1,
#                                      m10.mac1045_sionics_suppressor: 1,
#                                      m10.mac1045_extended_barrel: 1,
#                                      attachments.suppressor_obsidian_45: 1,
#                                  },
#                                  "Accessory Adapter M10": {None: 1, m10.mac10_trirail: 1},
#                                  "Underbarrel Accessory": {
#                                      None: 1,
#                                      attachments.grip_hera_cqr: 1,
#                                      attachments.grip_promag_vertical: 1,
#                                      attachments.grip_jem_vertical: 1,
#                                      attachments.grip_magpul_angled: 1,
#                                      attachments.grip_magpul_mvg: 1,
#                                      attachments.grip_aimtac_short: 1,
#                                      attachments.grip_magpul_handstop: 1,
#                                      attachments.grip_hipoint_folding: 1,
#                                  },
#                              },
#                              allowed_part_types=['M10 Lower', 'M10 Upper', 'Stock Adapter M10', 'Attachment Adapter',
#                                                  'Muzzle Adapter', 'M10 Stock', 'M10 Optics Mount', 'Muzzle Device',
#                                                  'Accessory Adapter M10', 'Side Mounted Accessory',
#                                                  'Underbarrel Accessory', 'Optic']
#                              )
#
# m109_weapon = PremadeWeapon(gun_item=m10.mac10,
#                             bullet=gun_parts.bullets_9mm_weighted,
#                             magazine=magazines.mac10_mag_9,
#                             optics=optics_test,
#                             part_dict={
#                                 "M10 Lower": m10.mac109_lower,
#                                 "M10 Upper": {m10.mac109_upper: 1,
#                                               m10.mac109_upper_tactical: 1,
#                                               m10.mac109_upper_max: 1,
#                                               m10.mac109_upper_max31: 1,
#                                               m10.mac109_upper_max31k: 1,
#                                               },
#                                 "M10 Barrel": {m10.mac109_barrel: 1,
#                                                m10.mac109_max_barrel: 1,
#                                                m10.mac109_carbine_barrel: 1,
#                                                m10.max1031_barrel_1228: 1,
#                                                m10.max1031k_barrel_1228: 1,
#                                                m10.max1031_barrel_3410: 1,
#                                                m10.max1031k_barrel_3410: 1,
#                                                },
#                                 "M10/45 Carbine Handguard": {m10.mac109_carbine_handguard_m16a2: 1,
#                                                              m10.mac109_carbine_handguard_picatinny: 1},
#                                 "Stock Adapter M10": {None: 1,
#                                                       m10.mac10_ar_stock_adapter: 1},
#                                 "M10 Stock": {m10.mac1045_full_stock: 1,
#                                               m10.mac1045_folding_stock: 1,
#                                               m10.mac1045_stock: 1},
#                                 "AR Stock": {
#                                     ar15.ar_stock_m16a2: 1,
#                                     ar15.ar_stock_moe: 1,
#                                     ar15.ar_stock_ubr: 1,
#                                     ar15.ar_stock_danieldefense: 1,
#                                     ar15.ar_stock_prs: 1,
#                                     ar15.ar_stock_maxim_cqb: 1,
#                                 },
#                                 "M10 Optics Mount": {None: 1, m10.mac10_optics_mount: 1},
#                                 "Muzzle Device": {
#                                     None: 1,
#                                     m10.mac109_sionics_suppressor: 1,
#                                     m10.mac109_extended_barrel: 1,
#                                     attachments.suppressor_wolfman_9mm: 1,
#                                     attachments.suppressor_obsidian_9: 1,
#                                 },
#                                 "Accessory Adapter M10": {None: 1, m10.mac10_trirail: 1},
#                                 "Underbarrel Accessory": {
#                                     None: 1,
#                                     attachments.grip_hera_cqr: 1,
#                                     attachments.grip_promag_vertical: 1,
#                                     attachments.grip_jem_vertical: 1,
#                                     attachments.grip_magpul_angled: 1,
#                                     attachments.grip_magpul_mvg: 1,
#                                     attachments.grip_aimtac_short: 1,
#                                     attachments.grip_magpul_handstop: 1,
#                                     attachments.grip_hipoint_folding: 1,
#                                 },
#                             },
#                             allowed_part_types=['M10 Lower', 'M10 Upper', 'Stock Adapter M10', 'Attachment Adapter',
#                                                 'Muzzle Adapter', 'M10 Stock', 'M10 Optics Mount', 'Muzzle Device',
#                                                 'Accessory Adapter M10', 'Side Mounted Accessory',
#                                                 'Underbarrel Accessory', 'Optic']
#                             )
#
# """
# SKS
# """
#
# sks_weapon = PremadeWeapon(gun_item=sks.sks,
#                            bullet=gun_parts.bullets_752_weighted,
#                            magazine={
#                                magazines.ak762_10rd: (1, 1, 1, 1, 1),
#                                magazines.ak762_20rd: (1, 1, 1, 1, 1),
#                                magazines.ak762_30rd: (1, 1, 1, 1, 1),
#                                magazines.ak762_40rd: (1, 1, 1, 1, 1),
#                                magazines.ak762_60rd: (1, 1, 1, 1, 1),
#                                magazines.ak762_75rd: (1, 1, 1, 1, 1),
#                                magazines.ak762_100rd: (1, 1, 1, 1, 1),
#                                magazines.sks_mag_20rd: (1, 1, 1, 1, 1),
#                                magazines.sks_mag_35rd: (1, 1, 1, 1, 1),
#                                magazines.sks_mag_75rd: (1, 1, 1, 1, 1)},
#                            clip=magazines.sks_clip,
#                            optics=optics_test,
#                            part_dict={
#                                "SKS Barrel": {
#                                    sks.barrel_sks:                      (1, 1, 1, 1, 1),
#                                    sks.barrel_sks_shortened:            (1, 1, 1, 1, 1),
#                                    sks.barrel_sks_auto:                 (1, 1, 1, 1, 1),
#                                    sks.barrel_sks_shortened_auto:       (1, 1, 1, 1, 1),
#                                    sks.barrel_sks_akmag:                (1, 1, 1, 1, 1),
#                                    sks.barrel_sks_shortened_akmag:      (1, 1, 1, 1, 1),
#                                    sks.barrel_sks_auto_akmag:           (1, 1, 1, 1, 1),
#                                    sks.barrel_sks_shortened_auto_akmag: (1, 1, 1, 1, 1),
#                                },
#                                "Thread Adapter": {None: 1,
#                                                   attachments.thread_adapter_sks: 1},
#                                "SKS Stock": {
#                                    sks.stock_sks: 1,
#                                    sks.stock_sks_tapco: 1,
#                                    sks.stock_sks_dragunov: 1,
#                                    sks.stock_sks_fab: 1,
#                                    sks.stock_sks_sabertooth: 1,
#                                    sks.stock_sks_bullpup: 1,
#                                },
#                                "AR Grip": {
#                                    ar15.ar_grip_trybe: 1,
#                                    ar15.ar_grip_moe: 1,
#                                    ar15.ar_grip_hogue: 1,
#                                    ar15.ar_grip_strikeforce: 1,
#                                    ar15.ar_grip_a2: 1,
#                                    ar15.ar_grip_stark: 1,
#                                },
#                                "AR Stock": {
#                                    ar15.ar_stock_m16a2: 1,
#                                    ar15.ar_stock_moe: 1,
#                                    ar15.ar_stock_ubr: 1,
#                                    ar15.ar_stock_danieldefense: 1,
#                                    ar15.ar_stock_prs: 1,
#                                    ar15.ar_stock_maxim_cqb: 1,
#                                },
#                                "SKS Internal Magazine": {sks.sks_integrated_mag: 1, None: 1},
#                                "SKS Optics Mount": {None: 1, sks.sks_optics_mount: 1},
#                                "Attachment Adapter": {None: 1,
#                                                       attachments.adapter_mlok_picrail: 1,
#                                                       attachments.adapter_mlok_picrail_short: 1},
#                                "Underbarrel Accessory": {
#                                    None: 1,
#                                    attachments.grip_hera_cqr: 1,
#                                    attachments.grip_promag_vertical: 1,
#                                    attachments.grip_jem_vertical: 1,
#                                    attachments.grip_magpul_angled: 1,
#                                    attachments.grip_magpul_mvg: 1,
#                                    attachments.grip_aimtac_short: 1,
#                                    attachments.grip_magpul_handstop: 1,
#                                    attachments.grip_hipoint_folding: 1,
#                                },
#                                "Muzzle Device": {
#                                    ak.muzzle_ak74: 1,
#                                    ak.muzzle_dtk: 1,
#                                    ak.muzzle_amd65: 1,
#                                    ak.muzzle_akm: 1,
#                                    ak.muzzle_akml: 1,
#                                    ak.muzzle_lantac: 1,
#                                    ak.muzzle_pbs4: 1,
#                                    ak.muzzle_pbs1: 1,
#                                    ak.muzzle_dynacomp: 1,
#                                },
#                            },
#                            allowed_part_types=['SKS Barrel', 'SKS Stock', 'SKS Internal Magazine', 'Attachment Adapter',
#                                                'SKS Optics Mount', 'Underbarrel Accessory', 'Side Mounted Accessory',
#                                                'Muzzle Device', 'Optic']
#                            )
#
# """
# Mosin Nagant
# """
#
# mosin_weapon = PremadeWeapon(gun_item=mosin.mosin_nagant,
#                              bullet=gun_parts.bullets_54r_weighted,
#                              magazine=magazines.mosin_nagant,
#                              clip=magazines.mosin_clip,
#                              optics=optics_test,
#                              part_dict={
#                                  "Mosin-Nagant Stock": {
#                                      mosin.mosin_stock: 1,
#                                      mosin.mosin_stock_montecarlo: 1,
#                                      mosin.mosin_archangel_stock: 1,
#                                      mosin.mosin_carbine_stock: 1,
#                                      mosin.mosin_obrez_stock: 1,
#                                  },
#                                  "Mosin-Nagant Barrel": {
#                                      mosin.mosin_barrel: 1,
#                                      mosin.mosin_carbine_barrel: 1,
#                                      mosin.mosin_obrez_barrel: 1,
#                                  },
#                                  "Thread Adapter": {None: 1,
#                                                     attachments.thread_adapter_mosin: 1},
#                                  "Mosin-Nagant Accessory Mount": {mosin.mosin_pic_scope_mount: 1, None: 1},
#                                  "Muzzle Device": {
#                                      None: 1,
#                                      mosin.mosin_suppressor: 1,
#                                      mosin.mosin_muzzlebreak: 1,
#                                      ar15.ar15_muzzle_flashhider: 1,
#                                      ar15.ar15_muzzle_st6012: 1,
#                                      ar15.ar15_muzzle_mi_mb4: 1,
#                                      ar15.ar15_muzzle_cobra: 1,
#                                  },
#                              },
#                              allowed_part_types=['Mosin-Nagant Stock', 'Mosin-Nagant Barrel', 'Attachment Adapter',
#                                                  'Muzzle Adapter', 'Mosin-Nagant Accessory Mount', 'Muzzle Device',
#                                                  'Optic', 'Side Mounted Accessory']
#                              )
#
# """
# 1911
# """
#
# m1911_45 = PremadeWeapon(gun_item=m1911.m1911,
#                          bullet=gun_parts.bullets_45_weighted,
#                          magazine={magazines.m1911_mag_45_8: (1, 1, 1, 1, 1),
#                                    magazines.m1911_mag_45_10: (1, 1, 1, 1, 1),
#                                    magazines.m1911_mag_45_15: (1, 1, 1, 1, 1),
#                                    magazines.m1911_mag_45_40: (1, 1, 1, 1, 1)},
#                          optics=optics_test,
#                          part_dict={
#                              "M1911 Frame": {
#                                  m1911.m1911_frame_gov_ss:                         (1, 1, 1, 1, 1),
#                                              m1911.m1911_frame_gov_alloy:          (1, 1, 1, 1, 1),
#                                              m1911.m1911_frame_gov_ss_tac:         (1, 1, 1, 1, 1),
#                                              m1911.m1911_frame_gov_alloy_tac:      (1, 1, 1, 1, 1),
#                                              m1911.m1911_frame_gov_ss_auto:        (1, 1, 1, 1, 1),
#                                              m1911.m1911_frame_gov_alloy_auto:     (1, 1, 1, 1, 1),
#                                              m1911.m1911_frame_gov_ss_tac_auto:    (1, 1, 1, 1, 1),
#                                              m1911.m1911_frame_gov_alloy_tac_auto: (1, 1, 1, 1, 1), },
#                              "M1911 Barrel": {m1911.m1911_barrel_gov: 1,
#                                               m1911.m1911_barrel_commander: 1,
#                                               m1911.m1911_barrel_long: 1,
#                                               m1911.m1911_barrel_gov_threaded: 1,
#                                               m1911.m1911_barrel_commander_threaded: 1,
#                                               m1911.m1911_barrel_long_threaded: 1, },
#                              "M1911 Slide": {m1911.m1911_slide_gov: 1,
#                                              m1911.m1911_slide_commander: 1,
#                                              m1911.m1911_slide_long: 1,
#                                              m1911.m1911_slide_gov_light: 1,
#                                              m1911.m1911_slide_commander_light: 1,
#                                              m1911.m1911_slide_long_light: 1,
#                                              m1911.m1911_slide_gov_optic: 1,
#                                              m1911.m1911_slide_commander_optic: 1,
#                                              m1911.m1911_slide_long_optic: 1,
#                                              m1911.m1911_slide_gov_light_optic: 1,
#                                              m1911.m1911_slide_commander_light_optic: 1,
#                                              m1911.m1911_slide_long_light_optic: 1,
#                                              },
#                              "M1911 Grip Panels": {m1911.m1911_grip_magpul: 1,
#                                                    m1911.m1911_grip_rectac: 1,
#                                                    m1911.m1911_grip_wood: 1,
#                                                    m1911.m1911_grip_operator: 1,
#                                                    m1911.m1911_grip_palmswell: 1,
#                                                    m1911.m1911_grip_hogue: 1,
#                                                    m1911.m1911_rec_stock: 1,
#                                                    },
#                              "M1911 Optics Mount": {None: 1, m1911.m1911_bridge_mount: 1},
#                              "Muzzle Device": {None: 1, m1911.m1911_comp_tj: 1, m1911.m1911_comp_punisher: 1,
#                                                m1911.m1911_comp_predator: 1, m1911.m1911_comp_castle: 1,
#                                                attachments.suppressor_obsidian_45: 1},
#                              "Underbarrel Accessory": {
#                                  None: 1,
#                                  attachments.grip_promag_vertical: 1,
#                                  attachments.grip_jem_vertical: 1,
#                                  attachments.grip_aimtac_short: 1,
#                                  attachments.grip_hipoint_folding: 1,
#                              },
#                          },
#                          allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
#                                              'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
#                                              'Optic', 'Muzzle Device']
#                          )
#
# m1911_9mm = PremadeWeapon(gun_item=m1911.m1911,
#                           bullet=gun_parts.bullets_9mm_weighted,
#                           magazine=magazines.m1911_mag_9_10,
#                           optics=optics_test,
#                           part_dict={
#                               "M1911 Frame": {
#                                   m1911.m1911_frame_gov_ss: (1, 1, 1, 1, 1),
#                                   m1911.m1911_frame_gov_alloy: (1, 1, 1, 1, 1),
#                                   m1911.m1911_frame_gov_ss_tac: (1, 1, 1, 1, 1),
#                                   m1911.m1911_frame_gov_alloy_tac: (1, 1, 1, 1, 1),
#                                   m1911.m1911_frame_gov_ss_auto: (1, 1, 1, 1, 1),
#                                   m1911.m1911_frame_gov_alloy_auto: (1, 1, 1, 1, 1),
#                                   m1911.m1911_frame_gov_ss_tac_auto: (1, 1, 1, 1, 1),
#                                   m1911.m1911_frame_gov_alloy_tac_auto: (1, 1, 1, 1, 1), },
#                               "M1911 Barrel": {m1911.m1911_barrel_gov_9mm: 1,
#                                                m1911.m1911_barrel_commander_9mm: 1,
#                                                m1911.m1911_barrel_long_9mm: 1,
#                                                m1911.m1911_barrel_gov_threaded_9mm: 1,
#                                                m1911.m1911_barrel_commander_threaded_9mm: 1,
#                                                m1911.m1911_barrel_long_threaded_9mm: 1, },
#                               "M1911 Slide": {m1911.m1911_slide_gov_9mm: 1,
#                                               m1911.m1911_slide_commander_9mm: 1,
#                                               m1911.m1911_slide_long_9mm: 1,
#                                               m1911.m1911_slide_gov_light_9mm: 1,
#                                               m1911.m1911_slide_commander_light_9mm: 1,
#                                               m1911.m1911_slide_long_light_9mm: 1,
#                                               m1911.m1911_slide_gov_9mm_optic: 1,
#                                               m1911.m1911_slide_commander_9mm_optic: 1,
#                                               m1911.m1911_slide_long_9mm_optic: 1,
#                                               m1911.m1911_slide_gov_light_9mm_optic: 1,
#                                               m1911.m1911_slide_commander_light_9mm_optic: 1,
#                                               m1911.m1911_slide_long_light_9mm_optic: 1,
#                                               },
#                               "M1911 Grip Panels": {m1911.m1911_grip_magpul: 1,
#                                                     m1911.m1911_grip_rectac: 1,
#                                                     m1911.m1911_grip_wood: 1,
#                                                     m1911.m1911_grip_operator: 1,
#                                                     m1911.m1911_grip_palmswell: 1,
#                                                     m1911.m1911_grip_hogue: 1,
#                                                     m1911.m1911_rec_stock: 1,
#                                                     },
#                               "M1911 Optics Mount": {None: 1, m1911.m1911_bridge_mount: 1},
#                               "Muzzle Device": {None: 1, m1911.m1911_comp_tj: 1, m1911.m1911_comp_punisher: 1,
#                                                 m1911.m1911_comp_predator: 1, m1911.m1911_comp_castle: 1,
#                                                 attachments.suppressor_wolfman_9mm: 1,
#                                                 attachments.suppressor_obsidian_9: 1,},
#                               "Underbarrel Accessory": {
#                                   None: 1,
#                                   attachments.grip_promag_vertical: 1,
#                                   attachments.grip_jem_vertical: 1,
#                                   attachments.grip_aimtac_short: 1,
#                                   attachments.grip_hipoint_folding: 1,
#                               },
#                           },
#                           allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
#                                               'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
#                                               'Optic', 'Muzzle Device']
#                           )
#
# m1911_10mm = PremadeWeapon(gun_item=m1911.m1911,
#                            bullet=gun_parts.bullets_10mm_weighted,
#                            magazine=magazines.m1911_mag_10_8,
#                            optics=optics_test,
#                            part_dict={
#                                "M1911 Frame": {
#                                    m1911.m1911_frame_gov_ss: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_ss_tac: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy_tac: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_ss_auto: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy_auto: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_ss_tac_auto: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy_tac_auto: (1, 1, 1, 1, 1), },
#                                "M1911 Barrel": {m1911.m1911_barrel_gov_10mm: 1,
#                                                 m1911.m1911_barrel_commander_10mm: 1,
#                                                 m1911.m1911_barrel_long_10mm: 1,
#                                                 m1911.m1911_barrel_gov_threaded_10mm: 1,
#                                                 m1911.m1911_barrel_commander_threaded_10mm: 1,
#                                                 m1911.m1911_barrel_long_threaded_10mm: 1, },
#                                "M1911 Slide": {m1911.m1911_slide_gov_40: 1,
#                                                m1911.m1911_slide_commander_40: 1,
#                                                m1911.m1911_slide_long_40: 1,
#                                                m1911.m1911_slide_gov_light_40: 1,
#                                                m1911.m1911_slide_commander_light_40: 1,
#                                                m1911.m1911_slide_long_light_40: 1,
#                                                m1911.m1911_slide_gov_40_optic: 1,
#                                                m1911.m1911_slide_commander_40_optic: 1,
#                                                m1911.m1911_slide_long_40_optic: 1,
#                                                m1911.m1911_slide_gov_light_40_optic: 1,
#                                                m1911.m1911_slide_commander_light_40_optic: 1,
#                                                m1911.m1911_slide_long_light_40_optic: 1,
#                                                },
#                                "M1911 Grip Panels": {m1911.m1911_grip_magpul: 1,
#                                                      m1911.m1911_grip_rectac: 1,
#                                                      m1911.m1911_grip_wood: 1,
#                                                      m1911.m1911_grip_operator: 1,
#                                                      m1911.m1911_grip_palmswell: 1,
#                                                      m1911.m1911_grip_hogue: 1,
#                                                      m1911.m1911_rec_stock: 1,
#                                                      },
#                                "M1911 Optics Mount": {None: 1, m1911.m1911_bridge_mount: 1},
#                                "Muzzle Device": {None: 1, m1911.m1911_comp_tj: 1, m1911.m1911_comp_punisher: 1,
#                                                  m1911.m1911_comp_predator: 1, m1911.m1911_comp_castle: 1,
#                                                  attachments.suppressor_sandman: 1},
#                                "Underbarrel Accessory": {
#                                    None: 1,
#                                    attachments.grip_promag_vertical: 1,
#                                    attachments.grip_jem_vertical: 1,
#                                    attachments.grip_aimtac_short: 1,
#                                    attachments.grip_hipoint_folding: 1,
#                                },
#                            },
#                            allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
#                                                'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
#                                                'Optic', 'Muzzle Device']
#                            )
#
# m1911_40sw = PremadeWeapon(gun_item=m1911.m1911,
#                            bullet=gun_parts.bullets_40sw_weighted,
#                            magazine=magazines.m1911_mag_40sw_8,
#                            optics=optics_test,
#                            part_dict={
#                                "M1911 Frame": {
#                                    m1911.m1911_frame_gov_ss: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_ss_tac: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy_tac: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_ss_auto: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy_auto: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_ss_tac_auto: (1, 1, 1, 1, 1),
#                                    m1911.m1911_frame_gov_alloy_tac_auto: (1, 1, 1, 1, 1), },
#                                "M1911 Barrel": {m1911.m1911_barrel_gov_40sw: 1,
#                                                 m1911.m1911_barrel_commander_40sw: 1,
#                                                 m1911.m1911_barrel_long_40sw: 1,
#                                                 m1911.m1911_barrel_gov_threaded_40sw: 1,
#                                                 m1911.m1911_barrel_commander_threaded_40sw: 1,
#                                                 m1911.m1911_barrel_long_threaded_40sw: 1, },
#                                "M1911 Slide": {m1911.m1911_slide_gov_40: 1,
#                                                m1911.m1911_slide_commander_40: 1,
#                                                m1911.m1911_slide_long_40: 1,
#                                                m1911.m1911_slide_gov_light_40: 1,
#                                                m1911.m1911_slide_commander_light_40: 1,
#                                                m1911.m1911_slide_long_light_40: 1,
#                                                m1911.m1911_slide_gov_40_optic: 1,
#                                                m1911.m1911_slide_commander_40_optic: 1,
#                                                m1911.m1911_slide_long_40_optic: 1,
#                                                m1911.m1911_slide_gov_light_40_optic: 1,
#                                                m1911.m1911_slide_commander_light_40_optic: 1,
#                                                m1911.m1911_slide_long_light_40_optic: 1,
#                                                },
#                                "M1911 Grip Panels": {m1911.m1911_grip_magpul: 1,
#                                                      m1911.m1911_grip_rectac: 1,
#                                                      m1911.m1911_grip_wood: 1,
#                                                      m1911.m1911_grip_operator: 1,
#                                                      m1911.m1911_grip_palmswell: 1,
#                                                      m1911.m1911_grip_hogue: 1,
#                                                      m1911.m1911_rec_stock: 1,
#                                                      },
#                                "M1911 Optics Mount": {None: 1, m1911.m1911_bridge_mount: 1},
#                                "Muzzle Device": {None: 1, m1911.m1911_comp_tj: 1, m1911.m1911_comp_punisher: 1,
#                                                  m1911.m1911_comp_predator: 1, m1911.m1911_comp_castle: 1,
#                                                  attachments.suppressor_sandman: 1},
#                                "Underbarrel Accessory": {
#                                    None: 1,
#                                    attachments.grip_promag_vertical: 1,
#                                    attachments.grip_jem_vertical: 1,
#                                    attachments.grip_aimtac_short: 1,
#                                    attachments.grip_hipoint_folding: 1,
#                                },
#                            },
#                            allowed_part_types=['M1911 Frame', 'M1911 Barrel', 'M1911 Slide', 'M1911 Grip Panels',
#                                                'M1911 Optics Mount', 'Side Mounted Accessory', 'Underbarrel Accessory',
#                                                'Optic', 'Muzzle Device']
#                            )
#
# """
# M1 Carbine
# """
#
# m1_carbine_gun = PremadeWeapon(gun_item=m1_carbine.m1_carbine,
#                                bullet={bullets.round_30carb_110_jhp: 1, bullets.round_30carb_110_fmj: 1},
#                                magazine={magazines.m1_carbine_15rd: 1, magazines.m1_carbine_30rd: 1},
#                                optics=optics_test,
#                                part_dict={
#                                    "M1 Reciever": m1_carbine.m1_reciever,
#                                    "M1/M2 Stock": {
#                                        m1_carbine.m1_stock: 1,
#                                        m1_carbine.m1_stock_ebr: 1,
#                                        m1_carbine.m1_stock_enforcer: 1,
#                                        m1_carbine.m1_stock_springfield: 1
#                                    },
#                                    "M1/M2 Barrel": {
#                                        m1_carbine.m1_barrel: 1,
#                                        m1_carbine.m1_barrel_enforcer: 1,
#                                        m1_carbine.m1_barrel_threaded: 1,
#                                        m1_carbine.m1_barrel_enforcer_threaded: 1,
#                                    },
#                                    "AR Grip": {
#                                        ar15.ar_grip_trybe: 1,
#                                        ar15.ar_grip_moe: 1,
#                                        ar15.ar_grip_hogue: 1,
#                                        ar15.ar_grip_strikeforce: 1,
#                                        ar15.ar_grip_a2: 1,
#                                        ar15.ar_grip_stark: 1,
#                                    },
#                                    "AR Stock": {
#                                        ar15.ar_stock_m16a2: 1,
#                                        ar15.ar_stock_moe: 1,
#                                        ar15.ar_stock_ubr: 1,
#                                        ar15.ar_stock_danieldefense: 1,
#                                        ar15.ar_stock_prs: 1,
#                                        ar15.ar_stock_maxim_cqb: 1,
#                                    },
#                                    "M1/M2 Carbine Optic Mount": {None: 1, m1_carbine.m1_m6b_mount: 1,
#                                                                  m1_carbine.m1_sk_mount: 1},
#                                    "Attachment Adapter": {None: 1, attachments.adapter_mlok_picrail: 1,
#                                                           attachments.adapter_mlok_picrail_short: 1},
#                                    "Muzzle Device": {
#                                        attachments.suppressor_obsidian_9: 1,
#                                        attachments.suppressor_wolfman_9mm: 1,
#                                        ar15.ar15_muzzle_flashhider: 1,
#                                        ar15.ar15_muzzle_st6012: 1,
#                                        ar15.ar15_muzzle_mi_mb4: 1,
#                                        ar15.ar15_muzzle_cobra: 1, },
#                                    "Underbarrel Accessory": {
#                                        None: 1,
#                                        attachments.grip_hera_cqr: 1,
#                                        attachments.grip_promag_vertical: 1,
#                                        attachments.grip_jem_vertical: 1,
#                                        attachments.grip_magpul_angled: 1,
#                                        attachments.grip_magpul_mvg: 1,
#                                        attachments.grip_aimtac_short: 1,
#                                        attachments.grip_magpul_handstop: 1,
#                                        attachments.grip_hipoint_folding: 1,
#                                    },
#                                },
#                                allowed_part_types=['M1 Reciever', 'M1/M2 Stock', 'M1/M2 Barrel',
#                                                    'M1/M2 Carbine Optic Mount', 'Attachment Adapter',
#                                                    'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
#                                                    'Optic', 'Muzzle Adapter']
#                                )
#
# m2_carbine_gun = PremadeWeapon(gun_item=m1_carbine.m2_carbine,
#                                bullet={bullets.round_30carb_110_jhp: 1, bullets.round_30carb_110_fmj: 1},
#                                magazine={magazines.m1_carbine_15rd: 1, magazines.m1_carbine_30rd: 1},
#                                optics=optics_test,
#                                part_dict={
#                                    "M2 Reciever": m1_carbine.m2_reciever,
#                                    "M1/M2 Stock": {
#                                        m1_carbine.m1_stock: 1,
#                                        m1_carbine.m1_stock_ebr: 1,
#                                        m1_carbine.m1_stock_enforcer: 1,
#                                        m1_carbine.m1_stock_springfield: 1
#                                    },
#                                    "M1/M2 Barrel": {
#                                        m1_carbine.m1_barrel: 1,
#                                        m1_carbine.m1_barrel_enforcer: 1,
#                                        m1_carbine.m1_barrel_threaded: 1,
#                                        m1_carbine.m1_barrel_enforcer_threaded: 1,
#                                    },
#                                    "AR Grip": {
#                                        ar15.ar_grip_trybe: 1,
#                                        ar15.ar_grip_moe: 1,
#                                        ar15.ar_grip_hogue: 1,
#                                        ar15.ar_grip_strikeforce: 1,
#                                        ar15.ar_grip_a2: 1,
#                                        ar15.ar_grip_stark: 1,
#                                    },
#                                    "AR Stock": {
#                                        ar15.ar_stock_m16a2: 1,
#                                        ar15.ar_stock_moe: 1,
#                                        ar15.ar_stock_ubr: 1,
#                                        ar15.ar_stock_danieldefense: 1,
#                                        ar15.ar_stock_prs: 1,
#                                        ar15.ar_stock_maxim_cqb: 1,
#                                    },
#                                    "M1/M2 Carbine Optic Mount": {None: 1, m1_carbine.m1_m6b_mount: 1,
#                                                                  m1_carbine.m1_sk_mount: 1},
#                                    "Attachment Adapter": {None: 1, attachments.adapter_mlok_picrail: 1,
#                                                           attachments.adapter_mlok_picrail_short: 1},
#                                    "Muzzle Device": {
#                                        attachments.suppressor_obsidian_9: 1,
#                                        attachments.suppressor_wolfman_9mm: 1,
#                                        ar15.ar15_muzzle_flashhider: 1,
#                                        ar15.ar15_muzzle_st6012: 1,
#                                        ar15.ar15_muzzle_mi_mb4: 1,
#                                        ar15.ar15_muzzle_cobra: 1, },
#                                    "Underbarrel Accessory": {
#                                        None: 1,
#                                        attachments.grip_hera_cqr: 1,
#                                        attachments.grip_promag_vertical: 1,
#                                        attachments.grip_jem_vertical: 1,
#                                        attachments.grip_magpul_angled: 1,
#                                        attachments.grip_magpul_mvg: 1,
#                                        attachments.grip_aimtac_short: 1,
#                                        attachments.grip_magpul_handstop: 1,
#                                        attachments.grip_hipoint_folding: 1,
#                                    },
#                                },
#                                allowed_part_types=['M2 Reciever', 'M1/M2 Stock', 'M1/M2 Barrel',
#                                                    'M1/M2 Carbine Optic Mount', 'Attachment Adapter',
#                                                    'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
#                                                    'Optic', 'Muzzle Adapter']
#                                )
#
# """
# M14 / M1A
# """
#
# m14_gun = PremadeWeapon(gun_item=m14.m14,
#                         bullet=gun_parts.bullets_308_weighted,
#                         magazine={magazines.m14_10rd: (1, 1, 1, 1,  1),
#                                   magazines.m14_20rd: (1, 1, 1, 1,  1),
#                                   magazines.m14_50rd: (1, 1, 1, 1,  1)},
#                         optics=optics_test,
#                         part_dict={
#                             "M14 - Reciever": {m14.m14_reciever:      (1, 1, 1, 1,  1),
#                                                m14.m14_reciever_auto: (1, 1, 1, 1,  1)},
#                             "M14/M1A Stock": {m14.m14_stock_fiberglass: 1,
#                                               m14.m14_stock_wood: 1,
#                                               m14.m14_stock_archangel: 1,
#                                               m14.m14_stock_bullpup: 1,
#                                               m14.m14_stock_ebr: 1,
#                                               m14.m14_stock_vltor: 1},
#                             "M14/M1A Barrel": {m14.m14_barrel: 1, m14.m14_barrel_18in: 1, m14.m14_barrel_socom: 1},
#                             "AR Grip": {
#                                 ar15.ar_grip_trybe: 1,
#                                 ar15.ar_grip_moe: 1,
#                                 ar15.ar_grip_hogue: 1,
#                                 ar15.ar_grip_strikeforce: 1,
#                                 ar15.ar_grip_a2: 1,
#                                 ar15.ar_grip_stark: 1,
#                             },
#                             "AR Stock": {
#                                 ar15.ar_stock_m16a2: 1,
#                                 ar15.ar_stock_moe: 1,
#                                 ar15.ar_stock_ubr: 1,
#                                 ar15.ar_stock_danieldefense: 1,
#                                 ar15.ar_stock_prs: 1,
#                                 ar15.ar_stock_maxim_cqb: 1,
#                             },
#                             "Thread Adapter": {None: 1,
#                                                attachments.thread_adapter_m14_5824: 1},
#                             "M14/M1A Picatinny Rail Optic Mount": {None: 1, m14.m14_optic_mount: 1},
#                             "Attachment Adapter": {None: 1, attachments.adapter_mlok_picrail: 1,
#                                                    attachments.adapter_mlok_picrail_short: 1},
#                             "Underbarrel Accessory": {
#                                 None: 1,
#                                 attachments.grip_hera_cqr: 1,
#                                 attachments.grip_promag_vertical: 1,
#                                 attachments.grip_jem_vertical: 1,
#                                 attachments.grip_magpul_angled: 1,
#                                 attachments.grip_magpul_mvg: 1,
#                                 attachments.grip_aimtac_short: 1,
#                                 attachments.grip_magpul_handstop: 1,
#                                 attachments.grip_hipoint_folding: 1,
#                             },
#                             "Muzzle Device": {m14.m14_muzzle_usgi: 1,
#                                               m14.m14_muzzle_uscg_brake: 1,
#                                               m14.m14_muzzle_vais_brake: 1,
#                                               m14.m14_muzzle_synergy_brake: 1,
#                                               ar15.ar15_300_muzzle_flashhider: 1,
#                                               ar15.ar15_300_muzzle_cobra: 1,
#                                               ar15.ar15_300_muzzle_pegasus: 1,
#                                               ar15.ar15_300_muzzle_strike: 1,
#                                               },
#                         },
#                         allowed_part_types=['M14 - Reciever', 'M14/M1A Stock', 'M14/M1A Barrel',
#                                             'M14/M1A Picatinny Rail Optic Mount', 'Attachment Adapter',
#                                             'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device', 'Optic']
#                         )
#
# """
# R870
# """
#
# r870_gun = PremadeWeapon(gun_item=r870.rem_870,
#                          bullet=gun_parts.bullets_12ga_weighted,
#                          magazine=magazines.r870_6rd,
#                          optics=optics_test,
#                          part_dict={
#                              "Model 870 Reciever": {r870.reciever_r870_4rd: (1, 1, 1, 1,  1),
#                                                     r870.reciever_r870dm:   (1, 1, 1, 1,  1),
#                                                     r870.reciever_r870_6rd: (1, 1, 1, 1,  1)},
#                              "Model 870 Barrel": {r870.r870_barrel_26:       (1, 1, 1, 1,  1),
#                                                   r870.r870_barrel_18:       (1, 1, 1, 1,  1),
#                                                   r870.r870_barrel_t14:      (1, 1, 1, 1,  1),
#                                                   r870.r870_barrel_18_bead:  (1, 1, 1, 1,  1),
#                                                   r870.r870_barrel_t14_bead: (1, 1, 1, 1,  1)},
#                              "Model 870 Stock": {r870.r870_stock: 1,
#                                                  r870.r870_stock_polymer: 1,
#                                                  r870.r870_stock_magpul: 1,
#                                                  r870.r870_stock_shockwave: 1,
#                                                  r870.r870_stock_pistol: 1,
#                                                  r870.r870_stock_maverick: 1,
#                                                  r870.r870_stock_sterling: 1,
#                                                  r870.r870_ar_stock_adapter: 1},
#                              "AR Grip": {
#                                  ar15.ar_grip_trybe: 1,
#                                  ar15.ar_grip_moe: 1,
#                                  ar15.ar_grip_hogue: 1,
#                                  ar15.ar_grip_strikeforce: 1,
#                                  ar15.ar_grip_a2: 1,
#                                  ar15.ar_grip_stark: 1,
#                              },
#                              "AR Stock": {
#                                  ar15.ar_stock_m16a2: 1,
#                                  ar15.ar_stock_moe: 1,
#                                  ar15.ar_stock_ubr: 1,
#                                  ar15.ar_stock_danieldefense: 1,
#                                  ar15.ar_stock_prs: 1,
#                                  ar15.ar_stock_maxim_cqb: 1,
#                              },
#                              "Model 870 Forend": {r870.r870_forend: 1,
#                                                   r870.r870_forend_polymer: 1,
#                                                   r870.r870_forend_magpul: 1,
#                                                   r870.r870_forend_tacstar: 1,
#                                                   r870.r870_forend_voa: 1},
#                              "Model 870 Choke": {
#                                  r870.r870_choke_im: 1,
#                                  r870.r870_choke_modified: 1,
#                                  r870.r870_choke_cylinder: 1,
#                                  r870.r870_choke_improved_ported: 1,
#                                  r870.r870_choke_cylinder_ported: 1,
#                              },
#                              "Model 870 Magazine Extension": {
#                                  None: 1,
#                                  r870.r870_extension_2rd: 1,
#                                  r870.r870_extension_4rd: 1,
#                                  r870.r870_extension_6rd: 1,
#                              },
#                              "Model 870 Optics Mount": {
#                                  None: 1,
#                                  r870.r870_optic_picrail: 1,
#                                  r870.r870_optic_picrail_ghost: 1,
#                              },
#                          },
#                          allowed_part_types=['Model 870 Reciever', 'Model 870 Barrel', 'Model 870 Stock',
#                                              'Model 870 Forend', 'Model 870 Choke', 'Attachment Adapter',
#                                              'Model 870 Magazine Extension', 'Model 870 Optics Mount',
#                                              'Underbarrel Accessory', 'Side Mounted Accessory', 'Optic']
#                          )
#
# supershorty_gun = PremadeWeapon(gun_item=r870.rem_870,
#                                 bullet=gun_parts.bullets_12ga_weighted,
#                                 magazine={},
#                                 optics=optics_test,
#                                 part_dict={
#                                     "Model 870 Reciever": {r870.reciever_r870_shorty: 1},
#                                     "Model 870 Barrel": {r870.r870_barrel_shorty: 1},
#                                     "Model 870 Stock": {r870.r870_stock: 1,
#                                                         r870.r870_stock_polymer: 1,
#                                                         r870.r870_stock_magpul: 1,
#                                                         r870.r870_stock_shockwave: 1,
#                                                         r870.r870_stock_pistol: 1,
#                                                         r870.r870_stock_maverick: 1,
#                                                         r870.r870_stock_sterling: 1,
#                                                         r870.r870_ar_stock_adapter: 1},
#                                     "AR Grip": {
#                                         ar15.ar_grip_trybe: 1,
#                                         ar15.ar_grip_moe: 1,
#                                         ar15.ar_grip_hogue: 1,
#                                         ar15.ar_grip_strikeforce: 1,
#                                         ar15.ar_grip_a2: 1,
#                                         ar15.ar_grip_stark: 1,
#                                     },
#                                     "AR Stock": {
#                                         ar15.ar_stock_m16a2: 1,
#                                         ar15.ar_stock_moe: 1,
#                                         ar15.ar_stock_ubr: 1,
#                                         ar15.ar_stock_danieldefense: 1,
#                                         ar15.ar_stock_prs: 1,
#                                         ar15.ar_stock_maxim_cqb: 1,
#                                     },
#                                     "Model 870 Choke": {
#                                         r870.r870_choke_im: 1,
#                                         r870.r870_choke_modified: 1,
#                                         r870.r870_choke_cylinder: 1,
#                                         r870.r870_choke_improved_ported: 1,
#                                         r870.r870_choke_cylinder_ported: 1,
#                                     },
#                                     "Model 870 Magazine Extension": {
#                                         None: 1,
#                                         r870.r870_extension_2rd: 1,
#                                         r870.r870_extension_4rd: 1,
#                                         r870.r870_extension_6rd: 1,
#                                     },
#                                     "Model 870 Optics Mount": {
#                                         None: 1,
#                                         r870.r870_optic_picrail: 1,
#                                         r870.r870_optic_picrail_ghost: 1,
#                                     },
#                                 },
#                                 allowed_part_types=['Super Shorty Reciever', 'Model 870 Barrel', 'Model 870 Stock',
#                                                     'Model 870 Forend', 'Model 870 Choke', 'Attachment Adapter',
#                                                     'Model 870 Magazine Extension', 'Model 870 Optics Mount',
#                                                     'Underbarrel Accessory', 'Side Mounted Accessory', 'Optic']
#                                 )
#
# """
# S&W M629
# """
#
# m629_gun = PremadeWeapon(gun_item=misc.sw629,
#                          bullet=gun_parts.bullets_44mag_weighted,
#                          magazine={},
#                          clip=magazines.m629_clip,
#                          optics=optics_test,
#                          part_dict={
#                              "S&W .44 Frame": misc.sw629_frame,
#                              "S&W .44 Barrel": {misc.sw629_barrel: 1,
#                                                 misc.sw629_barrel_stealth: 1,
#                                                 misc.sw629_barrel_5in: 1,
#                                                 misc.sw629_barrel_4in: 1,
#                                                 },
#                              "S&W N-Frame Optic Mount": {misc.sw629_optic_pistol: 1,
#                                                          misc.sw629_optic_pistol_picrail: 1,
#                                                          None: 1,
#                                                          },
#                          },
#                          allowed_part_types=['S&W .44 Frame', 'S&W .44 Barrel', 'S&W N-Frame Optic Mount', 'Optic']
#                          )
#
# """
# S&W M610
# """
#
# m610_gun = PremadeWeapon(gun_item=misc.sw610,
#                          bullet=gun_parts.bullets_10mm_40sw_weighted,
#                          magazine={},
#                          clip=magazines.m610_clip,
#                          optics=optics_test,
#                          part_dict={
#                              "S&W 10mm Frame": misc.sw610_frame,
#                              "S&W 10mm Barrel": {misc.sw610_barrel: 1,
#                                                  misc.sw610_barrel_4in: 1,
#                                                  },
#                              "S&W N-Frame Optic Mount": {misc.sw629_optic_pistol: 1,
#                                                          misc.sw629_optic_pistol_picrail: 1,
#                                                          None: 1,
#                                                          },
#                          },
#                          allowed_part_types=['S&W 10mm Frame', 'S&W 10mm Barrel', 'S&W N-Frame Optic Mount', 'Optic']
#                          )
#
# """
# DE XIX
# """
#
# dexix_gun = PremadeWeapon(gun_item=misc.de44,
#                           bullet=gun_parts.bullets_44mag_weighted,
#                           magazine=magazines.de44_mag,
#                           optics=optics_test,
#                           part_dict={
#                               "DE .44 Frame": misc.sw629_frame,
#                               "DE .44 Barrel": {misc.de44_barrel: 1,
#                                                 misc.de44_barrel_imb: 1,
#                                                 misc.de44_barrel_10in: 1,
#                                                 misc.de44_barrel_10in_threaded: 1,
#                                                 },
#                               "DE .44 Slide": misc.de44_slide,
#                               "Muzzle Device": {
#                                   ar15.ar15_300_muzzle_flashhider: 1,
#                                   ar15.ar15_300_muzzle_cobra: 1,
#                                   ar15.ar15_300_muzzle_pegasus: 1,
#                                   ar15.ar15_300_muzzle_strike: 1,
#                               },
#
#                           },
#                           allowed_part_types=['DE .44 Frame', 'DE .44 Barrel', 'DE .44 Slide', 'Optic',
#                                               'Muzzle Device']
#                           )
#
# """
# TT33
# """
#
# tt33_gun = PremadeWeapon(gun_item=misc.tt33,
#                          bullet=gun_parts.bullets_76225_weighted,
#                          magazine=magazines.tt33_magazine,
#                          optics=optics_test,
#                          part_dict={
#                              "Tokarev TT Frame": misc.tt33_frame,
#                              "Tokarev TT Barrel": misc.tt33_barrel,
#                              "Tokarev TT Slide": {misc.tt33_slide: 1,
#                                                   misc.tt33_slide_tactical: 1,
#                                                   },
#                              "Tokarev TT-33 Grip Panels": {misc.tt33_grip: 1,
#                                                            misc.tt33_grip_rubberised: 1,
#                                                            },
#                              "Muzzle Device": {
#                                  misc.tt33_compensator: 1,
#                                  None: 1,
#                              },
#
#                          },
#                          allowed_part_types=['Tokarev TT Frame', 'Tokarev TT Barrel', 'Tokarev TT Slide',
#                                              'Tokarev TT-33 Grip Panels', 'Optic', 'Muzzle Device']
#                          )
#
# """
# H015
# """
#
# h015_gun = PremadeWeapon(gun_item=misc.singleshot,
#                          bullet=gun_parts.bullets_12ga_weighted,
#                          magazine={},
#                          optics=optics_test,
#                          part_dict={
#                              "H015 Reciever": misc.single_shot_reciever,
#                              "H015 Barrel": {misc.single_shot_barrel: 1,
#                                              misc.single_shot_barrel_short: 1},
#                              "H015 Stock": {misc.single_shot_stock: 1,
#                                             misc.h015_birdshead: 1,
#                                             },
#                              "Model 870 Choke": {
#                                  r870.r870_choke_im: 1,
#                                  r870.r870_choke_modified: 1,
#                                  r870.r870_choke_cylinder: 1,
#                                  r870.r870_choke_improved_ported: 1,
#                                  r870.r870_choke_cylinder_ported: 1,
#                              },
#                              "H015 Optic Mount": {
#                                  misc.h015_scope_mount: 1,
#                                  None: 1,
#                              },
#
#                          },
#                          allowed_part_types=['H015 Reciever', 'H015 Barrel', 'H015 Stock',
#                                              'Model 870 Choke', 'H015 Optic Mount', 'Optic']
#                          )
#
# """
# M3
# """
#
# m3_gun = PremadeWeapon(gun_item=misc.m3_greasegun,
#                        bullet=gun_parts.bullets_45_weighted,
#                        magazine=magazines.greasegun_mag,
#                        optics=optics_test,
#                        part_dict={
#                            "M3 Reciever": {misc.m3_reciever: 1,
#                                            misc.m3_reciever_picrail: 1},
#                            "M3 Barrel": {misc.m3_barrel: 1,
#                                          misc.m3_barrel_threaded: 1},
#                            "M3 Stock": {misc.single_shot_stock: 1,
#                                         misc.h015_birdshead: 1,
#                                         },
#                            "Muzzle Device": {
#                                attachments.muzzle_nullifier: 1,
#                                attachments.muzzle_kak_45: 1,
#                                attachments.muzzle_kak_a2: 1,
#                                attachments.suppressor_obsidian_45: 1,
#                            },
#                        },
#                        allowed_part_types=['M3 Reciever', 'M3 Barrel', 'M3 Stock', 'Muzzle Device', 'Optic']
#                        )
#
# """
# PPSh
# """
#
# ppsh_gun = PremadeWeapon(gun_item=misc.ppsh_41,
#                          # bullet={**gun_parts.bullets_76225_weighted, **gun_parts.bullets_9mm_weighted},
#                          bullet=gun_parts.bullets_76225_weighted,
#                          magazine={magazines.ppsh_mag_35rd: 1, magazines.ppsh_71rd: 1},
#                          optics=optics_test,
#                          part_dict={
#                              "PPSh Reciever": misc.ppsh_reciever,
#                              "PPSh Barrel": {misc.ppsh_barrel: 1,
#                                              misc.ppsh_barrel_obrez: 1,
#                                              # misc.ppsh_barrel_9mm: 1,
#                                              # misc.ppsh_barrel_obrez_9mm: 1
#                                              },
#                              "PPSh Dust Cover": {misc.ppsh_cover: 1,
#                                                  misc.ppsh_cover_obrez: 1,
#                                                  misc.ppsh_cover_tactical: 1,
#                                                  misc.ppsh_cover_obrez_tactical: 1,
#                                                  },
#                              "PPSh Stock": {misc.ppsh_stock: 1,
#                                             misc.ppsh_stock_obrez: 1,
#                                             },
#                          },
#                          allowed_part_types=['PPSh Reciever', 'PPSh Barrel', 'PPSh Dust Cover', 'PPSh Stock', 'Optic']
#                          )
#
# """
# SVT-40
# """
#
# svt40_gun = PremadeWeapon(gun_item=misc.svt,
#                           bullet=gun_parts.bullets_54r_weighted,
#                           magazine=magazines.svt_10rd,
#                           clip=magazines.svt_clip,
#                           optics=optics_test,
#                           part_dict={
#                               "SVT Reciever": {misc.svt_barrel: 1,
#                                                misc.svt_barrel_auto: 1,
#                                                },
#                               "SVT Stock": misc.stock_svt,
#                               "SVT Optics Mount": {misc.svt_pic_scope_mount: 1,
#                                                    None: 1},
#                           },
#                           allowed_part_types=['SVT Reciever', 'SVT Stock', 'SVT Optics Mount', 'Optic']
#                           )
