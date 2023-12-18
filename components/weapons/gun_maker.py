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
import components.weapons.attachments as attachments
import components.weapons.gun_parts_weighted as gun_parts

import components.weapons.bullets as bullets
import components.weapons.magazines as magazines
from copy import deepcopy, copy
from random import choices, randint

from entity import Item

# TODO - probability of parts themselves influenced by which level the player is on


class PremadeWeapon:
    def __init__(self, gun_item: Item, part_dict: dict, bullet, optics: dict, allowed_part_types:list,
                 magazine=None, name: str = '', clip=None):

        self.allowed_part_types = allowed_part_types
        self.gun_item = gun_item
        self.name = name
        self.part_dict = part_dict
        self.magazine = magazine
        self.optics = optics
        self.bullet = bullet
        self.clip = clip

    def update_properties(self) -> Item:

        optic_added = False
        prevent_suppression = False

        if isinstance(self.bullet, dict):
            self.bullet = choices(population=list(self.bullet.keys()), weights=list(self.bullet.values()), k=1)[0]

        self.bullet.stacking.stack_size = 1

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
            if self.part_dict[part].usable_properties.functional_part:
                self.part_dict[part].usable_properties.condition_function = randint(1, 5)

            if self.part_dict[part].usable_properties.accuracy_part:
                self.part_dict[part].usable_properties.condition_accuracy = randint(1, 5)

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
                    if not magazine_type == magazine.usable_properties.magazine_type:
                        del compatible_magazines[magazine]

                # randomly selects magazine
                magazine = choices(population=list(compatible_magazines.keys()),
                                   weights=list(compatible_magazines.values()), k=1)[0]
                self.magazine = magazine.usable_properties

            else:
                self.magazine = self.magazine.usable_properties

        else:
            self.magazine = self.gun_item.usable_properties

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


optics_test = {attachments.holosun503: 1, attachments.acog_ta01: 1, attachments.eotech_exps3: 1,
               attachments.aimpoint_comp: 1, attachments.kobra_ekp: 1, attachments.kobra_ekp_picrail: 1,
               attachments.amguh1: 1, attachments.compactprism: 1, attachments.pm2scope: 1, attachments.pso1: 1,
               attachments.okp7: 1, }

""" 
Glock 9mm
"""

g_17 = PremadeWeapon(gun_item=glock17.glock_17,
                     bullet=gun_parts.bullets_9mm_weighted,
                     optics=optics_test,
                     magazine={magazines.glock_mag_9mm: 100, magazines.glock_mag_9mm_33: 20,
                               magazines.glock_mag_9mm_50: 5, magazines.glock_mag_9mm_100: 2},
                     part_dict={
                         "Glock 17 Frame": glock17.glock17_frame,
                         "Glock 17 Barrel": {
                             glock17.glock17_barrel: 90,
                             glock17.glock17l_barrel: 60,
                             glock17.glock_9in_barrel: 30,
                             glock17.glock17_barrel_ported: 40,
                             glock17.glock17l_barrel_ported: 30,
                         },
                         "G17 Slide": {
                             glock17.glock17_slide: 80,
                             glock17.glock17l_slide: 40,
                             glock17.glock17_slide_optic: 60,
                             glock17.glock17l_slide_optic: 30,
                             glock17.glock17_slide_custom: 20,
                             glock17.glock17l_slide_custom: 15,
                         },
                         "Glock Stock": {None: 50, glock17.glock_stock: 4, glock17.glock_pistol_brace: 2},
                         "Glock Optics Mount": {None: 50, glock17.glock_pic_rail: 2},
                         "Glock Base Plate": {None: 20, glock17.glock_switch: 1},
                         "Muzzle Device": {None: 20, glock17.glock_9mm_compensator: 2,
                                           glock17.suppressor_surefire_9mm: 1},
                     },
                     allowed_part_types=['Glock 17 Frame', 'Glock 17 Barrel', 'G17 Slide', 'Glock Stock',
                                         'Muzzle Adapter', 'Glock Optics Mount', 'Glock Base Plate',
                                         'Side Mounted Accessory', 'Underbarrel Accessory', 'Optic', 'Muzzle Device']
                     )

""" 
AR
"""

ar_optics = {**optics_test, **{ar15.ar_carry_handle: 100, attachments.irons_troy_rear: 30,
                               attachments.irons_dd_rear: 20, attachments.irons_magpul_rear: 50,
                               attachments.irons_sig_rear: 10}}

