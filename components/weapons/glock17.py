from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

glock17_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17 Frame",
    weight=0.155,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['Picrail Underbarrel - Short', ],
                                   functional_part=True
                                   ),
    description='Standard Glock frame compatible with Glock 17, 17L and 34 slides and barrels'
)

"""
BARRELS
"""

glock17_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17 Barrel",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
                                   compatible_parts={
                                       'Glock 17 Slide': ['Glock 17 Slide', "Glock 17 Slide w/ Optics Cut",
                                                          'Glock 17 Custom Slide']},
                                   barrel_length=0.37,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Standard Glock 17 barrel'
)

glock17l_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17L Barrel",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   velocity_modifier=1.035,
                                   is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
                                   compatible_parts={'Glock 17 Slide': ['Glock 17L Slide', 'Glock 17L Custom Slide',
                                                                        'Glock 17 Slide', 'Glock 17 Custom Slide',
                                                                        "Glock 17 Slide w/ Optics Cut",
                                                                        "Glock 17L Slide w/ Optics Cut"]},
                                   barrel_length=0.5,
                                   target_acquisition_ap=1.05,
                                   equip_time=1.05,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Glock 17L barrel. Longer than the standard Glock 17 barrel'
)

glock_9in_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="9 inch Glock 9mm Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   velocity_modifier=1.08,
                                   is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
                                   compatible_parts={'Glock 17 Slide': ['Glock 17L Slide', 'Glock 17L Custom Slide',
                                                                        'Glock 17 Slide', 'Glock 17 Custom Slide',
                                                                        "Glock 17 Slide w/ Optics Cut",
                                                                        "Glock 17L Slide w/ Optics Cut"]},
                                   barrel_length=0.75,
                                   target_acquisition_ap=1.11,
                                   equip_time=1.11,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Extra long 9 inch Glock 9mm barrel'
)

"""
BARRELS - PORTED
"""

glock17_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17 Ported Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   compatible_parts={'Glock 17 Slide': ['Glock 17 Custom Slide']},
                                   prevents_suppression=True,
                                   muzzle_break_efficiency=0.4,
                                   barrel_length=0.37,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Glock 17 barrel with milled cutouts to reduce muzzle climb'
)

glock17l_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17L Ported Barrel",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   velocity_modifier=1.035,
                                   compatible_parts={'Glock 17 Slide': ['Glock 17L Custom Slide', 'Glock 17 Slide',
                                                                        'Glock 17 Custom Slide']},
                                   prevents_suppression=True,
                                   muzzle_break_efficiency=0.4,
                                   barrel_length=0.5,
                                   target_acquisition_ap=1.05,
                                   equip_time=1.05,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Glock 17L barrel with milled cutouts to reduce muzzle climb'
)

"""
SLIDES
"""

glock17_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17 Slide",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Glock 17 slide'
)

glock17l_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17L Slide",
    weight=0.374,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='Glock 17L slide. Longer than the standard Glock 17 slide'
)

glock17_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17 Slide w/ Optics Cut",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True
                                   ),
    description='Glock 17 slide, machined to allow the mounting of optics such as RMRs'
)

glock17l_slide_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17L Slide w/ Optics Cut",
    weight=0.374,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True
                                   ),
    description='Glock 17L slide, machined to allow the mounting of optics such as RMRs. Longer than the standard '
                'Glock 17 slide'
)

glock17_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17 Custom Slide",
    weight=0.17,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   target_acquisition_ap=0.95,
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
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17L Custom Slide",
    weight=0.17,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   target_acquisition_ap=0.95,
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True
                                   ),
    description='Custom milled Glock 17L slide, reducing weight and vastly improving aesthetics. '
                'Machined to allow the mounting of optics such as RMRs'
)

"""
OTHER PARTS
"""

glock_switch = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Auto Switch",
    weight=0.03,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Base Plate',
                                   prefix='Automatic',
                                   fire_modes={'automatic': {'fire rate': 1200, 'automatic': True}}, ),
    description='Modifed Glock cover plate enabling automatic fire'
)

glock_9mm_compensator = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Compensator",
    weight=0.14,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread M13.5x1 LH',),
                                   muzzle_break_efficiency=0.26,
                                   target_acquisition_ap=1.03,
                                   sound_radius=1.1,
                                   ),
    description='A large compensator for Glock 9mm pistols'
)

# FAB defense glock cobra stock
glock_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Cobra Stock",
    weight=0.328,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   felt_recoil=0.79,
                                   equip_time=1.2,
                                   ap_distance_cost_modifier=0.71,
                                   spread_modifier=0.9,
                                   target_acquisition_ap=0.76,
                                   ),
    description='A folding stock for Glock pistols'
)

# FAB defense GIS
glock_pic_rail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
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
    fg_colour=colour.LIGHT_GRAY,
    name="Flux Defense Glock Pistol Brace",
    weight=0.013,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   felt_recoil=0.83,
                                   equip_time=1.14,
                                   ap_distance_cost_modifier=0.76,
                                   spread_modifier=0.94,
                                   target_acquisition_ap=0.71,
                                   ),
    description='Collapsing pistol brace "not a stock" for Glock handguns designed by Flux Defense'
)

# SF Ryder 9M
suppressor_surefire_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Surefire 9mm Suppressor",
    weight=0.255,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Barrel Thread M13.5x1 LH',),
                                   muzzle_break_efficiency=0.3,
                                   target_acquisition_ap=1.04,
                                   fire_rate_modifier=1.1,
                                   is_suppressor=True,
                                   sound_radius=0.3,
                                   ),
    description='A slim titanium suppressor by surefire for M13.5x1 LH barrel threading'
)

glock_17 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17",
    weight=0.62,
    stacking=None,
    description='The classic Glock 9mm handgun, famous for its simplicity and reliability ',
    usable_properties=GunMagFed(
        compatible_magazine_type='Glock 9mm',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=75,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        velocity_modifier=1.0,
        compatible_bullet_type='9mm',
        felt_recoil=1.1,
        barrel_length=0,
        receiver_height_above_bore=0.46,
        sight_height_above_bore=0.08,
        sound_modifier=1.0,
        zero_range=25,
        target_acquisition_ap=30,
        firing_ap_cost=20,
        ap_distance_cost_modifier=1.0,
        spread_modifier=0.055,
    )
)

glock17dict = {
    "guns": {
        "pistols": {
            "Glock 17": {
                "required parts": {
                    "Glock 17 Frame": 1,
                    "Glock 17 Barrel": 1,
                    "Glock 17 Slide": 1,
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
