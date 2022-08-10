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
    bg_colour=None,
    name="AKM Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Reciever',
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
    bg_colour=None,
    name="AK-74 Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Reciever',
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
    bg_colour=None,
    name="AK 100 series 5.56 Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Reciever',
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
    bg_colour=None,
    name="Wood AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   ),
    description='A wooden AKM-style hand guard'
)

handguard_amd65 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AMD-65 Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   recoil=0.87,
                                   ),
    description='AMD-65 hand guard with its distinctive vertical grip'
)

handguard_ak74 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Polymer AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   ),
    description='Polymer hand guard such as that of the AK-74 and the AK-100 series'
)

handguard_romanian = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Romanian AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   recoil=0.87,
                                   ),
    description="A wooden hand guard featuring the signature romanian-style verticle grip"
)

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

handguard_ak100 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK 100 Series Railed Handguard",
    weight=1,
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
    bg_colour=None,
    name="B-10M and B-19 AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   is_attachment_point_types=['Picrail Underbarrel',
                                                              'Picrail Optics Mount',
                                                              'Picrail Side Mount'],
                                   ),
    description='An aftermarket AK hand guard by Zenitco, featuring picatinny rails on all sides'
)

handguard_leader = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Leader AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   is_attachment_point_types=['Picrail Underbarrel',
                                                              'Picrail Optics Mount',
                                                              'Picrail Side Mount'],
                                   ),
    description='An aftermarket light weight long AK hand guard by Zenitco with picatinny rail attachment points'
)

handguard_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MOE AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Handguard',
                                   is_attachment_point_types=['Picrail Underbarrel',],
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
    bg_colour=None,
    name="AKM Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.84,
                                   base_accuracy=1.24,
                                   close_range_accuracy=0.84,
                                   ),
    description='A wooden AKM-style stock'
)

stock_rpk = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="RPK Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.74,
                                   base_accuracy=1.24,
                                   close_range_accuracy=0.99,
                                   ),
    description='An RPK style stock fitting AK type rifles'
)

stock_ak74 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK-74 Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.84,
                                   base_accuracy=1.24,
                                   close_range_accuracy=0.84,
                                   ),
    description='A polymer AK-74 style stock'
)

stock_ak100 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK-100 Series Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.91,
                                   base_accuracy=1.24,
                                   close_range_accuracy=0.89,
                                   ),
    description='A polymer folding stock made for the 100 series of AK rifles'
)

stock_ak_underfolder = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Underfolder Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.94,
                                   base_accuracy=1.19,
                                   close_range_accuracy=0.96,
                                   ),
    description='A metal underfolding stock for AK type rifles'
)

stock_ak_triangle = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Triangle Sidefolding Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.91,
                                   base_accuracy=1.19,
                                   close_range_accuracy=0.84,
                                   ),
    description='A metal side folding stock for AK type rifles of the type found on the AKS-74'
)

stock_ak12 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK-12 Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.87,
                                   base_accuracy=1.24,
                                   close_range_accuracy=0.91,
                                   ),
    description='A telescoping and folding polymer stock designed for the 2016 iteration of the AK-12'
)

stock_amd65 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AMD-65 Sidefolding Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.94,
                                   base_accuracy=1.29,
                                   close_range_accuracy=0.99,
                                   ),
    description='A wire sidefolding stock for the AMD-65'
)

stock_type56 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Type-56 AK Sidefolding Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.91,
                                   base_accuracy=1.19,
                                   close_range_accuracy=0.94,
                                   ),
    description='AK sidefolding stock such as those found on the chinese Norinco type 56-2'
)

stock_pmd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="PM md AK Sidefolding Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=1.34,
                                   base_accuracy=1.19,
                                   close_range_accuracy=0.99,
                                   ),
    description='AK wire sidefolding stock such as those found on the PM md. 90 carbine AK rifles'
)

stock_pt1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="PT-1 AK Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.89,
                                   close_range_accuracy=0.84,
                                   base_accuracy=1.29,
                                   ),
    description='An aftermarket telescopic sidefolding stock for AK rifles manufactured by Zenitco'
)