ar15_weapon = PremadeWeapon(gun_item=ar15.ar15,
                            bullet=gun_parts.bullets_556_weighted,
                            magazine={magazines.stanag_30rd: 200, magazines.stanag_40rd: 15, magazines.stanag_50rd: 10,
                                      magazines.stanag_60rd: 5, magazines.stanag_100rd: 4},
                            optics=ar_optics,
                            part_dict={
                                "AR Lower Receiver": {ar15.lower_ar15: 15, ar15.lower_ar15_auto: 1},
                                "AR Upper Receiver": {ar15.upper_ar_m16a2: 3, ar15.upper_ar_m16a4: 1},
                                "AR Buffer": {ar15.ar15_buffer: 20, ar15.ar15_buffer_heavy: 1,
                                              ar15.ar15_buffer_light: 2},
                                "AR Barrel": {
                                    ar15.ar_barrel_standard_556: 35,
                                    ar15.ar_barrel_standard_556_midlen: 35,
                                    ar15.ar_barrel_carbine_556: 25,
                                    ar15.ar_barrel_carbine_556_carblen: 25,
                                    ar15.ar_barrel_pistol_556: 20,
                                    ar15.ar_barrel_pistol_556_pistollen: 20,
                                    ar15.ar_barrel_carbine_300: 10,
                                    ar15.ar_barrel_carbine_300_carbinelen: 10,
                                    ar15.ar_barrel_pistol_300: 5,
                                    ar15.ar_barrel_pistol_300_pistollen: 5,
                                },
                                "AR Handguard": {
                                    ar15.ar_handguard_m16a1: 5,
                                    ar15.ar_handguard_m16a2: 24,
                                    ar15.ar_handguard_m16a2_carbine: 20,
                                    ar15.ar_handguard_magpul: 14,
                                    ar15.ar_handguard_magpul_carbine: 10,
                                    ar15.ar_handguard_aero: 12,
                                    ar15.ar_handguard_aero_carbine: 12,
                                    ar15.ar_handguard_aero_pistol: 8,
                                    ar15.ar_handguard_faxon: 12,
                                    ar15.ar_handguard_faxon_carbine: 12,
                                    ar15.ar_handguard_faxon_pistol: 8,
                                    ar15.ar_handguard_mk18: 12,
                                },
                                "AR Grip": {
                                    ar15.ar_grip_trybe: 35,
                                    ar15.ar_grip_moe: 60,
                                    ar15.ar_grip_hogue: 20,
                                    ar15.ar_grip_strikeforce: 25,
                                    ar15.ar_grip_a2: 80,
                                    ar15.ar_grip_stark: 30,
                                },
                                "AR Stock": {
                                    None: 20,
                                    ar15.ar_stock_m16a2: 100,
                                    ar15.ar_stock_moe: 50,
                                    ar15.ar_stock_ubr: 20,
                                    ar15.ar_stock_danieldefense: 45,
                                    ar15.ar_stock_prs: 30,
                                    ar15.ar_stock_maxim_cqb: 10,
                                },
                                "AR Optics Mount": {None: 8, ar15.carry_handle_optic_mount: 1},
                                "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                                attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                                attachments.irons_sig_front: 10, },
                                "Muzzle Device": {
                                    ar15.ar15_muzzle_flashhider: 100,
                                    ar15.ar15_muzzle_st6012: 8,
                                    ar15.ar15_muzzle_mi_mb4: 5,
                                    ar15.ar15_muzzle_cobra: 3,
                                    attachments.suppressor_obsidian_9: 1,
                                    attachments.suppressor_wolfman_9mm: 1,
                                    ar15.ar15_300_muzzle_flashhider: 100,
                                    ar15.ar15_300_muzzle_cobra: 8,
                                    ar15.ar15_300_muzzle_pegasus: 5,
                                    ar15.ar15_300_muzzle_strike: 3,
                                },
                                "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 200,
                                    attachments.grip_hera_cqr: 6,
                                    attachments.grip_promag_vertical: 20,
                                    attachments.grip_jem_vertical: 20,
                                    attachments.grip_magpul_angled: 12,
                                    attachments.grip_magpul_mvg: 16,
                                    attachments.grip_aimtac_short: 15,
                                    attachments.grip_magpul_handstop: 12,
                                    attachments.grip_hipoint_folding: 5,
                                },
                            },
                            allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer', 'AR Barrel',
                                                'AR Handguard', 'AR Grip', 'AR Stock', 'Attachment Adapter',
                                                'Muzzle Adapter', 'Front Sight', 'AR Optics Mount',
                                                'Underbarrel Accessory', 'Side Mounted Accessory', 'Muzzle Device',
                                                'Optic']
                            )

