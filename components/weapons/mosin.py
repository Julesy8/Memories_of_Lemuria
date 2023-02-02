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
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel", ]},
                                   felt_recoil=0.42,
                                   ap_distance_cost_modifier=0.7,
                                   spread_modifier=0.9,
                                   target_acquisition_ap=0.91,
                                   equip_time=1.4,
                                   grip_properties={
                                       'felt_recoil': 0.88,
                                       'ap_distance_cost_modifier': 0.91,
                                       'spread_modifier': 0.93,
                                       'target_acquisition_ap': 0.82}),
    description='Standard M91/30 stock'
)

mosin_stock_montecarlo = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant ATI Monte Carlo Stock",
    weight=2.27,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Stock',
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel", ]},
                                   felt_recoil=0.47,
                                   ap_distance_cost_modifier=0.66,
                                   spread_modifier=0.86,
                                   target_acquisition_ap=0.78,
                                   equip_time=1.2,
                                   grip_properties={
                                       'felt_recoil': 0.82,
                                       'ap_distance_cost_modifier': 0.89,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.83}),
    description='A modern polymer monte-carlo style stock for the Mosin-Nagant M91/30'
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
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant M91/30 Barrel", ]},
                                   compatible_magazine_type='Mosin-Nagant',
                                   felt_recoil=0.51,
                                   ap_distance_cost_modifier=0.62,
                                   spread_modifier=0.89,
                                   target_acquisition_ap=0.75,
                                   equip_time=1.3,
                                   grip_properties={
                                       'felt_recoil': 0.86,
                                       'ap_distance_cost_modifier': 0.93,
                                       'spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.81}),
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
                                                                             "Mosin-Nagant Carbine Barrel", ]},
                                   felt_recoil=0.45,
                                   ap_distance_cost_modifier=0.72,
                                   spread_modifier=0.92,
                                   target_acquisition_ap=0.76,
                                   equip_time=1.2,
                                   grip_properties={
                                       'felt_recoil': 0.89,
                                       'ap_distance_cost_modifier': 0.86,
                                       'spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.79}),
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
                                   compatible_parts={'Mosin-Nagant Barrel': ["Mosin-Nagant Obrez Barrel", ]},
                                   felt_recoil=0.85,
                                   ap_distance_cost_modifier=0.93,
                                   spread_modifier=0.9,
                                   target_acquisition_ap=71,
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.93,
                                       'spread_modifier': 0.95,
                                       'target_acquisition_ap': 0.74}),
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
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier=1.14,
                                   is_attachment_point_types=['Mosin-Nagant Barrel', ],
                                   optic_properties={'target_acquisition_ap': 1.15,
                                                     'ap_distance_cost_modifier': 0.9,
                                                     'spread_modifier': 0.92, },
                                   is_optic=True,
                                   sound_radius=0.8,
                                   barrel_length=2.42,
                                   target_acquisition_ap=1.3,
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
                                   incompatibilities=(("Iron Sight",),),
                                   suffix="Carbine",
                                   velocity_modifier=1.05,
                                   is_attachment_point_types=['Mosin-Nagant Barrel', ],
                                   optic_properties={'target_acquisition_ap': 1.11,
                                                     'ap_distance_cost_modifier': 0.93,
                                                     'spread_modifier': 0.93, },
                                   is_optic=True,
                                   sound_radius=0.9,
                                   barrel_length=1.68,
                                   target_acquisition_ap=1.15,
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
                                   incompatibilities=(("Iron Sight",),),
                                   suffix="Obrez",
                                   velocity_modifier=0.79,
                                   is_attachment_point_types=['Mosin-Nagant Barrel', ],
                                   optic_properties={'target_acquisition_ap': 0.95,
                                                     'ap_distance_cost_modifier': 1.1,
                                                     'spread_modifier': 1.05, },
                                   is_optic=True,
                                   sound_radius=1.3,
                                   barrel_length=0.5,
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
    weight=0.26,
    stacking=None,
    usable_properties=GunComponent(part_type='Mosin-Nagant Accessory Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Short'],
                                   additional_required_parts=['Optic', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.56}, ),
    description='A three sided picatinny rail for mounting optics and other accessories to Mosin-Nagant rifles'
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
                                   muzzle_break_efficiency=0.43,
                                   sound_radius=0.54,
                                   fire_rate_modifier=1.1,
                                   target_acquisition_ap=1.13,
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
                                   muzzle_break_efficiency=0.71,
                                   target_acquisition_ap=1.04,
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
        ap_to_equip=75,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type='7.62x54R',
        mag_capacity=5,
        velocity_modifier=1.0,
        felt_recoil=1.0,
        target_acquisition_ap=50,
        firing_ap_cost=25,
        ap_distance_cost_modifier=1.0,
        sound_modifier=1.0,
        barrel_length=1.36,
        zero_range=100,
        receiver_height_above_bore=0.71,
        sight_height_above_bore=0.5,
        spread_modifier=0.05
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
                    "Muzzle Device": 1,
                    "Optic": 1,
                    "Side Mounted Accessory": 1,
                },
                "item": mosin_nagant
            },
        }
    },
}
