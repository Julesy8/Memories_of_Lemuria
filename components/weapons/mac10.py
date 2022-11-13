from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

mac1045_lower = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Lower Reciever",
    weight=1.02,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Lower',
                                   ),
    description='M10/45 lower reciever'
)

mac109_lower = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Lower Reciever",
    weight=1.02,
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
    name="M10/45 Upper Reciever",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Upper',
                                   compatible_parts={'M10/45 Barrel': ['M10/45 Barrel',
                                                                       'M10/45 Extended Barrel w/ Shroud'],
                                                     'M10 Optics Mount': ['M10 Picatinny Optics Mount',]
                                                     },
                                   ),
    description='M10/45 upper reciever'
)

mac1045_upper_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Tactical Upper Reciever",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Upper',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   compatible_parts={'M10/45 Barrel': ['M10/45 Barrel',
                                                                       'M10/45 Extended Barrel w/ Shroud']},
                                   additional_required_parts=('Optic',)
                                   ),
    description='M10/45 side cocking upper reciever featuring a picatinny rail for optics mounting.'
)

mac1045_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/45 Upper Reciever",
    weight=1.07,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Upper',
                                   fire_modes={'automatic': 750},
                                   is_attachment_point_types=['Picrail Optics Mount', 'Picrail Side Mount',
                                                              'Picrail Underbarrel'],
                                   compatible_parts={'M10/45 Barrel': ['MAX-10/45 Barrel',]},
                                   additional_required_parts=('Optic', ),
                                   accuracy_distribution=0.95,
                                   ),
    description='MAX-10 side charging extended upper reciever for the M10/45 by Lage Manufacturing. '
                'Decreases rate of fire and sports picatinny rail attachment points.'
)

# 9mm

mac109_upper = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Upper Reciever",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Upper',
                                   compatible_parts={'M10/9 Barrel': ['M10/9 Barrel',
                                                                      'M10/9 Extended Barrel w/ Shroud'],
                                                     'M10 Optics Mount': ['M10 Picatinny Optics Mount',]
                                                     },
                                   ),
    description='M10/9 upper reciever'
)

mac109_upper_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Tactical Upper Reciever",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Upper',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   compatible_parts={'M10/9 Barrel': ['M10/9 Barrel',
                                                                      'M10/9 Extended Barrel w/ Shroud']},
                                   additional_required_parts=('Optic',)
                                   ),
    description='M10/9 side cocking upper reciever featuring a picatinny rail for optics mounting.'
)

mac109_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/9 Upper Reciever",
    weight=1.07,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Upper',
                                   fire_modes={'automatic': 750},
                                   is_attachment_point_types=['Picrail Optics Mount', 'Picrail Side Mount',
                                                              'Picrail Underbarrel'],
                                   compatible_parts={'M10/9 Barrel': ['MAX-10/9 Barrel', ]},
                                   additional_required_parts=('Optic', ),
                                   accuracy_distribution=0.95,
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
    name="M10/45 Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread 7/8x9', 'M10 Barrel'],
                                   velocity_modifier=0.94
                                   ),
    description='A standard length M10/45 barrel'
)

mac1045_max_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/45 Barrel",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28',],
                                   velocity_modifier=1.07
                                   ),
    description='9 inch barrel for the M10/45 intended for use with the MAX-10 upper'
)

mac1045_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Extended Barrel w/ Shroud",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28', 'M10 Barrel'],
                                   velocity_modifier=1.02
                                   ),
    description='7 inch extended barrel with barrel shroud for the M10/45'
)

mac1045_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Carbine Barrel",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28',],
                                   velocity_modifier=1.11
                                   ),
    description='A 16" carbine barrel for the M10/45 with an AR-15 style handguard'
)

# 9mm

mac109_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 3/4x10', 'M10 Barrel'],
                                   velocity_modifier=1.066
                                   ),
    description='A standard length M10/9 barrel'
)

mac109_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Extended Barrel w/ Shroud",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', 'M10 Barrel'],
                                   velocity_modifier=1.094
                                   ),
    description='7 inch extended barrel with barrel shroud for the M10/9'
)

mac109_max_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/9 Barrel",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28',],
                                   velocity_modifier=1.14
                                   ),
    description='9 inch barrel for the M10/9 intended for use with the MAX-10 upper'
)

mac109_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Carbine Barrel",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28',],
                                   velocity_modifier=1.17
                                   ),
    description='A 16" carbine barrel for the M10/9 with an AR-15 style handguard'
)

"""
Stocks
"""

mac1045_full_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Full Stock",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Stock',
                                   felt_recoil=0.7,
                                   accuracy_distribution=1.15,
                                   ),
    description='A sturdy rifle stock for the M10'
)

mac1045_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Stock",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Stock',
                                   felt_recoil=0.76,
                                   accuracy_distribution=1.08,
                                   ),
    description='A collapsing wire buttstock for the M10'
)

"""
Other
"""

mac10_vertical_grip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Vertical Grip",
    weight=0.06,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('M10 Barrel',),
                                   accuracy_distribution=1.1,
                                   ),
    description='A vertical grip that clamps onto the barrel of M10 pattern guns'
)

mac10_optics_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Picatinny Optics Mount",
    weight=0.05,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   additional_required_parts=('Optic', )
                                   ),
    description='A picatinny rail optics mount for the M10'
)

mac10_trirail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Tri Rail Mount",
    weight=0.01,
    stacking=None,
    usable_properties=GunComponent(part_type='Accessory Adapter M10',
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel'],
                                   incompatibilities=(("M10 Vertical Grip",),)
                                   ),
    description='A picatinny tri rail side and underbarrel mount for the M10'
)

mac10_ar_stock_adapter = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 AR Buffertube Stock Adapter",
    weight=0.01,
    stacking=None,
    usable_properties=GunComponent(part_type='Stock Adapter M10',
                                   compatible_parts={'M10 Stock': []},
                                   additional_required_parts=('AR Stock',),
                                   ),
    description='A stock adapter for the M10 allowing the use of AR stocks'
)

mac1045_sionics_suppressor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Sionics Suppressor",
    weight=0.54,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   is_suppressor=True,
                                   muzzle_break_efficiency=0.2,
                                   accuracy_distribution=0.8,
                                   velocity_modifier=1.14,
                                   attachment_point_required=('Barrel Thread 7/8x9',),
                                   sound_radius=0.16,
                                   ),
    description='A large suppressor for the M10/45 that significantly reduces the sound of firing'
)

"""
Guns
"""

# TODO: update item descriptions

mac1045 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
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
        parts=Parts(),
        enemy_attack_range=8,
        compatible_bullet_type='.45 ACP',
        velocity_modifier=1.0,
        felt_recoil=1.0,
    )
)

mac109 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
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
        parts=Parts(),
        enemy_attack_range=8,
        compatible_bullet_type='9mm',
        velocity_modifier=1.0,
        felt_recoil=1.0,
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
                    "Stock Adapter M10": 1,
                    "M10 Stock": 1,
                    "M10 Optics Mount": 1,
                    "Muzzle Device": 1,
                    "Accessory Adapter M10": 1,
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
                    "Stock Adapter M10": 1,
                    "M10 Stock": 1,
                    "M10 Optics Mount": 1,
                    "Muzzle Device": 1,
                    "Accessory Adapter M10": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1
                },
                "item": mac109
            },
        }
    },
}