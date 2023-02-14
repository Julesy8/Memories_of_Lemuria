import components.weapons.glock17 as glock17
# import ar15
# import kalashnikov
# import mac10
# import sks
# import mosin
import components.weapons.attachments as attachments
import components.weapons.gun_parts_weighted as gun_parts

import components.weapons.magazines as magazines
from copy import deepcopy, copy
from random import choices, randint

from entity import Item

optics_test = {attachments.holosun503: 1, attachments.acog_ta01: 1, attachments.eotech_exps3: 1,
               attachments.aimpoint_comp: 1, attachments.kobra_ekp: 1, attachments.kobra_ekp_picrail: 1,
               attachments.amguh1: 1, attachments.compactprism: 1, attachments.pm2scope: 1, attachments.pso1: 1,
               attachments.okp7: 1, }


class PremadeWeapon:
    def __init__(self, gun_item: Item, part_dict: dict, bullet, optics: dict, magazine=None, name: str = ''):

        self.gun_item = gun_item
        self.name = name
        self.part_dict = part_dict
        self.magazine = magazine
        self.optics = optics
        self.bullet = bullet

    def update_properties(self) -> Item:

        optic_added = False
        prevent_suppression = False

        if isinstance(self.magazine, dict):
            self.magazine = choices(population=list(self.magazine.keys()), weights=list(self.magazine.values()), k=1)[0]

        if isinstance(self.bullet, dict):
            self.bullet = choices(population=list(self.bullet.keys()), weights=list(self.bullet.values()), k=1)[0]

        self.bullet.stacking.stack_size = 1

        compatible_parts = {}
        attachment_points = []

        # sets part values
        for part in self.part_dict.keys():

            # checks if current part selection is the same as the type as item in the prerequisite parts
            # if it is, only adds parts to options that are in prerequisites
            add_only_compatible = False
            for part_type in compatible_parts.keys():
                if part_type == part:
                    add_only_compatible = True

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
                        tags = [x.usable_properties.part_type, ]

                        if hasattr(x.usable_properties, 'tags'):
                            tags.extend(getattr(x.usable_properties, 'tags'))

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

                selection = deepcopy(choices(population=list(self.part_dict[part].keys()),
                                             weights=list(self.part_dict[part].values()), k=1)[0])
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
                        compatible_parts[key] = \
                            value.extend(self.part_dict[part].usable_properties.compatible_parts[key])
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
            if self.part_dict[part].usable_properties.functional_part:
                self.part_dict[part].usable_properties.condition_function = randint(1, 5)

            if self.part_dict[part].usable_properties.accuracy_part:
                self.part_dict[part].usable_properties.condition_accuracy = randint(1, 5)

        # sets magazine if gun has internal magazine
        if self.magazine is None and hasattr(self.gun_item.usable_properties, 'magazine'):
            self.magazine = self.gun_item
            self.gun_item.usable_properties.previously_loaded_round = self.bullet

        # loads magazine with bullets
        for i in range(self.magazine.usable_properties.mag_capacity):
            self.magazine.usable_properties.magazine.append(self.bullet)

        # sets chambered round
        self.gun_item.usable_properties.chambered_bullet = self.bullet

        # if not keep_round_chambered - i.e. gun is bolt action or open bolt, removes bullet from magazine
        if not self.gun_item.usable_properties.keep_round_chambered:
            self.magazine.usable_properties.magazine.pop()

        # sets magazine if gun if magazine fed
        if hasattr(self.gun_item.usable_properties, 'loaded_magazine'):
            self.gun_item.usable_properties.loaded_magazine = self.magazine
            self.gun_item.usable_properties.previously_loaded_magazine = deepcopy(self.magazine)

        # updates gun properties
        self.gun_item.usable_properties.parts.update_partlist(attachment_dict={})

        # sets gun name
        if not self.name == '':
            self.gun_item.name = self.name

        return self.gun_item


""" 
Glock 9mm
"""

