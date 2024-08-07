from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

# add belt fed upper, 7.62x39 parts, 9mm/45 acp parts, P90 mag conversion thing

# 1.5 seconds average to draw, aim, shoot - pistol
# can pull trigger 4 times per second
#
# pistol base line - Glock 17
# rifle base line - M4
#
# equip (pistol - from holster) - 75
# equip (rifle - from sling) - 100
# acquire target (pistol) - 50
# acquire target (rifle) - 30
# shoot (pistol and rifle) -
#
# recoil reduction
#     stock - 45%
#     handguard - 15%
#     pistol grip - 10%
#     additional 5-10% for rifle stocks with integrated pistol grip
#
# ap distance cost modifier
#     stock - 0.7
#     hand guard - 0.9
#     pistol grip -
#
# spread reduction
#     stock - 0.86
#     handguard - 0.9
#     pistol grip -
#
# target acquisition ap
#     stock - 0.75
#     handguard - 0.8
#     pistol grip -


"""
Action
"""
# total action weight - 1.02 kg
#
# action_r700_556 = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 Action 5.56x45/.300 BLK",
#     weight=1.02,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Action',
#                                    compatible_magazine_type=(, ),
#                                    compatible_parts={},
#                                    functional_part=True,
#                                    accuracy_part=True
#                                    ),
#     description='5.56x45 / .300 Blackout Remington 700 action.'
# )
#
# action_r700_308 = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 Action .308",
#     weight=1.02,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Action',
#                                    suffix='.308',
#                                    compatible_magazine_type=(, ),
#                                    compatible_parts={},
#                                    functional_part=True,
#                                    accuracy_part=True
#                                    ),
#     description='.308 Remington 700 action.'
# )
#
# action_r700_3006 = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 Action .30-06",
#     weight=1.02,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Action',
#                                    suffix='.30-06',
#                                    compatible_magazine_type=(, ),
#                                    compatible_parts={},
#                                    functional_part=True,
#                                    accuracy_part=True
#                                    ),
#     description='.30-06 Remington 700 action.'
# )
#
#
# """
# Barrel
# """
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )
#
# r700_barrel_cal_len = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_GRAY,
#     name="R700 LEN Barrel CALIBRE",
#     weight=,
#     stacking=None,
#     usable_properties=GunComponent(part_type='R700 Barrel',
#                                    compatible_magazine_type=(, ),
#                                    compatible_bullet_type=(,),
#                                    is_attachment_point_types=[, ],
#                                    barrel_length=,
#                                    velocity_modifier={},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    ),
#     description='LENGTH inch R700 barrel chambered in CALIBRE'
# )

"""
Lower Receivers
"""

lower_ar15 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-15 Lower Receiver",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Receiver',
                                   suffix='15',
                                   tags=['Lower AR-15', ],
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_parts={'AR Upper Receiver': ['M16A2 Upper Receiver',
                                                                           'M16A4 Upper Receiver'],
                                                     'MCR Upper Receiver': ['MCR-060 Upper Assembly',]},
                                   functional_part=True,
                                   ),
    description='A standard AR-15 type semi-automatic lower receiver'
)

lower_ar_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 9mm/40 S&W Lower Receiver",
    weight=0.368,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Receiver',
                                   tags=['Lower AR-15', ],
                                   compatible_parts={'AR Upper Receiver': ['AR 9mm/40 S&W Upper Reciever'],
                                                     'MCR Upper Receiver': []},
                                   functional_part=True,
                                   ),
    description='An AR-15 type semi-automatic lower receiver. Accepts Glock style 9mm/40 S&W magazines.'
)

lower_ar_9mm_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 9mm/40 S&W Select Fire Lower Receiver",
    weight=0.368,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Receiver',
                                   prefix='Full-Auto',
                                   tags=['Lower AR-15', ],
                                   compatible_parts={'AR Upper Receiver': ['AR 9mm/40 S&W Upper Reciever',],
                                                     'MCR Upper Receiver': []},
                                   fire_modes={'automatic': {'fire rate': 700, 'automatic': True}},
                                   functional_part=True,
                                   ),
    description='An AR-15 type select fire lower receiver. Accepts Glock style 9mm/40 S&W magazines.'
)

lower_ar10 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 Lower Receiver",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Receiver',
                                   suffix='10',
                                   tags=['Lower AR-10', ],
                                   compatible_magazine_type=('AR10 7.62x51', ),
                                   compatible_parts={'AR Upper Receiver': ['AR10 Upper Receiver', ],
                                                     'MCR Upper Receiver': []},
                                   functional_part=True,
                                   description='Developed in the 1950s by Eugene Stoner, the AR-10 was designed as a '
                                               'selective-fire rifle for military use and later gained popularity in '
                                               'the civilian market. Unlike the AR-15, which is chambered for smaller '
                                               'cartridges like the .223 Remington, the AR-10 is typically chambered '
                                               'for larger cartridges such as the 7.62x51mm NATO.',
                                   ),
    description='AR-10 receiver designed for rifle calibre AR rifles'
)

lower_ar15_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-15 Select Fire Lower Receiver",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Receiver',
                                   suffix='15',
                                   prefix='Full-Auto',
                                   tags=['Lower AR-15', ],
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_parts={'AR Upper Receiver': ['M16A2 Upper Receiver',
                                                                           'M16A4 Upper Receiver'],
                                                     'MCR Upper Receiver': ['MCR-060 Upper Assembly',]},
                                   fire_modes={'automatic': {'fire rate': 700, 'automatic': True}},
                                   functional_part=True,
                                   ),
    description='An AR-15 type lower receiver with select fire capability'
)

