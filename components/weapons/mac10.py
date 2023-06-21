from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

mac1045_lower = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Lower Receiver",
    weight=1.02,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Lower',
                                   compatible_parts={'M10 Upper': ["M10/45 Upper Receiver",
                                                                   "M10/45 Side Cocking Upper Receiver",
                                                                   "MAX-10/45 mk2 Upper Receiver (M10/45)",
                                                                   "MAX-10/31 Upper Receiver (M10)",
                                                                   "MAX-10/31k Upper Receiver (M10)", ], },
                                   functional_part=True,
                                   ),
    description='M10/45 lower receiver'
)

mac109_lower = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Lower Receiver",
    weight=1.02,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Lower',
                                   compatible_parts={'M10 Upper': ["M10/9 Upper Receiver",
                                                                   "M10/9 Side Cocking Upper Receiver",
                                                                   "MAX-10/9 mk2 Upper Receiver (M10/9)",
                                                                   "M10/9 'CalicoMac' Conversion Kit",
                                                                   "MAX-10/31 Upper Receiver (M10)",
                                                                   "MAX-10/31k Upper Receiver (M10)", ], },
                                   functional_part=True,
                                   ),
    description='M10/9 lower receiver'
)

"""
Uppers 
"""

# 45

mac1045_upper = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Upper Receiver",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   compatible_parts={'M10 Barrel': ['M10/45 Barrel', "MAX-10/45 Barrel",
                                                                    "M10/45 Carbine Barrel"],
                                                     'M10 Optics Mount': ['M10 Picatinny Optics Mount', ]},
                                   fire_modes={'automatic': {'fire rate': 1000, 'automatic': True}},
                                   compatible_magazine_type='M10/45',
                                   additional_required_parts=('M10 Barrel',),
                                   suffix="M10/45",
                                   sight_height_above_bore=0.5,
                                   optic_mount_properties={'receiver_height_above_bore': 1.15, },
                                   is_optic=True,
                                   optic_properties={'target_acquisition_ap': 1.05,
                                                     'spread_modifier': 1.08, },
                                   grip_properties={
                                       'spread_modifier': 0.94,
                                       'felt_recoil': 0.95,
                                       'target_acquisition_ap': 0.87,
                                       'ap_distance_cost_modifier': 0.95},
                                   functional_part=True,
                                   ),
    description='M10/45 upper receiver'
)

mac1045_upper_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Side Cocking Upper Receiver",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   is_attachment_point_types=['Picrail Optics Mount - Short',
                                                              'Picrail Top Mount - Short'],
                                   compatible_parts={'M10 Barrel': ['M10/45 Barrel', "MAX-10/45 Barrel",
                                                                    "M10/45 Carbine Barrel"], },
                                   fire_modes={'automatic': {'fire rate': 1000, 'automatic': True}},
                                   additional_required_parts=('M10 Barrel',),
                                   suffix="M10/45 Side Cocking",
                                   compatible_magazine_type='M10/45',
                                   optic_mount_properties={'receiver_height_above_bore': 1.59},
                                   grip_properties={
                                       'spread_modifier': 0.94,
                                       'felt_recoil': 0.95,
                                       'target_acquisition_ap': 0.87,
                                       'ap_distance_cost_modifier': 0.95},
                                   functional_part=True,
                                   ),
    description='M10/45 upper receiver with featuring a non-reciprocating side cocking charging handle as opposed to '
                'the original top cocking upper receivers. Also features a picatinny rail optics mount.'
)

