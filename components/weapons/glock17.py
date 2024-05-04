from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

glock17_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock Frame",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Standard Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['Picrail Underbarrel - Short', ],
                                   functional_part=True,
                                   ),
    description='Standard Glock frame compatible with Glock 17, 17L, 22 and 24 slides and barrels'
)

glock20_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock Large Frame",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['Picrail Underbarrel - Short', ],
                                   functional_part=True,
                                   ),
    description='Standard Glock frame compatible with 10mm slides and barrels'
)

"""
BARRELS
"""

glock_9in_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="9 inch Glock 9mm Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   suffix='Long Barrel',
                                   velocity_modifier={'9mm': 1.131},
                                   compatible_parts={'G17 Slide': ['Glock 17L Slide', 'Glock 17L Custom Slide',
                                                                   'Glock 17 Slide', 'Glock 17 Custom Slide',
                                                                   "Glock 17 Slide w/ Optics Cut",
                                                                   "Glock 17L Slide w/ Optics Cut"]},
                                   barrel_length=9,
                                   target_acquisition_ap=1.05,
                                   ap_to_equip=1.05,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Extra long 9 inch Glock 9mm barrel'
)

glock_9in_barrel_10mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="9 inch Glock 10mm Barrel",
    weight=0.227,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   suffix='Long Barrel',
                                   velocity_modifier={'10mm': 1.077},
                                   compatible_parts={
                                       'Glock 10mm Slide': ['Glock 40 Slide', "Glock 40 Slide w/ Optics Cut",
                                                            'Glock 40 Custom Slide', 'Glock 20 Slide',
                                                            "Glock 20 Slide w/ Optics Cut",
                                                            'Glock 20 Custom Slide']},
                                   barrel_length=9,
                                   target_acquisition_ap=1.05,
                                   ap_to_equip=1.05,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Extra long 9 inch Glock 10mm barrel'
)

glock17_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17 Barrel",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   compatible_parts={
                                       'G17 Slide': ['Glock 17 Slide', "Glock 17 Slide w/ Optics Cut",
                                                     'Glock 17 Custom Slide']},
                                   barrel_length=4.49,
                                   velocity_modifier={'9mm': 1.033},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Standard 4.49 inch Glock 17 barrel'
)

glock17l_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17L Barrel",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   velocity_modifier={'9mm': 1.0859},
                                   compatible_parts={'G17 Slide': ['Glock 17L Slide', 'Glock 17L Custom Slide',
                                                                   'Glock 17 Slide', 'Glock 17 Custom Slide',
                                                                   "Glock 17 Slide w/ Optics Cut",
                                                                   "Glock 17L Slide w/ Optics Cut"]},
                                   barrel_length=6.02,
                                   target_acquisition_ap=1.03,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Glock 17L barrel. Longer than the standard Glock 17 barrel, at 6.02 inches.'
)

glock20_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 20 Barrel",
    weight=0.122,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Barrel',
                                   compatible_parts={
                                       'Glock 10mm Slide': ['Glock 20 Slide', "Glock 20 Slide w/ Optics Cut",
                                                            'Glock 20 Custom Slide']},
                                   barrel_length=4.6,
                                   compatible_bullet_type=('10mm',),
                                   velocity_modifier={'10mm': 0.99},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Standard 4.6 inch Glock 20 barrel'
)

glock40_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 40 Barrel",
    weight=0.19,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Barrel',
                                   compatible_parts={
                                       'Glock 10mm Slide': ['Glock 40 Slide', "Glock 40 Slide w/ Optics Cut",
                                                            'Glock 40 Custom Slide', 'Glock 20 Slide',
                                                            "Glock 20 Slide w/ Optics Cut",
                                                            'Glock 20 Custom Slide']},
                                   barrel_length=6.02,
                                   target_acquisition_ap=1.03,
                                   compatible_bullet_type=('10mm',),
                                   velocity_modifier={'10mm': 1.0318},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Standard 6.02 inch Glock 40 barrel'
)

