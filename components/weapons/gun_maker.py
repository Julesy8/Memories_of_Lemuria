import glock17
import ar15
import kalashnikov
import mac10
import sks
import mosin
import attachments

from typing import Optional
import components.weapons.bullets as bullets
import components.weapons.magazines as magazines
from copy import deepcopy

import pickle

from components.consumables import Bullet
from entity import Item


class PremadeWeapon:
    def __init__(self, gun_item: Item, name: str, part_dict: dict, bullet: Bullet,
                 optic_mount: Optional[Item] = None, magazine: Optional[Item] = None):

        self.gun_item = gun_item
        self.name = name
        self.part_dict = part_dict
        self.optic_mount = optic_mount
        self.magazine = magazine
        self.bullet = bullet

        for key, value in self.part_dict.items():
            setattr(self.gun_item.usable_properties.parts, key, deepcopy(value))

        if self.magazine is None and hasattr(self.gun_item.usable_properties, 'magazine'):
            self.magazine = self.gun_item

        for i in range(self.magazine.usable_properties.mag_capacity):
            self.magazine.usable_properties.magazine.append(bullet)

    def update_properties(self) -> Item:

        self.gun_item.usable_properties.chambered_bullet = self.bullet

        if hasattr(self.gun_item.usable_properties, 'loaded_magazine'):
            self.gun_item.usable_properties.loaded_magazine = self.magazine

        self.gun_item.usable_properties.parts.update_partlist(attachment_dict={})
        if self.optic_mount is not None and hasattr(self.optic_mount.usable_properties, 'optic_mount_properties'):
            self.gun_item.usable_properties.parts. \
                set_property(self.optic_mount.usable_properties.optic_mount_properties)
        self.gun_item.name = self.name
        return self.gun_item


""" 
Glock 9mm
"""

glock17_stock = PremadeWeapon(gun_item=deepcopy(glock17.glock_17), name='Glock 17',
                              bullet=deepcopy(bullets.round_9mm_115_fmj),
                              magazine=deepcopy(magazines.glock_mag_9mm),
                              part_dict={
                                  "Glock 17 Frame": glock17.glock17_frame,
                                  "Glock 17 Barrel": glock17.glock17_barrel,
                                  "Glock 17 Slide": glock17.glock17_slide, },
                              ).update_properties()

glock17_comp = PremadeWeapon(gun_item=deepcopy(glock17.glock_17), name='Glock 17 - Competition',
                             bullet=deepcopy(bullets.round_9mm_115_fmj),
                             magazine=deepcopy(magazines.glock_mag_9mm),
                             part_dict={
                                 "Glock 17 Frame": glock17.glock17_frame,
                                 "Glock 17 Barrel": glock17.glock17_barrel_ported,
                                 "Glock 17 Slide": glock17.glock17_slide_custom, },
                             ).update_properties()

glock17_auto = PremadeWeapon(gun_item=deepcopy(glock17.glock_17), name='Glock 17 Automatic',
                             bullet=deepcopy(bullets.round_9mm_115_fmj),
                             magazine=deepcopy(magazines.glock_mag_9mm_33),
                             part_dict={
                                 "Glock 17 Frame": glock17.glock17_frame,
                                 "Glock 17 Barrel": glock17.glock17_barrel,
                                 "Glock 17 Slide": glock17.glock17_slide,
                                 "Glock Base Plate": glock17.glock_switch,
                             },
                             ).update_properties()

glock17_pdw = PremadeWeapon(gun_item=deepcopy(glock17.glock_17), name='Glock 17 PDW',
                            bullet=deepcopy(bullets.round_9mm_115_fmj),
                            magazine=deepcopy(magazines.glock_mag_9mm),
                            part_dict={
                                "Glock 17 Frame": glock17.glock17_frame,
                                "Glock 17 Barrel": glock17.glock17_barrel,
                                "Glock 17 Slide": glock17.glock17_slide,
                                "Muzzle Device": glock17.glock_9mm_compensator,
                                "Glock Stock": glock17.glock_pistol_brace,
                            },
                            ).update_properties()

glock17l = PremadeWeapon(gun_item=deepcopy(glock17.glock_17), name='Glock 17L',
                         bullet=deepcopy(bullets.round_9mm_115_fmj),
                         magazine=deepcopy(magazines.glock_mag_9mm),
                         part_dict={
                             "Glock 17 Frame": glock17.glock17_frame,
                             "Glock 17 Barrel": glock17.glock17l_barrel,
                             "Glock 17 Slide": glock17.glock17l_slide, },
                         ).update_properties()