mac1045_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/45 mk2 Upper Receiver (M10/45)",
    weight=1.07,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Short',
                                                              'Picrail Underbarrel - Short',
                                                              'Picrail Top Mount - Long'],
                                   compatible_parts={'M10 Barrel': ['MAX-10/45 Barrel', ]},
                                   additional_required_parts=('Optic', 'M10 Barrel'),
                                   suffix='M10 (MAX-10/45 mk2 Conversion)',
                                   compatible_magazine_type='M10/45',
                                   optic_mount_properties={'receiver_height_above_bore': 1.59},
                                   grip_properties={
                                       'spread_modifier': 0.91,
                                       'felt_recoil': 0.88,
                                       'target_acquisition_ap': 0.82,
                                       'ap_distance_cost_modifier': 0.91},
                                   functional_part=True,
                                   gun_type='pdw',
                                   description="The MAX 10 is a conversion of the M10 submachine gun, also known as "
                                               "the MAC-10. Developed by Lage Manufacturing, the MAX 10 kit allows "
                                               "the user to convert their M10 into a more accurate and controllable "
                                               "firearm, primarily through decreasing the rate of fire."
                                   ),
    description='MAX-10 upper receiver for the M10/45 by Lage Manufacturing. Unlike the original upper receiver, '
                'it is side charging rather than top charging and features picatinny rails for mounting of '
                'accessories and optics. It is longer than the original upper, and as such has a reduced rate of '
                'fire, from ~1,000 RPM to ~750 RPM'
)

# 9mm

mac109_upper = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Upper Receiver",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': {'fire rate': 1100, 'automatic': True}},
                                   compatible_parts={'M10 Barrel': ['M10/9 Barrel', "MAX-10/9 Barrel",
                                                                    "M10/9 Carbine Barrel"],
                                                     'M10 Optics Mount': ['M10 Picatinny Optics Mount', ]
                                                     },
                                   additional_required_parts=('M10 Barrel',),
                                   compatible_magazine_type='M10/9',
                                   sight_height_above_bore=0.5,
                                   optic_mount_properties={'receiver_height_above_bore': 1.15},
                                   optic_properties={'target_acquisition_ap': 1.05,
                                                     'spread_modifier': 1.08, },
                                   is_optic=True,
                                   suffix="M10/9",
                                   grip_properties={
                                       'spread_modifier': 0.94,
                                       'felt_recoil': 0.95,
                                       'target_acquisition_ap': 0.87,
                                       'ap_distance_cost_modifier': 0.95},
                                   functional_part=True,
                                   ),
    description='M10/9 upper receiver'
)

mac109_upper_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Side Cocking Upper Receiver",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': {'fire rate': 1100, 'automatic': True}},
                                   is_attachment_point_types=['Picrail Optics Mount - Short',
                                                              'Picrail Top Mount - Short'],
                                   compatible_parts={'M10 Barrel': ['M10/9 Barrel', "MAX-10/9 Barrel",
                                                                    "M10/9 Carbine Barrel"]},
                                   additional_required_parts=('M10 Barrel',),
                                   compatible_magazine_type='M10/9',
                                   suffix='M10/9 Side Cocking',
                                   optic_mount_properties={'receiver_height_above_bore': 1.59},
                                   grip_properties={
                                       'spread_modifier': 0.94,
                                       'felt_recoil': 0.95,
                                       'target_acquisition_ap': 0.87,
                                       'ap_distance_cost_modifier': 0.95},
                                   functional_part=True,
                                   ),
    description='M10/9 upper receiver with featuring a non-reciprocating side cocking charging handle as opposed to '
                'the original top cocking upper receivers. Also features a picatinny rail optics mount.'
)

mac109_upper_max = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/9 mk2 Upper Receiver (M10/9)",
    weight=1.07,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Side Mount - Short',
                                                              'Picrail Underbarrel - Short'],
                                   compatible_parts={'M10 Barrel': ['MAX-10/9 Barrel', ]},
                                   additional_required_parts=('Optic', 'M10 Barrel'),
                                   compatible_magazine_type='M10/9',
                                   suffix='M10 (MAX-10/9 mk2 Conversion)',
                                   optic_mount_properties={'receiver_height_above_bore': 1.59},
                                   grip_properties={
                                       'spread_modifier': 0.91,
                                       'felt_recoil': 0.88,
                                       'target_acquisition_ap': 0.82,
                                       'ap_distance_cost_modifier': 0.91},
                                   functional_part=True,
                                   gun_type='pdw',
                                   description="The MAX 10 is a conversion of the M10 submachine gun, also known as "
                                               "the MAC-10. Developed by Lage Manufacturing, the MAX 10 kit allows "
                                               "the user to convert their M10 into a more accurate and controllable "
                                               "firearm, primarily through decreasing the rate of fire."
                                   ),
    description='MAX-10 upper receiver for the M10/9 by Lage Manufacturing. Unlike the original upper receiver, '
                'it is side charging rather than top charging and features picatinny rails for mounting of '
                'accessories and optics. It is longer than the original upper, and as such has a reduced rate of '
                'fire, from ~1,100 RPM to ~750 RPM')