lower_ar10_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 Lower Receiver",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Lower Receiver',
                                   suffix='10',
                                   prefix='Full-Auto',
                                   tags=['Lower AR-10', ],
                                   compatible_magazine_type=('AR10 7.62x51', ),
                                   compatible_parts={'AR Upper Receiver': ['AR10 Upper Receiver', ],
                                                     'MCR Upper Receiver': []},
                                   fire_modes={'automatic': {'fire rate': 700, 'automatic': True}},
                                   functional_part=True,
                                   description='Developed in the 1950s by Eugene Stoner, the AR-10 was designed as a '
                                               'selective-fire rifle for military use and later gained popularity in '
                                               'the civilian market. Unlike the AR-15, which is chambered for smaller '
                                               'cartridges like the .223 Remington, the AR-10 is typically chambered '
                                               'for larger cartridges such as the 7.62x51mm NATO.',
                                   ),
    description='AR-10 receiver designed for rifle calibre AR rifles with select fire capability'
)

"""
Upper Receiver
"""

upper_ar_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M16A2 Upper Receiver",
    weight=0.68,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Receiver',
                                   additional_required_parts=('Front Sight',),
                                   tags=['Iron Sight', ],
                                   optic_properties={'target_acquisition_ap': 1.03,
                                                     'ap_distance_cost_modifier': 0.96,
                                                     'sight_spread_modifier': 0.02,
                                                     'zero_range': 25, },
                                   optic_mount_properties={'receiver_height_above_bore': 2.5},
                                   prevents_attachment_of={'AR Handguard': ['Optic', ],
                                                           'Handguard': ['Iron Sight', ],
                                                           'Attachment Adapter': ['Optic', ]
                                                           },
                                   is_optic=True,
                                   functional_part=True,
                                   ),
    description='A standard AR-15 type upper receiver for 5.56x45 or .300 Blackout rifles with integrated '
                'carrying handle'
)

upper_ar_m16a4 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M16A4 Upper Receiver",
    weight=0.527,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Receiver',
                                   additional_required_parts=('Optic',),
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   compatible_parts={'AR Optics Mount': []},
                                   optic_mount_properties={'receiver_height_above_bore': 1.11},
                                   prevents_attachment_of={'Handguard': ['Iron Sight', ]},
                                   functional_part=True,
                                   ),
    description='A standard AR-15 type upper receiver for 5.56x45 or .300 Blackout rifles with a picatinny '
                'rail optics mount'
)

upper_ar_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 9mm/40 S&W Upper Receiver",
    weight=0.64,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Receiver',
                                   additional_required_parts=('Optic',),
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   compatible_parts={'AR Optics Mount': []},
                                   optic_mount_properties={'receiver_height_above_bore': 1.11},
                                   prevents_attachment_of={'Handguard': ['Iron Sight', ]},
                                   functional_part=True,
                                   ),
    description='An AR type upper receiver for 9mm / 40 S&W AR-type pistols with a picatinny '
                'rail optics mount'
)

upper_ar10 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR10 Upper Receiver",
    weight=0.65,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Upper Receiver',
                                   additional_required_parts=('Optic',),
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   compatible_parts={'AR Optics Mount': []},
                                   optic_mount_properties={'receiver_height_above_bore': 1.11},
                                   prevents_attachment_of={'Handguard': ['Iron Sight', ]},
                                   functional_part=True,
                                   ),
    description='An AR-10 type upper receiver for rifle calibres such as 7.62x51'
)

"""
Barrels
"""

"""5.56x39"""

ar_barrel_standard_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 5.56x45 Standard Barrel - Rifle Length Gas System",
    weight=0.99,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('5.56x45',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .223', ],
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
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['full length barrel', ],
                                   barrel_length=20,
                                   velocity_modifier={'5.56x45': 0.953},
                                   functional_part=True,
                                   accuracy_part=True,
                                   ),
    description='A 20" standard length AR 5.56x45 barrel with a rifle length gas system'
)

ar_barrel_standard_556_midlen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 5.56x45 Standard Barrel - Mid Length Gas System",
    weight=0.99,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('5.56x45',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .223', ],
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
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['full length barrel', ],
                                   barrel_length=20,
                                   velocity_modifier={'5.56x45': 0.953},
                                   fire_rate_modifier=1.054,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 20" standard length AR 5.56x45 barrel with a mid length gas system'
)