glock22_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 22 Barrel",
    weight=0.10,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Barrel',
                                   compatible_bullet_type=('40 S&W',),
                                   compatible_parts={
                                       'Glock .40 S&W Slide': ['Glock 22 Slide', "Glock 22 Slide w/ Optics Cut",
                                                               'Glock 22 Custom Slide']},
                                   barrel_length=4.49,
                                   velocity_modifier={'40 S&W': 1.03},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Standard 4.6 inch Glock 20 barrel'
)

glock24_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 24 Barrel",
    weight=0.122,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Barrel',
                                   compatible_parts={
                                       'Glock .40 S&W Slide': ['Glock 24 Slide', "Glock 24 Slide w/ Optics Cut",
                                                               'Glock 24 Custom Slide', 'Glock 22 Slide',
                                                               "Glock 22 Slide w/ Optics Cut",
                                                               'Glock 22 Custom Slide']},
                                   barrel_length=6.02,
                                   compatible_bullet_type=('40 S&W',),
                                   velocity_modifier={'40 S&W': 1.0806},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Standard 6.02 inch Glock 24 barrel'
)

# TODO - adjust length of threaded barrels, add 6 inch 50 GI barrelo

#
# glock17_barrel_threaded = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock 17 Threaded Barrel",
#     weight=0.11,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Glock 17 Barrel',
#                                    is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
#                                    compatible_parts={
#                                        'G17 Slide': ['Glock 17 Slide', "Glock 17 Slide w/ Optics Cut",
#                                                      'Glock 17 Custom Slide']},
#                                    barrel_length=4.49,
#                                    velocity_modifier={'9mm': 1.033},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    short_barrel=True
#                                    ),
#     description='Standard 4.49 inch Glock 17 barrel. It has been threaded to accept muzzle devices.'
# )
#
# glock17l_barrel_threaded = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock 17L Threaded Barrel",
#     weight=0.11,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Glock 17 Barrel',
#                                    velocity_modifier={'9mm': 1.0859},
#                                    is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
#                                    compatible_parts={'G17 Slide': ['Glock 17L S``lide', 'Glock 17L Custom Slide',
#                                                                    'Glock 17 Slide', 'Glock 17 Custom Slide',
#                                                                    "Glock 17 Slide w/ Optics Cut",
#                                                                    "Glock 17L Slide w/ Optics Cut"]},
#                                    barrel_length=6.02,
#                                    target_acquisition_ap=1.03,
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    short_barrel=True
#                                    ),
#     description='Glock 17L barrel. Longer than the standard Glock 17 barrel, at 6.02 inches. '
#                 'It has been threaded to accept muzzle devices.'
# )
#
# glock20_barrel_threaded = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock 20 Threaded Barrel",
#     weight=0.122,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Glock 10mm Barrel',
#                                    is_attachment_point_types=['Barrel Thread 9/16x24', ],
#                                    compatible_parts={
#                                        'Glock 10mm Slide': ['Glock 20 Slide', "Glock 20 Slide w/ Optics Cut",
#                                                      'Glock 20 Custom Slide']},
#                                    barrel_length=4.6,
#                                    velocity_modifier={'10mm': 0.99},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    short_barrel=True
#                                    ),
#     description='Standard 4.6 inch Glock 20 barrel. It has been threaded to accept muzzle devices.'
# )
#
# glock40_barrel_threaded = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock 40 Threaded Barrel",
#     weight=0.19,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Glock 17 Barrel',
#                                    is_attachment_point_types=['Barrel Thread 9/16x24', ],
#                                    compatible_parts={
#                                        'Glock 10mm Slide': ['Glock 40 Slide', "Glock 40 Slide w/ Optics Cut",
#                                                      'Glock 40 Custom Slide', 'Glock 20 Slide',
#                                                             "Glock 20 Slide w/ Optics Cut",
#                                                      'Glock 20 Custom Slide']},
#                                    barrel_length=6.02,
#                                    target_acquisition_ap=1.03,
#                                    velocity_modifier={'10mm': 1.0318},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    short_barrel=True
#                                    ),
#     description='Standard 6.02 inch Glock 40 barrel. It has been threaded to accept muzzle devices.'
# )
#
# glock22_barrel_threaded = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock 22 Threaded Barrel",
#     weight=0.10,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Glock .40 S&W Barrel',
#                                    is_attachment_point_types=['Barrel Thread 9/16x24', ],
#                                    compatible_parts={
#                                        'Glock .40 S&W Slide': ['Glock 22 Slide', "Glock 22 Slide w/ Optics Cut",
#                                                      'Glock 22 Custom Slide']},
#                                    barrel_length=4.49,
#                                    velocity_modifier={'40 S&W': 1.03},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    short_barrel=True
#                                    ),
#     description='Standard 4.6 inch Glock 20 barrel. It has been threaded to accept muzzle devices.'
# )
#
# glock24_barrel_threaded = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock 24 Threaded Barrel",
#     weight=0.122,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Glock .40 S&W Barrel',
#                                    is_attachment_point_types=['Barrel Thread 9/16x24', ],
#                                    compatible_parts={
#                                        'Glock .40 S&W Slide': ['Glock 24 Slide', "Glock 24 Slide w/ Optics Cut",
#                                                      'Glock 24 Custom Slide', 'Glock 22 Slide',
#                                                                "Glock 22 Slide w/ Optics Cut",
#                                                      'Glock 22 Custom Slide']},
#                                    barrel_length=6.02,
#                                    velocity_modifier={'40 S&W': 1.0806},
#                                    functional_part=True,
#                                    accuracy_part=True,
#                                    short_barrel=True
#                                    ),
#     description='Standard 6.02 inch Glock 24 barrel. It has been threaded to accept muzzle devices.'
# )