mac109_calico_conv = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 'CalicoMac' Conversion Kit",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': {'fire rate': 1100, 'automatic': True}},
                                   compatible_magazine_type='Calico 9mm',
                                   compatible_parts={'M10 Barrel': ['M10/9 Barrel', "MAX-10/9 Barrel",
                                                                    "M10/9 Carbine Barrel", ],
                                                     'Optic': []},
                                   additional_required_parts=('M10 Barrel',),
                                   suffix="M10/9 ('CalicoMac' Conversion)",
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.06, },
                                   is_optic=True,
                                   sight_height_above_bore=1.6,
                                   receiver_height_above_bore=1.15,
                                   grip_properties={
                                       'spread_modifier': 0.91,
                                       'felt_recoil': 0.88,
                                       'target_acquisition_ap': 0.82,
                                       'ap_distance_cost_modifier': 0.91},
                                   functional_part=True,
                                   ),
    description='An upper receiver for the M10/9 made by Calico Firearms compatible with high capacity helical Calico '
                'magazines, feeding from the top of the receiver')

# MAX-10/31

mac109_upper_max31 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/31 Upper Receiver (M10)",
    weight=1.74,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': {'fire rate': 600, 'automatic': True}},
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Side Mount - Long',
                                                              'Picrail Underbarrel - Long', ],
                                   compatible_parts={'M10 Barrel': ["MAX-10/31 Barrel - 1/2-28 Threaded",
                                                                    "MAX-10/31k Barrel - 1/2-28 Threaded",
                                                                    "MAX-10/31 Barrel - 3/4-10 Threaded",
                                                                    "MAX-10/31k Barrel - 3/4-10 Threaded"]},
                                   compatible_magazine_type='Suomi M31',
                                   additional_required_parts=('M10 Barrel',),
                                   suffix="M10 (MAX-10/31 Conversion)",
                                   optic_mount_properties={'receiver_height_above_bore': 1.59},
                                   grip_properties={
                                       'spread_modifier': 0.9,
                                       'felt_recoil': 0.86,
                                       'target_acquisition_ap': 0.81,
                                       'ap_distance_cost_modifier': 0.91},
                                   functional_part=True,
                                   gun_type='pdw',
                                   description="The MAX-10/31 is a conversion for the M10 submachinegun by Lage "
                                               "Manufacturing featuring compatibility with Suomi M31 magazines and "
                                               "decreased rate of fire at 600 RPM."
                                   ),
    description='Upper receiver for the M10/9 by Lage Manufacturing. Featuring compatibility with Suomi M31 '
                'magazines and decreased rate of fire at 600 RPM. Also sporting picatinny rail optic and accessory '
                'attachment points.')

mac109_upper_max31k = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/31k Upper Receiver (M10)",
    weight=1.51,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': {'fire rate': 631, 'automatic': True}},
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Side Mount - Short',
                                                              'Picrail Underbarrel - Short'],
                                   compatible_parts={'M10 Barrel': ["MAX-10/31 Barrel - 1/2-28 Threaded",
                                                                    "MAX-10/31k Barrel - 1/2-28 Threaded",
                                                                    "MAX-10/31 Barrel - 3/4-10 Threaded",
                                                                    "MAX-10/31k Barrel - 3/4-10 Threaded"]},
                                   compatible_magazine_type='Suomi M31',
                                   additional_required_parts=('Optic', 'M10 Barrel'),
                                   suffix="M10 (MAX-10/31k Conversion)",
                                   optic_mount_properties={'receiver_height_above_bore': 1.59},
                                   grip_properties={
                                       'spread_modifier': 0.91,
                                       'felt_recoil': 0.87,
                                       'target_acquisition_ap': 0.79,
                                       'ap_distance_cost_modifier': 0.91},
                                   functional_part=True,
                                   gun_type='pdw',
                                   description="Designed as a shortened variant of the Max-10/31, the MAX-10/31k is a "
                                               "conversion for the M10 submachinegun by Lage "
                                               "Manufacturing featuring compatibility with Suomi M31 magazines and "
                                               "decreased rate."
                                   ),
    description='Shorter version of the MAX-10/31. Upper receiver for the M10/9 by Lage Manufacturing. '
                'Featuring compatibility with Suomi M31 magazines and decreased rate of fire at 631 RPM. '
                'Also sporting picatinny rail optic and accessory attachment points.')