glock17l_comp = PremadeWeapon(gun_item=deepcopy(glock17.glock_17), name='Glock 17L - Competition',
                              bullet=deepcopy(bullets.round_9mm_115_fmj),
                              magazine=deepcopy(magazines.glock_mag_9mm),
                              part_dict={
                                  "Glock 17 Frame": glock17.glock17_frame,
                                  "Glock 17 Barrel": glock17.glock17l_barrel_ported,
                                  "Glock 17 Slide": glock17.glock17l_slide_custom, },
                              ).update_properties()

""" 
AR 15 5.56 
"""

ar15_m16a4 = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16A4',
                           bullet=deepcopy(bullets.round_556_60_fmj),
                           magazine=deepcopy(magazines.stanag_30rd),
                           part_dict={
                               "AR Lower Receiver": ar15.lower_ar15,
                               "AR Upper Receiver": ar15.upper_ar_m16a2,
                               "AR Buffer": ar15.ar15_buffer,
                               "AR Barrel": ar15.ar_barrel_standard_556,
                               "AR Handguard": ar15.ar_handguard_m16a2,
                               "AR Grip": ar15.ar_grip_a2,
                               "AR Stock": ar15.ar_stock_m16a2,
                               "Front Sight": ar15.ar_front_sight,
                               "Muzzle Device": ar15.ar15_muzzle_flashhider,
                           },
                           ).update_properties()

ar15_lmg = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16 LMG',
                         bullet=deepcopy(bullets.round_556_60_fmj),
                         magazine=deepcopy(magazines.stanag_60rd),
                         optic_mount=deepcopy(ar15.upper_ar_m16a4),
                         part_dict={
                             "AR Lower Receiver": ar15.lower_ar15,
                             "AR Upper Receiver": ar15.upper_ar_m16a4,
                             "AR Buffer": ar15.ar15_buffer_heavy,
                             "AR Barrel": ar15.ar_barrel_standard_556,
                             "AR Handguard": ar15.ar_handguard_m16a2,
                             "AR Grip": ar15.ar_grip_a2,
                             "AR Stock": ar15.ar_stock_m16a2,
                             "Front Sight": ar15.ar_front_sight,
                             "Optic": attachments.eotech_exps3,
                             "Muzzle Device": ar15.ar15_muzzle_flashhider,
                         },
                         ).update_properties()

car15 = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='CAR-15',
                      bullet=deepcopy(bullets.round_556_60_fmj),
                      magazine=deepcopy(magazines.stanag_30rd),
                      part_dict={
                          "AR Lower Receiver": ar15.lower_ar15,
                          "AR Upper Receiver": ar15.upper_ar_m16a2,
                          "AR Buffer": ar15.ar15_buffer,
                          "AR Barrel": ar15.ar_barrel_carbine_556_carblen,
                          "AR Handguard": ar15.ar_handguard_m16a2,
                          "AR Grip": ar15.ar_grip_a2,
                          "AR Stock": ar15.ar_stock_moe,
                          "Front Sight": ar15.ar_front_sight,
                          "Muzzle Device": ar15.ar15_muzzle_flashhider,
                      },
                      ).update_properties()

ar15_marksman = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16 - Marksman',
                              bullet=deepcopy(bullets.round_556_60_fmj),
                              magazine=deepcopy(magazines.stanag_30rd),
                              optic_mount=deepcopy(ar15.upper_ar_m16a4),
                              part_dict={
                                  "AR Lower Receiver": ar15.lower_ar15,
                                  "AR Upper Receiver": ar15.upper_ar_m16a4,
                                  "AR Buffer": ar15.ar15_buffer,
                                  "AR Barrel": ar15.ar_barrel_standard_556,
                                  "AR Handguard": ar15.ar_handguard_m16a2,
                                  "AR Grip": ar15.ar_grip_a2,
                                  "AR Stock": ar15.ar_stock_prs,
                                  "Front Sight": ar15.ar_front_sight,
                                  "Muzzle Device": ar15.ar15_muzzle_flashhider,
                                  "Optic": attachments.pm2scope
                              },
                              ).update_properties()

