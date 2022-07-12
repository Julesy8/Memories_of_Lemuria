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
    bg_colour=None,
    name="Mosin-Nagant M91/30 Stock",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel",]},
                                   ),
    description='Standard M91/30 stock'
)

mosin_archangel_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant M91/30 Archangel Stock",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   prefix="Archangel",
                                   recoil=0.92,
                                   close_range_accuracy=0.94,
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel",]}
                                   ),
    description='Tactical polymer Archangel replacement stock for the M91/30 Mosin-Nagant designed by ProMag'
)

mosin_carbine_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Carbine Stock",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   recoil=1.03,
                                   close_range_accuracy=1.05,
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel",
                                                                             "Mosin-Nagant Carbine Barrel",]}
                                   ),
    description='A shortened carbine stock for the Mosin-Nagant'
)

mosin_obrez_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Obrez Stock",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   recoil=1.1,
                                   close_range_accuracy=1.05,
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
    bg_colour=None,
    name="Mosin-Nagant M91/30 Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Barrel',
                                   is_attachment_point_types=['Mosin-Nagant Barrel',],
                                   ),
    description='Standard length M91/30 barrel assembly'
)


mosin_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Carbine Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Barrel',
                                   suffix="Carbine",
                                   recoil=1.04,
                                   close_range_accuracy=1.08,
                                   base_meat_damage=0.95,
                                   base_armour_damage=0.95,
                                   base_accuracy=0.96,
                                   is_attachment_point_types=['Mosin-Nagant Barrel',],
                                   ),
    description='A shortened carbine length barrel assembly for the Mosin-Nagant'
)

mosin_obrez_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Obrez Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Barrel',
                                   suffix="Obrez",
                                   prerequisite_parts=(mosin_obrez_stock,),
                                   recoil=1.1,
                                   close_range_accuracy=1.14,
                                   base_meat_damage=0.80,
                                   base_armour_damage=0.80,
                                   base_accuracy=0.88,
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
    bg_colour=None,
    name="Mosin-Nagant Triple Picatinny Rail Mount",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Accessory Mount',
                                   is_attachment_point_types=['Picrail Optics Mount', 'Picrail Side Mount'],
                                   additional_required_parts=['Optic',]
                                   ),
    description='A three sided picatinny rail for mounting optics and other accessories to Mosin-Nagant rifles'
)


mosin_pistol_grip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Pistol Grip",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Grip',
                                   prefix="Bubba'd",
                                   base_accuracy=0.96,
                                   close_range_accuracy=1.05,
                                   ),
    description='An AK-style vertical pistol grip retrofitted onto a Mosin-Nagant stock'
)

mosin_magazine_conversion = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Magazine Conversion",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Magazine Conversion',
                                   suffix="Magazine Conversion",
                                   compatible_magazine_type='Mosin-Nagant',
                                   ),
    description='Converts the mosin nagant to take after market magazines'
)

mosin_suppressor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Bramit Suppressor",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   suffix="Suppressed",
                                   recoil=0.95,
                                   close_range_accuracy=0.95,
                                   sound_radius=0.7,
                                   attachment_point_required='Mosin-Nagant Barrel',
                                   is_suppressor=True
                                   ),
    description='Suppressor for 7.62x54R Mosin-Nagant rifles'
)

mosin_muzzlebreak = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mosin-Nagant Texas Precision Muzzle Break",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   recoil=0.92,
                                   attachment_point_required='Mosin-Nagant Barrel'
                                   ),
    description='Muzzle break for 7.62x54R Mosin-Nagant rifles by Texas Precision'
)

mosin_nagant = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    bg_colour=None,
    name="Mosin-Nagant",
    weight=0.7,
    stacking=None,
    description='A classic Russian bolt-action rifle invented in 1891 and used in hundreds of conflicts world wide '
                'since. It is renowned as much for its durability and reliability as for its ubiquitousness.',
    usable_properties=GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=True,
        equip_time=1,
        fire_modes={'single shot': 1},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=1.0,
        range_accuracy_dropoff=30,
        parts=Parts(),
        enemy_attack_range=15,
        possible_parts={},
        sound_radius=1.0,
        recoil=0.95,
        close_range_accuracy=0.8,
        compatible_bullet_type='7.62x54R',
        mag_capacity=5
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