# MAX-10/15
# doesnt currently work since barrels all work on AR gas sys

"""
mac10_upper_max15 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/15 Upper Receiver (M10)",
    weight=1.07,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Upper',
                                   fire_modes={'automatic': 790},
                                   is_attachment_point_types=['Picrail Optics Mount', 'Picrail Side Mount',
                                                              'Picrail Underbarrel'],
                                   additional_required_parts=('Optic', 'AR Barrel', 'AR Handguard'),
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
                                                                      "AR Daniel Defense MK18 Carbine Handguard", ],
                                                     'AR Barrel': ["AR 5.56x45 Standard Barrel",
                                                                   "AR 5.56x45 Carbine Barrel",
                                                                   "AR 5.56x45 HBAR Barrel",
                                                                   "AR 5.56x45 Pistol Barrel", ]},
                                   suffix="M10 (MAX-10/15 Conversion)",
                                   felt_recoil=0.9,
                                   receiver_height_above_bore=1.11, ),
    description='Upper receiver for the M10 submachinegun by Lage Manufacturing. Compatible with AR-15 barrels and '
                'STANAG magazines, essentially converting the M10 into an assault rifle. Features a picatinny optics '
                'rail.')
"""

"""
Barrels
"""

# 45

mac1045_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Barrel',
                                   is_attachment_point_types=['Barrel Thread 7/8x9', 'M10 Barrel'],
                                   velocity_modifier=1.036,
                                   compatible_bullet_type='.45 ACP',
                                   barrel_length=5.75,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A standard length 5.75 inch .45 calibre M10/45 barrel')

mac1045_max_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/45 Barrel",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28', ],
                                   barrel_length=9,
                                   velocity_modifier=1.093,
                                   target_acquisition_ap=1.04,
                                   equip_time=1.07,
                                   compatible_bullet_type='.45 ACP',
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='9 inch .45 calibre barrel for the M10/45 intended for use with the MAX-10 upper receiver')

mac1045_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Carbine Barrel",
    weight=0.22,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28', ],
                                   additional_required_parts=('M10/45 Carbine Handguard',),
                                   barrel_length=16,
                                   velocity_modifier=1.154,
                                   target_acquisition_ap=1.1,
                                   equip_time=1.2,
                                   compatible_bullet_type='.45 ACP',
                                   suffix="Carbine",
                                   accuracy_part=True,
                                   ),
    description='A 16" carbine barrel for the M10/45 manufactured by MasterPiece Arms')

# 9mm

mac109_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Barrel',
                                   is_attachment_point_types=['Barrel Thread 3/4x10', 'M10 Barrel'],
                                   barrel_length=5.75,
                                   velocity_modifier=1.049,
                                   compatible_bullet_type='9mm',
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A standard length 5.75 inch M10/9 barrel in 9mm'
)

mac109_max_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/9 Barrel",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   barrel_length=9,
                                   velocity_modifier=1.131,
                                   target_acquisition_ap=1.04,
                                   equip_time=1.07,
                                   compatible_bullet_type='9mm',
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='9 inch 9mm barrel for the M10/9 intended for use with the MAX-10 upper receiver'
)

mac109_carbine_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Carbine Barrel",
    weight=0.22,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   additional_required_parts=('M10/45 Carbine Handguard',),
                                   barrel_length=16,
                                   equip_time=1.2,
                                   target_acquisition_ap=1.1,
                                   velocity_modifier=1.183,
                                   compatible_bullet_type='9mm',
                                   suffix="Carbine",
                                   accuracy_part=True,
                                   ),
    description='A 16" carbine barrel for the M10/9 in 9mm for the M10/9 manufactured by MasterPiece Arms'
)