stock_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Magpul MOE AK Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.88,
                                   close_range_accuracy=0.84,
                                   base_accuracy=1.27,
                                   ),
    description='An aftermarket polymer adjustable fixed stock for AK rifles manufactured by Magpul'
)

stock_zhukov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Magpul Zhukov-S AK Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Stock',
                                   recoil=0.91,
                                   close_range_accuracy=0.88,
                                   base_accuracy=1.24
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
    bg_colour=None,
    name="AK Barrel - 7.62x39",
    weight=1,
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
    bg_colour=None,
    name="AK Barrel - 5.45x39",
    weight=1,
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
                                                                      ]}
                                   ),
    description="A standard 415mm (16.3 inch) AK barrel assembly chambered in 5.45x39"
)

barrel_ak556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Barrel - 5.56x45",
    weight=1,
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
                                   ),
    description="A standard 415mm (16.3 inch) AK barrel assembly chambered in 5.56x45 such as that of the AK-101"
)

barrel_rpk762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="RPK Barrel - 7.62x39",
    weight=1,
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
                                   base_meat_damage=1.04,
                                   base_armour_damage=1.04,
                                   base_accuracy=1.1,
                                   range_accuracy_dropoff=1.06,
                                   recoil=0.93,
                                   close_range_accuracy=0.85,
                                   equip_time=1.15,
                                   ),
    description="A longer, heavier AK barrel assembly intended for the RPK, chambered in 7.62x39"
)

barrel_rpk545 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="RPK-74 Barrel - 5.45x39",
    weight=1,
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
                                   base_meat_damage=1.04,
                                   base_armour_damage=1.04,
                                   base_accuracy=1.1,
                                   range_accuracy_dropoff=1.06,
                                   recoil=0.93,
                                   close_range_accuracy=0.85,
                                   equip_time=1.15,
                                   ),
    description="A longer, heavier AK barrel assembly intended for the RPK-74, chambered in 5.45x39"
)

barrel_ak762_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Carbine Barrel - 7.62x39",
    weight=1,
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
                                   base_meat_damage=0.93,
                                   base_armour_damage=0.93,
                                   base_accuracy=0.9,
                                   range_accuracy_dropoff=0.85,
                                   recoil=1.05,
                                   close_range_accuracy=1.15,
                                   equip_time=0.85,
                                   ),
    description="A shortened 314mm (12.4 inch) carbine AK barrel assembly chambered in 7.62x39 such as that of "
                "the AK-104"
)

barrel_ak545_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Carbine Barrel - 5.45x39",
    weight=1,
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
                                   base_meat_damage=0.92,
                                   base_armour_damage=0.92,
                                   base_accuracy=0.9,
                                   range_accuracy_dropoff=0.85,
                                   recoil=1.05,
                                   close_range_accuracy=1.15,
                                   equip_time=0.85,
                                   ),
    description="A shortened 314mm (12.4 inch) carbine AK barrel assembly chambered in 5.45x39 such as that of "
                "the AK-105"
)

barrel_ak556_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Carbine Barrel - 5.56x45",
    weight=1,
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
                                   base_meat_damage=0.92,
                                   base_armour_damage=0.92,
                                   base_accuracy=0.9,
                                   range_accuracy_dropoff=0.85,
                                   recoil=1.05,
                                   close_range_accuracy=1.15,
                                   equip_time=0.85,
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
    bg_colour=None,
    name="AK Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   ),
    description="AK pistol grip"
)

grip_ak12 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK-12 Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   base_accuracy=1.05,
                                   recoil=0.98,
                                   ),
    description="AK-12 2016 model pistol grip"
)


grip_sniper = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK AGS-74 Sniper Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   base_accuracy=1.08,
                                   recoil=0.96,
                                   close_range_accuracy=0.95,
                                   ),
    description="Ergonomic AK pistol grip featuring a palm shelf manufactured by Custom Arms"
)

grip_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK MOE Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   ),
    description="Polymer AK grip manufactured by Magpul"
)

grip_rk3 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK RK-3 Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   base_accuracy=1.05,
                                   recoil=0.98,
                                   ),
    description="Polymer AK grip manufactured by Zenitco"
)

