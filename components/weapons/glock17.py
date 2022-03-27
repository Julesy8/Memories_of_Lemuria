from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour
from components.commonitems import steel, polymer

glock17_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Frame",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='glock17_frame', material={polymer: 2}, accessory_attachment=True),
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
    usable_properties=GunComponent(part_type='glock17_barrel',
                                   material={steel: 1}),
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
    usable_properties=GunComponent(part_type='glock17_barrel',
                                   material={steel: 1},
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
    usable_properties=GunComponent(part_type='glock17_barrel',
                                   material={steel: 1},
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
    usable_properties=GunComponent(part_type='glock17_barrel',
                                   material={steel: 1},
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
    usable_properties=GunComponent(part_type='glock17_barrel', suffix='Long',
                                   material={steel: 1},
                                   range_accuracy_dropoff=1.05,
                                   recoil=0.65,
                                   close_range_accuracy=0.9,
                                   prevents_suppression=True,
                                   sound_radius=1.25,
                                   base_accuracy=1.01
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   suffix='17',
                                   material={steel: 1},
                                   pistol_optics_mount=True,
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   material={steel: 1},
                                   suffix='17L',
                                   prerequisite_parts=[glock17l_barrel, ],
                                   recoil=0.94,
                                   close_range_accuracy=0.95,
                                   pistol_optics_mount=True,
                                   ),
    description='Glock 17L slide. Longer than the standard Glock 17 slide'
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   suffix='17 Ported',
                                   prerequisite_parts=[glock17_barrel_ported, ],
                                   material={steel: 1},
                                   pistol_optics_mount=True,
                                   ),
    description='Glock 17 slide with milled cutouts to accept a ported barrel'
)

glock17l_slide_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Ported Glock 17L Slide",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='glock17_slide',
                                   suffix='17L Ported',
                                   prerequisite_parts=[glock17l_barrel_ported, ],
                                   material={steel: 1},
                                   recoil=0.92,
                                   close_range_accuracy=0.95,
                                   pistol_optics_mount=True,
                                   ),
    description='Glock 17L slide with milled cutouts to accept a ported barrel'
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
    usable_properties=GunComponent(part_type='glock_switch', prefix='Automatic',
                                   material={steel: 1},
                                   fire_modes={'single shot': 1, 'automatic': 1200}, ),
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
    usable_properties=GunComponent(part_type='glock_9mm_muzzle',
                                   material={steel: 1},
                                   recoil=0.70,
                                   sound_radius=1.3,
                                   base_accuracy=1.05,
                                   close_range_accuracy=0.95,),
    description='Glock compensator'
)

glock_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock G-Stock",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='glock_stock',
                                   material={polymer: 1},
                                   base_accuracy=1.05,
                                   recoil=0.8,
                                   close_range_accuracy=0.9,
                                   ),
    description='Sturdy G-stock for more accurate fire and decreased recoil'
)

glock_kit_pdw = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Carbine Kit",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='glock_stock',
                                   suffix='PDW',
                                   material={polymer: 1},
                                   base_accuracy=1.1,
                                   recoil=0.70,
                                   close_range_accuracy=0.85,
                                   large_optics_mount=True,
                                   ),
    description='A chassis for the glock 17 that provides a more carbine like profile and a stock'
)

glock_parts_dict = {
    "glock17_frame": ([glock17_frame, 1], [glock17_frame, 1]),
    "glock17_slide": ([glock17_slide, 1], [glock17_slide, 1]),
    "glock17_barrel": ([glock17_barrel, 1], [glock17l_barrel, 1]),
    "glock_stock": ([None, 1], [glock_stock, 1]),
}

glock_17 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock",
    weight=0.7,
    stacking=None,
    description='The classic Glock 9mm handgun, famous for their simplicity and reliability',
    usable_properties=GunMagFed(
        compatible_magazine_type='glock9mm',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1},
        current_fire_mode='single shot',
        base_meat_damage=1.0,
        base_armour_damage=1.0,
        base_accuracy=0.9,
        range_accuracy_dropoff=18,
        parts=Parts(),
        enemy_attack_range=7,
        possible_parts=glock_parts_dict,
        sound_radius=8,
        recoil=3,
        close_range_accuracy=1.1,
    )
)
