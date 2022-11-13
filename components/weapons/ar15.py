from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
Lower Recievers
"""

lower_ar15 = Item(
    x=0, y=0,
    char=ord("!"),
    fg_colour=colour.LIGHT_GRAY,
    name="AR Lower Reciever",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Reciever',
                                   compatible_parts={'AR Upper Reciever': ['M16A2 Upper Reciever',
                                                                           'M16A4 Upper Reciever']},
                                   ),
    description='A standard AR-15 type lower reciever capable of automatic fire'
)

lower_ar10 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 Lower Reciever",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Reciever',
                                   compatible_parts={'AR Upper Reciever': ['AR10 Upper Reciever',]},
                                   ),
    description='AR-10 reciever designed for rifle calibre AR rifles'
)

"""
Upper Recievers
"""

upper_ar_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M16A2 Upper Reciever",
    weight=0.42,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Reciever',
                                   additional_required_parts=('AR Front Sight', ),
                                   ),
    description='A standard AR-15 type upper reciever for 5.56x45 or .300 Blackout rifles with integrated '
                'carrying handle'
)

upper_ar_m16a4 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M16A4 Upper Reciever",
    weight=0.27,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Reciever',
                                   is_attachment_point_types=['Picrail Optics Mount', ],
                                   additional_required_parts=('Optic', ),
                                   compatible_parts={'AR Optics Mount': []},
                                   ),
    description='A standard AR-15 type upper reciever for 5.56x45 or .300 Blackout rifles with a picatinny '
                'rail optics mount'
)

upper_ar10 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR10 Upper Reciever",
    weight=0.65,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Reciever',
                                   is_attachment_point_types=['Picrail Optics Mount', ],
                                   additional_required_parts=('Optic', ),
                                   compatible_parts={'AR Optics Mount': []},
                                   ),
    description='A standard AR-15 type upper reciever for 5.56x45 or .300 Blackout rifles with a picatinny '
                'rail optics mount'
)

"""
Barrels
"""

"""5.56x39"""

ar_barrel_standard_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR 5.56x45 Standard Barrel",
    weight=0.99,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG',
                                   compatible_bullet_type='5.56x45',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'AR Handguard': ["AR M16A1 Handguard",
                                                                      "AR M16A2 Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "AR Daniel Defense MK18 Handguard",
                                                                      "AR Daniel Defense MK18 Carbine Handguard",
                                                                      ]},
                                   tags=['full length barrel',],
                                   ),
    description='A 20" standard length AR 5.56x45 barrel'
)

ar_barrel_carbine_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR 5.56x45 Carbine Barrel",
    weight=0.79,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG',
                                   compatible_bullet_type='5.56x45',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'AR Handguard': ["AR M16A1 Handguard",  # TODO: remove depricated parts from list
                                                                      "AR M16A2 Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "AR Daniel Defense MK18 Handguard",
                                                                      "AR Daniel Defense MK18 Carbine Handguard",
                                                                      "AR Magpul MOE Pistol Handguard",
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR Daniel Defense MK18 Pistol Handguard",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   equip_time=0.8,
                                   base_meat_damage=0.96,
                                   base_armour_damage=0.96,
                                   base_accuracy=0.95,
                                   range_accuracy_dropoff=0.95,
                                   enemy_attack_range=0.9,
                                   sound_radius=1.1,
                                   recoil=1.06,
                                   close_range_accuracy=1.08,
                                   ),
    description='A 16" carbine length AR 5.56x45 barrel'
)

ar_barrel_standard_556_heavy = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR 5.56x45 HBAR Barrel",
    weight=1.29,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG',
                                   compatible_bullet_type='5.56x45',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'AR Handguard': ["AR M16A1 Handguard",
                                                                      "AR M16A2 Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "AR Daniel Defense MK18 Carbine Handguard",
                                                                      ]},
                                   tags=['full length barrel', ],
                                   base_accuracy=1.05,
                                   sound_radius=1.1,
                                   recoil=0.96,
                                   close_range_accuracy=0.95,
                                   ),
    description='A 20" standard length AR 5.56x45 heavy barrel'
)

ar_barrel_pistol_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR 5.56x45 Pistol Barrel",
    weight=0.54,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG',
                                   compatible_bullet_type='5.56x45',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'AR Handguard': ["AR Magpul MOE Pistol Handguard",
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR Daniel Defense MK18 Pistol Handguard",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   equip_time=0.6,
                                   base_meat_damage=0.8,
                                   base_armour_damage=0.8,
                                   base_accuracy=0.85,
                                   range_accuracy_dropoff=0.8,
                                   enemy_attack_range=0.7,
                                   sound_radius=1.4,
                                   recoil=1.16,
                                   close_range_accuracy=1.2,
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

""".300 Blackout"""

ar_barrel_carbine_300 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR .300 Blackout Carbine Barrel",
    weight=0.82,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_magazine_type='STANAG',
                                   compatible_bullet_type='.300 Blackout',
                                   compatible_parts={'AR Handguard': ["AR M16A1 Handguard",
                                                                      "AR M16A2 Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "AR Daniel Defense MK18 Handguard",
                                                                      "AR Daniel Defense MK18 Carbine Handguard",
                                                                      "AR Magpul MOE Pistol Handguard",
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR Daniel Defense MK18 Pistol Handguard",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   equip_time=0.8,
                                   base_meat_damage=0.96,
                                   base_armour_damage=0.96,
                                   base_accuracy=0.95,
                                   range_accuracy_dropoff=0.95,
                                   enemy_attack_range=13,
                                   sound_radius=1.1,
                                   recoil=1.06,
                                   close_range_accuracy=1.08,
                                   ),
    description='A 16" carbine length AR .300 Blackout barrel'
)

ar_barrel_pistol_300 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR .300 Blackout Pistol Barrel",
    weight=0.59,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_magazine_type='STANAG',
                                   compatible_bullet_type='.300 Blackout',
                                   compatible_parts={'AR Handguard': ["AR Magpul MOE Pistol Handguard",
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR Daniel Defense MK18 Pistol Handguard",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   equip_time=0.6,
                                   base_meat_damage=0.87,
                                   base_armour_damage=0.87,
                                   base_accuracy=0.9,
                                   range_accuracy_dropoff=0.9,
                                   enemy_attack_range=0.9,
                                   sound_radius=1.4,
                                   recoil=1.1,
                                   close_range_accuracy=1.17,
                                   ),
    description='A 10" pistol length AR .300 Blackout barrel'
)

""".308"""

ar_barrel_standard_308 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR 7.62x51 Standard Barrel",
    weight=1.58,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='AR10 7.62x51',
                                   compatible_bullet_type='7.62x51',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 A2 Handguard",
                                                                      "AR-10 A2 Carbine Handguard",
                                                                      "AR-10 Wilson Combat Handguard"
                                                                      "AR-10 Wilson Combat Carbine Handguard",
                                                                      "AR-10 V Seven Ultra-Light Handguard",
                                                                      "AR-10 V Seven Ultra-Light Carbine Handguard",
                                                                      "AR-10 HERA Arms Handguard",
                                                                      "AR-10 HERA Arms Carbine Handguard",
                                                                      "AR-10 Brigand Arms Atlas Carbine Handguard",
                                                                      ]},
                                   tags=['full length barrel',],
                                   equip_time=1.1,
                                   base_meat_damage=0.94,
                                   base_armour_damage=0.94,
                                   base_accuracy=0.92,
                                   sound_radius=1.15,
                                   recoil=1.1,
                                   close_range_accuracy=0.95,
                                   ),
    description='A 20" standard length AR 5.56x45 barrel'
)

ar_barrel_carbine_308 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR 7.62x51 Carbine Barrel",
    weight=0.87,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='AR10 7.62x51',
                                   compatible_bullet_type='7.62x51',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 A2 Carbine Handguard",
                                                                      "AR-10 Wilson Combat Carbine Handguard",
                                                                      "AR-10 V Seven Ultra-Light Carbine Handguard",
                                                                      "AR-10 HERA Arms Carbine Handguard",
                                                                      "AR-10 Brigand Arms Atlas Carbine Handguard",
                                                                      "AR-10 Brigand Arms Atlas Pistol Handguard",
                                                                      "AR-10 HERA Arms Pistol Handguard",
                                                                      "AR-10 V Seven Ultra-Light Pistol Handguard",
                                                                      "AR-10 Wilson Combat Pistol Handguard",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   base_meat_damage=0.90,
                                   base_armour_damage=0.90,
                                   base_accuracy=0.87,
                                   sound_radius=1.2,
                                   recoil=1.14,
                                   close_range_accuracy=1.02,
                                   ),
    description='A 16" carbine length AR 5.56x45 barrel'
)

ar_barrel_pistol_308 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR 7.62x51 Pistol Barrel",
    weight=0.85,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='AR10 7.62x51',
                                   compatible_bullet_type='7.62x51',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 Brigand Arms Atlas Pistol Handguard",
                                                                      "AR-10 HERA Arms Pistol Handguard",
                                                                      "AR-10 V Seven Ultra-Light Pistol Handguard",
                                                                      "AR-10 Wilson Combat Pistol Handguard",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   equip_time=0.8,
                                   base_meat_damage=0.76,
                                   base_armour_damage=0.76,
                                   base_accuracy=0.7,
                                   range_accuracy_dropoff=0.8,
                                   enemy_attack_range=0.7,
                                   sound_radius=1.4,
                                   recoil=1.25,
                                   close_range_accuracy=1.14,
                                   ),
    description='A 10" pistol length AR 7.62x51 barrel'
)

"""
Stocks
"""

ar_stock_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR M16A1 Stock",
    weight=0.71,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   base_accuracy=1.24,
                                   recoil=0.84,
                                   close_range_accuracy=0.84,
                                   ),
    description='M16A2 style fixed rifle stock'
)

ar_stock_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Magpul MOE Stock",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=0.89,
                                   base_accuracy=1.21,
                                   recoil=0.87,
                                   close_range_accuracy=0.88,
                                   ),
    description='A light weight collapsing stock carbine by Magpul'
)

ar_stock_ubr = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Magpul UBR Stock",
    weight=0.6,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=0.9,
                                   base_accuracy=1.22,
                                   recoil=0.86,
                                   close_range_accuracy=0.87,
                                   ),
    description='A sturdy adjustable stock designed to provide similar support to a fixed stock'
)

ar_stock_danieldefense = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Daniel Defense Stock",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=0.87,
                                   felt_recoil=0.89,
                                   ),
    description='A collapsing stock by Dnaiel Defense, light weight and providing a solid cheek rest'
)

ar_stock_prs = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Magpul PRS Stock",
    weight=0.9,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=1.1,
                                   felt_recoil=0.8,
                                   ),
    description='A precision stock for AR rifles featuring an adjustable cheek rest and butstock'
)

ar_stock_maxim_cqb = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Maxim CQB Stock",
    weight=0.64,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=0.6,
                                   felt_recoil=0.93,
                                   ),
    description='A compact, PDW-style adjustable stock for AR rifles by Maxim Defense. As the name suggests, ideal for '
                'close quarters gunfighting'
)

"""
Handguards
"""

ar_handguard_m16a1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR M16A1 Handguard",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   ),
    description='Retro M16A1 style handguard for AR rifles'
)

ar_handguard_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR M16A2 Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   ),
    description='M16A2 style handguard for AR rifles'
)

ar_handguard_m16a2_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR M16A2 Carbine Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   ),
    description='Carbine length M16A2 style handguard for AR rifles'
)

ar_handguard_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Magpul MOE Handguard",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   ),
    description='A polymer handguard for AR rifles by Magpul featuring MLOK accessory mounts'
)

ar_handguard_magpul_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Magpul MOE Carbine Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   ),
    description='A carbine length polymer handguard for AR rifles by Magpul featuring MLOK accessory mounts'
)

ar_handguard_aero = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Aero Precision Handguard",
    weight=0.31,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A light weight free floated handguard for AR rifles featuring MLOK accessory mounts'
)

ar_handguard_aero_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Aero Precision Carbine Handguard",
    weight=0.27,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A carbine length light weight free floated handguard for AR rifles featuring MLOK accessory mounts'
)

ar_handguard_aero_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Aero Precision Pistol Handguard",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   tags=['pistol length covers barrel', ],
                                   ),
    description='A pistol length light weight free floated handguard for AR rifles featuring MLOK accessory mounts'
)

ar_handguard_faxon = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Faxon Streamline Handguard",
    weight=0.22,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   ),
    description='A super light weight carbon fibre handguard for AR rifles with MLOK accessory mounts'
)

ar_handguard_faxon_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Faxon Streamline Carbine Handguard",
    weight=0.21,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   tags=['carbine length covers barrel', ],
                                   ),
    description='A super light weight carbon fibre carbine length handguard for AR rifles with MLOK accessory mounts'
)

ar_handguard_faxon_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Faxon Streamline Pistol Handguard",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   tags=['pistol length covers barrel', ],
                                   ),
    description='A super light weight carbon fibre pistol length handguard for AR rifles with MLOK accessory mounts'
)

ar_handguard_mk18 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Daniel Defense MK18 Handguard",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A free floated M4 style handguard with picatinny rail mounts by Daniel Defense'
)

ar10_handguard_a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 A2 Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   ),
    description='A2 style handguard for AR-10 rifles'
)

ar10_handguard_a2_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 M16A2 Carbine Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   ),
    description='Carbine length A2 style handguard for AR-10 rifles'
)

ar10_handguard_wilson = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 Wilson Combat Handguard",
    weight=0.41,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A light weight aluminium free floated handguard for AR-10 rifles featuring MLOK accessory mounts'
)

ar_handguard_wilson_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 Wilson Combat Carbine Handguard",
    weight=0.32,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A carbine length light weight aluminium free floated handguard for AR-10 rifles featuring MLOK '
                'accessory mounts'
)

ar10_handguard_vseven = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 V Seven Hyper-Light Handguard",
    weight=0.21,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A super light weight lithium-aluminium alloy AR-10 handguard with M-LOK attachment points'
)

ar_handguard_vseven_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 V Seven Hyper-Light Carbine Handguard",
    weight=0.18,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A super light weight carbine length lithium-aluminium alloy AR-10 '
                'handguard with M-LOK attachment points'
)

ar_handguard_vseven_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 V Seven Hyper-Light Pistol Handguard",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   tags=['pistol length covers barrel', ],
                                   ),
    description='A super light weight pistol length lithium-aluminium alloy AR-10 handguard with M-LOK '
                'attachment points'
)

ar_handguard_hera_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 HERA Arms IRS Handguard",
    weight=0.65,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A carbine length light weight aluminium free floated handguard for AR-10 rifles '
                'featuring picatinny rail accessory mounts'
)

ar_handguard_atlas_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 Brigand Arms Atlas Carbine Handguard",
    weight=0.22,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A carbon-fibre and aluminium carbine AR10 handguard with a wire frame appearance featuring picatinny '
                'rail attachment points'
)

ar_handguard_atlas_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 Brigand Arms Atlas Pistol Handguard",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   ),
    description='A carbon-fibre and aluminium pistol AR10 handguard with a wire frame appearance featuring picatinny'
                ' rail attachment points'
)

"""
Pistol Grip
"""

ar_grip_trybe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR TRYBE Defense Grip",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='An aluminium skeletonised pistol grip for AR rifles'
)

ar_grip_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Magpul MOE Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='A polymer pistol grip for AR rifles by Magpul'
)


ar_grip_hogue = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Hogue Rubber Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='An ergonomic rubberised grip for AR rifles'
)

ar_grip_strikeforce = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR ATI Outdoors Strikeforce Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='An ergonomic rubberised grip by ATI outdoors for AR rifles'
)

ar_grip_a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR A2 Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='An A2 style polymer pistol grip for AR rifles '
)

ar_grip_hera = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Hera Arms H15G Grip",
    weight=0.07,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='A polymer pistol grip for AR rifles by Hera Arms'
)


ar_grip_stark = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Stark Grip",
    weight=0.09,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='An ergonomic pistol grip for AR rifles by Stark Equipment'
)

"""
Other
"""

ar_front_sight = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Clamp On A2 Front Sight",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Front Sight',
                                   incompatibilities=(('full length barrel', 'full length covers barrel'),
                                                      ('carbine length barrel', 'carbine length covers barrel'),
                                                      ('pistol length barrel', 'pistol length covers barrel'),
                                                      )
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

ar_front_sight_picatinny = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Picatinny Rail Front Sight",
    weight=0.002,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Front Sight',
                                   attachment_point_required=('Picrail Top Mount',)
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

ar_front_sight_mlok = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR MLOK Front Sight",
    weight=0.002,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Front Sight',
                                   attachment_point_required=('MLOK Top Mount',),
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)


ar_carry_handle = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Carry Handle Sight",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='Optics',
                                   tags=['Carry Handle Attachment',],
                                   sight_height_above_bore=1.4
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

carry_handle_optic_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR Carry Handle Optics Mount",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount', ],
                                   additional_required_parts=('Optic', ),
                                   incompatibilities=(('Carry Handle Attachment',),),
                                   sight_height_above_bore=0.2
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

ar15 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="AR15",
    weight=1,
    stacking=None,
    description='The iconic American assault rifle designed by Armalite in the 1950s',
    usable_properties=GunMagFed(
        compatible_magazine_type='STANAG 5.56x45',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=2,
        fire_modes={'single shot': 1, 'rapid fire (semi-auto)': 3, 'automatic': 800},
        current_fire_mode='single shot',
        parts=Parts(),
        enemy_attack_range=15,
        compatible_bullet_type='5.56x45',
        velocity_modifier=1.0,
        felt_recoil=1.0,
        sound_modifier=1.0,
        barrel_length=20,
        zero_range=25,
        sight_height_above_bore=1.2
    )
)

ardict = {
    "guns": {
        "automatic rifles": {
            "AR Rifle": {
                "required parts": {
                    "AR Lower Reciever": 1,
                    "AR Upper Reciever": 1,
                    "AR Barrel": 1,
                    "AR Handguard": 1,
                    "AR Grip": 1,
                },
                "compatible parts": {
                    "AR Stock": 1,
                    "AR Front Sight": 1,
                    "AR Optics Mount": 1,
                    "Underbarrel Accessory": 1,
                    "Side Mounted Accessory": 1,
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": ar15
            },
        }
    },
}