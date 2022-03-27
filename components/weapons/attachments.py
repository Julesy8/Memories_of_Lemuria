from entity import Item
from components.consumables import GunComponent
import colour
from components.commonitems import steel

suppressor_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Suppressor 9mm",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='9mm_suppressor',
                                   material={steel: 1},
                                   sound_radius=0.77,
                                   recoil=0.90,
                                   close_range_accuracy=0.85,
                                   is_suppressor=True,
                                   ),
    description='Traps gasses as they exit the barrel, quietening the sound of shots'
)

reddot_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Pistol Red Dot",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   is_pistol_optic=True
                                   ),
    description='A small, unmagnified red dight sight intended for pistols'
)

laser_sight = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Laser Sight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='gun_accessory',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   ),
    description='A small red laser to assist with target aquisition'
)