max1031_barrel_1228 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/31 Barrel - 1/2-28 Threaded",
    weight=0.12,
    stacking=None,
    usable_properties=GunComponent(part_type="M10 Barrel",
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'M10 Upper': ["MAX-10/31k Upper Receiver (M10/9)"]},
                                   barrel_length=8.375,
                                   velocity_modifier=1.127,
                                   target_acquisition_ap=1.03,
                                   equip_time=1.03,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='8-3/8 inch MAX-10/31 barrel with 1/2-28 threads'
)

max1031k_barrel_1228 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/31k Barrel - 1/2-28 Threaded",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type="M10 Barrel",
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={'M10 Upper': ["MAX-10/31 Upper Receiver (M10/9)",
                                                                   "MAX-10/31k Upper Receiver (M10/9)"]},
                                   barrel_length=5.75,
                                   velocity_modifier=1.049,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='5-3/4 inch MAX-10/31 barrel with 1/2-28 threads'
)

max1031_barrel_3410 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/31 Barrel - 3/4-10 Threaded",
    weight=0.12,
    stacking=None,
    usable_properties=GunComponent(part_type="M10 Barrel",
                                   is_attachment_point_types=['Barrel Thread 3/4x10', ],
                                   compatible_parts={'M10 Upper': ["MAX-10/31k Upper Receiver (M10/9)"]},
                                   barrel_length=8.375,
                                   velocity_modifier=1.127,
                                   compatible_bullet_type='9mm',
                                   target_acquisition_ap=1.03,
                                   equip_time=1.03,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='8-3/8 inch MAX-10/31 barrel with 1/2-28 threads'
)

max1031k_barrel_3410 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MAX-10/31k Barrel - 3/4-10 Threaded",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type="M10 Barrel",
                                   is_attachment_point_types=['Barrel Thread 3/4x10', ],
                                   compatible_parts={'M10 Upper': ["MAX-10/31 Upper Receiver (M10/9)",
                                                                   "MAX-10/31k Upper Receiver (M10/9)"]},
                                   barrel_length=5.75,
                                   velocity_modifier=1.049,
                                   compatible_bullet_type='9mm',
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='5-3/4 inch MAX-10/31 barrel with 1/2-28 threads'
)

"""
Stocks
"""

mac1045_full_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Fixed Stock",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Stock',
                                   felt_recoil=0.6,
                                   ap_distance_cost_modifier=0.73,
                                   spread_modifier=0.6,
                                   equip_time=1.1,
                                   target_acquisition_ap=0.71,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='A sturdy fixed polymer buttstock for the M10 submachinegun by Lage Manufacturing, designed for use '
                'with their MAX-10 series of upper receivers'
)

mac1045_folding_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 'K' Folding Stock",
    weight=0.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Stock',
                                   felt_recoil=0.77,
                                   ap_distance_cost_modifier=0.85,
                                   spread_modifier=0.69,
                                   equip_time=1.03,
                                   target_acquisition_ap=0.69,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='A folding aluminium and polymer buttstock for the M10 submachinegun by Lage Manufacturing, '
                'designed for use with their "K" series of upper receivers'
)

mac1045_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Stock",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Stock',
                                   felt_recoil=0.8,
                                   ap_distance_cost_modifier=0.9,
                                   spread_modifier=0.74,
                                   target_acquisition_ap=0.78,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='The original collapsing wire buttstock for the M10 submachinegun'
)

"""
Other
"""

mac10_carbine_handguard_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Carbine A2 Style Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Carbine Handguard',
                                   tags=['Handguard', ],
                                   prevents_attachment_of={'Handguard': ['Iron Sight', ]},
                                   grip_properties={
                                       'spread_modifier': 0.87,
                                       'felt_recoil': 0.85,
                                       'target_acquisition_ap': 0.8,
                                       'ap_distance_cost_modifier': 0.9}, ),
    description='M16A2 style handguard for the 16 inch M10/45 carbine barrel by MasterPiece Arms')