ar_barrel_carbine_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 5.56x45 Carbine Barrel - Mid Length Gas System",
    weight=0.79,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Carbine',
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('5.56x45',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .223', ],
                                   compatible_parts={
                                       'AR Handguard': ["AR M16A1 Handguard",
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
                                                        "AR Aero Precision Pistol Handguard",
                                                        "AR Faxon Streamline Pistol Handguard",
                                                        "4 Inch AR Pistol Handguard - MLOK",
                                                        "4 Inch AR Pistol Handguard - Quad Rail",
                                                        ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   velocity_modifier={'5.56x45': 0.921},
                                   target_acquisition_ap=0.96,
                                   ap_to_equip=0.9,
                                   fire_rate_modifier=1.054,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" carbine length AR 5.56x45 barrel with a mid length gas system'
)

ar_barrel_carbine_556_carblen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 5.56x45 Carbine Barrel - Carbine Length Gas System",
    weight=0.79,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Carbine',
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('5.56x45',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .223', ],
                                   compatible_parts={
                                       'AR Handguard': ["AR M16A1 Handguard",
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
                                                        "AR Aero Precision Pistol Handguard",
                                                        "AR Faxon Streamline Pistol Handguard",
                                                        "4 Inch AR Pistol Handguard - MLOK",
                                                        "4 Inch AR Pistol Handguard - Quad Rail",
                                                        ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   velocity_modifier={'5.56x45': 0.921},
                                   target_acquisition_ap=0.96,
                                   ap_to_equip=0.9,
                                   fire_rate_modifier=1.235,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" carbine length AR 5.56x45 barrel with a carbine length gas system'
)

ar_barrel_pistol_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 5.56x45 Pistol Barrel - Carbine Length Gas System",
    weight=0.54,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Pistol',
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('5.56x45',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .223', ],
                                   compatible_parts={'AR Handguard': ["AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=10,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'5.56x45': 0.77},
                                   target_acquisition_ap=0.92,
                                   fire_rate_modifier=1.235,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel with a carbine length gas system'
)

ar_barrel_pistol_556_pistollen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 5.56x45 Pistol Barrel - Pistol Length Gas System",
    weight=0.54,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Pistol',
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('5.56x45',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .223', ],
                                   compatible_parts={'AR Handguard': ["AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=10,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'5.56x45': 0.77},
                                   target_acquisition_ap=0.92,
                                   fire_rate_modifier=1.35,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 10" pistol length AR 5.56x45 barrel with a pistol length gas system'
)

""".300 Blackout"""

ar_barrel_carbine_300 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR .300 Blackout Carbine Barrel - Mid Length Gas System",
    weight=0.82,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Carbine .300 Blk',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('.300 Blackout',),
                                   velocity_modifier={'.300 Blackout': 1.0},
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
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   target_acquisition_ap=0.96,
                                   ap_to_equip=0.9,
                                   fire_rate_modifier=1.054,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" carbine length AR .300 Blackout barrel with a mid length gas system'
)

ar_barrel_carbine_300_carbinelen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR .300 Blackout Carbine Barrel - Carbine Length Gas System",
    weight=0.82,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Carbine .300 Blk',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('.300 Blackout',),
                                   velocity_modifier={'.300 Blackout': 1.0},
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
                                                                      "AR Magpul MOE Pistol Handguard",
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   target_acquisition_ap=0.96,
                                   ap_to_equip=0.9,
                                   fire_rate_modifier=1.235,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" carbine length AR .300 Blackout barrel with a carbine length gas system'
)

ar_barrel_pistol_300 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR .300 Blackout Pistol Barrel - Pistol Length Gas System",
    weight=0.59,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Pistol .300 Blk',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('.300 Blackout',),
                                   compatible_parts={'AR Handguard': ["AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=10,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'.300 Blackout': 0.91},
                                   target_acquisition_ap=0.92,
                                   fire_rate_modifier=1.235,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 10" pistol length AR .300 Blackout barrel with a carbine length gas system'
)

ar_barrel_pistol_300_pistollen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR .300 Blackout Pistol Barrel - Pistol Length Gas System",
    weight=0.59,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Pistol .300 Blk',
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_magazine_type=('STANAG', ),
                                   compatible_bullet_type=('.300 Blackout',),
                                   compatible_parts={'AR Handguard': ["AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "AR M16A2 Carbine Handguard",
                                                                      "AR Magpul MOE Carbine Handguard",
                                                                      "AR Aero Precision Carbine Handguard",
                                                                      "AR Faxon Streamline Carbine Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=10,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'.300 Blackout': 0.91},
                                   target_acquisition_ap=0.92,
                                   fire_rate_modifier=1.35,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 10" pistol length AR .300 Blackout barrel with a pistol length gas system'
)

""".308"""

ar_barrel_standard_308 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 7.62x51 Standard Barrel - Rifle Length Gas System",
    weight=1.58,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('AR10 7.62x51',),
                                   compatible_bullet_type=('7.62x51',),
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 A2 Handguard",
                                                                      "AR-10 A2 Carbine Handguard",
                                                                      "AR-10 Wilson Combat Handguard",
                                                                      "AR-10 Wilson Combat Carbine Handguard",
                                                                      "AR-10 V Seven Hyper-Light Handguard",
                                                                      "AR-10 V Seven Hyper-Light Carbine Handguard",
                                                                      "AR-10 HERA Arms IRS Handguard",
                                                                      "AR-10 Brigand Arms Atlas Carbine Handguard",
                                                                      ]},
                                   tags=['full length barrel', ],
                                   barrel_length=20,
                                   ap_to_equip=1.1,
                                   velocity_modifier={'7.62x51': 0.968},
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 20" AR-10 7.62x51 barrel with a rifle length gas system'
)

ar_barrel_standard_308_midlen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 7.62x51 Standard Barrel - Mid Length Gas System",
    weight=1.58,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('AR10 7.62x51',),
                                   compatible_bullet_type=('7.62x51',),
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 A2 Handguard",
                                                                      "AR-10 A2 Carbine Handguard",
                                                                      "AR-10 Wilson Combat Handguard",
                                                                      "AR-10 Wilson Combat Carbine Handguard",
                                                                      "AR-10 V Seven Hyper-Light Handguard",
                                                                      "AR-10 V Seven Hyper-Light Carbine Handguard",
                                                                      "AR-10 HERA Arms IRS Handguard",
                                                                      "AR-10 Brigand Arms Atlas Carbine Handguard",
                                                                      ]},
                                   tags=['full length barrel', ],
                                   barrel_length=20,
                                   ap_to_equip=1.1,
                                   velocity_modifier={'7.62x51': 0.968},
                                   fire_rate_modifier=1.054,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 20" AR-10 7.62x51 barrel with a mid length gas system'
)

ar_barrel_carbine_308_midlen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 7.62x51 Carbine Barrel - Mid Length Gas System",
    weight=0.87,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('AR10 7.62x51',),
                                   compatible_bullet_type=('7.62x51',),
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 A2 Carbine Handguard",
                                                                      "AR-10 Wilson Combat Carbine Handguard",
                                                                      "AR-10 V Seven Hyper-Light Carbine Handguard",
                                                                      "AR-10 HERA Arms Carbine Handguard",
                                                                      "AR-10 Brigand Arms Atlas Carbine Handguard",
                                                                      "AR-10 Brigand Arms Atlas Pistol Handguard",
                                                                      "AR-10 HERA Arms Pistol Handguard",
                                                                      "AR-10 V Seven Hyper-Light Pistol Handguard",
                                                                      "AR-10 Wilson Combat Pistol Handguard",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   ap_to_equip=0.9,
                                   velocity_modifier={'7.62x51': 0.925},
                                   target_acquisition_ap=0.96,
                                   fire_rate_modifier=1.054,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" carbine length AR-10 7.62x51 barrel with a mid length gas system'
)

ar_barrel_carbine_308_carblen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 7.62x51 Carbine Barrel - Carbine Length Gas System",
    weight=0.87,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Carbine',
                                   compatible_magazine_type=('AR10 7.62x51',),
                                   compatible_bullet_type=('7.62x51',),
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 A2 Carbine Handguard",
                                                                      "AR-10 Wilson Combat Carbine Handguard",
                                                                      "AR-10 V Seven Hyper-Light Carbine Handguard",
                                                                      "AR-10 HERA Arms Carbine Handguard",
                                                                      "AR-10 Brigand Arms Atlas Carbine Handguard",
                                                                      "AR-10 Brigand Arms Atlas Pistol Handguard",
                                                                      "AR-10 HERA Arms Pistol Handguard",
                                                                      "AR-10 V Seven Hyper-Light Pistol Handguard",
                                                                      "AR-10 Wilson Combat Pistol Handguard",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   ap_to_equip=0.9,
                                   velocity_modifier={'7.62x51': 0.925},
                                   target_acquisition_ap=0.96,
                                   fire_rate_modifier=1.235,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" carbine length AR-10 7.62x51 barrel with a carbine length gas system'
)

