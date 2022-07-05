from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

glock17_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Frame",
    weight=0.2,
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
    bg_colour=None,
    name="Glock 17 Barrel",
    weight=0.2,
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
    bg_colour=None,
    name="Glock 17L Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   is_attachment_point_types=['Barrel Thread M13.5x1 LH', ],
                                   compatible_parts={'Glock 17 Slide': ['Glock 17L Slide', 'Glock 17L Custom Slide',
                                                                        'Glock 17 Slide', 'Glock 17 Custom Slide']},
                                   base_meat_damage=1.06,
                                   base_armour_damage=1.06,
                                   range_accuracy_dropoff=1.06,
                                   recoil=0.95,
                                   close_range_accuracy=0.9,
                                   base_accuracy=1.04
                                   ),
    description='Glock 17L barrel. Longer than the standard Glock 17 barrel'
)

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
BARRELS - PORTED
"""

glock17_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Ported Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   compatible_parts={'Glock 17 Slide': ['Ported Glock 17 Slide',
                                                                        'Glock 17 Custom Slide']},
                                   base_meat_damage=0.97,
                                   base_armour_damage=0.95,
                                   range_accuracy_dropoff=0.96,
                                   recoil=0.70,
                                   prevents_suppression=True,
                                   sound_radius=1.25,
                                   base_accuracy=0.97
                                   ),
    description='Glock 17 barrel with milled cutouts to reduce muzzle climb'
)

glock17l_barrel_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17L Ported Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Barrel',
                                   compatible_parts={'Glock 17 Slide': ['Ported Glock 17L Slide',
                                                                        'Glock 17L Custom Slide', 'Glock 17 Slide',
                                                                        'Glock 17 Custom Slide']},
                                   range_accuracy_dropoff=1.05,
                                   recoil=0.65,
                                   close_range_accuracy=0.9,
                                   prevents_suppression=True,
                                   sound_radius=1.25,
                                   base_accuracy=1.01,
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
    bg_colour=None,
    name="Glock 17 Slide",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optic', ],
                                   ),
    description='Glock 17 slide'
)

glock17l_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17L Slide",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optic', ],
                                   recoil=0.94,
                                   close_range_accuracy=0.95,
                                   ),
    description='Glock 17L slide. Longer than the standard Glock 17 slide'
)

glock17_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Custom Slide",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optic', ],
                                   recoil=1.06,
                                   base_accuracy=1.1,
                                   ),
    description='Custom milled Glock 17 slide, reducing weight and vastly improving aesthetics'
)

glock17l_slide_custom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17L Custom Slide",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optic', ],
                                   recoil=1.04,
                                   base_accuracy=1.1,
                                   close_range_accuracy=0.95,
                                   ),
    description='Custom milled Glock 17L slide, reducing weight and vastly improving aesthetics'
)

"""
SLIDES - PORTED
"""

glock17_slide_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Ported Glock 17 Slide",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optic', ],
                                   ),
    description='Glock 17 slide with milled cutouts for use with a ported barrel'
)

glock17l_slide_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Ported Glock 17L Slide",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock 17 Slide',
                                   is_attachment_point_types=['Pistol Optic', ],
                                   close_range_accuracy=0.95,
                                   ),
    description='Glock 17L slide with milled cutouts for use with a ported barrel'
)

"""
OTHER PARTS
"""

glock_switch = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Auto Switch",
    weight=0.2,
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
    bg_colour=None,
    name="Glock Compensator",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   recoil=0.70,
                                   sound_radius=1.3,
                                   base_accuracy=1.05,
                                   close_range_accuracy=0.95,
                                   attachment_point_required='Barrel Thread M13.5x1 LH'
                                   ),
    description='A large compensator for Glock 9mm pistols'
)

glock_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock G-Stock",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   base_accuracy=1.05,
                                   recoil=0.8,
                                   close_range_accuracy=0.9,
                                   ),
    description='A folding stock for Glock pistols'
)

glock_pic_rail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Picatinny Sight Mount",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Optics Mount',
                                   close_range_accuracy=0.95,
                                   is_attachment_point_types=['Picrail Optics Mount', ],
                                   ),
    description='An aftermarket picatinny rail sight mount for Glock handguns'
)


glock_pistol_brace = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Flux Defense Glock Pistol Brace",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Glock Stock',
                                   close_range_accuracy=0.95,
                                   recoil=0.80,
                                   base_accuracy=1.06,
                                   ),
    description='Collapsing pistol brace for Glock handguns designed by Flux Defense'
)

glock_parts_dict = {
    "glock17_frame": ((glock17_frame, 1), (glock17_frame, 1)),
    "glock17_slide": ((glock17_slide, 1), (glock17_slide, 1)),
    "glock17_barrel": ((glock17_barrel, 1), (glock17l_barrel, 1)),
    "glock_stock": ((None, 1), (glock_stock, 1)),
}

glock_17 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17",
    weight=0.7,
    stacking=None,
    description='The classic Glock 9mm handgun, famous for its simplicity and reliability',
    usable_properties=GunMagFed(
        compatible_magazine_type='glock9mm',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'rapid fire (semi-auto)': 3},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.9,
        range_accuracy_dropoff=18,
        parts=Parts(),
        enemy_attack_range=7,
        possible_parts=glock_parts_dict,
        sound_radius=1.0,
        recoil=1.0,
        close_range_accuracy=1.1,
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