ar15_pistol = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16 Pistol',
                            bullet=deepcopy(bullets.round_556_60_fmj),
                            magazine=deepcopy(magazines.stanag_30rd),
                            part_dict={
                                "AR Lower Receiver": ar15.lower_ar15,
                                "AR Upper Receiver": ar15.upper_ar_m16a2,
                                "AR Buffer": ar15.ar15_buffer,
                                "AR Barrel": ar15.ar_barrel_pistol_556_pistollen,
                                "AR Handguard": ar15.ar_handguard_faxon_pistol,
                                "AR Grip": ar15.ar_grip_a2,
                                "AR Stock": ar15.ar_stock_moe,
                                "Front Sight": ar15.ar_front_sight,
                                "Muzzle Device": ar15.ar15_muzzle_flashhider,
                            },
                            ).update_properties()

ar15_m4carbine = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M4 Carbine',
                               bullet=deepcopy(bullets.round_556_60_fmj),
                               magazine=deepcopy(magazines.stanag_30rd),
                               optic_mount=deepcopy(ar15.upper_ar_m16a4),
                               part_dict={
                                   "AR Lower Receiver": ar15.lower_ar15,
                                   "AR Upper Receiver": ar15.upper_ar_m16a4,
                                   "AR Buffer": ar15.ar15_buffer,
                                   "AR Barrel": ar15.ar_barrel_carbine_556,
                                   "AR Handguard": ar15.ar_handguard_mk18,
                                   "AR Grip": ar15.ar_grip_a2,
                                   "AR Stock": ar15.ar_stock_moe,
                                   "Front Sight": ar15.ar_front_sight,
                                   "Muzzle Device": ar15.ar15_muzzle_flashhider,
                                   "Optic": attachments.eotech_exps3
                               },
                               ).update_properties()

# .300

ar15_pistol_300 = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16 .300 Blackout Pistol',
                                bullet=deepcopy(bullets.round_300aac_150_jhp),
                                magazine=deepcopy(magazines.stanag_30rd),
                                part_dict={
                                    "AR Lower Receiver": ar15.lower_ar15,
                                    "AR Upper Receiver": ar15.upper_ar_m16a2,
                                    "AR Buffer": ar15.ar15_buffer,
                                    "AR Barrel": ar15.ar_barrel_pistol_300,
                                    "AR Handguard": ar15.ar_handguard_faxon_pistol,
                                    "AR Grip": ar15.ar_grip_a2,
                                    "AR Stock": ar15.ar_stock_moe,
                                    "Front Sight": ar15.ar_front_sight,
                                    "Muzzle Device": ar15.ar15_300_muzzle_flashhider,
                                },
                                ).update_properties()

ar15_m4carbine_300 = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16 .300 Blackout Carbine',
                                   bullet=deepcopy(bullets.round_300aac_150_jhp),
                                   magazine=deepcopy(magazines.stanag_30rd),
                                   optic_mount=deepcopy(ar15.upper_ar_m16a4),
                                   part_dict={
                                       "AR Lower Receiver": ar15.lower_ar15,
                                       "AR Upper Receiver": ar15.upper_ar_m16a4,
                                       "AR Buffer": ar15.ar15_buffer,
                                       "AR Barrel": ar15.ar_barrel_carbine_300,
                                       "AR Handguard": ar15.ar_handguard_mk18,
                                       "AR Grip": ar15.ar_grip_a2,
                                       "AR Stock": ar15.ar_stock_moe,
                                       "Front Sight": ar15.ar_front_sight,
                                       "Muzzle Device": ar15.ar15_300_muzzle_flashhider,
                                       "Optic": attachments.eotech_exps3
                                   },
                                   ).update_properties()

# AR-10

ar10 = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='AR10',
                     bullet=deepcopy(bullets.round_308_150_fmj),
                     magazine=deepcopy(magazines.ar10_20rd),
                     part_dict={
                         "AR Lower Receiver": ar15.lower_ar10,
                         "AR Upper Receiver": ar15.upper_ar10,
                         "AR Buffer": ar15.ar10_buffer,
                         "AR Barrel": ar15.ar_barrel_standard_308,
                         "AR Handguard": ar15.ar10_handguard_a2,
                         "AR Grip": ar15.ar_grip_a2,
                         "AR Stock": ar15.ar_stock_m16a2,
                         "Front Sight": ar15.ar_front_sight,
                         "Muzzle Device": ar15.ar15_300_muzzle_flashhider,
                     },
                     ).update_properties()