"""
G40
overall weight - 0.91852455
weight of slide - 0.57492833
weight of slide + barrel + spring - 0.765437124

weight of frame - 0.153 kg
weight of barrel + spring  - 0.190 kg

G20
overall weight - 0.765437124
weight of frame - 0.153 kg

50 GI slide + barrel - 0.64636913 kg
slide estimate - 0.485 kg
barrel estimate - 0.161

slide / barrel ratio - 4.016
weight of slide w/o barrel and spring - 0.4904468 
weight of barrel and spring - 0.122
"""

"""
G22 
overall weight - 0.645  
weight of slide - 0.40
weight of barrel - 0.104893
weight of frame - 0.15 


G24
overall weight - 0.760
weight of slide - 0.49
weight of barrel - 0.122 
weight of frame - 0.15 
"""

glock50_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock .50 Barrel",
    weight=0.161,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .50 GI Barrel',
                                   barrel_length=4.6,
                                   velocity_modifier={'.50 GI': 1.0},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='4.6 inch .50 GI Glock barrel'
)

glock50_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock .50 Ported Barrel",
    weight=0.161,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .50 GI Barrel',
                                   barrel_length=4.6,
                                   muzzle_break_efficiency=0.4,
                                   velocity_modifier={'.50 GI': 1.0},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='4.6 inch .50 GI Glock barrel'
)

"""
BARRELS - PORTED
"""

glock17_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17 Ported Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   velocity_modifier={'9mm': 1.033},
                                   compatible_parts={'G17 Slide': ['Glock 17 Custom Slide']},
                                   barrel_length=4.49,
                                   prevents_suppression=True,
                                   muzzle_break_efficiency=0.4,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Glock 17 barrel with milled cutouts to reduce muzzle climb'
)

glock17l_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17L Ported Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   velocity_modifier={'9mm': 1.0859},
                                   compatible_parts={'G17 Slide': ['Glock 17L Custom Slide',
                                                                   'Glock 17 Custom Slide']},
                                   barrel_length=6.02,
                                   prevents_suppression=True,
                                   muzzle_break_efficiency=0.4,
                                   target_acquisition_ap=1.03,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Glock 17L barrel with milled cutouts to reduce muzzle climb'
)

glock20_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 20 Ported Barrel",
    weight=0.112,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'Glock 10mm Slide': ['Glock 20 Custom Slide']},
                                   barrel_length=4.6,
                                   muzzle_break_efficiency=0.4,
                                   compatible_bullet_type=('10mm',),
                                   velocity_modifier={'10mm': 0.99},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Glock 20 barrel with milled cutouts to reduce muzzle climb'
)

