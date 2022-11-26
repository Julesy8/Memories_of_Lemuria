from entity import Item
from components.consumables import GunIntegratedMag, GunComponent
from components.gunparts import Parts
import colour

"""
stocks
"""

stock_sks = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Stock",
    weight=0.70,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   felt_recoil=0.76,
                                   ),
    description='Wood SKS rifle stock'
)

stock_sks_tapco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS TAPCO Stock",
    weight=1.08,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount'],
                                   additional_required_parts=('AR Stock',),
                                   accuracy_distribution=0.90,
                                   ),
    description='A polymer rifle stock for the SKS by TAPCO, including a AR-15 stock adapter'
)

stock_sks_dragunov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Dragunov Stock",
    weight=1.01,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   accuracy_distribution=0.95,
                                   felt_recoil=0.7,
                                   ),
    description='A polymer Dragunov rifle style stock for the SKS'
)

stock_sks_fab = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS FAB Defense Stock",
    weight=1.36,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount'],
                                   additional_required_parts=('AR Stock',),
                                   accuracy_distribution=0.86,
                                   ),
    description='A light weight tactical polymer stock for the SKS, including a folding AR-15 stock adapter'
)

stock_sks_sabertooth = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Sabertooth Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount',
                                                              'Picrail Side Mount'],
                                   additional_required_parts=('AR Stock', 'AR Grip'),
                                   accuracy_distribution=0.90,
                                   ),
    description='A polymer assualt rifle style stock for the SKS, including a AR-15 stock adapter'
)

stock_sks_bullpup = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS SGWorks Bullpup Stock",
    weight=0.93,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount',
                                                              'Picrail Side Mount'],
                                   additional_required_parts=('AR Stock', 'AR Grip', 'Optic'),
                                   accuracy_distribution=1.12,
                                   ),
    description='A polymer assualt rifle style stock for the SKS, including a AR-15 stock adapter'
)

"""
barrels
"""

barrel_sks = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Reciever & Barrel",
    weight=3.15,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   is_attachment_point_types=['Barrel Thread 14x1', ],
                                   ),
    description="A standard length SKS barrel"
)

barrel_sks_shortened = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Reciever & Barrel - Shortened",
    weight=2.9,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   is_attachment_point_types=['Barrel Thread 14x1', ],
                                   accuracy_distribution=0.87,
                                   ),
    description="A cut down 17.5 inch SKS barrel"
)

"""
other
"""

sks_ak_mag_adapter = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS AK Magazine Adapter",
    weight=0.01,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Magazine Adapter',
                                   compatible_magazine_type='STANAG 5.56x45',
                                   compatible_parts={'AK Reciever': ['AK 100 series 5.56 Reciever', ]},
                                   ),
    description="Magazine adapter SKS rifles providing compatibility with 7.62x39 AK style magazines"
)

sks_full_auto_conversion = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Full Auto Conversion",
    weight=0.001,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Automatic Conversion',
                                   fire_modes={'automatic': 750, },
                                   ),
    description="Converts the SKS select fire, allowing fully automatic fire"
)

sks_optics_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Picatinny Optics Mount",
    weight=0.16,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   additional_required_parts=('Optic',),
                                   ),
    description="Picatinny rail optics mount for the SKS by Matador arms mounting to the reciever"
)

sks = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS",
    weight=1,
    stacking=None,
    description='A soviet gas operated semi-automatic rifle featuring an integrated magazing introduced shortly '
                'after WW2',
    usable_properties=GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=True,
        equip_time=2,
        fire_modes={'single shot': 1, 'rapid fire (semi-auto)': 3},
        current_fire_mode='single shot',
        parts=Parts(),
        enemy_attack_range=25,
        compatible_bullet_type='7.62x39',
        mag_capacity=10,
        velocity_modifier=1.0,
        felt_recoil=1.0,
        target_acquisition_ap=15,
        firing_ap_cost=15,
        ap_distance_cost_modifier=15
    )
)

sksdict = {
    "guns": {
        "automatic rifles": {
            "SKS Rifle": {
                "required parts": {
                    "SKS Reciever": 1,
                    "SKS Barrel": 1,
                    "SKS Stock": 1,
                },
                "compatible parts": {
                    "SKS Magazine Adapter": 1,
                    "SKS Automatic Conversion": 1,
                    "SKS Optics Mount": 1,
                    "Underbarrel Accessory": 1,
                    "Side Mounted Accessory": 1,
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": sks
            },
        }
    },
}