ar10_lmg = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='AR10 LMG',
                         bullet=deepcopy(bullets.round_308_150_fmj),
                         magazine=deepcopy(magazines.ar10_40rd),
                         optic_mount=deepcopy(ar15.upper_ar10),
                         part_dict={
                             "AR Lower Receiver": ar15.lower_ar10,
                             "AR Upper Receiver": ar15.upper_ar10,
                             "AR Buffer": ar15.ar10_buffer,
                             "AR Barrel": ar15.ar_barrel_standard_308,
                             "AR Handguard": ar15.ar10_handguard_vseven,
                             "AR Grip": ar15.ar_grip_a2,
                             "AR Stock": ar15.ar_stock_m16a2,
                             "Front Sight": ar15.ar_front_sight,
                             "Muzzle Device": ar15.ar15_300_muzzle_pegasus,
                             "Optic": attachments.acog_ta01,
                         },
                         ).update_properties()

ar10_marksman = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='AR10 - Marksman',
                              bullet=deepcopy(bullets.round_308_150_fmj),
                              magazine=deepcopy(magazines.ar10_20rd),
                              optic_mount=deepcopy(ar15.upper_ar10),
                              part_dict={
                                  "AR Lower Receiver": ar15.lower_ar10,
                                  "AR Upper Receiver": ar15.upper_ar10,
                                  "AR Buffer": ar15.ar10_buffer,
                                  "AR Barrel": ar15.ar_barrel_standard_308,
                                  "AR Handguard": ar15.ar10_handguard_wilson,
                                  "AR Grip": ar15.ar_grip_a2,
                                  "AR Stock": ar15.ar_stock_prs,
                                  "Front Sight": ar15.ar_front_sight,
                                  "Muzzle Device": ar15.ar15_300_muzzle_pegasus,
                                  "Optic": attachments.pm2scope,
                              },
                              ).update_properties()

ar10_pistol = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='AR10 Pistol',
                            bullet=deepcopy(bullets.round_308_150_fmj),
                            magazine=deepcopy(magazines.ar10_20rd),
                            optic_mount=deepcopy(ar15.upper_ar10),
                            part_dict={
                                "AR Lower Receiver": ar15.lower_ar10,
                                "AR Upper Receiver": ar15.upper_ar10,
                                "AR Buffer": ar15.ar10_buffer,
                                "AR Barrel": ar15.ar_barrel_pistol_308_pistollen,
                                "AR Handguard": ar15.ar10_handguard_a2_carbine,
                                "AR Grip": ar15.ar_grip_a2,
                                "AR Stock": ar15.ar_stock_moe,
                                "Front Sight": ar15.ar_front_sight,
                                "Muzzle Device": ar15.ar15_300_muzzle_flashhider,
                                "Optic": attachments.holosun503,
                            },
                            ).update_properties()

ar10_m4carbine = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='AR10 Carbine',
                               bullet=deepcopy(bullets.round_308_150_fmj),
                               magazine=deepcopy(magazines.ar10_20rd),
                               optic_mount=deepcopy(ar15.upper_ar10),
                               part_dict={
                                   "AR Lower Receiver": ar15.lower_ar10,
                                   "AR Upper Receiver": ar15.upper_ar10,
                                   "AR Buffer": ar15.ar10_buffer,
                                   "AR Barrel": ar15.ar_barrel_carbine_308_carblen,
                                   "AR Handguard": ar15.ar10_handguard_a2,
                                   "AR Grip": ar15.ar_grip_a2,
                                   "AR Stock": ar15.ar_stock_moe,
                                   "Front Sight": ar15.ar_front_sight,
                                   "Muzzle Device": ar15.ar15_300_muzzle_flashhider,
                                   "Optic": attachments.eotech_exps3,
                               },
                               ).update_properties()

"""
AK 7.62
"""

akm = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AKM',
                    bullet=deepcopy(bullets.round_76239_123_fmj),
                    magazine=deepcopy(magazines.ak762_30rd),
                    part_dict={
                        "AK Reciever": kalashnikov.reciever_akm,
                        "AK Barrel": kalashnikov.barrel_ak762,
                        "AK Handguard": kalashnikov.handguard_akm,
                        "AK Grip": kalashnikov.grip_akm,
                        "AK Stock": kalashnikov.stock_akm,
                        "Muzzle Device": kalashnikov.muzzle_akm,
                    },
                    ).update_properties()

ak_pistol = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK Pistol',
                          bullet=deepcopy(bullets.round_76239_123_fmj),
                          magazine=deepcopy(magazines.ak762_30rd),
                          part_dict={
                              "AK Reciever": kalashnikov.reciever_akm,
                              "AK Barrel": kalashnikov.barrel_ak762_short,
                              "AK Handguard": kalashnikov.handguard_akm,
                              "AK Grip": kalashnikov.grip_akm,
                          },
                          ).update_properties()

