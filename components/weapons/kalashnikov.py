from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
Recievers
"""

reciever_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AKM Reciever",
    weight=2.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Reciever',
                                   is_attachment_point_types=['AK Side Mount', ],
                                   compatible_magazine_type='AK 7.62x39',
                                   compatible_bullet_type='7.62x39',
                                   compatible_parts={'AK Barrel': ['AK Barrel - 7.62x39', 'RPK Barrel - 7.62x39',
                                                                   'AK Carbine Barrel - 7.62x39',
                                                                   'AK Pistol Barrel - 7.62x39']},
                                   ),
    description='AKM stamped kalashnikov type reciever'
)

reciever_ak74 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK-74 Reciever",
    weight=2.11,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Reciever',
                                   is_attachment_point_types=['AK Side Mount', ],
                                   compatible_magazine_type='AK 5.45x39',
                                   compatible_bullet_type='5.45x39',
                                   compatible_parts={'AK Barrel': ['AK Barrel - 5.45x39', 'RPK-74 Barrel - 5.45x39',
                                                                   'AK Carbine Barrel - 5.45x39',
                                                                   'AK Pistol Barrel - 5.45x39']},
                                   ),
    description='AK-74 stamped kalashnikov type reciever'
)

reciever_100556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 100 series 5.56 Reciever",
    weight=2.11,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Reciever',
                                   is_attachment_point_types=['AK Side Mount', ],
                                   compatible_magazine_type='AK 5.56x45',
                                   compatible_bullet_type='5.56x45',
                                   compatible_parts={'AK Barrel': ['AK Barrel - 5.56x45',
                                                                   'AK Carbine Barrel - 5.56x45',
                                                                   'AK Pistol Barrel - 5.56x45']},
                                   ),
    description='AK 101/102 series reciever for 5.56x45 AK rifles'
)

"""
Handguards
"""

handguard_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Wood AK Handguard",
    weight=0.144,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   ),
    description='A wooden AKM-style hand guard'
)

handguard_amd65 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AMD-65 Handguard",
    weight=0.284,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   felt_recoil=0.98,
                                   accuracy_distribution=1.05,
                                   ),
    description='AMD-65 steel AK hand guard with vertical grip'
)

handguard_ak74 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Polymer AK Handguard",
    weight=0.273,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   ),
    description='Polymer hand guard such as that of the AK-74 and the AK-100 series'
)

handguard_romanian = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Romanian AK Handguard",
    weight=0.23,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   felt_recoil=0.97,
                                   accuracy_distribution=1.03,
                                   ),
    description="A wooden hand guard featuring the signature romanian-style verticle grip"
)

"""
handguard_microdraco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Micro Draco AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   ),
    description="Very short AK hand guard made for the Micro Draco AK pistol"
)
"""

handguard_ak100 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 100 Series Railed Handguard",
    weight=0.27,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   is_attachment_point_types=['Picrail Underbarrel', ],
                                   ),
    description="A polymer AK hand guard featuring picatinny rails on the underside"
)

handguard_B10M = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="B-10M and B-19 AK Handguard",
    weight=0.27,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   is_attachment_point_types=['Picrail Underbarrel',
                                                              'Picrail Optics Mount',
                                                              'Picrail Side Mount'],
                                   accuracy_distribution=0.96,
                                   ),
    description='An aftermarket AK hand guard by Zenitco, featuring picatinny rails on all sides'
)

handguard_leader = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Leader AK Handguard",
    weight=0.385,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   is_attachment_point_types=['MLOK Underbarrel',
                                                              'MLOK Optics Mount',
                                                              'MLOK Side Mount'],
                                   compatible_parts={'AK Barrel': ["AK Barrel - 7.62x39",
                                                                   "AK Barrel - 5.45x39",
                                                                   "AK Barrel - 5.56x45",
                                                                   "RPK Barrel - 7.62x39",
                                                                   "RPK-74 Barrel - 5.45x39",]},
                                   accuracy_distribution=1.04,
                                   ),
    description='An aftermarket light weight long AK hand guard by Zenitco with MLOK rail attachment points'
)

handguard_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MOE AK Handguard",
    weight=0.415,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   is_attachment_point_types=['MLOK Underbarrel',],
                                   accuracy_distribution=1.07,
                                   ),
    description='An aftermarket light weight polymer hand guard by Magpul with attachment points on its underside'
)

"""
Stocks
"""

stock_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AKM Stock",
    weight=0.364,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.7,
                                   accuracy_distribution=1.08,
                                   ideal_range=15,
                                   ),
    description='A wooden AKM-style stock'
)

stock_rpk = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="RPK Stock",
    weight=0.88,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.56,
                                   accuracy_distribution=0.8,
                                   ideal_range=12,
                                   ),
    description='An RPK style stock fitting AK type rifles'
)

stock_ak74 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK-74 Stock",
    weight=0.273,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.7,
                                   accuracy_distribution=1.08,
                                   ideal_range=15,
                                   ),
    description='A polymer AK-74 style stock'
)

stock_ak100 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK-100 Series Stock",
    weight=0.273,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.73,
                                   ideal_range=15,
                                   ),
    description='A polymer folding stock made for the 100 series of AK rifles'
)

stock_ak_underfolder = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Underfolder Stock",
    weight=0.564,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.8,
                                   accuracy_distribution=0.94,
                                   ideal_range=10,
                                   ),
    description='A metal underfolding stock for AK type rifles such as the AKM-S'
)

stock_ak_triangle = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Triangle Sidefolding Stock",
    weight=0.45,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.68,
                                   accuracy_distribution=0.98,
                                   ideal_range=12,
                                   ),
    description='An almuninium ZPAP style side folding stock for AK type rifles'
)

stock_ak12 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK-12 Stock",
    weight=0.272,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.6,
                                   accuracy_distribution=1.13,
                                   ideal_range=15,
                                   ),
    description='A telescoping and folding polymer stock designed for the 2016 iteration of the AK-12'
)

stock_amd65 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AMD-65 Sidefolding Stock",
    weight=0.38,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.82,
                                   accuracy_distribution=0.9,
                                   ideal_range=12,
                                   ),
    description='A wire sidefolding stock for the AMD-65'
)

stock_pt1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="PT-1 AK Stock",
    weight=0.48,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.64,
                                   accuracy_distribution=1.2,
                                   ideal_range=10,
                                   ),
    description='An aftermarket telescopic sidefolding stock for AK rifles manufactured by Zenitco'
)

stock_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul MOE AK Stock",
    weight=0.354,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.64,
                                   accuracy_distribution=1.12,
                                   ideal_range=15,
                                   ),
    description='An aftermarket polymer fixed stock for AK rifles manufactured by Magpul'
)

stock_zhukov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul Zhukov-S AK Stock",
    weight=0.421,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   felt_recoil=0.62,
                                   accuracy_distribution=1.08,
                                   ideal_range=15,
                                   ),
    description='An aftermarket polymer folding stock for AK rifles manufactured by Magpul'
)

"""
Barrel + Gas Tube
"""

barrel_ak762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Barrel - 7.62x39",
    weight=0.377,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 14x1', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   ),
    description="A standard 415mm (16.3 inch) AK barrel assembly chambered in 7.62x39"
)

barrel_ak545 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Barrel - 5.45x39",
    weight=0.46,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 24x1.5', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   velocity_modifier=1.082,
                                   ),
    description="A standard 415mm (16.3 inch) AK barrel assembly chambered in 5.45x39"
)

barrel_ak556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Barrel - 5.56x45",
    weight=0.46,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   velocity_modifier=1.082,
                                   ),
    description="A standard 415mm (16.3 inch) AK barrel assembly chambered in 5.56x45 such as that of the AK-101"
)

barrel_rpk762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="RPK Barrel - 7.62x39",
    weight=0.53,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 14x1', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   ideal_range=1.3,
                                   accuracy_distribution=0.84,
                                   velocity_modifier=1.066,
                                   ),
    description="A longer (23.2 inch), heavier AK barrel assembly intended for the RPK, chambered in 7.62x39"
)

barrel_rpk545 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="RPK-74 Barrel - 5.45x39",
    weight=0.65,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 24x1.5', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   ideal_range=1.3,
                                   accuracy_distribution=0.84,
                                   velocity_modifier=1.056,
                                   ),
    description="A longer (23.2 inch), heavier AK barrel assembly intended for the RPK-74, chambered in 5.45x39"
)

barrel_ak762_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Carbine Barrel - 7.62x39",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 14x1', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   ideal_range=0.8,
                                   accuracy_distribution=1.3,
                                   velocity_modifier=0.91,
                                   ),
    description="A shortened 314mm (12.4 inch) carbine AK barrel assembly chambered in 7.62x39 such as that of "
                "the AK-104"
)

barrel_ak545_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Carbine Barrel - 5.45x39",
    weight=0.35,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 24x1.5', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   ideal_range=0.8,
                                   accuracy_distribution=1.3,
                                   velocity_modifier=0.81,
                                   ),
    description="A shortened 314mm (12.4 inch) carbine AK barrel assembly chambered in 5.45x39 such as that of "
                "the AK-105"
)

barrel_ak556_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Carbine Barrel - 5.56x45",
    weight=0.35,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'AK Handguard': ["Wood AK Handguard",
                                                                      "AMD-65 Handguard",
                                                                      "Polymer AK Handguard",
                                                                      "Romanian AK Handguard",
                                                                      "AK 100 Series Handguard",
                                                                      "B-10M and B-19 AK Handguard",
                                                                      "Leader AK Handguard",
                                                                      "MOE AK Handguard"
                                                                      ]},
                                   ideal_range=0.8,
                                   accuracy_distribution=1.3,
                                   velocity_modifier=0.95,
                                   ),
    description="A shortened 314mm (12.4 inch) carbine AK barrel assembly chambered in 5.56x39 such as that of "
                "the AK-102"
)

"""
Grips
"""

grip_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   ),
    description="AK pistol grip"
)

grip_ak12 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK-12 Grip",
    weight=0.05,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.03,
                                   ),
    description="AK-12 2016 model pistol grip"
)


grip_sniper = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK AGS-74 Sniper Grip",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.06,
                                   ),
    description="Ergonomic AK pistol grip featuring a palm shelf manufactured by Custom Arms"
)

grip_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK MOE Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.02,
                                   ),
    description="Polymer AK grip manufactured by Magpul"
)

grip_rk3 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK RK-3 Grip",
    weight=0.225,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.04,
                                   ),
    description="Polymer AK grip manufactured by Zenitco"
)

grip_tapco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Tapco SAW Grip",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.05,
                                   ),
    description="Polymer AK grip modelled after the SAW pistol grip manufactured by Tapco"
)

grip_skeletonised = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Skeletonised Grip",
    weight=0.038,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.02
                                   ),
    description="Aluminium skeletonised AK grip manufactured by NDZ"
)

grip_hogue = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK OverMolded Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.05,
                                   ),
    description="A large rubberised AK grip manufactured by Hogue"
)

grip_fab = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK FAB Defense Grip",
    weight=0.12,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   accuracy_distribution=1.06,
                                   ),
    description="A rubberised AK grip by FAB Defense"
)

"""
Muzzle devices
"""

muzzle_ak74 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK-74 Compensator",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 24x1.5',),
                                   muzzle_break_efficiency=0.38,
                                   accuracy_distribution=0.97,
                                   velocity_modifier=1.05,
                                   ),
    description="A compensator/muzzle brake designed for the AK-74 fitting 5.45x39 AK rifles"
)

muzzle_dtk = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK DTK-1 Compensator",
    weight=0.128,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 24x1.5',),
                                   muzzle_break_efficiency=0.2,
                                   accuracy_distribution=0.95,
                                   velocity_modifier=1.08,
                                   ),
    description="A muzzle brake/compensator fitting 5.45x49 AK rifles by Zenitco"
)

muzzle_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AKM Compensator",
    weight=0.02,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   muzzle_break_efficiency=0.7,
                                   ),
    description="A muzzle brake/compensator made for the AKM fitting 7.62x39 AK rifles"
)

muzzle_akml = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AKML Flash Hider",
    weight=0.05,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   muzzle_break_efficiency=0.66,
                                   accuracy_distribution=0.98,
                                   velocity_modifier=1.1,
                                   ),
    description="Flash hider and muzzle brake for 7.62x39 AK rifles"
)

muzzle_lantac = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Drakon Compensator",
    weight=0.09,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   muzzle_break_efficiency=0.16,
                                   accuracy_distribution=0.9,
                                   velocity_modifier=1.06,
                                   ),
    description="Compensator and muzzle brake fitting 7.62x39 AK rifles manufactured by Lantac"
)

muzzle_pbs4 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="PBS-4 5.45x39 Suppressor",
    weight=0.7,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 24x1.5',),
                                   muzzle_break_efficiency=0.3,
                                   accuracy_distribution=0.85,
                                   velocity_modifier=1.1,
                                   is_suppressor=True,
                                   sound_radius=0.25,
                                   ),
    description="Sound suppressor designed for 5.45x39 AK types rifles"
)

muzzle_pbs1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Zenitco DTK-4M 7.62x39 Suppressor",
    weight=0.354,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   muzzle_break_efficiency=0.36,
                                   accuracy_distribution=0.92,
                                   velocity_modifier=1.07,
                                   sound_radius=0.3,
                                   ),
    description="Sound suppressor designed for 7.62x39 AK types rifles"
)

muzzle_dynacomp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Dynacomp Compensator",
    weight=0.076,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   muzzle_break_efficiency=0.25,
                                   accuracy_distribution=0.96,
                                   velocity_modifier=1.05,
                                   ),
    description="Compensator and muzzle brake designed for AK rifles manufactured by Spikes Tactical"
)

"""
Other Accessories
"""

accessory_dustcoverrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Dust Cover W/ Picatinny Rail",
    weight=0.01,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   additional_required_parts=('Optic',),
                                   ),
    description="An AK dust cover featuring a picatinny rail for optics mounting"
)

accessory_railsidemount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK Side Mounted Picatinny Rail",
    weight=0.175,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount',],
                                   additional_required_parts=('Optic',),
                                   ),
    description="A side mounted AK picatinny rail for optics mounting"
)

ak_ar_mag_adapter = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK STANAG Magazine Adapter",
    weight=0.153,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Magazine Adapter',
                                   compatible_magazine_type='STANAG 5.56x45',
                                   compatible_parts={'AK Reciever': ['AK 100 series 5.56 Reciever', ]},
                                   ),
    description="Magazine adapter for 5.56 AK rifles providing compatibility with STANAG magazines by Shaffer Machining"
)

ak = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="Kalashnikov Assualt Rifle",
    weight=1,
    stacking=None,
    description='The classic Russian assault rifle first produced in 1947 and used in almost every global '
                'conflict since.',
    usable_properties=GunMagFed(
        compatible_magazine_type='AK 7.62x39',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=2,
        fire_modes={'single shot': 1, 'rapid fire (semi-auto)': 3, 'automatic': 600},
        current_fire_mode='single shot',
        parts=Parts(),
        enemy_attack_range=20,
        compatible_bullet_type='7.62x39',
        velocity_modifier=1.0,
        felt_recoil=1.0,
    )
)

akmdict = {
    "guns": {
        "automatic rifles": {
            "Kalashnikov Rifle": {
                "required parts": {
                    "AK Reciever": 1,
                    "AK Barrel": 1,
                    "AK Handguard": 1,
                    "AK Grip": 1,
                },
                "compatible parts": {
                    "AK Stock": 1,
                    "AK Optics Mount": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Muzzle Device": 1,
                    "AK Magazine Adapter": 1,
                    "Optic": 1
                },
                "item": ak
            },
        }
    },
}