glock40_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 40 Ported Barrel",
    weight=0.18,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'Glock 10mm Slide': ['Glock 20 Custom Slide', 'Glock 40 Custom Slide']},
                                   barrel_length=6.02,
                                   target_acquisition_ap=1.03,
                                   muzzle_break_efficiency=0.4,
                                   compatible_bullet_type=('10mm',),
                                   velocity_modifier={'10mm': 1.0318},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Glock 40 barrel with milled cutouts to reduce muzzle climb'
)

glock22_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 22 Ported Barrel",
    weight=0.10,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'Glock .40 S&W Slide': ['Glock 22 Custom Slide']},
                                   barrel_length=4.49,
                                   muzzle_break_efficiency=0.4,
                                   compatible_bullet_type=('40 S&W', ),
                                   velocity_modifier={'40 S&W': 1.03},
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Glock 20 barrel with milled cutouts to reduce muzzle climb'
)

glock24_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 24 Ported Barrel",
    weight=0.122,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   muzzle_break_efficiency=0.4,
                                   compatible_parts={
                                       'Glock .40 S&W Slide': ['Glock 22 Custom Slide', 'Glock 24 Custom Slide']},
                                   barrel_length=6.02,
                                   velocity_modifier={'40 S&W': 1.0806},
                                   compatible_bullet_type=('40 S&W',),
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Glock 24 barrel with milled cutouts to reduce muzzle climb'
)

"""
SLIDES
"""

glock17_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17 Slide",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='G17 Slide',
                                   suffix='17',
                                   compatible_magazine_type=('Glock 9mm',),
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 17 slide'
)

glock17l_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17L Slide",
    weight=0.374,
    stacking=None,
    usable_properties=GunComponent(part_type='G17 Slide',
                                   compatible_magazine_type=('Glock 9mm',),
                                   suffix='17L',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Glock 17L slide. Longer than the standard Glock 17 slide'
)

glock22_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 22 Slide",
    weight=0.40,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Slide',
                                   suffix='22',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 22 slide'
)

glock24_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 24 Slide",
    weight=0.49,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Slide',
                                   suffix='24',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 24 slide'
)

glock17_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17 Slide w/ Optics Cut",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='G17 Slide',
                                   suffix='17',
                                   compatible_magazine_type=('Glock 9mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True
                                   ),
    description='Glock 17 slide, machined to allow the mounting of optics such as RMRs'
)

glock17l_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17L Slide w/ Optics Cut",
    weight=0.374,
    stacking=None,
    usable_properties=GunComponent(part_type='G17 Slide',
                                   suffix='17L',
                                   compatible_magazine_type=('Glock 9mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True
                                   ),
    description='Glock 17L slide, machined to allow the mounting of optics such as RMRs. Longer than the standard '
                'Glock 17 slide'
)

glock22_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 22 Slide w/ Optics Cut",
    weight=0.40,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Slide',
                                   suffix='22',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 22 slide'
)

glock24_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 24 Slide w/ Optics Cut",
    weight=0.49,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Slide',
                                   suffix='24',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 24 slide'
)

glock17_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17 Custom Slide",
    weight=0.285,
    stacking=None,
    usable_properties=GunComponent(part_type='G17 Slide',
                                   suffix='17 Custom',
                                   compatible_magazine_type=('Glock 9mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True
                                   ),
    description='Custom milled Glock 17 slide, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

glock17l_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 17L Custom Slide",
    weight=0.299,
    stacking=None,
    usable_properties=GunComponent(part_type='G17 Slide',
                                   suffix='17L Custom',
                                   compatible_magazine_type=('Glock 9mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True
                                   ),
    description='Custom milled Glock 17L slide, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

glock22_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 22 Custom Slide",
    weight=0.319,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Slide',
                                   suffix='22 Custom',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Custom milled Glock 22 slide, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

glock24_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 24 Custom Slide",
    weight=0.391,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .40 S&W Slide',
                                   suffix='24 Custom',
                                   compatible_magazine_type=('Glock .40 S&W',),
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Custom milled Glock 24 slide, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

glock50_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name=".50 GI Glock Slide",
    weight=0.49,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .50 Slide',
                                   suffix='.50 GI',
                                   compatible_magazine_type=('Glock .50 GI',),
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A slide designed by Guncrafter Industries compatible with large frame Glock pistols, converting it '
                'fire the specialised .50 GI cartridge when combined with an appropriate barrel'
)

glock50_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name=".50 GI Glock Slide w/ Optics Cut",
    weight=0.49,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .50 Slide',
                                   suffix='.50 GI',
                                   compatible_magazine_type=('Glock .50 GI',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A slide designed by Guncrafter Industries compatible with large frame Glock pistols, converting it '
                'fire the specialised .50 GI cartridge when combined with an appropriate barrel. It has been machined '
                'to allow the mounting of optics such as RMRs.'
)

glock50_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name=".50 GI Glock Custom Slide",
    weight=0.391,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock .50 Slide',
                                   suffix='.50 GI',
                                   compatible_magazine_type=('Glock .50 GI',),
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A slide designed by Guncrafter Industries compatible with large frame Glock pistols, converting it '
                'fire the specialised .50 GI cartridge when combined with an appropriate barrel. It has been custom '
                'milled, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

glock20_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 20 Slide",
    weight=0.49,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Slide',
                                   suffix='20',
                                   compatible_magazine_type=('Glock 10mm',),
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 20 slide'
)