mac10_carbine_handguard_picatinny = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Carbine Tactical Handguard",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/45 Carbine Handguard',
                                   tags=['Handguard', ],
                                   prevents_attachment_of={'Handguard': ['Iron Sight', ]},
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long',
                                                              'Picrail Underbarrel - Long'],
                                   optic_mount_properties={'receiver_height_above_bore': 1.59,
                                                           'spread_modifier': 1.04,
                                                           'target_acquisition_ap': 0.93},
                                   grip_properties={
                                       'spread_modifier': 0.92,
                                       'felt_recoil': 0.86,
                                       'target_acquisition_ap': 0.85,
                                       'ap_distance_cost_modifier': 0.93},),
    description='Handguard with picatinny rail accessory mounts for the 16 inch M10/45 carbine barrel by '
                'MasterPiece Arms')

mac109_carbine_handguard_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Carbine A2 Style Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Carbine Handguard',
                                   tags=['Handguard', ],
                                   prevents_attachment_of={'Handguard': ['Iron Sight', ]},
                                   grip_properties={
                                       'spread_modifier': 0.87,
                                       'felt_recoil': 0.85,
                                       'target_acquisition_ap': 0.8,
                                       'ap_distance_cost_modifier': 0.9}, ),
    description='M16A2 style handguard for the 16 inch M10/9 carbine barrel by MasterPiece Arms'
)

mac109_carbine_handguard_picatinny = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Carbine Tactical Handguard",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='M10/9 Carbine Handguard',
                                   tags=['Handguard', ],
                                   prevents_attachment_of={'Handguard': ['Iron Sight', ]},
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long',
                                                              'Picrail Underbarrel - Long'],
                                   optic_mount_properties={'receiver_height_above_bore': 1.59,
                                                           'spread_modifier': 1.04,
                                                           'target_acquisition_ap': 0.93},
                                   grip_properties={
                                       'spread_modifier': 0.92,
                                       'felt_recoil': 0.86,
                                       'target_acquisition_ap': 0.85,
                                       'ap_distance_cost_modifier': 0.93},),
    description='Handguard with picatinny rail accessory mounts for the 16 inch M10/9 carbine barrel by'
                ' MasterPiece Arms'
)

mac10_vertical_grip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Vertical Grip",
    weight=0.06,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('M10 Barrel',),
                                   grip_properties={
                                       'spread_modifier': 0.93,
                                       'felt_recoil': 0.8,
                                       'target_acquisition_ap': 0.77,
                                       'ap_distance_cost_modifier': 0.95},
                                   ),
    description='A vertical grip that clamps onto the barrel of M10 pattern submachineguns'
)

mac10_optics_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Picatinny Optics Mount",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='M10 Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Short', ],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.75},
                                   ),
    description='A picatinny rail optics mount for the M10. Screwed into place on the rear of the stock M10 upper '
                'receiver'
)

mac10_trirail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 Tri Rail Mount",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Accessory Adapter M10',
                                   is_attachment_point_types=['Picrail Side Mount - Short',
                                                              'Picrail Underbarrel - Short'],
                                   incompatibilities=(("M10 Vertical Grip",),)
                                   ),
    description='A picatinny tri rail side and underbarrel accessory mount for M10 submachineguns'
)

mac10_ar_stock_adapter = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10 AR Buffertube Stock Adapter",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='Stock Adapter M10',
                                   compatible_parts={'M10 Stock': []},
                                   additional_required_parts=('AR Stock',),
                                   ),
    description='A stock adapter for M10 submachineguns allowing the use of AR stocks through the addition of an '
                'AR 15 style buffer tube'
)

mac1045_sionics_suppressor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Sionics Suppressor",
    weight=0.54,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   is_suppressor=True,
                                   muzzle_break_efficiency=0.46,
                                   velocity_modifier=1.14,
                                   fire_rate_modifier=1.06,
                                   sound_radius=0.16,
                                   equip_time=1.11,
                                   attachment_point_required=('Barrel Thread 7/8x9',),
                                   grip_properties={
                                       'spread_modifier': 0.75,
                                       'felt_recoil': 0.8,
                                       'target_acquisition_ap': 0.95,
                                       'ap_distance_cost_modifier': 0.95},
                                   gun_type='pdw',
                                   ),
    description='A large suppressor manufactured by the Sionics company for the M10/45. Uses a two-stage design to '
                'significantly reduce the sound of firing, to the point that the bolt can be heard cycling when '
                'subsonic ammunition is used. Also functions as a grip, increasing controllability in full auto.')

