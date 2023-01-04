import glock17
from typing import Optional
import components.weapons.bullets as bullets
import components.weapons.magazines as magazines
from copy import deepcopy

import pickle

from components.consumables import Bullet
from entity import Item


class PremadeWeapon:
    def __init__(self, gun_item: Item, name: str, part_dict: dict, magazine: Optional[Item], bullet: Bullet,
                 optic_mount: Optional[Item] = None,):

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
            self.gun_item.usable_properties.parts.\
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

guns = (glock17_stock,)


def name_of_global_obj(xx):
    return [objname for objname, oid in globals().items()
            if id(oid) == id(xx)][0]


def main() -> None:

    for gun in guns:
        with open(f'components/weapons/premade_weapons/{name_of_global_obj(gun)}.pkl', 'wb') as outp:
            pickle.dump(gun, outp, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