grip_tapco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Tapco SAW Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   recoil=0.95,
                                   close_range_accuracy=0.97,
                                   ),
    description="Polymer AK grip modelled after the SAW pistol grip manufactured by Tapco"
)

grip_palm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK US Palm Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   recoil=0.95,
                                   close_range_accuracy=0.97,
                                   ),
    description="Polymer AK grip manufactured by US Palm"
)

grip_skeletonised = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Skeletonised Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   recoil=1.05,
                                   close_range_accuracy=1.07,
                                   ),
    description="Aluminium skeletonised AK grip manufactured by NDZ"
)

grip_hogue = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK OverMolded Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   base_accuracy=1.05,
                                   close_range_accuracy=0.98,
                                   ),
    description="A large rubberised AK grip manufactured by Hogue"
)

grip_fab = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK FAB Defense Grip",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Grip',
                                   base_accuracy=1.05,
                                   recoil=0.97
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
    bg_colour=None,
    name="AK-74 Compensator",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 24x1.5',),
                                   recoil=0.95,
                                   close_range_accuracy=0.98,
                                   ),
    description="A compensator/muzzle brake designed for the AK-74 fitting 5.45x39 AK rifles"
)

muzzle_aks74 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AKS-74U Muzzle Brake",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 24x1.5',),
                                   recoil=0.94,
                                   close_range_accuracy=0.97,
                                   ),
    description="A muzzle brake for the AKS-74U fitting 5.45x39 AK rifles"
)

muzzle_dtk = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK DTK-1 Compensator",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 24x1.5',),
                                   recoil=0.90,
                                   close_range_accuracy=0.94,
                                   ),
    description="A muzzle brake/compensator fitting 5.45x49 AK rifles by Zenitco"
)

muzzle_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AKM Compensator",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   recoil=0.98,
                                   ),
    description="A muzzle brake/compensator made for the AKM fitting 7.62x39 AK rifles"
)

muzzle_akml = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AKML Flash Hider",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   recoil=0.96,
                                   close_range_accuracy=0.94,
                                   ),
    description="Flash hider and muzzle brake for 7.62x39 AK rifles"
)

muzzle_lantac = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Drakon Compensator",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   recoil=0.86,
                                   close_range_accuracy=0.90,
                                   base_accuracy=0.96,
                                   ),
    description="Compensator and muzzle brake fitting 7.62x39 AK rifles manufactured by Lantac"
)

muzzle_pbs4 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="PBS-4 5.45x39 Suppressor",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 24x1.5',),
                                   recoil=0.95,
                                   close_range_accuracy=0.92,
                                   sound_radius=0.7,
                                   ),
    description="Sound suppressor designed for 5.45x39 AK types rifles"
)

muzzle_pbs1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="PBS-1 7.62x39 Suppressor",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   recoil=0.95,
                                   close_range_accuracy=0.92,
                                   sound_radius=0.7,
                                   ),
    description="Sound suppressor designed for 7.62x39 AK types rifles"
)

muzzle_dynacomp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Dynacomp Compensator",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 14x1',),
                                   recoil=0.94,
                                   close_range_accuracy=0.96,
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
    bg_colour=None,
    name="AK Dust Cover W/ Picatinny Rail",
    weight=1,
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
    bg_colour=None,
    name="AK Side Mounted Picatinny Rail",
    weight=1,
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
    bg_colour=None,
    name="AK STANAG Magazine Adapter",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='AK Magazine Adapter',
                                   compatible_magazine_type='STANAG 5.56x45',
                                   compatible_parts={'AK Reciever': ['AK 100 series 5.56 Reciever', ]},
                                   ),
    description="Magazine adapter for 5.56 AK rifles providing compatibility with STANAG magazines"
)

ak = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
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
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.8,
        range_accuracy_dropoff=1.0,
        parts=Parts(),
        enemy_attack_range=15,
        possible_parts={},
        sound_radius=1.0,
        recoil=1.24,
        close_range_accuracy=1.2,
        compatible_bullet_type='7.62x39'
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