rpk = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='RPK',
                    bullet=deepcopy(bullets.round_76239_123_fmj),
                    magazine=deepcopy(magazines.ak762_40rd),
                    part_dict={
                        "AK Reciever": kalashnikov.reciever_akm,
                        "AK Barrel": kalashnikov.barrel_rpk762,
                        "AK Handguard": kalashnikov.handguard_akm,
                        "AK Grip": kalashnikov.grip_akm,
                        "AK Stock": kalashnikov.stock_rpk,
                        "Muzzle Device": kalashnikov.muzzle_akm,
                    },
                    ).update_properties()

ak_zenitco = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AKM - Zenitco',
                           bullet=deepcopy(bullets.round_76239_123_fmj),
                           magazine=deepcopy(magazines.ak762_30rd),
                           optic_mount=deepcopy(kalashnikov.accessory_dustcoverrail),
                           part_dict={
                               "AK Reciever": kalashnikov.reciever_akm,
                               "AK Barrel": kalashnikov.barrel_ak762,
                               "AK Handguard": kalashnikov.handguard_leader,
                               "AK Grip": kalashnikov.grip_rk3,
                               "AK Stock": kalashnikov.stock_pt1,
                               "AK Optics Mount": kalashnikov.accessory_dustcoverrail,
                               "Muzzle Device": kalashnikov.muzzle_dtk,
                               "Optic": attachments.holosun503
                           },
                           ).update_properties()

ak_marksman = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AKM - Marksman',
                            bullet=deepcopy(bullets.round_76239_123_fmj),
                            magazine=deepcopy(magazines.ak762_30rd),
                            optic_mount=deepcopy(kalashnikov.reciever_akm),
                            part_dict={
                                "AK Reciever": kalashnikov.reciever_akm,
                                "AK Barrel": kalashnikov.barrel_ak762,
                                "AK Handguard": kalashnikov.handguard_akm,
                                "AK Grip": kalashnikov.grip_sniper,
                                "AK Stock": kalashnikov.stock_akm,
                                "Muzzle Device": kalashnikov.muzzle_akm,
                                "Optic": attachments.pso1
                            },
                            ).update_properties()

ak_magpul = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK Magpul MOE',
                          bullet=deepcopy(bullets.round_76239_123_fmj),
                          magazine=deepcopy(magazines.ak762_30rd),
                          part_dict={
                              "AK Reciever": kalashnikov.reciever_akm,
                              "AK Barrel": kalashnikov.barrel_ak762,
                              "AK Handguard": kalashnikov.handguard_magpul,
                              "AK Grip": kalashnikov.grip_moe,
                              "AK Stock": kalashnikov.stock_moe,
                              "Muzzle Device": kalashnikov.muzzle_akm,
                          },
                          ).update_properties()

ak_104 = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK-104',
                       bullet=deepcopy(bullets.round_76239_123_fmj),
                       magazine=deepcopy(magazines.ak762_30rd),
                       optic_mount=deepcopy(kalashnikov.reciever_akm),
                       part_dict={
                           "AK Reciever": kalashnikov.reciever_akm,
                           "AK Barrel": kalashnikov.barrel_ak762_short,
                           "AK Handguard": kalashnikov.handguard_ak74,
                           "AK Grip": kalashnikov.grip_akm,
                           "AK Stock": kalashnikov.stock_ak100,
                           "Muzzle Device": kalashnikov.muzzle_akm,
                           "Optic": attachments.kobra_ekp
                       },
                       ).update_properties()

amd_65 = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AMD 65',
                       bullet=deepcopy(bullets.round_76239_123_fmj),
                       magazine=deepcopy(magazines.ak762_40rd),
                       part_dict={
                           "AK Reciever": kalashnikov.reciever_akm,
                           "AK Barrel": kalashnikov.barrel_rpk762,
                           "AK Handguard": kalashnikov.handguard_amd65,
                           "AK Grip": kalashnikov.grip_akm,
                           "AK Stock": kalashnikov.stock_amd65,
                           "Muzzle Device": kalashnikov.muzzle_amd65,
                       },
                       ).update_properties()

""" 
AK 5.45
"""

