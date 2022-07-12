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
    usable_properties=GunComponent(part_type='M10/45 Lower',
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
    usable_properties=GunComponent(part_type='M10/9 Lower',
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
    usable_properties=GunComponent(part_type='M10/45 Upper',
                                   compatible_parts={'M10/45 Barrel': ['M10/45 Barrel',
                                                                       'M10/45 Extended Barrel w/ Shroud']},
                                   ),
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
    usable_properties=GunComponent(part_type='M10/45 Upper',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   compatible_parts={'M10/45 Barrel': ['M10/45 Barrel',
                                                                       'M10/45 Extended Barrel w/ Shroud']},
                                   additional_required_parts=['Optic', ]
                                   ),
    description='M10/45 side cocking upper reciever featuring a picatinny rail for optics mounting.'
)

mac1045_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MAX-10/45 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Upper',
                                   fire_modes={'automatic': 750},
                                   base_accuracy=1.1,
                                   is_attachment_point_types=['Picrail Optics Mount', 'Picrail Side Mount',
                                                              'Picrail Underbarrel'],
                                   compatible_parts={'M10/45 Barrel': ['MAX-10/45 Barrel',]},
                                   additional_required_parts=['Optic', ]
                                   ),
    description='MAX-10 side charging extended upper reciever for the M10/45 by Lage Manufacturing. '
                'Decreases rate of fire and sports picatinny rail attachment points.'
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
    usable_properties=GunComponent(part_type='M10/9 Upper',
                                   compatible_parts={'M10/9 Barrel': ['M10/9 Barrel',
                                                                      'M10/9 Extended Barrel w/ Shroud']},
                                   ),
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
    usable_properties=GunComponent(part_type='M10/9 Upper',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   compatible_parts={'M10/9 Barrel': ['M10/9 Barrel',
                                                                      'M10/9 Extended Barrel w/ Shroud']},
                                   additional_required_parts=['Optic', ]
                                   ),
    description='M10/9 side cocking upper reciever featuring a picatinny rail for optics mounting.'
)

mac109_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MAX-10/9 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Upper',
                                   fire_modes={'automatic': 750},
                                   base_accuracy=1.1,
                                   is_attachment_point_types=['Picrail Optics Mount', 'Picrail Side Mount',
                                                              'Picrail Underbarrel'],
                                   compatible_parts={'M10/9 Barrel': ['MAX-10/9 Barrel', ]},
                                   additional_required_parts=['Optic', ]
                                   ),
    description='MAX-10 side charging extended upper reciever for the M10/9 by Lage Manufacturing. '
                'Decreases rate of fire and sports picatinny rail attachment points.'
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
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread 7/8x9', 'M10 Barrel'],
                                   ),
    description='A standard length M10/45 barrel'
)

mac1045_max_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MAX-10/45 Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28',],
                                   base_meat_damage=1.07,
                                   base_armour_damage=1.07,
                                   base_accuracy=1.2,
                                   recoil=0.8,
                                   close_range_accuracy=0.9,
                                   range_accuracy_dropoff=1.07,
                                   ),
    description='9 inch barrel for the M10/45 intended for use with the MAX-10 upper'
)

mac1045_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Extended Barrel w/ Shroud",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28', 'M10 Barrel'],
                                   base_meat_damage=1.04,
                                   base_armour_damage=1.04,
                                   base_accuracy=1.12,
                                   recoil=0.94,
                                   close_range_accuracy=0.95,
                                   range_accuracy_dropoff=1.04,
                                   ),
    description='7 inch extended barrel with barrel shroad for the M10/9'
)

mac1045_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Carbine Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28',],
                                   base_meat_damage=1.1,
                                   base_armour_damage=1.1,
                                   base_accuracy=1.3,
                                   recoil=0.75,
                                   close_range_accuracy=0.8,
                                   range_accuracy_dropoff=1.1,
                                   ),
    description='A 16" carbine barrel for the M10/45 with an AR-15 style handguard'
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
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 3/4x10', 'M10 Barrel'],
                                   ),
    description='A standard length M10/9 barrel'
)