glock20_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 20 Slide w/ Optics Cut",
    weight=0.49,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Slide',
                                   suffix='20',
                                   compatible_magazine_type=('Glock 10mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 20 slide, machined to allow the mounting of optics such as RMRs'
)

glock20_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 20 Custom Slide",
    weight=0.392,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Slide',
                                   suffix='20 Custom',
                                   compatible_magazine_type=('Glock 10mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Custom milled Glock 20 slide, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

glock40_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 40 Slide",
    weight=0.575,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Slide',
                                   suffix='40 Custom',
                                   compatible_magazine_type=('Glock 10mm',),
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 40 slide'
)

glock40_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 40 Slide w/ Optics Cut",
    weight=0.575,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Slide',
                                   suffix='40',
                                   compatible_magazine_type=('Glock 10mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard Glock 40 slide, machined to allow the mounting of optics such as RMRs.'
)

glock40_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock 40 Custom Slide",
    weight=0.46,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 10mm Slide',
                                   suffix='40 Custom',
                                   compatible_magazine_type=('Glock 10mm',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Custom milled Glock 40 slide, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

"""
OTHER PARTS
"""

glock_switch = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock Auto Switch",
    weight=0.03,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Base Plate',
                                   prefix='Automatic',
                                   fire_modes={'automatic': {'fire rate': 1200, 'automatic': True}}, ),
    description='Modifed Glock slide base plate enabling automatic fire'
)

# glock_9mm_compensator = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock 9mm Compensator",
#     weight=0.14,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Muzzle Device',
#                                    attachment_point_required=('Barrel Thread M13.5x1 LH',),
#                                    muzzle_break_efficiency=0.26,
#                                    target_acquisition_ap=1.01,
#                                    sound_radius=1.1,
#                                    ),
#     description='A large compensator for Glock 9mm pistols'
# )
#
# glock_40sw_compensator = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Glock .40 S&W / 10mm Micro Compensator",
#     weight=0.056699,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Muzzle Device',
#                                    attachment_point_required=('Barrel Thread 9/16x24',),
#                                    muzzle_break_efficiency=0.23,
#                                    sound_radius=1.06,
#                                    ),
#     description='A small compensator / muzzle brake for Glock .40 S&W and 10mm pistols'
# )

# FAB defense glock cobra stock
glock_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock Cobra Stock",
    weight=0.328,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   suffix='PDW',
                                   felt_recoil=0.79,
                                   ap_to_equip=1.2,
                                   ap_distance_cost_modifier=0.71,
                                   handling_spread_modifier=0.9,
                                   target_acquisition_ap=0.76,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='A folding stock for Glock pistols'
)

# FAB defense GIS
glock_pic_rail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Glock Picatinny Sight Mount",
    weight=0.056,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Short', ],
                                   additional_required_parts=['Optic', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.49},
                                   ),
    description='An aftermarket picatinny rail sight mount for Glock handguns'
)

