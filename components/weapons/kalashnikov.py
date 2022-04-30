from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
Recievers
"""

reciever_ak47 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Reciever - Milled",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_reciever',
                                   compatible_calibres=('762', ),
                                   recoil=0.97,
                                   close_range_accuracy=0.95,
                                   suffix='Milled 7.62x39'

                                   ),
    description='The original milled AK type reciever'
)

reciever_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AKM Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_reciever',
                                   compatible_calibres=('762', ),
                                   suffix='Stamped 7.62x39'
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
    usable_properties=GunComponent(part_type='ak_reciever',
                                   compatible_calibres=('545', ),
                                   suffix='5.45x39',
                                   compatible_magazine_type='ak545'
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
    usable_properties=GunComponent(part_type='ak_reciever',
                                   compatible_calibres=('556', ),
                                   suffix='100 Series 5.56x45',
                                   compatible_magazine_type='ak556'
                                   ),
    description='AK 101/102 series reciever for 5.56x45 AK rifles'
)

reciever_100762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK 100 series 7.62 Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_reciever',
                                   compatible_calibres=('762', ),
                                   suffix='100 Series 7.62x39'
                                   ),
    description='AK 103/104 series reciever for 7.62x39 AK rifles'
)

reciever_ak9 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK-9 Reciever",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_reciever',
                                   compatible_calibres=('9mm', ),
                                   ),
    description='AK-9 reciever for 9mm AK rifles'
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
    usable_properties=GunComponent(part_type='ak_handguard',
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
    usable_properties=GunComponent(part_type='ak_handguard',
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
    usable_properties=GunComponent(part_type='ak_handguard',
                                   ),
    description='Polymer hand guard scuh as that of the AK-74 and the AK-100 series'
)

handguard_romanian = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Romanian AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_handguard',
                                   recoil=0.87,
                                   ),
    description="A wooden hand guard featuring the signature romanian-style 'dong' verticle grip"
)

handguard_minidraco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mini Draco AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_handguard',
                                   ),
    description="Shortened AK hand guard made for the Mini Draco AK pistol"
)

handguard_microdraco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Micro Draco AK Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_handguard',
                                   ),
    description="Very short AK hand guard made for the Micro Draco AK pistol"
)

handguard_aks74U = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AKS-74U Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_handguard',
                                   ),
    description="A shortened AK hand guard designed for the AKS-74U"
)

handguard_ak100 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK 100 Series Railed Handguard",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_handguard',
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   accessory_attachment=True,
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
    usable_properties=GunComponent(part_type='ak_handguard',
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   accessory_attachment=True,
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
    usable_properties=GunComponent(part_type='ak_handguard',
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   accessory_attachment=True,
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
    usable_properties=GunComponent(part_type='ak_handguard',
                                   accessory_attachment=True,
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_stock',
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
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('762', ),
                                   ),
    description="A standard length AK barrel chambered in 7.62x39"
)

barrel_ak545 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Barrel - 5.45x39",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('545', ),
                                   ),
    description="A standard length AK barrel chambered in 5.45x39"
)

barrel_ak556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Barrel - 5.56x45",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('556', ),
                                   ),
    description="A standard length AK barrel chambered in 5.56x45"
)

barrel_rpk762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="RPK Barrel - 7.62x39",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('762', ),
                                   base_meat_damage=1.1,
                                   base_armour_damage=1.15,
                                   base_accuracy=1.1,
                                   range_accuracy_dropoff=1.2,
                                   recoil=0.9,
                                   close_range_accuracy=0.8,
                                   equip_time=1.2,
                                   ),
    description="A longer, heavier AK barrel intended for the RPK, chambered in 7.62x39"
)

barrel_rpk545 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="RPK-74 Barrel - 5.45x39",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('545', ),
                                   base_meat_damage=1.1,
                                   base_armour_damage=1.15,
                                   base_accuracy=1.1,
                                   range_accuracy_dropoff=1.2,
                                   recoil=0.9,
                                   close_range_accuracy=0.8,
                                   equip_time=1.2,
                                   ),
    description="A longer, heavier AK barrel intended for the RPK-74, chambered in 5.45x39"
)

barrel_ak762_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Carbine Barrel - 7.62x39",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('762', ),
                                   base_meat_damage=0.9,
                                   base_armour_damage=0.85,
                                   base_accuracy=0.9,
                                   range_accuracy_dropoff=0.85,
                                   recoil=1.1,
                                   close_range_accuracy=1.2,
                                   equip_time=0.85,
                                   fire_rate_modifier=1.25
                                   ),
    description="A shortened carbine AK barrel chambered in 7.62x39"
)

barrel_ak545_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Carbine Barrel - 5.45x39",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('545', ),
                                   base_meat_damage=0.9,
                                   base_armour_damage=0.85,
                                   base_accuracy=0.9,
                                   range_accuracy_dropoff=0.85,
                                   recoil=1.1,
                                   close_range_accuracy=1.2,
                                   equip_time=0.85,
                                   fire_rate_modifier=1.25
                                   ),
    description="A shortened carbine AK barrel chambered in 5.45x39"
)

barrel_ak556_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Carbine Barrel - 5.56x45",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('556', ),
                                   base_meat_damage=0.9,
                                   base_armour_damage=0.85,
                                   base_accuracy=0.9,
                                   range_accuracy_dropoff=0.85,
                                   recoil=1.1,
                                   close_range_accuracy=1.2,
                                   equip_time=0.85,
                                   fire_rate_modifier=1.25
                                   ),
    description="A shortened carbine AK barrel chambered in 5.56x45"
)

barrel_ak762_micro = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Pistol Barrel - 7.62x39",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('762', ),
                                   base_meat_damage=0.85,
                                   base_armour_damage=0.80,
                                   base_accuracy=0.8,
                                   range_accuracy_dropoff=0.75,
                                   recoil=1.2,
                                   close_range_accuracy=1.4,
                                   equip_time=0.75,
                                   fire_rate_modifier=1.3
                                   ),
    description="A pistol length AK barrel chambered in 7.62x39"
)

barrel_ak545_micro = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Pistol Barrel - 5.45x39",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('545', ),
                                   base_meat_damage=0.85,
                                   base_armour_damage=0.80,
                                   base_accuracy=0.8,
                                   range_accuracy_dropoff=0.75,
                                   recoil=1.2,
                                   close_range_accuracy=1.4,
                                   equip_time=0.75,
                                   fire_rate_modifier=1.3
                                   ),
    description="A pistol length AK barrel chambered in 5.45x39"
)

barrel_ak556_micro = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AK Pistol Barrel - 5.56x45",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_barrel',
                                   compatible_calibres=('556', ),
                                   base_meat_damage=0.85,
                                   base_armour_damage=0.80,
                                   base_accuracy=0.8,
                                   range_accuracy_dropoff=0.75,
                                   recoil=1.2,
                                   close_range_accuracy=1.4,
                                   equip_time=0.75,
                                   fire_rate_modifier=1.3
                                   ),
    description="A pistol length AK barrel chambered in 5.56x45"
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_grip',
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.95,
                                   close_range_accuracy=0.98,
                                   compatible_calibres=('545', ),
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.94,
                                   close_range_accuracy=0.97,
                                   compatible_calibres=('545', ),
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.90,
                                   close_range_accuracy=0.94,
                                   compatible_calibres=('545', '762'),
                                   ),
    description="A muzzle brake/compensator fitting 7.62x39 and 5.45x49 AK rifles by Zenitco"
)

muzzle_akm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="AKM Compensator",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.98,
                                   compatible_calibres=('762', ),
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.96,
                                   close_range_accuracy=0.94,
                                   compatible_calibres=('762', ),
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.86,
                                   close_range_accuracy=0.90,
                                   base_accuracy=0.96,
                                   compatible_calibres=('762', ),
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.95,
                                   close_range_accuracy=0.92,
                                   sound_radius=0.7,
                                   compatible_calibres=('545', ),
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.95,
                                   close_range_accuracy=0.92,
                                   sound_radius=0.7,
                                   compatible_calibres=('762', ),
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
    usable_properties=GunComponent(part_type='ak_muzzle',
                                   recoil=0.94,
                                   close_range_accuracy=0.96,
                                   compatible_calibres=('762', ),
                                   ),
    description="Compensator and muzzle brake fitting 7.62x39 AK rifles manufactured by Spikes Tactical"
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
    usable_properties=GunComponent(part_type='ak_accessory',
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   optics_mount_type='picatinny'
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
    usable_properties=GunComponent(part_type='ak_accessory',
                                   large_optics_mount=True,
                                   pistol_optics_mount=True,
                                   optics_mount_type='picatinny'
                                   ),
    description="A side mounted AK picatinny rail for optics mounting"
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
                'conflict since',
    usable_properties=GunMagFed(
        compatible_magazine_type='ak762',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=2,
        fire_modes={'single shot': 1, 'automatic': 600},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.8,
        range_accuracy_dropoff=1.0,
        parts=Parts(),
        enemy_attack_range=15,
        possible_parts=mac1045_parts_dict,
        sound_radius=1.0,
        recoil=1.2,
        close_range_accuracy=1.2,
    )
)