ak_74 = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK-74',
                      bullet=deepcopy(bullets.round_545_63_fmj),
                      magazine=deepcopy(magazines.ak545_30rd),
                      part_dict={
                          "AK Reciever": kalashnikov.reciever_ak74,
                          "AK Barrel": kalashnikov.barrel_ak545,
                          "AK Handguard": kalashnikov.handguard_ak74,
                          "AK Grip": kalashnikov.grip_akm,
                          "AK Stock": kalashnikov.stock_ak74,
                          "Muzzle Device": kalashnikov.muzzle_ak74,
                      },
                      ).update_properties()

ak_74_pistol = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK Pistol 5.45x39',
                             bullet=deepcopy(bullets.round_545_63_fmj),
                             magazine=deepcopy(magazines.ak545_30rd),
                             part_dict={
                                 "AK Reciever": kalashnikov.reciever_ak74,
                                 "AK Barrel": kalashnikov.barrel_ak545_short,
                                 "AK Handguard": kalashnikov.handguard_ak74,
                                 "AK Grip": kalashnikov.grip_akm,
                             },
                             ).update_properties()

rpk_74 = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='RPK-74',
                       bullet=deepcopy(bullets.round_545_63_fmj),
                       magazine=deepcopy(magazines.ak545_30rd),
                       part_dict={
                           "AK Reciever": kalashnikov.reciever_ak74,
                           "AK Barrel": kalashnikov.barrel_rpk545,
                           "AK Handguard": kalashnikov.handguard_ak74,
                           "AK Grip": kalashnikov.grip_akm,
                           "AK Stock": kalashnikov.stock_rpk,
                           "Muzzle Device": kalashnikov.muzzle_ak74,
                       },
                       ).update_properties()

ak_74_zenitco = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK-74 - Zenitco',
                              bullet=deepcopy(bullets.round_545_63_fmj),
                              magazine=deepcopy(magazines.ak545_30rd),
                              optic_mount=deepcopy(kalashnikov.accessory_dustcoverrail),
                              part_dict={
                                  "AK Reciever": kalashnikov.reciever_ak74,
                                  "AK Barrel": kalashnikov.barrel_ak545,
                                  "AK Handguard": kalashnikov.handguard_leader,
                                  "AK Grip": kalashnikov.grip_rk3,
                                  "AK Stock": kalashnikov.stock_pt1,
                                  "AK Optics Mount": kalashnikov.accessory_dustcoverrail,
                                  "Muzzle Device": kalashnikov.muzzle_dtk,
                                  "Optic": attachments.holosun503
                              },
                              ).update_properties()

ak_74_marksman = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK-74 - Marksman',
                               bullet=deepcopy(bullets.round_545_63_fmj),
                               magazine=deepcopy(magazines.ak545_30rd),
                               optic_mount=deepcopy(kalashnikov.reciever_ak74),
                               part_dict={
                                   "AK Reciever": kalashnikov.reciever_ak74,
                                   "AK Barrel": kalashnikov.barrel_ak762,
                                   "AK Handguard": kalashnikov.handguard_ak74,
                                   "AK Grip": kalashnikov.grip_sniper,
                                   "AK Stock": kalashnikov.stock_zhukov,
                                   "Muzzle Device": kalashnikov.muzzle_ak74,
                                   "Optic": attachments.pso1
                               },
                               ).update_properties()

ak_74_magpul = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK Magpul MOE',
                             bullet=deepcopy(bullets.round_545_63_fmj),
                             magazine=deepcopy(magazines.ak545_30rd),
                             part_dict={
                                 "AK Reciever": kalashnikov.reciever_ak74,
                                 "AK Barrel": kalashnikov.barrel_ak545,
                                 "AK Handguard": kalashnikov.handguard_magpul,
                                 "AK Grip": kalashnikov.grip_moe,
                                 "AK Stock": kalashnikov.stock_moe,
                                 "Muzzle Device": kalashnikov.muzzle_ak74,
                             },
                             ).update_properties()

ak_105 = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK-105',
                       bullet=deepcopy(bullets.round_545_63_fmj),
                       magazine=deepcopy(magazines.ak545_30rd),
                       optic_mount=deepcopy(kalashnikov.reciever_ak74),
                       part_dict={
                           "AK Reciever": kalashnikov.reciever_ak74,
                           "AK Barrel": kalashnikov.barrel_ak545_short,
                           "AK Handguard": kalashnikov.handguard_ak74,
                           "AK Grip": kalashnikov.grip_akm,
                           "AK Stock": kalashnikov.stock_ak100,
                           "Muzzle Device": kalashnikov.muzzle_akm,
                           "Optic": attachments.okp7,
                       },
                       ).update_properties()