# TODO - make proper classes
glock17_normal = PremadeWeapon(gun_item=deepcopy(glock17.glock_17), name='Glock 17',
                               bullet=deepcopy(gun_parts.bullets_9mm_weighted),
                               optics=optics_test,
                               magazine=deepcopy({magazines.glock_mag_9mm: 50, magazines.glock_mag_9mm_33: 10,
                                                  magazines.glock_mag_9mm_50: 5, magazines.glock_mag_9mm_100: 1}),
                               part_dict={
                                   "Glock 17 Frame": glock17.glock17_frame,
                                   "Glock 17 Barrel": {glock17.glock17_barrel: 1,
                                                       glock17.glock17l_barrel: 1,
                                                       glock17.glock_9in_barrel: 1,
                                                       glock17.glock17_barrel_ported: 1,
                                                       glock17.glock17l_barrel_ported: 1,
                                                       },
                                   "Glock 17 Slide": {glock17.glock17_slide: 1,
                                                      glock17.glock17l_slide: 1,
                                                      glock17.glock17_slide_optic: 1,
                                                      glock17.glock17l_slide_optic: 1,
                                                      glock17.glock17_slide_custom: 1,
                                                      glock17.glock17l_slide_custom: 1,
                                                      },
                                   "Glock Stock": {None: 10, glock17.glock_stock: 1, glock17.glock_pistol_brace: 1},
                                   "Glock Optics Mount": {None: 10, glock17.glock_pic_rail: 1},
                                   "Glock Base Plate": {None: 10, glock17.glock_switch: 1},
                                   "Muzzle Device": {None: 10, glock17.glock_9mm_compensator: 1,
                                                     glock17.suppressor_surefire_9mm: 1},
                               },
                               )

""" 
AR 15 5.56 
"""
#
# ar15_m16a4 = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16A4',
#                            bullet=deepcopy(bullets.round_556_60_fmj),
#                            magazine=deepcopy(magazines.stanag_30rd),
#                            part_dict={
#                                "AR Lower Receiver": ar15.lower_ar15,
#                                "AR Upper Receiver": ar15.upper_ar_m16a2,
#                                "AR Buffer": ar15.ar15_buffer,
#                                "AR Barrel": ar15.ar_barrel_standard_556,
#                                "AR Handguard": ar15.ar_handguard_m16a2,
#                                "AR Grip": ar15.ar_grip_a2,
#                                "AR Stock": ar15.ar_stock_m16a2,
#                                "Front Sight": ar15.ar_front_sight,
#                                "Muzzle Device": ar15.ar15_muzzle_flashhider,
#                            },
#                            ).update_properties()

"""
AK 7.62
"""

# akm = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AKM',
#                     bullet=deepcopy(bullets.round_76239_123_fmj),
#                     magazine=deepcopy(magazines.ak762_30rd),
#                     part_dict={
#                         "AK Reciever": kalashnikov.reciever_akm,
#                         "AK Barrel": kalashnikov.barrel_ak762,
#                         "AK Handguard": kalashnikov.handguard_akm,
#                         "AK Grip": kalashnikov.grip_akm,
#                         "AK Stock": kalashnikov.stock_akm,
#                         "Muzzle Device": kalashnikov.muzzle_akm,
#                     },
#                     ).update_properties()

"""
MAC 10
"""

# mac109 = PremadeWeapon(gun_item=deepcopy(mac10.mac10), name='M10/9',
#                        bullet=deepcopy(bullets.round_9mm_124_fmj),
#                        magazine=deepcopy(magazines.mac10_mag_9),
#                        part_dict={
#                            "M10 Lower": mac10.mac109_lower,
#                            "M10 Upper": mac10.mac109_upper,
#                            'M10 Barrel': mac10.mac109_barrel,
#                        },
#                        ).update_properties()
#
# mac1045 = PremadeWeapon(gun_item=deepcopy(mac10.mac10), name='M10/45',
#                         bullet=deepcopy(bullets.round_45_200_fmj),
#                         magazine=deepcopy(magazines.mac10_mag_45),
#                         part_dict={
#                             "M10 Lower": mac10.mac1045_lower,
#                             "M10 Upper": mac10.mac1045_upper,
#                             'M10 Barrel': mac10.mac1045_barrel,
#                         },
#                         ).update_properties()

"""
SKS
"""

# sks_gun = PremadeWeapon(gun_item=deepcopy(sks.sks), name='SKS',
#                         bullet=deepcopy(bullets.round_76239_150_fmj),
#                         part_dict={
#                             "SKS Barrel": sks.barrel_sks,
#                             "SKS Stock": sks.stock_sks,
#                         },
#                         ).update_properties()

"""
Mosin Nagant
"""

# mosin_gun = PremadeWeapon(gun_item=deepcopy(mosin.mosin_nagant), name='Mosin-Nagant M91/30',
#                           bullet=deepcopy(bullets.round_54r_174_jrn),
#                           part_dict={
#                               "Mosin-Nagant Stock": mosin.mosin_stock,
#                               "Mosin-Nagant Barrel": mosin.mosin_barrel,
#                           },
#                           ).update_properties()
