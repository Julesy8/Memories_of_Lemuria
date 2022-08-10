from entity import Item
from components.consumables import GunIntegratedMag, GunComponent
from components.gunparts import Parts
import colour

sks_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="SKS Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Reciever',
                                   ),
    description='SKS reciever'
)

"""
stocks
"""

stock_sks = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="SKS Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   close_range_accuracy=0.9,
                                   ),
    description='Wood SKS rifle stock'
)

stock_sks_tapco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="SKS TAPCO Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount'],
                                   additional_required_parts=('AR Stock',),
                                   close_range_accuracy=1.05,
                                   base_accuracy=0.96,
                                   recoil=1.04,
                                   equip_time=0.85,
                                   ),
    description='A polymer rifle stock for the SKS by TAPCO, including a AR-15 stock adapter'
)

stock_sks_dragunov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="SKS Dragunov Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   close_range_accuracy=0.95,
                                   base_accuracy=1.06,
                                   recoil=0.96,
                                   equip_time=1.06,
                                   ),
    description='A polymer Dragunov rifle style stock for the SKS'
)

stock_sks_fab = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="SKS FAB Defense Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount'],
                                   additional_required_parts=('AR Stock',),
                                   close_range_accuracy=1.07,
                                   base_accuracy=0.98,
                                   recoil=1.06,
                                   equip_time=0.94,
                                   ),
    description='A light weight tactical polymer stock for the SKS, including a folding AR-15 stock adapter'
)

stock_sks_sabertooth = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="SKS Sabertooth Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount',
                                                              'Picrail Side Mount'],
                                   additional_required_parts=('AR Stock', 'AR Grip'),
                                   close_range_accuracy=1.05,
                                   base_accuracy=0.95,
                                   recoil=1.03,
                                   equip_time=0.93,
                                   ),
    description='A polymer assualt rifle style stock for the SKS, including a AR-15 stock adapter'
)

stock_sks_bullpup = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="SKS SGWorks Bullpup Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   compatible_magazine_type='AK 7.62x39',
                                   is_attachment_point_types=['Picrail Underbarrel', 'Picrail Optics Mount',
                                                              'Picrail Side Mount'],
                                   additional_required_parts=('AR Stock', 'AR Grip', 'Optic'),
                                   close_range_accuracy=1.15,
                                   base_accuracy=0.88,
                                   equip_time=0.8,
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
    bg_colour=None,
    name="SKS Barrel",
    weight=1,
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
    bg_colour=None,
    name="SKS Barrel - Shortened",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   is_attachment_point_types=['Barrel Thread 14x1', ],
                                   equip_time=0.9,
                                   base_meat_damage=0.98,
                                   base_armour_damage=0.98,
                                   base_accuracy=0.96,
                                   range_accuracy_dropoff=0.98,
                                   sound_radius=1.05,
                                   recoil=1.03,
                                   close_range_accuracy=1.05,
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
    bg_colour=None,
    name="SKS AK Magazine Adapter",
    weight=1,
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
    bg_colour=None,
    name="SKS Full Auto Conversion",
    weight=1,
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
    bg_colour=None,
    name="SKS Picatinny Optics Mount",
    weight=1,
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
    bg_colour=None,
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
        base_meat_damage=0.97,
        base_armour_damage=0.97,
        base_accuracy=1,
        range_accuracy_dropoff=1.0,
        parts=Parts(),
        enemy_attack_range=15,
        possible_parts={},
        sound_radius=1.0,
        recoil=0.98,
        close_range_accuracy=1,
        compatible_bullet_type='7.62x39',
        mag_capacity=10,
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