ar10_weapon = PremadeWeapon(gun_item=ar15.ar15,
                            bullet=gun_parts.bullets_308_weighted,
                            magazine={magazines.ar10_20rd: 200, magazines.ar10_25rd: 15, magazines.ar10_40rd: 10,
                                      magazines.ar10_50rd: 5},
                            optics=ar_optics,
                            part_dict={
                                "AR Lower Receiver": {ar15.lower_ar10: 10, ar15.lower_ar10_auto: 1},
                                "AR Upper Receiver": ar15.upper_ar10,
                                "AR Buffer": {ar15.ar10_buffer: 20, ar15.ar10_buffer_heavy: 1,
                                              ar15.ar10_buffer_light: 2},
                                "AR Barrel": {
                                    ar15.ar_barrel_standard_308: 10,
                                    ar15.ar_barrel_standard_308_midlen: 20,
                                    ar15.ar_barrel_carbine_308_midlen: 15,
                                    ar15.ar_barrel_carbine_308_carblen: 15,
                                    ar15.ar_barrel_pistol_308_carblen: 5,
                                    ar15.ar_barrel_pistol_308_pistollen: 5,
                                },
                                "AR Handguard": {
                                    ar15.ar10_handguard_a2: 20,
                                    ar15.ar10_handguard_a2_carbine: 16,
                                    ar15.ar10_handguard_wilson: 12,
                                    ar15.ar_handguard_wilson_carbine: 12,
                                    ar15.ar10_handguard_vseven: 10,
                                    ar15.ar_handguard_vseven_carbine: 8,
                                    ar15.ar_handguard_vseven_pistol: 5,
                                    ar15.ar_handguard_hera_carbine: 8,
                                    ar15.ar_handguard_atlas_carbine: 8,
                                    ar15.ar_handguard_atlas_pistol: 5,
                                },
                                "AR Grip": {
                                    ar15.ar_grip_trybe: 35,
                                    ar15.ar_grip_moe: 60,
                                    ar15.ar_grip_hogue: 20,
                                    ar15.ar_grip_strikeforce: 25,
                                    ar15.ar_grip_a2: 80,
                                    ar15.ar_grip_stark: 30,
                                },
                                "AR Stock": {
                                    None: 20,
                                    ar15.ar_stock_m16a2: 100,
                                    ar15.ar_stock_moe: 50,
                                    ar15.ar_stock_ubr: 20,
                                    ar15.ar_stock_danieldefense: 45,
                                    ar15.ar_stock_prs: 30,
                                    ar15.ar_stock_maxim_cqb: 10,
                                },
                                "Front Sight": {ar15.ar_front_sight: 100, attachments.irons_troy_front: 30,
                                                attachments.irons_dd_front: 20, attachments.irons_magpul_front: 50,
                                                attachments.irons_sig_front: 10, },
                                "Muzzle Device": {
                                    ar15.ar15_muzzle_flashhider: 100,
                                    ar15.ar15_muzzle_st6012: 8,
                                    ar15.ar15_muzzle_mi_mb4: 5,
                                    ar15.ar15_muzzle_cobra: 3,
                                    ar15.ar15_300_muzzle_flashhider: 100,
                                    ar15.ar15_300_muzzle_cobra: 8,
                                    ar15.ar15_300_muzzle_pegasus: 5,
                                    ar15.ar15_300_muzzle_strike: 3,
                                },
                                "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 200,
                                    attachments.grip_hera_cqr: 6,
                                    attachments.grip_promag_vertical: 20,
                                    attachments.grip_jem_vertical: 20,
                                    attachments.grip_magpul_angled: 12,
                                    attachments.grip_magpul_mvg: 16,
                                    attachments.grip_aimtac_short: 15,
                                    attachments.grip_magpul_handstop: 12,
                                    attachments.grip_hipoint_folding: 5,
                                },
                            },
                            allowed_part_types=['AR Lower Receiver', 'AR Upper Receiver', 'AR Buffer', 'AR Barrel',
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
                            magazine={magazines.ak762_30rd: 200, magazines.ak762_40rd: 15, magazines.ak762_60rd: 7,
                                      magazines.ak762_75rd: 5, magazines.ak762_100rd: 4},
                            optics=optics_test,
                            part_dict={
                                "AK Reciever": {ak.reciever_akm: 10, ak.reciever_akm_auto: 1},
                                "AK Barrel": {ak.barrel_ak762: 100, ak.barrel_rpk762: 5, ak.barrel_ak762_short: 10},
                                "Thread Adapter": {None: 20,
                                                   attachments.thread_adapter_141_24mm: 1},
                                "AK Handguard": {
                                    ak.handguard_akm: 100,
                                    ak.handguard_amd65: 30,
                                    ak.handguard_ak74: 50,
                                    ak.handguard_romanian: 25,
                                    ak.handguard_ak100: 20,
                                    ak.handguard_B10M: 5,
                                    ak.handguard_leader: 5,
                                    ak.handguard_magpul: 20,
                                },
                                "AK Grip": {
                                    ak.grip_akm: 100,
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
                                    ak.stock_akm: 200,
                                    ak.stock_rpk: 20,
                                    ak.stock_ak74: 100,
                                    ak.stock_ak100: 15,
                                    ak.stock_ak_underfolder: 50,
                                    ak.stock_ak_triangle: 30,
                                    ak.stock_ak12: 5,
                                    ak.stock_amd65: 25,
                                    ak.stock_pt1: 10,
                                    ak.stock_moe: 40,
                                    ak.stock_zhukov: 35,
                                },
                                "AK Optics Mount": {None: 100, ak.accessory_dustcoverrail: 5,
                                                    ak.accessory_railsidemount: 5},
                                "Muzzle Device": {
                                    ak.muzzle_ak74: 150,
                                    ak.muzzle_dtk: 15,
                                    ak.muzzle_amd65: 30,
                                    ak.muzzle_akm: 300,
                                    ak.muzzle_akml: 100,
                                    ak.muzzle_lantac: 15,
                                    ak.muzzle_pbs4: 10,
                                    ak.muzzle_pbs1: 10,
                                    ak.muzzle_dynacomp: 12,
                                },
                                "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 200,
                                    attachments.grip_hera_cqr: 6,
                                    attachments.grip_promag_vertical: 20,
                                    attachments.grip_jem_vertical: 20,
                                    attachments.grip_magpul_angled: 12,
                                    attachments.grip_magpul_mvg: 16,
                                    attachments.grip_aimtac_short: 15,
                                    attachments.grip_magpul_handstop: 12,
                                    attachments.grip_hipoint_folding: 5,
                                },
                            },
                            allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
                                                'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
                                                'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
                                                'AK Magazine Adapter', 'Optic']
                            )