ar_barrel_pistol_308_carblen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 7.62x51 Pistol Barrel - Carbine Length Gas System",
    weight=0.85,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Pistol',
                                   compatible_magazine_type=('AR10 7.62x51',),
                                   compatible_bullet_type=('7.62x51',),
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 Brigand Arms Atlas Pistol Handguard",
                                                                      "AR-10 HERA Arms Pistol Handguard",
                                                                      "AR-10 V Seven Hyper-Light Pistol Handguard",
                                                                      "AR-10 Wilson Combat Pistol Handguard",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=10,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'7.62x51': 0.79},
                                   target_acquisition_ap=0.92,
                                   fire_rate_modifier=1.235,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 10" pistol length AR 7.62x51 barrel with a carbine length gas system'
)

ar_barrel_pistol_308_pistollen = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 7.62x51 Pistol Barrel - Pistol Length Gas System",
    weight=0.85,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   suffix='Pistol',
                                   compatible_magazine_type=('AR10 7.62x51',),
                                   compatible_bullet_type=('7.62x51',),
                                   is_attachment_point_types=['Barrel Thread 5/8x24', ],
                                   compatible_parts={'AR Handguard': ["AR-10 Brigand Arms Atlas Pistol Handguard",
                                                                      "AR-10 HERA Arms Pistol Handguard",
                                                                      "AR-10 V Seven Hyper-Light Pistol Handguard",
                                                                      "AR-10 Wilson Combat Pistol Handguard",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=10,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'7.62x51': 0.79},
                                   target_acquisition_ap=0.92,
                                   fire_rate_modifier=1.35,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 10" pistol length AR 7.62x51 barrel with a pistol length gas system'
)

"""9mm"""

ar_barrel_9mm_16in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 9mm Barrel - 16 Inches",
    weight=0.68,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('Glock 9mm',),
                                   suffix='9mm',
                                   compatible_bullet_type=('9mm',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .30', ],
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
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   velocity_modifier={'9mm': 1.183},
                                   target_acquisition_ap=0.96,
                                   ap_to_equip=0.9,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" AR barrel chambered for 9mm'
)

ar_barrel_9mm_11in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 9mm Barrel - 11 Inches",
    weight=0.51,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('Glock 9mm',),
                                   suffix='9mm',
                                   compatible_bullet_type=('9mm',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .30', ],
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
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=11,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'9mm': 1.159},
                                   target_acquisition_ap=0.92,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 11" AR barrel chambered for 9mm'
)

ar_barrel_9mm_4in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR 9mm Barrel - 4.5 Inches",
    weight=0.229,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('Glock 9mm',),
                                   tags=['pistol barrel', ],
                                   suffix='9mm',
                                   compatible_bullet_type=('9mm',),
                                   is_attachment_point_types=['Barrel Thread 1/2x28 - .30', ],
                                   compatible_parts={'AR Handguard': ["4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   barrel_length=4.5,
                                   ap_to_equip=0.56,
                                   velocity_modifier={'9mm': 1.033},
                                   target_acquisition_ap=0.84,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 4.5" AR barrel chambered for 9mm'
)

"""40 S&W"""

ar_barrel_40_16in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR .40 S&W Barrel - 16 Inches",
    weight=0.544,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   suffix='.40 S&W',
                                   compatible_bullet_type=('40 S&W',),
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
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
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['carbine barrel', ],
                                   barrel_length=16,
                                   velocity_modifier={'40 S&W': 1.18},
                                   target_acquisition_ap=0.96,
                                   ap_to_equip=0.9,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A 16" AR barrel chambered for .40 S&W'
)

ar_barrel_40_12in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR .40 S&W Barrel - 12.5 Inches",
    weight=0.363,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   suffix='.40 S&W',
                                   compatible_bullet_type=('40 S&W',),
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
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
                                                                      "AR Aero Precision Pistol Handguard",
                                                                      "AR Faxon Streamline Pistol Handguard",
                                                                      "4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   tags=['pistol barrel', ],
                                   barrel_length=12.5,
                                   ap_to_equip=0.78,
                                   velocity_modifier={'40 S&W': 1.159},
                                   target_acquisition_ap=0.92,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 12.5" AR barrel chambered for .40 S&W'
)

