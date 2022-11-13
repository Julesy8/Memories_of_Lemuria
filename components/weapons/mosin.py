from entity import Item
from components.consumables import GunIntegratedMag, GunComponent
from components.gunparts import Parts
import colour

"""
STOCKS
"""

mosin_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant M91/30 Stock",
    weight=2.78,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel",]},
                                   felt_recoil=0.82,
                                   ),
    description='Standard M91/30 stock'
)

mosin_stock_montecarlo = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant ATI Monte Carlo Stock",
    weight=2.78,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel",]},
                                   felt_recoil=0.71,
                                   ),
    description='Standard M91/30 stock'
)

mosin_archangel_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant M91/30 Archangel Stock",
    weight=1.6,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   prefix="Archangel",
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel",]},
                                   compatible_magazine_type='Mosin-Nagant',
                                   felt_recoil=0.64,
                                   ),
    description='Tactical polymer Archangel replacement stock for the M91/30 Mosin-Nagant designed by ProMag'
)

mosin_carbine_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Carbine Stock",
    weight=2.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel",
                                                                             "Mosin-Nagant Carbine Barrel",]},
                                   felt_recoil=0.82,
                                   accuracy_distribution=1.13,
                                   ),
    description='A shortened carbine stock for the Mosin-Nagant'
)

mosin_obrez_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Obrez Stock",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant Obrez Barrel",]}
                                   ),
    description='A stockless pistol length housing for the Mosin-Nagant, perfect for concealment'
)

"""
BARREL
"""

mosin_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant M91/30 Barrel",
    weight=1.22,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Barrel',
                                   velocity_modifier=1.14,
                                   is_attachment_point_types=['Mosin-Nagant Barrel',],
                                   ),
    description='Standard 29 inch M91/30 barrel assembly'
)


mosin_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Carbine Barrel",
    weight=1.14,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Barrel',
                                   suffix="Carbine",
                                   ideal_range=0.78,
                                   velocity_modifier=1.05,
                                   is_attachment_point_types=['Mosin-Nagant Barrel',],
                                   ),
    description='A shortened 20.2 inch carbine length barrel assembly for the Mosin-Nagant'
)

mosin_obrez_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Obrez Barrel",
    weight=0.5,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Barrel',
                                   suffix="Obrez",
                                   ideal_range=0.025,
                                   velocity_modifier=0.79,
                                   accuracy_distribution=0.21,
                                   is_attachment_point_types=['Mosin-Nagant Barrel',],
                                   ),
    description='A pistol length barrel assembly for the Mosin-Nagant'
)

"""
OTHER
"""

mosin_pic_scope_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Triple Picatinny Rail Mount",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Accessory Mount',
                                   is_attachment_point_types=['Picrail Optics Mount', 'Picrail Side Mount'],
                                   additional_required_parts=['Optic',]
                                   ),
    description='A three sided picatinny rail for mounting optics and other accessories to Mosin-Nagant rifles'
)

mosin_magazine_conversion = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Magazine Conversion",
    weight=0.03,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Magazine Conversion',
                                   suffix="Magazine Conversion",
                                   ),
    description='Converts the mosin nagant to take after market magazines'
)

mosin_suppressor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Bramit Suppressor",
    weight=1.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   suffix="Suppressed",
                                   muzzle_break_efficiency=0.5,
                                   sound_radius=0.7,
                                   attachment_point_required=('Mosin-Nagant Barrel',),
                                   is_suppressor=True
                                   ),
    description='Suppressor for 7.62x54R Mosin-Nagant rifles'
)

mosin_muzzlebreak = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Texas Precision Muzzle Break",
    weight=0.099,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   muzzle_break_efficiency=0.3,
                                   attachment_point_required=('Mosin-Nagant Barrel',)
                                   ),
    description='Muzzle break for 7.62x54R Mosin-Nagant rifles by Texas Precision'
)

mosin_nagant = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="Mosin-Nagant",
    weight=0.7,
    stacking=None,
    description='A classic Russian bolt-action rifle invented in 1891 and used in hundreds of conflicts world wide '
                'since. It is renowned as much for its durability and reliability as for its ubiquitousness.',
    usable_properties=GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=True,
        equip_time=2,
        fire_modes={'single shot': 1},
        current_fire_mode='single shot',
        parts=Parts(),
        enemy_attack_range=25,
        compatible_bullet_type='7.62x54R',
        mag_capacity=5,
        velocity_modifier=1.0,
        felt_recoil=1.0,
    )
)

mosindict = {
    "guns": {
        "rifles": {
            "Mosin-Nagant 91/30": {
                "required parts": {
                    "Mosin-Nagant Stock": 1,
                    "Mosin-Nagant Barrel": 1,
                },
                "compatible parts": {
                    "Mosin-Nagant Accessory Mount": 1,
                    "Mosin-Nagant Grip": 1,
                    "Mosin-Nagant Magazine Conversion": 1,
                    "Muzzle Device": 1,
                    "Optic": 1,
                    "Side Mounted Accessory": 1,
                },
                "item": mosin_nagant
            },
        }
    },
}