"""
AK 5.56
"""

ak_556 = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK 5.56',
                       bullet=deepcopy(bullets.round_556_60_fmj),
                       magazine=deepcopy(magazines.ak556_30rd),
                       part_dict={
                           "AK Reciever": kalashnikov.reciever_100556,
                           "AK Barrel": kalashnikov.barrel_ak556,
                           "AK Handguard": kalashnikov.handguard_ak74,
                           "AK Grip": kalashnikov.grip_akm,
                           "AK Stock": kalashnikov.stock_ak74,
                           "Muzzle Device": ar15.ar15_muzzle_flashhider,
                       },
                       ).update_properties()

ak_556_pistol = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK Pistol 5.56',
                              bullet=deepcopy(bullets.round_556_60_fmj),
                              magazine=deepcopy(magazines.ak556_30rd),
                              part_dict={
                                  "AK Reciever": kalashnikov.reciever_100556,
                                  "AK Barrel": kalashnikov.barrel_ak556_short,
                                  "AK Handguard": kalashnikov.handguard_ak74,
                                  "AK Grip": kalashnikov.grip_akm,
                                  "Muzzle Device": ar15.ar15_muzzle_flashhider,
                              },
                              ).update_properties()

ak_556_marksman = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK 5.56 - Marksman',
                                bullet=deepcopy(bullets.round_556_60_fmj),
                                magazine=deepcopy(magazines.ak556_30rd),
                                optic_mount=deepcopy(kalashnikov.accessory_railsidemount),
                                part_dict={
                                    "AK Reciever": kalashnikov.reciever_100556,
                                    "AK Barrel": kalashnikov.barrel_ak556_short,
                                    "AK Handguard": kalashnikov.handguard_ak74,
                                    "AK Grip": kalashnikov.grip_sniper,
                                    "AK Stock": kalashnikov.stock_moe,
                                    "AK Optics Mount": kalashnikov.accessory_railsidemount,
                                    "Optic": attachments.acog_ta01,
                                    "Muzzle Device": ar15.ar15_muzzle_flashhider,
                                },
                                ).update_properties()

ak_556_magpul = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK 5.56 Magpul MOE',
                              bullet=deepcopy(bullets.round_556_60_fmj),
                              magazine=deepcopy(magazines.ak556_30rd),
                              part_dict={
                                  "AK Reciever": kalashnikov.reciever_100556,
                                  "AK Barrel": kalashnikov.barrel_ak556,
                                  "AK Handguard": kalashnikov.handguard_magpul,
                                  "AK Grip": kalashnikov.grip_moe,
                                  "AK Stock": kalashnikov.stock_moe,
                                  "Muzzle Device": ar15.ar15_muzzle_flashhider,
                              },
                              ).update_properties()

ak_102 = PremadeWeapon(gun_item=deepcopy(kalashnikov.ak), name='AK-102',
                       bullet=deepcopy(bullets.round_556_60_fmj),
                       magazine=deepcopy(magazines.ak556_30rd),
                       optic_mount=deepcopy(kalashnikov.accessory_railsidemount),
                       part_dict={
                           "AK Reciever": kalashnikov.reciever_100556,
                           "AK Barrel": kalashnikov.barrel_ak556,
                           "AK Handguard": kalashnikov.handguard_ak74,
                           "AK Grip": kalashnikov.grip_akm,
                           "AK Stock": kalashnikov.stock_ak100,
                           "AK Optics Mount": kalashnikov.accessory_railsidemount,
                           "Optic": attachments.eotech_exps3,
                           "Muzzle Device": ar15.ar15_muzzle_flashhider,
                       },
                       ).update_properties()

"""
MAC 10
"""

mac109 = PremadeWeapon(gun_item=deepcopy(mac10.mac10), name='M10/9',
                       bullet=deepcopy(bullets.round_9mm_124_fmj),
                       magazine=deepcopy(magazines.mac10_mag_9),
                       part_dict={
                           "M10 Lower": mac10.mac109_lower,
                           "M10 Upper": mac10.mac109_upper,
                           'M10 Barrel': mac10.mac109_barrel,
                       },
                       ).update_properties()

mac1045 = PremadeWeapon(gun_item=deepcopy(mac10.mac10), name='M10/45',
                        bullet=deepcopy(bullets.round_45_200_fmj),
                        magazine=deepcopy(magazines.mac10_mag_45),
                        part_dict={
                            "M10 Lower": mac10.mac1045_lower,
                            "M10 Upper": mac10.mac1045_upper,
                            'M10 Barrel': mac10.mac1045_barrel,
                        },
                        ).update_properties()