ar_barrel_40_4in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR .40 S&W Barrel - 4 Inches",
    weight=0.272,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Barrel',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   tags=['pistol barrel', ],
                                   suffix='.40 S&W',
                                   compatible_bullet_type=('40 S&W',),
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={'AR Handguard': ["4 Inch AR Pistol Handguard - MLOK",
                                                                      "4 Inch AR Pistol Handguard - Quad Rail",
                                                                      ]},
                                   barrel_length=4,
                                   ap_to_equip=0.56,
                                   velocity_modifier={'40 S&W': 1.0},
                                   target_acquisition_ap=0.84,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A 4" AR barrel chambered for .40 S&W'
)

"""
Stocks
"""

ar_stock_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR M16A1 Stock",
    weight=0.71,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   felt_recoil=0.55,
                                   ap_distance_cost_modifier=0.71,
                                   handling_spread_modifier=0.86,
                                   ap_to_equip=1.2,
                                   target_acquisition_ap=0.75,
                                   has_stock=True,
                                   ),
    description='M16A2 style fixed rifle stock'
)

ar_stock_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Magpul MOE Stock",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   felt_recoil=0.62,
                                   ap_distance_cost_modifier=0.76,
                                   handling_spread_modifier=0.9,
                                   ap_to_equip=1.08,
                                   target_acquisition_ap=0.7,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='A light weight collapsing stock carbine by Magpul'
)

ar_stock_ubr = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Magpul UBR Stock",
    weight=0.6,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   ap_to_equip=1.18,
                                   felt_recoil=0.59,
                                   ap_distance_cost_modifier=0.71,
                                   handling_spread_modifier=0.84,
                                   target_acquisition_ap=0.76,
                                   has_stock=True,
                                   ),
    description='A sturdy adjustable stock designed to provide similar support to a fixed stock'
)

ar_stock_danieldefense = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Daniel Defense Stock",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   felt_recoil=0.59,
                                   ap_distance_cost_modifier=0.76,
                                   handling_spread_modifier=0.89,
                                   ap_to_equip=1.1,
                                   target_acquisition_ap=0.73,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='A collapsing stock by Daniel Defense, light weight and providing a solid cheek rest'
)

ar_stock_prs = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Magpul PRS Stock",
    weight=0.9,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   felt_recoil=0.51,
                                   ap_distance_cost_modifier=0.7,
                                   handling_spread_modifier=0.81,
                                   ap_to_equip=1.22,
                                   target_acquisition_ap=0.79,
                                   has_stock=True,
                                   ),
    description='A precision stock for AR rifles featuring an adjustable cheek rest and butstock'
)

ar_stock_maxim_cqb = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Maxim CQB Stock",
    weight=0.64,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Stock',
                                   felt_recoil=0.7,
                                   ap_distance_cost_modifier=0.81,
                                   handling_spread_modifier=0.93,
                                   target_acquisition_ap=0.68,
                                   ap_to_equip=1.03,
                                   has_stock=True,
                                   pdw_stock=True,
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
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR M16A1 Handguard",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.86,
                                       'handling_spread_modifier': 0.91,
                                       'target_acquisition_ap': 0.82}, ),
    description='Retro M16A1 style handguard for AR rifles')

ar_handguard_m16a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR M16A2 Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.89,
                                       'handling_spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.8}, ),
    description='M16A2 style handguard for AR rifles')

ar_handguard_m16a2_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR M16A2 Carbine Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.77}, ),
    description='Carbine length M16A2 style handguard for AR rifles')

ar_handguard_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Magpul MOE Handguard",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'MLOK Top Mount - Long', 'MLOK Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.91,
                                       'handling_spread_modifier': 0.91,
                                       'target_acquisition_ap': 0.78}, ),
    description='A polymer handguard for AR rifles by Magpul featuring MLOK accessory mounts'
)

ar_handguard_magpul_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Magpul MOE Carbine Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'MLOK Top Mount - Long', 'MLOK Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.84,
                                       'ap_distance_cost_modifier': 0.93,
                                       'handling_spread_modifier': 0.93,
                                       'target_acquisition_ap': 0.76}, ),
    description='A carbine length polymer handguard for AR rifles by Magpul featuring MLOK accessory mounts')

ar_handguard_aero = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Aero Precision Handguard",
    weight=0.31,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   grip_properties={
                                       'felt_recoil': 0.88,
                                       'ap_distance_cost_modifier': 0.89,
                                       'handling_spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.8}, ),
    description='A light weight free floated handguard for AR rifles featuring MLOK accessory mounts')

ar_handguard_aero_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Aero Precision Carbine Handguard",
    weight=0.27,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.89,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.78}, ),
    description='A carbine length light weight free floated handguard for AR rifles featuring MLOK accessory mounts')

ar_handguard_aero_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Aero Precision Pistol Handguard",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   tags=['pistol length covers barrel', 'Handguard'],
                                   grip_properties={
                                       'felt_recoil': 0.89,
                                       'ap_distance_cost_modifier': 0.92,
                                       'handling_spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.76}, ),
    description='A pistol length light weight free floated handguard for AR rifles featuring MLOK accessory mounts')

ar_handguard_faxon = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Faxon Streamline Handguard",
    weight=0.22,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'MLOK Top Mount - Long', 'MLOK Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.9,
                                       'ap_distance_cost_modifier': 0.88,
                                       'handling_spread_modifier': 0.86,
                                       'target_acquisition_ap': 0.81}, ),
    description='A super light weight carbon fibre handguard for AR rifles with MLOK accessory mounts')