mac109_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Extended Barrel w/ Shroud",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', 'M10 Barrel'],
                                   base_meat_damage=1.04,
                                   base_armour_damage=1.04,
                                   base_accuracy=1.12,
                                   recoil=0.94,
                                   close_range_accuracy=0.95,
                                   range_accuracy_dropoff=1.04,
                                   ),
    description='7 inch extended barrel with barrel shroad for the M10/9'
)

mac109_max_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MAX-10/9 Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28',],
                                   base_meat_damage=1.06,
                                   base_armour_damage=1.06,
                                   base_accuracy=1.2,
                                   recoil=0.8,
                                   close_range_accuracy=0.9,
                                   range_accuracy_dropoff=1.06,
                                   ),
    description='9 inch barrel for the M10/9 intended for use with the MAX-10 upper'
)

mac109_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9 Carbine Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28',],
                                   base_meat_damage=1.1,
                                   base_armour_damage=1.1,
                                   base_accuracy=1.3,
                                   recoil=0.75,
                                   close_range_accuracy=0.8,
                                   range_accuracy_dropoff=1.1,
                                   ),
    description='A 16" carbine barrel for the M10/9 with an AR-15 style handguard'
)

"""
Stocks
"""

mac10_full_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10 Full Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Stock',
                                   base_accuracy=1.08,
                                   recoil=0.88,
                                   close_range_accuracy=0.90,
                                   ),
    description='A sturdy rifle stock for the M10/45 and M10/9'
)

mac10_folding_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10 Folding Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Stock',
                                   base_accuracy=1.05,
                                   recoil=0.93,
                                   close_range_accuracy=0.95,
                                   ),
    description='A folding buttstock for the M10/45 and M10/9'
)

"""
Other
"""

mac10_vertical_grip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10 Vertical Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required='M10 Barrel',
                                   recoil=0.94,
                                   close_range_accuracy=1.03,
                                   ),
    description='A vertical grip that clamps onto the barrel of M10 pattern guns'
)

mac1045_sionics_suppressor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45 Sionics Suppressor",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   recoil=0.80,
                                   close_range_accuracy=0.85,
                                   sound_radius=0.60,
                                   is_suppressor=True,
                                   attachment_point_required='Barrel Thread 7/8x9'
                                   ),
    description='A large suppressor for the M10/45 that significantly reduces the sound of firing'
)

"""
Guns
"""

mac1045 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/45",
    weight=1,
    stacking=None,
    description='An American blowback operated machine pistol, commonly known as the MAC-10. '
                'It is known for its blistering rate of fire.',
    usable_properties=GunMagFed(
        compatible_magazine_type='M10/45',
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'rapid fire (semi-auto)': 3, 'automatic': 1100},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.8,
        range_accuracy_dropoff=1.0,
        parts=Parts(),
        enemy_attack_range=8,
        possible_parts={},
        sound_radius=1.0,
        recoil=1.0,
        close_range_accuracy=0.9,
    )
)

mac109 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M10/9",
    weight=1,
    stacking=None,
    description='An American blowback operated machine pistol, commonly known as the MAC-10. '
                'It is known for its blistering rate of fire.',
    usable_properties=GunMagFed(
        compatible_magazine_type='M10/9',
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'rapid fire (semi-auto)': 3, 'automatic': 1200},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.8,
        range_accuracy_dropoff=24,
        parts=Parts(),
        enemy_attack_range=8,
        possible_parts={},
        sound_radius=1.0,
        recoil=1.1,
        close_range_accuracy=0.9,
    )
)

mac10dict = {
    "guns": {
        "submachineguns": {
            "MAC10/45": {
                "required parts": {
                    "M10/45 Lower": 1,
                    "M10/45 Upper": 1,
                    "M10/45 Barrel": 1,
                },
                "compatible parts": {
                    "M10 Stock": 1,
                    "M10 Foregrip": 1,
                    "Muzzle Device": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1
                },
                "item": mac1045
            },
            "MAC10/9": {
                "required parts": {
                    "M10/9 Lower": 1,
                    "M10/9 Upper": 1,
                    "M10/9 Barrel": 1,
                },
                "compatible parts": {
                    "M10 Stock": 1,
                    "M10 Foregrip": 1,
                    "Muzzle Device": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1
                },
                "item": mac109
            },
        }
    },
}