mac109_sionics_suppressor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Sionics Suppressor",
    weight=0.54,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   is_suppressor=True,
                                   muzzle_break_efficiency=0.46,
                                   velocity_modifier=1.14,
                                   fire_rate_modifier=1.06,
                                   sound_radius=0.16,
                                   equip_time=1.11,
                                   attachment_point_required=('Barrel Thread 3/4x10',),
                                   grip_properties={
                                       'spread_modifier': 0.75,
                                       'felt_recoil': 0.8,
                                       'target_acquisition_ap': 0.95,
                                       'ap_distance_cost_modifier': 0.95},
                                   gun_type='pdw',
                                   ),
    description='A large suppressor manufactured by the Sionics company for the M10/9. Uses a two-stage design to '
                'significantly reduce the sound of firing, to the point that the bolt can be heard cycling when '
                'subsonic ammunition is used. Also functions as a grip, increasing controllability in full auto.')

mac1045_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 'Blackout' Barrel Extension",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 7/8x9',),
                                   compatible_parts={'M10 Barrel': ['M10/45 Barrel', ]},
                                   equip_time=1.09,
                                   grip_properties={
                                       'spread_modifier': 0.7,
                                       'felt_recoil': 0.85,
                                       'target_acquisition_ap': 0.95,
                                       'ap_distance_cost_modifier': 0.9},
                                   gun_type='pdw',
                                   ),
    description='A 7 inch barrel extension for the M10/45. Threads onto the original M10 barrel and acts as a '
                'counterbalance, adding weight to the front of the gun and as a grip.')

mac109_extended_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 'Blackout' Barrel Extension",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 3/4x10',),
                                   compatible_parts={'M10 Barrel': ['M10/45 Barrel', ]},
                                   equip_time=1.09,
                                   grip_properties={
                                       'spread_modifier': 0.7,
                                       'felt_recoil': 0.85,
                                       'target_acquisition_ap': 0.95,
                                       'ap_distance_cost_modifier': 0.9},
                                   gun_type='pdw',
                                   ),
    description='A 7 inch barrel extension for the M10/9. Threads onto the original M10 barrel and acts as a '
                'counterbalance, adding weight to the front of the gun and as a grip.'
)

"""
Guns
"""

mac10 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="",
    weight=1,
    stacking=None,
    description='The M10, also known as the MAC-10, is a compact submachine gun that was developed by Gordon Ingram '
                'in the 1960s. A simple open bolt blowback design, it is known for its compact size and blisteringly '
                'high rate of fire. Models were produced chambered in both 9mm parabellum and .45 ACP. ',
    usable_properties=GunMagFed(
        compatible_magazine_type='M10/45',
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        ap_to_equip=75,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type='',
        firing_ap_cost=50,
        velocity_modifier=1.0,
        felt_recoil=1.13,
        ap_distance_cost_modifier=1.0,
        sight_height_above_bore=0,
        receiver_height_above_bore=0,
        sound_modifier=1.0,
        target_acquisition_ap=50,
        zero_range=25,
        spread_modifier=0.06,
        gun_type='pistol',
        barrel_length=4
    )
)

mac10dict = {
    "guns": {
        "submachineguns": {
            "MAC 10": {
                "required parts": {
                    "M10 Lower": 1,
                    "M10 Upper": 1,
                },
                "compatible parts": {
                    "Stock Adapter M10": 1,
                    "Attachment Adapter": 1,
                    "Muzzle Adapter": 1,
                    "M10 Stock": 1,
                    "M10 Optics Mount": 1,
                    "Muzzle Device": 1,
                    "Accessory Adapter M10": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1
                },
                "item": mac10
            },
        },
    }
}