ar_handguard_faxon_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Faxon Streamline Carbine Handguard",
    weight=0.21,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'MLOK Top Mount - Long', 'MLOK Optics Mount - Long'],
                                   tags=['carbine length covers barrel', 'Handguard'],
                                   grip_properties={
                                       'felt_recoil': 0.91,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.86,
                                       'target_acquisition_ap': 0.8}, ),
    description='A super light weight carbon fibre carbine length handguard for AR rifles with MLOK accessory mounts')

ar_handguard_faxon_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Faxon Streamline Pistol Handguard",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'MLOK Top Mount - Long', 'MLOK Optics Mount - Long'],
                                   tags=['pistol length covers barrel', 'Handguard'],
                                   grip_properties={
                                       'felt_recoil': 0.92,
                                       'ap_distance_cost_modifier': 0.92,
                                       'handling_spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.78}, ),
    description='A super light weight carbon fibre pistol length handguard for AR rifles with MLOK accessory mounts')

ar_handguard_mk18 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Daniel Defense MK18 Handguard",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['Picrail Side Mount - Long', 'Picrail Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.92,
                                       'handling_spread_modifier': 0.93,
                                       'target_acquisition_ap': 0.78}, ),
    description='A free floated M4 style handguard with picatinny rail mounts by Daniel Defense')

ar10_handguard_a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 A2 Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.89,
                                       'handling_spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.8}),
    description='A2 style handguard for AR-10 rifles')

ar10_handguard_a2_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 M16A2 Carbine Handguard",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.77}),
    description='Carbine length A2 style handguard for AR-10 rifles')

ar10_handguard_wilson = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 Wilson Combat Handguard",
    weight=0.41,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.89,
                                       'ap_distance_cost_modifier': 0.88,
                                       'handling_spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.84}),
    description='A light weight aluminium free floated handguard for AR-10 rifles featuring MLOK accessory mounts')

ar_handguard_wilson_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 Wilson Combat Carbine Handguard",
    weight=0.32,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.9,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.82}),
    description='A carbine length light weight aluminium free floated handguard for AR-10 rifles featuring MLOK '
                'accessory mounts')

ar10_handguard_vseven = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 V Seven Hyper-Light Handguard",
    weight=0.21,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.92,
                                       'ap_distance_cost_modifier': 0.87,
                                       'handling_spread_modifier': 0.85,
                                       'target_acquisition_ap': 0.82}),
    description='A super light weight lithium-aluminium alloy AR-10 handguard with M-LOK attachment points')

ar_handguard_vseven_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 V Seven Hyper-Light Carbine Handguard",
    weight=0.18,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.92,
                                       'ap_distance_cost_modifier': 0.88,
                                       'handling_spread_modifier': 0.86,
                                       'target_acquisition_ap': 0.8}),
    description='A super light weight carbine length lithium-aluminium alloy AR-10 '
                'handguard with M-LOK attachment points')

ar_handguard_vseven_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 V Seven Hyper-Light Pistol Handguard",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   tags=['pistol length covers barrel', 'Handguard'],
                                   grip_properties={
                                       'felt_recoil': 0.9,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.77}),
    description='A super light weight pistol length lithium-aluminium alloy AR-10 handguard with M-LOK '
                'attachment points'
)

ar_handguard_hera_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 HERA Arms IRS Handguard",
    weight=0.65,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['Picrail Side Mount - Long', 'Picrail Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.82,
                                       'ap_distance_cost_modifier': 0.92,
                                       'handling_spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.82}),
    description='A carbine length light weight aluminium free floated handguard for AR-10 rifles '
                'featuring picatinny rail accessory mounts'
)

ar_handguard_atlas_carbine = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 Brigand Arms Atlas Carbine Handguard",
    weight=0.22,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['Picrail Side Mount - Long', 'Picrail Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.94,
                                       'ap_distance_cost_modifier': 0.86,
                                       'handling_spread_modifier': 0.86,
                                       'target_acquisition_ap': 0.81}),
    description='A carbon-fibre and aluminium carbine AR10 handguard with a wire frame appearance featuring picatinny '
                'rail attachment points')

ar_handguard_atlas_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR-10 Brigand Arms Atlas Pistol Handguard",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', ],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['Picrail Side Mount - Long', 'Picrail Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.95,
                                       'ap_distance_cost_modifier': 0.87,
                                       'handling_spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.78}),
    description='A carbon-fibre and aluminium pistol AR10 handguard with a wire frame appearance featuring picatinny'
                ' rail attachment points')

ar_handguard_pcc_mlok = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="4 Inch AR Pistol Handguard - MLOK",
    weight=0.188,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', 'pistol length covers barrel'],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['MLOK Side Mount - Short', 'MLOK Underbarrel - Short',
                                                              'Picrail Top Mount - Short',
                                                              'Picrail Optics Mount - Short'],
                                   grip_properties={
                                       'felt_recoil': 0.93,
                                       'ap_distance_cost_modifier': 0.96,
                                       'handling_spread_modifier': 0.94,
                                       'target_acquisition_ap': 0.8}, ),
    description='An aluminium 4 inch AR pistol handguard featuring a picatinny top rail as well as MLOK attachment '
                'points')

ar_handguard_pcc_quadrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="4 Inch AR Pistol Handguard - Quad Rail",
    weight=0.217,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Handguard',
                                   tags=['Handguard', 'pistol length covers barrel'],
                                   optic_mount_properties={'receiver_height_above_bore': 1.11,
                                                           'handling_spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   is_attachment_point_types=['Picrail Side Mount - Short',
                                                              'Picrail Underbarrel - Short',
                                                              'Picrail Top Mount - Short',
                                                              'Picrail Optics Mount - Short'],
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.96,
                                       'handling_spread_modifier': 0.97,
                                       'target_acquisition_ap': 0.82}, ),
    description='An aluminium 4 inch AR pistol handguard featuring a picatinny rail attachment poitns')

