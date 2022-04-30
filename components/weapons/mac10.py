from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

mac1045_lower = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Lower Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac1045_lower',
                                   compatible_calibres=('45', )
                                   ),
    description='M10/45 lower reciever'
)

mac109_lower = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Lower Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac109_lower',
                                   compatible_calibres=('9mm', )
                                   ),
    description='M10/9 lower reciever'
)

"""
Uppers 
"""

# 45

mac1045_upper = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac1045_upper'),
    description='M10/45 upper reciever'
)

mac1045_upper_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Tactical Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac1045_upper',
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   ),
    description='M10/45 side cocking upper reciever featuring a picatinny rail for optics mounting.'
)

mac1045_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MAX-10 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac1045_upper',
                                   fire_modes={'single shot': 1, 'automatic': 750},
                                   base_accuracy=1.1,
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   accessory_attachment=True,
                                   ),
    description='MAX-10 extended upper reciever for the M10/45. Decreases rate of fire and sports a picatinny rail.'
)

# 9mm

mac109_upper = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac109_upper'),
    description='M10/9 upper reciever'
)

mac109_upper_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Tactical Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac109_upper',
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   ),
    description='M10/9 side cocking upper reciever featuring a picatinny rail for optics mounting.'
)

mac109_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MAX-10 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac109_upper',
                                   fire_modes={'single shot': 1, 'automatic': 750},
                                   base_accuracy=1.1,
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   accessory_attachment=True,
                                   ),
    description='MAX-10 extended upper reciever for the M10/9. Decreases rate of fire and sports a picatinny rail.'
)

"""
Barrels
"""

# 45

mac1045_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac1045_barrel',
                                   ),
    description='M10/45 barrel'
)

mac1045_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Extended Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac1045_barrel',
                                   base_meat_damage=1.07,
                                   base_armour_damage=1.07,
                                   base_accuracy=1.2,
                                   recoil=0.8,
                                   close_range_accuracy=0.9,
                                   range_accuracy_dropoff=1.07,
                                   ),
    description='Extended barrel for the M10/45'
)

mac1045_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Carbine Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac1045_barrel',
                                   base_meat_damage=1.1,
                                   base_armour_damage=1.1,
                                   base_accuracy=1.3,
                                   recoil=0.75,
                                   close_range_accuracy=0.8,
                                   range_accuracy_dropoff=1.1,
                                   ),
    description='An 16" carbine barrel for the M10/45'
)

# 9mm

mac109_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac109_barrel',
                                   compatible_calibres=('9mm', )
                                   ),
    description='M10/9 barrel'
)

mac109_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Extended Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac109_barrel',
                                   base_meat_damage=1.06,
                                   base_armour_damage=1.06,
                                   base_accuracy=1.2,
                                   recoil=0.8,
                                   close_range_accuracy=0.9,
                                   range_accuracy_dropoff=1.06,
                                   compatible_calibres=('9mm', )
                                   ),
    description='Extended barrel for the M10/9'
)

mac109_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Carbine Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac109_barrel',
                                   base_meat_damage=1.1,
                                   base_armour_damage=1.1,
                                   base_accuracy=1.3,
                                   recoil=0.75,
                                   close_range_accuracy=0.8,
                                   range_accuracy_dropoff=1.1,
                                   compatible_calibres=('9mm', )
                                   ),
    description='An extended carbine barrel for the M10/9'
)

"""
Stocks
"""

mac10_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10 Full Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac10_stock',
                                   base_accuracy=1.08,
                                   recoil=0.8,
                                   close_range_accuracy=0.90,
                                   ),
    description='A sturdy rifle stock for the M10/45 and M10/9'
)

"""
Other
"""

mac10_carbine_foregrip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10 Carbine Foregrip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac10_foregrip',
                                   recoil=0.90,
                                   ),
    description='An extened M16A2 style foregrip for the M10 intended for use with a carbine length barrel'
)

mac10_barrel_shroud = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10 Barrel Shroud",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='mac10_foregrip',
                                   recoil=0.95,
                                   ),
    description='Barrel shroud for the M10 extended for use with an extended barrel'
)

mac1045_parts_dict = {
    "mac10_lower": ([glock17_frame, 1], [glock17_frame, 1]),
    "glock17_slide": ([glock17_slide, 1], [glock17_slide, 1]),
    "glock17_barrel": ([glock17_barrel, 1], [glock17l_barrel, 1]),
    "glock_stock": ([None, 1], [glock_stock, 1]),
}

mac1045 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45",
    weight=1,
    stacking=None,
    description='An iconic 80s machine pistol known for its blistering rate of fire',
    usable_properties=GunMagFed(
        compatible_magazine_type='mac1045',
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'automatic': 1100},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.8,
        range_accuracy_dropoff=1.0,
        parts=Parts(),
        enemy_attack_range=8,
        possible_parts=mac1045_parts_dict,
        sound_radius=1.0,
        recoil=1.0,
        close_range_accuracy=0.9,
    )
)

mac1045_sionics_suppressor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Sionics Suppressor",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='muzzle_device',
                                   recoil=0.80,
                                   close_range_accuracy=0.85,
                                   sound_radius=0.60,
                                   is_suppressor=True,
                                   compatible_items=(mac1045,)
                                   ),
    description='A large suppressor for the M10/45 that significantly reduces the sound of firing'
)

mac109 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9",
    weight=1,
    stacking=None,
    description='An iconic 80s machine pistol known for its blistering rate of fire',
    usable_properties=GunMagFed(
        compatible_magazine_type='mac109',
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'automatic': 1200},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.8,
        range_accuracy_dropoff=24,
        parts=Parts(),
        enemy_attack_range=8,
        possible_parts=mac109_parts_dict,
        sound_radius=1.0,
        recoil=1.0,
        close_range_accuracy=0.9,
    )
)
