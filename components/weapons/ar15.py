from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
Lower Recievers
"""

lower_ar15 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Lower Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Reciever',
                                   ),
    description='A standard AR-15 type lower reciever capable of automatic fire'
)

"""
Upper Recievers
"""

upper_ar_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M16A2 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Reciever',
                                   additional_required_parts=['AR Front Sight', ],
                                   ),
    description='A standard AR-15 type upper reciever for 5.56x45 or .300 Blackout rifles with integrated '
                'carrying handle'
)

upper_ar_m16a4 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="M16A4 Upper Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Reciever',
                                   is_attachment_point_types=['Picrail Optics Mount', ],
                                   additional_required_parts=['Optic', ],
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
    bg_colour=None,
    name="AR 5.56x45 Standard Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG 5.56x45',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'AR Handguard': ["AR M16A1 Handguard",
                                                                      "AR M16A2 Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Magpul MOE Pistol Handguard",
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
    bg_colour=None,
    name="AR 5.56x45 Carbine Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG 5.56x45',
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
    bg_colour=None,
    name="AR 5.56x45 Standard Heavy Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG 5.56x45',
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
    bg_colour=None,
    name="AR 5.56x45 Pistol Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type='STANAG 5.56x45',
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

ar_barrel_standard_300 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR .300 Blackout Standard Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR M16A1 Handguard",
                                                                      "AR M16A2 Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Magpul MOE Pistol Handguard",
                                                                      "AR Aero Precision Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "AR Daniel Defense MK18 Handguard",
                                                                      "AR Daniel Defense MK18 Carbine Handguard",
                                                                      ]},
                                   tags=['full length barrel', ],
                                   ),
    description='A 20" standard length AR .300 Blackout barrel'
)

ar_barrel_carbine_300 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR .300 Blackout Carbine Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
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

ar_barrel_standard_300_heavy = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR .300 Blackout Standard Heavy Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
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
    description='A 20" standard length AR .300 Blackout heavy barrel'
)

ar_barrel_pistol_300 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR .300 Blackout Pistol Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
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

"""
Stocks
"""

ar_stock_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR M16A1 Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   base_accuracy=1.24,
                                   recoil=0.84,
                                   close_range_accuracy=0.84,
                                   ),
    description='M16A2 style fixed rifle stock'
)

ar_stock_m4a1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR M4A1 Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=0.87,
                                   base_accuracy=1.19,
                                   recoil=0.9,
                                   close_range_accuracy=0.89,
                                   ),
    description='A light weight, compact M4A1 style collapsing carbine stock'
)

ar_stock_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Magpul MOE Stock",
    weight=1,
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
    bg_colour=None,
    name="AR Magpul UBR Stock",
    weight=1,
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
    bg_colour=None,
    name="AR Daniel Defense Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=0.87,
                                   base_accuracy=1.22,
                                   recoil=0.89,
                                   close_range_accuracy=0.85,
                                   ),
    description='A collapsing stock by Dnaiel Defense, light weight and providing a solid cheek rest'
)

ar_stock_prs = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Magpul PRS Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=1.1,
                                   base_accuracy=1.29,
                                   recoil=0.8,
                                   close_range_accuracy=0.8,
                                   ),
    description='A precision stock for AR rifles featuring an adjustable cheek rest and butstock'
)

ar_stock_maxim_cqb = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Maxim CQB Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=0.6,
                                   base_accuracy=1.16,
                                   recoil=0.93,
                                   close_range_accuracy=0.96,
                                   ),
    description='A compact, PDW-style adjustable stock for AR rifles by Maxim Defense. As the name suggests, ideal for '
                'close quarters gunfighting'
)

ar_stock_mdt_skeleton = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR MDT Skeleton Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   equip_time=1.06,
                                   base_accuracy=1.26,
                                   recoil=0.84,
                                   close_range_accuracy=0.82,
                                   ),
    description='A light weight skeletonised precision stock for AR rifles by MDT, featuring adjustable buttstock and '
                'cheek rest'
)

"""
Handguards
"""

ar_handguard_m16a1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR M16A1 Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   ),
    description='Retro M16A1 style handguard for AR rifles'
)

ar_handguard_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR M16A2 Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   ),
    description='M16A2 style handguard for AR rifles'
)

ar_handguard_m16a2_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR M16A2 Carbine Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   base_accuracy=0.97,
                                   recoil=1.04,
                                   close_range_accuracy=1.05,
                                   ),
    description='Carbine length M16A2 style handguard for AR rifles'
)

ar_handguard_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Magpul MOE Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   base_accuracy=1.03,
                                   recoil=0.97,
                                   close_range_accuracy=0.97,
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   tags=['full length covers barrel', ],
                                   ),
    description='A polymer handguard for AR rifles by Magpul featuring MLOK accessory mounts'
)

ar_handguard_magpul_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Magpul MOE Carbine Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   base_accuracy=0.97,
                                   recoil=1.02,
                                   close_range_accuracy=1.03,
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   tags=['carbine length covers barrel', ],
                                   ),
    description='A carbine length polymer handguard for AR rifles by Magpul featuring MLOK accessory mounts'
)

ar_handguard_magpul_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Magpul MOE Pistol Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   recoil=0.97,
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   ),
    description='A pistol length polymer handguard for AR rifles by Magpul featuring MLOK accessory mounts'
)

ar_handguard_aero = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Aero Precision Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   equip_time=0.95,
                                   base_accuracy=1.04,
                                   recoil=1.03,
                                   close_range_accuracy=1.03,
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   tags=['full length covers barrel', ],
                                   ),
    description='A light weight free floated handguard for AR rifles featuring MLOK accessory mounts'
)

ar_handguard_aero_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Aero Precision Carbine Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   equip_time=0.92,
                                   base_accuracy=1.02,
                                   recoil=1.05,
                                   close_range_accuracy=1.05,
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel',
                                                              'Picrail Top Mount'],
                                   tags=['carbine length covers barrel', ],
                                   ),
    description='A carbine length light weight free floated handguard for AR rifles featuring MLOK accessory mounts'
)

ar_handguard_aero_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Aero Precision Pistol Handguard",
    weight=1,
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
    bg_colour=None,
    name="AR Faxon Streamline Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   equip_time=0.9,
                                   base_accuracy=1.08,
                                   recoil=1.06,
                                   close_range_accuracy=1.05,
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   tags=['full length covers barrel', ],
                                   ),
    description='A super light weight carbon fibre handguard for AR rifles with MLOK accessory mounts'
)

ar_handguard_faxon_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Faxon Streamline Carbine Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   equip_time=0.87,
                                   base_accuracy=1.05,
                                   recoil=1.08,
                                   close_range_accuracy=1.09,
                                   is_attachment_point_types=['MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'],
                                   tags=['carbine length covers barrel', ],
                                   ),
    description='A super light weight carbon fibre carbine length handguard for AR rifles with MLOK accessory mounts'
)

ar_handguard_faxon_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Faxon Streamline Pistol Handguard",
    weight=1,
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
    bg_colour=None,
    name="AR Daniel Defense MK18 Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   equip_time=1.05,
                                   base_accuracy=0.97,
                                   recoil=0.95,
                                   close_range_accuracy=0.97,
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   tags=['full length covers barrel', ],
                                   ),
    description='An M4 style handguard with picatinny rail mounts by Daniel Defense'
)

ar_handguard_mk18_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Daniel Defense MK18 Carbine Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   equip_time=1.03,
                                   recoil=0.97,
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   tags=['carbine length covers barrel', ],
                                   ),
    description='An M4 style carbine length handguard with picatinny rail mounts by Daniel Defense'
)

ar_handguard_mk18_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Daniel Defense MK18 Pistol Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   recoil=0.98,
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   tags=['pistol length covers barrel', ],
                                   ),
    description='An M4 style pistol length handguard with picatinny rail mounts by Daniel Defense'
)

"""
Pistol Grip
"""

ar_grip_trybe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR TRYBE Defense Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   equip_time=0.95,
                                   base_accuracy=0.95,
                                   recoil=1.03,
                                   close_range_accuracy=1.03,
                                   ),
    description='A light weight skeletonised pistol grip for AR rifles'
)

ar_grip_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Magpul MOE Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   base_accuracy=1.02,
                                   ),
    description='A polymer pistol grip for AR rifles by Magpul'
)

ar_grip_ergo = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Ergo Palm Shelf Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   equip_time=1.05,
                                   base_accuracy=1.06,
                                   recoil=0.96,
                                   close_range_accuracy=0.95,
                                   ),
    description='A rubberised grip with a palm shelf for AR rifles'
)

ar_grip_hogue = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Hogue Rubber Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   base_accuracy=1.03,
                                   recoil=0.98,
                                   close_range_accuracy=1.02,
                                   ),
    description='An ergonomic rubberised grip for AR rifles'
)

ar_grip_strikeforce = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR ATI Outdoors Strikeforce Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   base_accuracy=1.04,
                                   recoil=0.97,
                                   ),
    description='An ergonomic rubberised grip by ATI outdoors for AR rifles'
)

ar_grip_a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR A2 Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   ),
    description='An A2 style polymer pistol grip for AR rifles '
)

ar_grip_hera = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Hera Arms HG-15 Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   base_accuracy=1.02,
                                   close_range_accuracy=1.02,
                                   ),
    description='A polymer pistol grip for AR rifles by Hera Arms'
)


ar_grip_stark = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Stark Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   equip_time=1.02,
                                   base_accuracy=1.05,
                                   recoil=0.97,
                                   close_range_accuracy=0.97,
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
    bg_colour=None,
    name="AR Clamp On A2 Front Sight",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Front Sight',
                                   incompatibilities=[['full length barrel', 'full length covers barrel'],
                                                      ['carbine length barrel', 'carbine length covers barrel'],
                                                      ['pistol length barrel', 'pistol length covers barrel'],
                                                      ]
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

ar_front_sight_picatinny = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Picatinny Rail Front Sight",
    weight=1,
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
    bg_colour=None,
    name="AR MLOK Front Sight",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Front Sight',
                                   attachment_point_required=('MLOK Top Mount',)
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)


ar_carry_handle = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Carry Handle Sight",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Optics',
                                   tags=['Carry Handle Attachment',]
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

carry_handle_optic_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AR Carry Handle Optics Mount",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount', ],
                                   additional_required_parts=['Optic', ],
                                   incompatibilities=[['Carry Handle Attachment',]]
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel'
)

ar15 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
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
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.8,
        range_accuracy_dropoff=1.0,
        parts=Parts(),
        enemy_attack_range=15,
        possible_parts={},
        sound_radius=1.0,
        recoil=1.2,
        close_range_accuracy=1.2,
    )
)