"""
Pistol Grip
"""

ar_grip_trybe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR TRYBE Defense Grip",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   target_acquisition_ap=0.9,
                                   felt_recoil=0.94,
                                   ),
    description='An aluminium skeletonised pistol grip for AR rifles'
)

ar_grip_moe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Magpul MOE Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   felt_recoil=0.9,
                                   target_acquisition_ap=0.95,
                                   ),
    description='A polymer pistol grip for AR rifles by Magpul'
)

ar_grip_hogue = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Hogue Rubber Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   felt_recoil=0.88,
                                   target_acquisition_ap=0.98,
                                   ),
    description='An ergonomic rubberised grip for AR rifles'
)

ar_grip_strikeforce = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR ATI Outdoors Strikeforce Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   felt_recoil=0.97,
                                   ap_distance_cost_modifier=0.96,
                                   handling_spread_modifier=0.96,
                                   ),
    description='An ergonomic rubberised grip by ATI outdoors for AR rifles'
)

ar_grip_a2 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR A2 Grip",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   felt_recoil=0.92,
                                   target_acquisition_ap=0.93,
                                   ),
    description='An A2 style polymer pistol grip for AR rifles '
)

ar_grip_stark = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Stark Grip",
    weight=0.09,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Grip',
                                   felt_recoil=0.88,
                                   handling_spread_modifier=0.95,
                                   ),
    description='An ergonomic pistol grip for AR rifles by Stark Equipment'
)

"""
Buffer Assembly
"""

"""AR 15"""

ar15_buffer_tube = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 Buffer Tube - Standard",
    weight=0.125,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer Tube',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-15', ]},
                                   functional_part=True),
    description='Buffer tube for AR15 type rifles.'
)

ar15_buffer = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 Buffer - Standard",
    weight=0.085,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-15', ]},
                                   functional_part=True),
    description='Standard buffer for AR15 type rifles.'
)

ar15_buffer_heavy = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 MGI Rate and Recoil Reducing Buffer",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-15', ]},
                                   fire_rate_modifier=0.857,
                                   felt_recoil=0.93,
                                   functional_part=True
                                   ),
    description='Heavy buffer for AR-15 type rifles.'
)

ar15_buffer_light = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 KAK Lightweight Buffer",
    weight=0.062,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-15', ]},
                                   fire_rate_modifier=1.078,
                                   felt_recoil=1.05,
                                   functional_part=True
                                   ),
    description='A light-weight AR-15 buffer.'
)

"""AR 10"""

ar10_buffer_tube = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR10 Buffer Tube - Standard",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer Tube',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-10', ]},
                                   functional_part=True),
    description='Buffer tube for AR15 type rifles.'
)

ar10_buffer = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR10 Buffer Assembly - Standard",
    weight=0.147,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-10', ]},
                                   functional_part=True
                                   ),
    description='Standard buffer assembly for AR10 type rifles'
)

ar10_buffer_heavy = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR10 MGI Rate and Recoil Reducing Buffer",
    weight=0.22,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-10', ]},
                                   fire_rate_modifier=0.857,
                                   felt_recoil=0.93,
                                   functional_part=True
                                   ),
    description='Buffer assembly for AR15 type rifles featuring a heavier buffer'
)

ar10_buffer_light = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR10 ODIN Works Lightweight Buffer",
    weight=0.098,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Buffer',
                                   compatible_parts={'AR Lower Receiver': ['Lower AR-10', ]},
                                   fire_rate_modifier=1.078,
                                   felt_recoil=1.05,
                                   functional_part=True
                                   ),
    description='Buffer assembly for AR15 type rifles featuring a light-weight buffer'
)

"""
Muzzle Devices
"""

# 5.56

ar15_muzzle_flashhider = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5.56x45 A2 Flash Hider",
    weight=0.064,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 1/2x28 - .223',),
                                   muzzle_break_efficiency=0.11,
                                   ),
    description="Flash hider designed for AR15 type 5.56x45 rifles"
)

ar15_muzzle_st6012 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5.56x45 ST-6012 Muzzle Brake",
    weight=0.125,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 1/2x28 - .223',),
                                   muzzle_break_efficiency=0.5,
                                   sound_radius=1.12,
                                   ),
    description="Muzzle brake designed for AR15 type 5.56x45 rifles designed by bulletec"
)

ar15_muzzle_mi_mb4 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5.56x45 MI-MB4 Muzzle Brake",
    weight=0.085,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 1/2x28 - .223',),
                                   muzzle_break_efficiency=0.18,
                                   sound_radius=1.05,
                                   ),
    description="A small two chamber muzzle brake designed for AR15 type 5.56x45 rifles designed by Midwest Industries"
)

ar15_muzzle_cobra = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5.56x45 Cobra Billet Muzzle Brake",
    weight=0.124,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 1/2x28 - .223',),
                                   muzzle_break_efficiency=0.55,
                                   sound_radius=1.16,
                                   ),
    description="A large muzzle brake designed for AR15 type 5.56x45 rifles designed by Jacob Grey Firearms"
)

# .300 blackout / .308

ar15_300_muzzle_flashhider = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5/8x24 A2 Flash Hider",
    weight=0.053,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 5/8x24',),
                                   muzzle_break_efficiency=0.11,
                                   sound_radius=1.03,
                                   ),
    description="Flash hider designed for AR15/AR10 type rifles designed by Diamondback Firearms"
)