"""
SKS
"""

sks_gun = PremadeWeapon(gun_item=deepcopy(sks.sks), name='SKS',
                        bullet=deepcopy(bullets.round_76239_150_fmj),
                        part_dict={
                            "SKS Barrel": sks.barrel_sks,
                            "SKS Stock": sks.stock_sks,
                        },
                        ).update_properties()

sks_auto = PremadeWeapon(gun_item=deepcopy(sks.sks), name='SKS - Full Auto Conversion',
                         bullet=deepcopy(bullets.round_76239_150_fmj),
                         part_dict={
                             "SKS Barrel": sks.barrel_sks_shortened_auto,
                             "SKS Stock": sks.stock_sks,
                             "SKS Magazine Adapter": sks.sks_ak_mag_adapter,
                         },
                         ).update_properties()

sks_tactical = PremadeWeapon(gun_item=deepcopy(sks.sks), name='SKS - Tactical',
                             bullet=deepcopy(bullets.round_76239_150_fmj),
                             optic_mount=deepcopy(sks.stock_sks_tapco),
                             part_dict={
                                 "SKS Barrel": sks.barrel_sks,
                                 "SKS Stock": sks.stock_sks_tapco,
                                 "Optic": attachments.eotech_exps3
                             },
                             ).update_properties()

"""
Mosin Nagant
"""

mosin_gun = PremadeWeapon(gun_item=deepcopy(mosin.mosin_nagant), name='Mosin-Nagant M91/30',
                          bullet=deepcopy(bullets.round_54r_174_jrn),
                          part_dict={
                              "Mosin-Nagant Stock": mosin.mosin_stock,
                              "Mosin-Nagant Barrel": mosin.mosin_barrel,
                          },
                          ).update_properties()

mosin_obrez = PremadeWeapon(gun_item=deepcopy(mosin.mosin_nagant), name='Mosin-Nagant Obrez',
                            bullet=deepcopy(bullets.round_54r_174_jrn),
                            part_dict={
                                "Mosin-Nagant Stock": mosin.mosin_obrez_stock,
                                "Mosin-Nagant Barrel": mosin.mosin_obrez_barrel,
                            },
                            ).update_properties()

mosin_tactical = PremadeWeapon(gun_item=deepcopy(mosin.mosin_nagant), name='Mosin-Nagant - Archangel',
                               bullet=deepcopy(bullets.round_54r_174_jrn),
                               magazine=deepcopy(magazines.mosin_nagant),
                               optic_mount=deepcopy(mosin.mosin_pic_scope_mount),
                               part_dict={
                                   "Mosin-Nagant Stock": mosin.mosin_archangel_stock,
                                   "Mosin-Nagant Barrel": mosin.mosin_barrel,
                                   "Mosin-Nagant Accessory Mount": mosin.mosin_pic_scope_mount,
                                   "Optic": attachments.pm2scope,
                               },
                               ).update_properties()

guns = (

    # glock 9mm
    glock17_stock, glock17_comp, glock17_auto, glock17_pdw, glock17l, glock17l_comp,

    # AR 5.56
    ar15_m16a4, ar15_lmg, car15, ar15_marksman, ar15_pistol, ar15_m4carbine,

    # .300 Blackout
    ar15_pistol_300, ar15_m4carbine_300,

    # AR-10
    ar10, ar10_lmg, ar10_marksman, ar10_pistol, ar10_m4carbine,

    # AK 7.62
    akm, ak_pistol, rpk, ak_zenitco, ak_marksman, ak_magpul, ak_104, amd_65,

    # AK 5.56
    ak_556, ak_556_pistol, ak_556_marksman, ak_556_magpul, ak_102,

    # AK 5.45
    ak_74, ak_74_pistol, rpk_74, ak_74_zenitco, ak_74_marksman, ak_74_magpul, ak_105,

    # MAC 10
    mac109, mac1045,

    # SKS
    sks_gun, sks_auto, sks_tactical,

    # Mosin-Nagant
    mosin_gun, mosin_obrez, mosin_tactical,
)


def name_of_global_obj(xx):
    return [objname for objname, oid in globals().items()
            if id(oid) == id(xx)][0]


def main() -> None:
    for gun in guns:
        with open(f'components/weapons/premade_weapons/{name_of_global_obj(gun)}.pkl', 'wb') as outp:
            pickle.dump(gun, outp, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