ak74_weapon = PremadeWeapon(gun_item=ak.ak,
                            bullet=gun_parts.bullets_545_weighted,
                            magazine={magazines.ak545_30rd: 200, magazines.ak545_45rd: 15, magazines.ak545_60rd: 7,
                                      magazines.ak545_100rd: 4},
                            optics=optics_test,
                            part_dict={
                                "AK Reciever": {ak.reciever_ak74: 10, ak.reciever_ak74_auto: 1},
                                "AK Barrel": {ak.barrel_ak545: 100, ak.barrel_rpk545: 5, ak.barrel_ak545_short: 10},
                                "Thread Adapter": {None: 20,
                                                   attachments.thread_adapter_2415_5824: 1},
                                "AK Handguard": {
                                    ak.handguard_akm: 100,
                                    ak.handguard_amd65: 30,
                                    ak.handguard_ak74: 50,
                                    ak.handguard_romanian: 25,
                                    ak.handguard_ak100: 20,
                                    ak.handguard_B10M: 5,
                                    ak.handguard_leader: 5,
                                    ak.handguard_magpul: 20,
                                },
                                "AK Grip": {
                                    ak.grip_akm: 100,
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
                                    None: 25,
                                    ak.stock_akm: 200,
                                    ak.stock_rpk: 20,
                                    ak.stock_ak74: 100,
                                    ak.stock_ak100: 15,
                                    ak.stock_ak_underfolder: 50,
                                    ak.stock_ak_triangle: 30,
                                    ak.stock_ak12: 5,
                                    ak.stock_amd65: 25,
                                    ak.stock_pt1: 10,
                                    ak.stock_moe: 40,
                                    ak.stock_zhukov: 35,
                                },
                                "AK Optics Mount": {None: 100, ak.accessory_dustcoverrail: 5,
                                                    ak.accessory_railsidemount: 5},
                                "Muzzle Device": {
                                    ak.muzzle_ak74: 150,
                                    ak.muzzle_dtk: 15,
                                    ak.muzzle_amd65: 30,
                                    ak.muzzle_akm: 300,
                                    ak.muzzle_akml: 100,
                                    ak.muzzle_lantac: 15,
                                    ak.muzzle_pbs4: 10,
                                    ak.muzzle_pbs1: 10,
                                    ak.muzzle_dynacomp: 12,
                                    ar15.ar15_300_muzzle_flashhider: 100,
                                    ar15.ar15_300_muzzle_cobra: 8,
                                    ar15.ar15_300_muzzle_pegasus: 5,
                                    ar15.ar15_300_muzzle_strike: 3,
                                },
                                "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                       attachments.adapter_mlok_picrail_short: 1},
                                "Underbarrel Accessory": {
                                    None: 200,
                                    attachments.grip_hera_cqr: 6,
                                    attachments.grip_promag_vertical: 20,
                                    attachments.grip_jem_vertical: 20,
                                    attachments.grip_magpul_angled: 12,
                                    attachments.grip_magpul_mvg: 16,
                                    attachments.grip_aimtac_short: 15,
                                    attachments.grip_magpul_handstop: 12,
                                    attachments.grip_hipoint_folding: 5,
                                },
                            },
                            allowed_part_types=['AK Reciever', 'AK Barrel', 'AK Handguard', 'AK Grip', 'AK Stock',
                                                'Attachment Adapter', 'Muzzle Adapter', 'AK Optics Mount',
                                                'Side Mounted Accessory', 'Underbarrel Accessory', 'Muzzle Device',
                                                'AK Magazine Adapter', 'Optic']
                            )

