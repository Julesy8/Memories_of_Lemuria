import glock17
import ar15
import attachments

from typing import Optional
import components.weapons.bullets as bullets
import components.weapons.magazines as magazines
from copy import deepcopy

import pickle

from components.consumables import Bullet
from entity import Item


class PremadeWeapon:
    def __init__(self, gun_item: Item, name: str, part_dict: dict, magazine: Optional[Item], bullet: Bullet,
                 optic_mount: Optional[Item] = None, ):

        self.gun_item = gun_item
        self.name = name
        self.part_dict = part_dict
        self.optic_mount = optic_mount
        self.bullet = bullet

        for key, value in self.part_dict.items():
            setattr(self.gun_item.usable_properties.parts, key, deepcopy(value))

        if magazine:
            self.magazine = magazine

        elif hasattr(self.gun_item.usable_properties, 'magazine'):
            self.magazine = self.gun_item.usable_properties.magazine

        for i in range(magazine.usable_properties.mag_capacity):
            self.magazine.usable_properties.magazine.append(bullet)

    def update_properties(self) -> Item:

        self.gun_item.usable_properties.chambered_bullet = self.bullet

        if hasattr(self.gun_item.usable_properties, 'loaded_magazine'):
            self.gun_item.usable_properties.loaded_magazine = self.magazine

        self.gun_item.usable_properties.parts.update_partlist(attachment_dict={})
        if self.optic_mount is not None:
            self.gun_item.usable_properties.parts. \
                set_property(self.optic_mount.usable_properties.optic_mount_properties)
        self.gun_item.name = self.name
        return self.gun_item


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

# ar15 = PremadeWeapon(gun_item=deepcopy(ar15.ar15), name='M16A4',
#                      bullet=deepcopy(bullets.round_556_60_fmj),
#                      magazine=deepcopy(magazines.stanag_30rd),
#                      part_dict={
#                          "AR Lower Receiver": 1,
#                          "AR Upper Receiver": 1,
#                          "AR Buffer": 1,
#                          "AR Barrel": 1,
#                          "AR Handguard": 1,
#                          "AR Grip": 1,
#                          "AR Stock": 1,
#                          "Attachment Adapter": 1,
#                          "Front Sight": 1,
#                          "AR Optics Mount": 1,
#                          "Underbarrel Accessory": 1,
#                          "Side Mounted Accessory": 1,
#                          "Muzzle Device": 1,
#                          "Optic": 1
#                      },
#                      ).update_properties()

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
                               "Front Sight": ar15.ar_front_sight,  # TODO - add muzzle devices
                               # "Muzzle Device": ar15.,
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
                             "Optic": attachments.eotech_exps3
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
                      },
                      ).update_properties()

guns = (glock17_stock, glock17_comp, glock17_auto, glock17_pdw,
        ar15_m16a4, ar15_lmg, car15,

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
