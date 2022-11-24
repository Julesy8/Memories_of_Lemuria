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
                                   is_attachment_point_types=['Picrail Underbarrel',],
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
                                   is_attachment_point_types=['Barrel Thread M13.5x1 LH',],
                                   compatible_parts={'Glock 17 Slide': ['Glock 17 Slide', 'Glock 17 Custom Slide']},
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
                                   velocity_modifier=1.05,
                                   is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
                                   compatible_parts={'Glock 17 Slide': ['Glock 17L Slide', 'Glock 17L Custom Slide',
                                                                        'Glock 17 Slide', 'Glock 17 Custom Slide']},
                                   ),
    description='Glock 17L barrel. Longer than the standard Glock 17 barrel'
)

"""
glock_9in_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="9 inch Glock 9mm Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
                                   compatible_parts={'Glock 17 Slide': ['Glock 17L Slide', 'Glock 17L Custom Slide',
                                                                        'Glock 17 Slide', 'Glock 17 Custom Slide']},
                                   base_meat_damage=1.1,
                                   base_armour_damage=1.1,
                                   range_accuracy_dropoff=1.1,
                                   recoil=0.90,
                                   close_range_accuracy=0.8,
                                   base_accuracy=1.08,
                                   sound_radius=0.9,
                                   ),
    description='Extra long 9 inch Glock 9mm barrel'
)
"""

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
                                   muzzle_break_efficiency=0.7,
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
                                   compatible_parts={'Glock 17 Slide': ['Glock 17L Custom Slide', 'Glock 17 Slide',
                                                                        'Glock 17 Custom Slide']},
                                   prevents_suppression=True,
                                   muzzle_break_efficiency=0.7,
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
                                   is_attachment_point_types=['Dovetail Optics Mount', ],
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
                                   is_attachment_point_types=['Dovetail Optics Mount', ],
                                   accuracy_distribution=1.1,
                                   ),
    description='Glock 17L slide. Longer than the standard Glock 17 slide'
)

glock17_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17 Custom Slide",
    weight=0.17,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Dovetail Optics Mount', ],
                                   ),
    description='Custom milled Glock 17 slide, reducing weight and vastly improving aesthetics'
)

glock17l_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock 17L Custom Slide",
    weight=0.17,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Dovetail Optics Mount', ],
                                   accuracy_distribution=1.1,
                                   ),
    description='Custom milled Glock 17L slide, reducing weight and vastly improving aesthetics'
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
                                   fire_modes={'automatic': 1200}, ),
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
                                   velocity_modifier=1.04,
                                   ),
    description='A large compensator for Glock 9mm pistols'
)

# FAB defense glock cobra stock
glock_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Cobra Stock",
    weight=0.02,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   felt_recoil=0.79,
                                   accuracy_distribution=1.1,
                                   equip_time=2.0,
                                   ),
    description='A folding stock for Glock pistols'
)

# FAB defense GIS
glock_pic_rail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Picatinny Sight Mount",
    weight=0.004,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount', ],
                                   additional_required_parts=['Optic', ]
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
                                   accuracy_distribution=1.06,
                                   equip_time=1.4,
                                   ),
    description='Collapsing pistol brace for Glock handguns designed by Flux Defense'
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
                                   muzzle_break_efficiency=0.4,
                                   velocity_modifier=1.06,
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
    description='The classic Glock 9mm handgun, famous for its simplicity and reliability',
    usable_properties=GunMagFed(
        compatible_magazine_type='Glock 9mm',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1},
        current_fire_mode='single shot',
        parts=Parts(),
        velocity_modifier=1.0,
        enemy_attack_range=16,
        compatible_bullet_type='9mm',
        felt_recoil=1.0,
        barrel_length=7,
        sight_height_above_bore=0.2,
        sound_modifier=1.0,
        zero_range=25,
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
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": glock_17
            },
        }
    },
}