ak556_weapon = PremadeWeapon(gun_item=ak.ak,
                             bullet=gun_parts.bullets_556_weighted,
                             magazine=magazines.ak556_30rd,
                             optics=optics_test,
                             part_dict={
                                 "AK Reciever": {ak.reciever_100556: 10, ak.reciever_100556_auto: 1},
                                 "AK Barrel": {ak.barrel_ak556: 100, ak.barrel_ak556_short: 10},
                                 "Thread Adapter": {None: 20,
                                                    attachments.thread_adapter_2415_5824: 1},
                                 "AK Handguard": {
                                     ak.handguard_akm: 100,
                                     ak.handguard_amd65: 30,
                                     ak.handguard_ak74: 50,
                                     ak.handguard_romanian: 25,
                                     ak.handguard_ak100: 20,
                                     ak.handguard_B10M: 5,
                                     ak.handguard_leader: 5,
                                     ak.handguard_magpul: 20,
                                 },
                                 "AK Grip": {
                                     ak.grip_akm: 100,
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
                                     None: 25,
                                     ak.stock_akm: 200,
                                     ak.stock_rpk: 20,
                                     ak.stock_ak74: 100,
                                     ak.stock_ak100: 15,
                                     ak.stock_ak_underfolder: 50,
                                     ak.stock_ak_triangle: 30,
                                     ak.stock_ak12: 5,
                                     ak.stock_amd65: 25,
                                     ak.stock_pt1: 10,
                                     ak.stock_moe: 40,
                                     ak.stock_zhukov: 35,
                                 },
                                 "AK Optics Mount": {None: 100, ak.accessory_dustcoverrail: 5,
                                                     ak.accessory_railsidemount: 5},
                                 "Muzzle Device": {
                                     ak.muzzle_ak74: 150,
                                     ak.muzzle_dtk: 15,
                                     ak.muzzle_amd65: 30,
                                     ak.muzzle_akm: 300,
                                     ak.muzzle_akml: 100,
                                     ak.muzzle_lantac: 15,
                                     ak.muzzle_pbs4: 10,
                                     ak.muzzle_pbs1: 10,
                                     ak.muzzle_dynacomp: 12,
                                     ar15.ar15_300_muzzle_flashhider: 100,
                                     ar15.ar15_300_muzzle_cobra: 8,
                                     ar15.ar15_300_muzzle_pegasus: 5,
                                     ar15.ar15_300_muzzle_strike: 3,
                                 },
                                 "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                        attachments.adapter_mlok_picrail_short: 1},
                                 "Underbarrel Accessory": {
                                     None: 200,
                                     attachments.grip_hera_cqr: 6,
                                     attachments.grip_promag_vertical: 20,
                                     attachments.grip_jem_vertical: 20,
                                     attachments.grip_magpul_angled: 12,
                                     attachments.grip_magpul_mvg: 16,
                                     attachments.grip_aimtac_short: 15,
                                     attachments.grip_magpul_handstop: 12,
                                     attachments.grip_hipoint_folding: 5,
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
                                               m10.mac1045_upper_tactical: 20,
                                               m10.mac1045_upper_max: 4},
                                 "M10 Barrel": {m10.mac1045_barrel: 100,
                                                m10.mac1045_max_barrel: 5,
                                                m10.mac1045_carbine_barrel: 5,
                                                },
                                 "M10/45 Carbine Handguard": {m10.mac10_carbine_handguard_m16a2: 1,
                                                              m10.mac10_carbine_handguard_picatinny: 1},
                                 "Stock Adapter M10": {None: 50,
                                                       m10.mac10_ar_stock_adapter: 1},
                                 "M10 Stock": {m10.mac1045_full_stock: 8, m10.mac1045_folding_stock: 4,
                                               m10.mac1045_stock: 100},
                                 "AR Stock": {
                                     None: 20,
                                     ar15.ar_stock_m16a2: 100,
                                     ar15.ar_stock_moe: 50,
                                     ar15.ar_stock_ubr: 20,
                                     ar15.ar_stock_danieldefense: 45,
                                     ar15.ar_stock_prs: 30,
                                     ar15.ar_stock_maxim_cqb: 10,
                                 },
                                 "M10 Optics Mount": {None: 10, m10.mac10_optics_mount: 1},
                                 "Muzzle Device": {
                                     None: 50,
                                     attachments.muzzle_nullifier: 3,
                                     attachments.muzzle_kak_45: 5,
                                     attachments.muzzle_kak_a2: 50,
                                     m10.mac1045_sionics_suppressor: 1,
                                     m10.mac1045_extended_barrel: 5,
                                     attachments.suppressor_obsidian_45: 2,
                                 },
                                 "Accessory Adapter M10": {None: 10, m10.mac10_trirail: 1},
                                 "Underbarrel Accessory": {
                                     attachments.grip_hera_cqr: 6,
                                     attachments.grip_promag_vertical: 20,
                                     attachments.grip_jem_vertical: 20,
                                     attachments.grip_magpul_angled: 12,
                                     attachments.grip_magpul_mvg: 16,
                                     attachments.grip_aimtac_short: 15,
                                     attachments.grip_magpul_handstop: 12,
                                     attachments.grip_hipoint_folding: 5,
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
                                              m10.mac109_upper_tactical: 20,
                                              m10.mac109_upper_max: 4,
                                              m10.mac109_upper_max31: 2,
                                              m10.mac109_upper_max31k: 2,
                                              },
                                "M10 Barrel": {m10.mac109_barrel: 100,
                                               m10.mac109_max_barrel: 5,
                                               m10.mac109_carbine_barrel: 5,
                                               m10.max1031_barrel_1228: 5,
                                               m10.max1031k_barrel_1228: 5,
                                               m10.max1031_barrel_3410: 5,
                                               m10.max1031k_barrel_3410: 5,
                                               },
                                "M10/45 Carbine Handguard": {m10.mac109_carbine_handguard_m16a2: 1,
                                                             m10.mac109_carbine_handguard_picatinny: 1},
                                "Stock Adapter M10": {None: 50,
                                                      m10.mac10_ar_stock_adapter: 1},
                                "M10 Stock": {m10.mac1045_full_stock: 8, m10.mac1045_folding_stock: 4,
                                              m10.mac1045_stock: 100},
                                "AR Stock": {
                                    None: 20,
                                    ar15.ar_stock_m16a2: 100,
                                    ar15.ar_stock_moe: 50,
                                    ar15.ar_stock_ubr: 20,
                                    ar15.ar_stock_danieldefense: 45,
                                    ar15.ar_stock_prs: 30,
                                    ar15.ar_stock_maxim_cqb: 10,
                                },
                                "M10 Optics Mount": {None: 10, m10.mac10_optics_mount: 1},
                                "Muzzle Device": {
                                    None: 50,
                                    m10.mac109_sionics_suppressor: 1,
                                    m10.mac109_extended_barrel: 5,
                                    attachments.suppressor_wolfman_9mm: 3,
                                    attachments.suppressor_obsidian_9: 2,
                                },
                                "Accessory Adapter M10": {None: 10, m10.mac10_trirail: 1},
                                "Underbarrel Accessory": {
                                    attachments.grip_hera_cqr: 6,
                                    attachments.grip_promag_vertical: 20,
                                    attachments.grip_jem_vertical: 20,
                                    attachments.grip_magpul_angled: 12,
                                    attachments.grip_magpul_mvg: 16,
                                    attachments.grip_aimtac_short: 15,
                                    attachments.grip_magpul_handstop: 12,
                                    attachments.grip_hipoint_folding: 5,
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
                           magazine={magazines.ak762_30rd: 200, magazines.ak762_40rd: 15, magazines.ak762_60rd: 7,
                                     magazines.ak762_75rd: 5, magazines.ak762_100rd: 4, magazines.sks_mag_20rd: 200,
                                     magazines.sks_mag_35rd: 80, magazines.sks_mag_75rd: 8},
                           clip=magazines.sks_clip,
                           optics=optics_test,
                           part_dict={
                               "SKS Barrel": {
                                   sks.barrel_sks: 200,
                                   sks.barrel_sks_shortened: 70,
                                   sks.barrel_sks_auto: 20,
                                   sks.barrel_sks_shortened_auto: 15,
                                   sks.barrel_sks_akmag: 60,
                                   sks.barrel_sks_shortened_akmag: 30,
                                   sks.barrel_sks_auto_akmag: 10,
                                   sks.barrel_sks_shortened_auto_akmag: 5,
                               },
                               "Thread Adapter": {None: 20,
                                                  attachments.thread_adapter_sks: 1},
                               "SKS Stock": {
                                   sks.stock_sks: 200,
                                   sks.stock_sks_tapco: 20,
                                   sks.stock_sks_dragunov: 15,
                                   sks.stock_sks_fab: 10,
                                   sks.stock_sks_sabertooth: 6,
                                   sks.stock_sks_bullpup: 3,
                               },
                               "AR Grip": {
                                   ar15.ar_grip_trybe: 35,
                                   ar15.ar_grip_moe: 60,
                                   ar15.ar_grip_hogue: 20,
                                   ar15.ar_grip_strikeforce: 25,
                                   ar15.ar_grip_a2: 80,
                                   ar15.ar_grip_stark: 30,
                               },
                               "AR Stock": {
                                   None: 20,
                                   ar15.ar_stock_m16a2: 100,
                                   ar15.ar_stock_moe: 50,
                                   ar15.ar_stock_ubr: 20,
                                   ar15.ar_stock_danieldefense: 45,
                                   ar15.ar_stock_prs: 30,
                                   ar15.ar_stock_maxim_cqb: 10,
                               },
                               "SKS Internal Magazine": {sks.sks_integrated_mag: 1, None: 1},
                               "SKS Optics Mount": {None: 20, sks.sks_optics_mount: 1},
                               "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                      attachments.adapter_mlok_picrail_short: 1},
                               "Underbarrel Accessory": {
                                   None: 200,
                                   attachments.grip_hera_cqr: 6,
                                   attachments.grip_promag_vertical: 20,
                                   attachments.grip_jem_vertical: 20,
                                   attachments.grip_magpul_angled: 12,
                                   attachments.grip_magpul_mvg: 16,
                                   attachments.grip_aimtac_short: 15,
                                   attachments.grip_magpul_handstop: 12,
                                   attachments.grip_hipoint_folding: 5,
                               },
                               "Muzzle Device": {
                                   ak.muzzle_ak74: 150,
                                   ak.muzzle_dtk: 15,
                                   ak.muzzle_amd65: 30,
                                   ak.muzzle_akm: 300,
                                   ak.muzzle_akml: 100,
                                   ak.muzzle_lantac: 15,
                                   ak.muzzle_pbs4: 10,
                                   ak.muzzle_pbs1: 10,
                                   ak.muzzle_dynacomp: 12, },
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
                                     mosin.mosin_stock: 200,
                                     mosin.mosin_stock_montecarlo: 20,
                                     mosin.mosin_archangel_stock: 60,
                                     mosin.mosin_carbine_stock: 100,
                                     mosin.mosin_obrez_stock: 50,
                                 },
                                 "Mosin-Nagant Barrel": {
                                     mosin.mosin_barrel: 100,
                                     mosin.mosin_carbine_barrel: 50,
                                     mosin.mosin_obrez_barrel: 300,
                                 },
                                 "Thread Adapter": {None: 20,
                                                    attachments.thread_adapter_mosin: 1},
                                 "Mosin-Nagant Accessory Mount": {mosin.mosin_pic_scope_mount: 1, None: 20},
                                 "Muzzle Device": {
                                     None: 150,
                                     mosin.mosin_suppressor: 5,
                                     mosin.mosin_muzzlebreak: 10,
                                     ar15.ar15_muzzle_flashhider: 100,
                                     ar15.ar15_muzzle_st6012: 8,
                                     ar15.ar15_muzzle_mi_mb4: 5,
                                     ar15.ar15_muzzle_cobra: 3,
                                     ar15.ar15_300_muzzle_flashhider: 100,
                                     ar15.ar15_300_muzzle_cobra: 8,
                                     ar15.ar15_300_muzzle_pegasus: 5,
                                     ar15.ar15_300_muzzle_strike: 3,
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
                         magazine={magazines.m1911_mag_45_8: 200, magazines.m1911_mag_45_10: 20,
                                   magazines.m1911_mag_45_15: 10, magazines.m1911_mag_45_40: 3},
                         optics=optics_test,
                         part_dict={
                             "M1911 Frame": {m1911.m1911_frame_gov_ss: 200,
                                             m1911.m1911_frame_gov_alloy: 15,
                                             m1911.m1911_frame_gov_ss_tac: 20,
                                             m1911.m1911_frame_gov_alloy_tac: 5,
                                             m1911.m1911_frame_gov_ss_auto: 1,
                                             m1911.m1911_frame_gov_alloy_auto: 1,
                                             m1911.m1911_frame_gov_ss_tac_auto: 1,
                                             m1911.m1911_frame_gov_alloy_tac_auto: 1, },
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
                             "Muzzle Device": {None: 100, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                               m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10,
                                               attachments.suppressor_obsidian_45: 3},
                             "Underbarrel Accessory": {
                                 None: 200,
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
                              "M1911 Frame": {m1911.m1911_frame_gov_ss: 200,
                                              m1911.m1911_frame_gov_alloy: 15,
                                              m1911.m1911_frame_gov_ss_tac: 20,
                                              m1911.m1911_frame_gov_alloy_tac: 5,
                                              m1911.m1911_frame_gov_ss_auto: 1,
                                              m1911.m1911_frame_gov_alloy_auto: 1,
                                              m1911.m1911_frame_gov_ss_tac_auto: 1,
                                              m1911.m1911_frame_gov_alloy_tac_auto: 1, },
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
                              "Muzzle Device": {None: 100, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                                m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10},
                              "Underbarrel Accessory": {
                                  None: 200,
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
                               "M1911 Frame": {m1911.m1911_frame_gov_ss: 200,
                                               m1911.m1911_frame_gov_alloy: 15,
                                               m1911.m1911_frame_gov_ss_tac: 20,
                                               m1911.m1911_frame_gov_alloy_tac: 5,
                                               m1911.m1911_frame_gov_ss_auto: 1,
                                               m1911.m1911_frame_gov_alloy_auto: 1,
                                               m1911.m1911_frame_gov_ss_tac_auto: 1,
                                               m1911.m1911_frame_gov_alloy_tac_auto: 1, },
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
                               "Muzzle Device": {None: 100, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                                 m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10,
                                                 attachments.suppressor_obsidian_9: 2,
                                                 attachments.suppressor_wolfman_9mm: 2,
                                                 attachments.suppressor_octane45: 2},
                               "Underbarrel Accessory": {
                                   None: 200,
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
                               "M1911 Frame": {m1911.m1911_frame_gov_ss: 200,
                                               m1911.m1911_frame_gov_alloy: 15,
                                               m1911.m1911_frame_gov_ss_tac: 20,
                                               m1911.m1911_frame_gov_alloy_tac: 5,
                                               m1911.m1911_frame_gov_ss_auto: 1,
                                               m1911.m1911_frame_gov_alloy_auto: 1,
                                               m1911.m1911_frame_gov_ss_tac_auto: 1,
                                               m1911.m1911_frame_gov_alloy_tac_auto: 1, },
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
                               "Muzzle Device": {None: 100, m1911.m1911_comp_tj: 3, m1911.m1911_comp_punisher: 8,
                                                 m1911.m1911_comp_predator: 8, m1911.m1911_comp_castle: 10,
                                                 attachments.suppressor_octane45: 2},
                               "Underbarrel Accessory": {
                                   None: 200,
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
                                       m1_carbine.m1_stock: 100,
                                       m1_carbine.m1_stock_ebr: 2,
                                       m1_carbine.m1_stock_enforcer: 5,
                                       m1_carbine.m1_stock_springfield: 15
                                   },
                                   "M1/M2 Barrel": {
                                       m1_carbine.m1_barrel: 10,
                                       m1_carbine.m1_barrel_enforcer: 10,
                                       m1_carbine.m1_barrel_threaded: 1,
                                       m1_carbine.m1_barrel_enforcer_threaded: 1,
                                   },
                                   "AR Grip": {
                                       ar15.ar_grip_trybe: 35,
                                       ar15.ar_grip_moe: 60,
                                       ar15.ar_grip_hogue: 20,
                                       ar15.ar_grip_strikeforce: 25,
                                       ar15.ar_grip_a2: 80,
                                       ar15.ar_grip_stark: 30,
                                   },
                                   "AR Stock": {
                                       None: 20,
                                       ar15.ar_stock_m16a2: 100,
                                       ar15.ar_stock_moe: 50,
                                       ar15.ar_stock_ubr: 20,
                                       ar15.ar_stock_danieldefense: 45,
                                       ar15.ar_stock_prs: 30,
                                       ar15.ar_stock_maxim_cqb: 10,
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
                                       None: 200,
                                       attachments.grip_promag_vertical: 10,
                                       attachments.grip_jem_vertical: 10,
                                       attachments.grip_aimtac_short: 5,
                                       attachments.grip_hipoint_folding: 5,
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
                                       m1_carbine.m1_stock: 100,
                                       m1_carbine.m1_stock_ebr: 2,
                                       m1_carbine.m1_stock_enforcer: 5,
                                       m1_carbine.m1_stock_springfield: 15
                                   },
                                   "M1/M2 Barrel": {
                                       m1_carbine.m1_barrel: 10,
                                       m1_carbine.m1_barrel_enforcer: 10,
                                       m1_carbine.m1_barrel_threaded: 1,
                                       m1_carbine.m1_barrel_enforcer_threaded: 1,
                                   },
                                   "AR Grip": {
                                       ar15.ar_grip_trybe: 35,
                                       ar15.ar_grip_moe: 60,
                                       ar15.ar_grip_hogue: 20,
                                       ar15.ar_grip_strikeforce: 25,
                                       ar15.ar_grip_a2: 80,
                                       ar15.ar_grip_stark: 30,
                                   },
                                   "AR Stock": {
                                       None: 20,
                                       ar15.ar_stock_m16a2: 100,
                                       ar15.ar_stock_moe: 50,
                                       ar15.ar_stock_ubr: 20,
                                       ar15.ar_stock_danieldefense: 45,
                                       ar15.ar_stock_prs: 30,
                                       ar15.ar_stock_maxim_cqb: 10,
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
                                       None: 200,
                                       attachments.grip_promag_vertical: 10,
                                       attachments.grip_jem_vertical: 10,
                                       attachments.grip_aimtac_short: 5,
                                       attachments.grip_hipoint_folding: 5,
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
                        magazine={magazines.m14_10rd: 20, magazines.m14_20rd: 10, magazines.m14_50rd: 1},
                        optics=optics_test,
                        part_dict={
                            "M14 - Reciever": m14.m14_reciever,
                            "M14/M1A Stock": {m14.m14_stock_fiberglass: 15, m14.m14_stock_wood: 15,
                                              m14.m14_stock_archangel: 7, m14.m14_stock_bullpup: 1,
                                              m14.m14_stock_ebr: 2, m14.m14_stock_vltor: 5},
                            "M14/M1A Barrel": {m14.m14_barrel: 10, m14.m14_barrel_18in: 3, m14.m14_barrel_socom: 1},
                            "AR Grip": {
                                ar15.ar_grip_trybe: 35,
                                ar15.ar_grip_moe: 60,
                                ar15.ar_grip_hogue: 20,
                                ar15.ar_grip_strikeforce: 25,
                                ar15.ar_grip_a2: 80,
                                ar15.ar_grip_stark: 30,
                            },
                            "AR Stock": {
                                None: 20,
                                ar15.ar_stock_m16a2: 100,
                                ar15.ar_stock_moe: 50,
                                ar15.ar_stock_ubr: 20,
                                ar15.ar_stock_danieldefense: 45,
                                ar15.ar_stock_prs: 30,
                                ar15.ar_stock_maxim_cqb: 10,
                            },
                            "Thread Adapter": {None: 20,
                                               attachments.thread_adapter_m14_5824: 1},
                            "M14/M1A Picatinny Rail Optic Mount": {None: 15, m14.m14_optic_mount: 1},
                            "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                   attachments.adapter_mlok_picrail_short: 1},
                            "Underbarrel Accessory": {
                                None: 200,
                                attachments.grip_promag_vertical: 10,
                                attachments.grip_jem_vertical: 10,
                                attachments.grip_aimtac_short: 5,
                                attachments.grip_hipoint_folding: 5,
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

m1a_gun = PremadeWeapon(gun_item=m14.m1a,
                        bullet=gun_parts.bullets_308_weighted,
                        magazine={magazines.m14_10rd: 20, magazines.m14_20rd: 10, magazines.m14_50rd: 1},
                        optics=optics_test,
                        part_dict={
                            "M1A - Reciever": m14.m14_reciever,
                            "M14/M1A Stock": {m14.m14_stock_fiberglass: 15, m14.m14_stock_wood: 15,
                                              m14.m14_stock_archangel: 7, m14.m14_stock_bullpup: 1,
                                              m14.m14_stock_ebr: 2, m14.m14_stock_vltor: 5},
                            "M14/M1A Barrel": {m14.m14_barrel: 10, m14.m14_barrel_18in: 3, m14.m14_barrel_socom: 1},
                            "AR Grip": {
                                ar15.ar_grip_trybe: 35,
                                ar15.ar_grip_moe: 60,
                                ar15.ar_grip_hogue: 20,
                                ar15.ar_grip_strikeforce: 25,
                                ar15.ar_grip_a2: 80,
                                ar15.ar_grip_stark: 30,
                            },
                            "AR Stock": {
                                None: 20,
                                ar15.ar_stock_m16a2: 100,
                                ar15.ar_stock_moe: 50,
                                ar15.ar_stock_ubr: 20,
                                ar15.ar_stock_danieldefense: 45,
                                ar15.ar_stock_prs: 30,
                                ar15.ar_stock_maxim_cqb: 10,
                            },
                            "Thread Adapter": {None: 20,
                                               attachments.thread_adapter_m14_5824: 1},
                            "M14/M1A Picatinny Rail Optic Mount": {None: 15, m14.m14_optic_mount: 1},
                            "Attachment Adapter": {None: 30, attachments.adapter_mlok_picrail: 1,
                                                   attachments.adapter_mlok_picrail_short: 1},
                            "Underbarrel Accessory": {
                                None: 200,
                                attachments.grip_promag_vertical: 10,
                                attachments.grip_jem_vertical: 10,
                                attachments.grip_aimtac_short: 5,
                                attachments.grip_hipoint_folding: 5,
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
                        allowed_part_types=['M1A - Reciever', 'M14/M1A Stock', 'M14/M1A Barrel',
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
                             "Model 870 Reciever": {r870.reciever_r870_4rd: 100,
                                                    r870.reciever_r870dm: 5,
                                                    r870.reciever_r870_6rd: 20},
                             "Model 870 Barrel": {r870.r870_barrel_26: 200,
                                                  r870.r870_barrel_18: 75,
                                                  r870.r870_barrel_t14: 30,
                                                  r870.r870_barrel_18_bead: 25,
                                                  r870.r870_barrel_t14_bead: 15},
                             "Model 870 Stock": {r870.r870_stock: 300,
                                                 r870.r870_stock_polymer: 300,
                                                 r870.r870_stock_magpul: 75,
                                                 r870.r870_stock_shockwave: 25,
                                                 r870.r870_stock_pistol: 15,
                                                 r870.r870_stock_maverick: 40,
                                                 r870.r870_stock_sterling: 15,
                                                 r870.r870_ar_stock_adapter: 5},
                             "AR Grip": {
                                 ar15.ar_grip_trybe: 35,
                                 ar15.ar_grip_moe: 60,
                                 ar15.ar_grip_hogue: 20,
                                 ar15.ar_grip_strikeforce: 25,
                                 ar15.ar_grip_a2: 80,
                                 ar15.ar_grip_stark: 30,
                             },
                             "AR Stock": {
                                 None: 20,
                                 ar15.ar_stock_m16a2: 100,
                                 ar15.ar_stock_moe: 50,
                                 ar15.ar_stock_ubr: 20,
                                 ar15.ar_stock_danieldefense: 45,
                                 ar15.ar_stock_prs: 30,
                                 ar15.ar_stock_maxim_cqb: 10,
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
                                 r870.r870_choke_cylinder_ported: 40,
                             },
                             "Model 870 Magazine Extension": {
                                 None: 100,
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
                                                        r870.r870_stock_magpul: 75,
                                                        r870.r870_stock_shockwave: 25,
                                                        r870.r870_stock_pistol: 15,
                                                        r870.r870_stock_maverick: 40,
                                                        r870.r870_stock_sterling: 15,
                                                        r870.r870_ar_stock_adapter: 5},
                                    "AR Grip": {
                                        ar15.ar_grip_trybe: 35,
                                        ar15.ar_grip_moe: 60,
                                        ar15.ar_grip_hogue: 20,
                                        ar15.ar_grip_strikeforce: 25,
                                        ar15.ar_grip_a2: 80,
                                        ar15.ar_grip_stark: 30,
                                    },
                                    "AR Stock": {
                                        None: 20,
                                        ar15.ar_stock_m16a2: 100,
                                        ar15.ar_stock_moe: 50,
                                        ar15.ar_stock_ubr: 20,
                                        ar15.ar_stock_danieldefense: 45,
                                        ar15.ar_stock_prs: 30,
                                        ar15.ar_stock_maxim_cqb: 10,
                                    },
                                    "Model 870 Choke": {
                                        r870.r870_choke_im: 15,
                                        r870.r870_choke_modified: 50,
                                        r870.r870_choke_cylinder: 300,
                                        r870.r870_choke_improved_ported: 10,
                                        r870.r870_choke_cylinder_ported: 40,
                                    },
                                    "Model 870 Magazine Extension": {
                                        None: 100,
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