ar15_300_muzzle_cobra = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5/8x24 Cobra Billet Muzzle Brake",
    weight=0.124,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 5/8x24',),
                                   muzzle_break_efficiency=0.55,
                                   sound_radius=1.16,
                                   ),
    description="A large muzzle brake designed for AR15/AR10 type rifles designed by Jacob Grey Firearms"
)

ar15_300_muzzle_pegasus = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5/8x24 Pegasus Muzzle Brake",
    weight=0.189,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 5/8x24',),
                                   muzzle_break_efficiency=0.58,
                                   sound_radius=1.13,
                                   ),
    description="A large muzzle brake designed for AR15/AR10 type rifles designed by Ultradyne USA"
)

ar15_300_muzzle_strike = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR15 5/8x24 King Muzzle Brake",
    weight=0.097,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread 5/8x24',),
                                   muzzle_break_efficiency=0.41,
                                   sound_radius=1.17,
                                   ),
    description="A muzzle brake/compensator designed for AR15/AR10 type rifles designed by Strike Industries"
)

"""
Other
"""

ar_front_sight = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR A2 Front Sight",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='Front Sight',
                                   incompatibilities=(('full length barrel', 'full length covers barrel'),
                                                      ('carbine length barrel', 'carbine length covers barrel'),
                                                      ('pistol length barrel', 'pistol length covers barrel'),),
                                   compatible_parts={'AR Barrel': ['AR Barrel', ]},
                                   ),

    description='An M16A2-style front sight for AR type rifles')

ar_carry_handle = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Carry Handle Sight",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Carry Handle Attachment', 'Iron Sight'],
                                   additional_required_parts=('Front Sight',),
                                   ap_to_equip=1.04,
                                   attachment_point_required=('Picrail Optics Mount - Long',),
                                   # keys: mount type, values: accessory type
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   optic_mount_properties={'receiver_height_above_bore': 1.4},
                                   optic_properties={'target_acquisition_ap': 1.03,
                                                     'ap_distance_cost_modifier': 0.96,
                                                     'sight_spread_modifier': 0.02,
                                                     'zero_range': 25, },
                                   ),
    description='Carry handle rear sight intended for AR-15 type rifles.')

carry_handle_optic_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="AR Carry Handle Optics Mount",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='AR Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Short', ],
                                   additional_required_parts=('Optic',),
                                   incompatibilities=(('Carry Handle Attachment',),),
                                   optic_mount_properties={'receiver_height_above_bore': 0.2,
                                                           'handling_spread_modifier': 1.03,
                                                           'target_acquisition_ap': 0.95},
                                   ),
    description='Picatinny rail optics mount for AR type carry handle rear iron sights.')

ar15 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="AR",
    weight=1,
    stacking=None,
    description='The AR-15 rifle was first developed by the American company ArmaLite in the late 1950s as a '
                'lightweight and versatile rifle for military use. It was designed by Eugene Stoner and was later '
                'adopted by the United States military as the M16 rifle. The M16 saw widespread use during the '
                'Vietnam War and has since become one of the most iconic rifles in American military history.',
    usable_properties=GunMagFed(
        compatible_magazine_type=('STANAG', ),
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=100,
        current_fire_mode='single shot',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        parts=Parts(),
        compatible_bullet_type=('5.56x45',),
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0,
        sight_height_above_bore=0,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        barrel_length=20,
        gun_type='rifle',
        action_type='semi-auto rifle',
    ))

upper_mcr = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="MCR-060 Upper Assembly",
    weight=3.316,
    stacking=None,
    usable_properties=GunComponent(part_type='MCR Upper',
                                   is_attachment_point_types=['Picrail Optics Mount - Long',
                                                              'Barrel Thread 1/2x28 - .223', 'Picrail Side Mount - Long',
                                                              'Picrail Underbarrel - Long',
                                                              'Picrail Top Mount - Long',
                                                              'Picrail Optics Mount - Long'],
                                   optic_mount_properties={'receiver_height_above_bore': 2.25},
                                   optic_properties={'target_acquisition_ap': 1.03,
                                                     'ap_distance_cost_modifier': 0.96,
                                                     'sight_spread_modifier': 0.02,
                                                     'sight_height_above_bore': 0.75,
                                                     'zero_range': 25, },
                                   accuracy_part=True,
                                   functional_part=True,
                                   compatible_bullet_type=('5.56x45',),
                                   velocity_modifier={'5.56x45': 0.921},
                                   target_acquisition_ap=0.96,
                                   compatible_magazine_type=('STANAG', 'MCR Linked Ammunition Magazine'),
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.92,
                                       'handling_spread_modifier': 0.93,
                                       'target_acquisition_ap': 0.78},
                                   ),
    description="Short-stroke gas piston operated belt-fed and magazine fed 5.56x45 upper assembly designed by "
                "FightLite compatible with AR-15 lower recievers. Can feed both from STANAG magazines and "
                "M27 linked ammunition. Complete with picatinny rail handguard and 16.25 inch barrel."
)

fightlite_mcr = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="MCR",
    weight=1,
    stacking=None,
    description="Originally developed as the Ares Shrike in 2002, the MCR is a short-stroke gas piston operated "
                "belt-fed and magazine fed 5.56x45 upper assembly designed by FightLite compatible with AR-15 lower"
                " recievers. Can feed both from STANAG magazines and M27 linked ammunition.",
    usable_properties=GunMagFed(
        compatible_magazine_type=('STANAG', 'MCR Linked Ammunition Magazine'),
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        fire_rate_modifier=1.1428,
        ap_to_equip=100,
        current_fire_mode='single shot',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        parts=Parts(),
        compatible_bullet_type=('5.56x45',),
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0,
        sight_height_above_bore=0,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        barrel_length=16.25,
        gun_type='rifle',
        action_type='belt fed',
    ))