glock_pistol_brace = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Flux Defense Glock Pistol Brace",
    weight=0.51,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   suffix='PDW',
                                   felt_recoil=0.83,
                                   ap_to_equip=1.14,
                                   ap_distance_cost_modifier=0.76,
                                   handling_spread_modifier=0.94,
                                   target_acquisition_ap=0.71,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='Collapsing pistol brace for Glock standard frame handguns designed by Flux Defense'
)

glock_brace_rt = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Recover Tactical 20/21 Glock Pistol Brace",
    weight=0.72,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   suffix='PDW',
                                   felt_recoil=0.84,
                                   ap_to_equip=1.14,
                                   ap_distance_cost_modifier=0.73,
                                   handling_spread_modifier=0.94,
                                   target_acquisition_ap=0.68,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='Folding pistol brace for Glock 20 and 40 handguns designed by Recover Tactical'
)

# # SF Ryder 9M
# suppressor_surefire_9mm = Item(
#     x=0, y=0,
#     char="!",
#     fg_colour=colour.LIGHT_MAGENTA,
#     name="Surefire 9mm Suppressor",
#     weight=0.255,
#     stacking=None,
#     usable_properties=GunComponent(part_type='Muzzle Device',
#                                    suffix='Suppressed',
#                                    attachment_point_required=('Barrel Thread M13.5x1 LH',),
#                                    muzzle_break_efficiency=0.3,
#                                    target_acquisition_ap=1.04,
#                                    fire_rate_modifier=1.1,
#                                    is_suppressor=True,
#                                    sound_radius=0.3,
#                                    ),
#     description='A slim titanium suppressor by surefire for M13.5x1 LH barrel threading'
# )

glock_17 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock",
    weight=0.62,
    stacking=None,
    description='The Glock is a striker fired handgun that was designed in the early 1980s by Austrian engineer '
                'Gaston Glock. It was originally developed for military use, but quickly gained popularity in the '
                'civilian market due to its lightweight and reliable design.',
    usable_properties=GunMagFed(
        compatible_magazine_type=('Glock 9mm',),
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=100,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        current_fire_mode='single shot',
        parts=Parts(),
        velocity_modifier={'9mm': 1.0, 'single projectile': 1.0},
        compatible_bullet_type=('9mm',),
        felt_recoil=1.0,
        receiver_height_above_bore=0.46,  # TODO - glock 20 and 22 height above bore
        sight_height_above_bore=0.08,
        sound_modifier=1.0,
        zero_range=25,
        target_acquisition_ap=30,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        gun_type='pistol',
        action_type='semi-auto pistol',
        barrel_length=4.49
    )
)

glock17dict = {
    "guns": {
        "pistols": {
            "Glock 17": {
                "required parts": {
                    "Glock Standard Frame": 1,
                    "Glock 17 Barrel": 1,
                    "G17 Slide": 1,
                },
                "compatible parts": {
                    "Glock Stock": 1,
                    "Muzzle Adapter": 1,
                    "Glock Optics Mount": 1,
                    "Glock Base Plate": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": glock_17
            },
        }
    },
}

glock40swdict = {
    "guns": {
        "pistols": {
            "Glock .40 S&W": {
                "required parts": {
                    "Glock Standard Frame": 1,
                    "Glock .40 S&W Barrel": 1,
                    "Glock .40 S&W Slide": 1,
                },
                "compatible parts": {
                    "Glock Stock": 1,
                    "Glock Optics Mount": 1,
                    "Glock Base Plate": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": glock_17
            },
        }
    },
}

glock10mmdict = {
    "guns": {
        "pistols": {
            "Glock 20/40": {
                "required parts": {
                    "Glock 10mm Frame": 1,
                    "Glock 10mm Barrel": 1,
                    "Glock 10mm Slide": 1,
                },
                "compatible parts": {
                    "Muzzle Adapter": 1,
                    "Glock Base Plate": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": glock_17
            },
        }
    },
}

glock50gidict = {
    "guns": {
        "pistols": {
            "Glock .50 GI": {
                "required parts": {
                    "Glock 10mm Frame": 1,
                    "Glock .50 GI Barrel": 1,
                    "Glock .50 GI Slide": 1,
                },
                "compatible parts": {
                    "Glock Base Plate": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                },
                "item": glock_17
            },
        }
    },
}
