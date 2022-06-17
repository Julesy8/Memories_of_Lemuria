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

glock17_frame_stippled = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Frame - Stippled",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='glock17_frame',
                                   material={polymer: 2},
                                   accessory_attachment=True,
                                   recoil=0.95,
                                   base_accuracy=1.04
                                   ),
    description='Standard Glock frame compatible with Glock 17, 17L and 34 slides and barrels. Stippling has been added'
                'to improve grip in adverse conditions.'
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   suffix='17',
                                   material={steel: 1},
                                   optics_mount_types=('dovetail', 'glock')
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
                                   recoil=0.94,
                                   close_range_accuracy=0.95,
                                   optics_mount_types=('dovetail', 'glock')
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   suffix='17',
                                   material={steel: 1},
                                   recoil=1.1,
                                   base_accuracy=1.1,
                                   optics_mount_types=('dovetail', 'glock')
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   material={steel: 1},
                                   suffix='17L',
                                   recoil=1.04,
                                   base_accuracy=1.1,
                                   close_range_accuracy=0.95,
                                   optics_mount_types=('dovetail', 'glock')
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   suffix='17 Ported',
                                   material={steel: 1},
                                   optics_mount_types=('dovetail', 'glock')
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
    usable_properties=GunComponent(part_type='glock17_slide',
                                   suffix='17L Ported',
                                   material={steel: 1},
                                   close_range_accuracy=0.95,
                                   optics_mount_types=('dovetail', 'glock')
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
    usable_properties=GunComponent(part_type='glock_switch', prefix='Automatic',
                                   material={steel: 1},
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
                                   material={polymer: 3},
                                   base_accuracy=1.1,
                                   recoil=0.70,
                                   close_range_accuracy=0.85,
                                   optics_mount_types=('picrail',)
                                   ),
    description='A chassis for the glock 17 that provides a more carbine like profile and a stock'
)

glock_flared_magwell = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Flared Magwell",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='magwell',
                                   material={steel: 1}, load_time_modifier=0.8
                                   ),
    description='Aftermarket Magwell for Glock Handguns, allows for more rapid reloads in tense situations'
)

glock_pic_rail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Picatinny Sight Mount",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='glock_baseplate',
                                   material={steel: 1},
                                   close_range_accuracy=0.95,
                                   optics_mount_types=('picrail',)
                                   ),
    description='An aftermarket picatinny rail sight mount for Glock handguns'
)

glock_night_sights = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Night Sights",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   incompatible_parts=(glock_kit_pdw,),
                                   base_accuracy=1.03,
                                   ),
    description='Glow in the dark replacement for the standard Glock iron sights for enhanced accuracy in low light '
                'situations'
)

glock_pistol_brace = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Flux Defense Glock Pistol Brace",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='glock_stock', prefix='Automatic',
                                   material={steel: 2},
                                   close_range_accuracy=0.95,
                                   recoil=0.80,
                                   base_accuracy=1.06,
                                   ),
    description='Collapsing pistol brace for Glock handguns designed by Flux Defense'
)

glock_charging_handle = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Slide Charging Handle",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='glock_baseplate',
                                   material={steel: 1},
                                   load_time_modifier=0.9
                                   ),
    description='Aftermarket replacement base plate for Glock handguns featuring a rifle style side charging handle '
                'for more rapid reloads. Favoured by competition shooters.'
)

glock_competition_trigger = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Competition Trigger",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='glock_trigger',
                                   material={steel: 1},
                                   base_accuacy=1.05,
                                   ),
    description='Aftermarket trigger for Glock handguns featuring a lighter pull, allowing for more accurate shot '
                'placement more shots in rapid fire'
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
    name="Glock",
    weight=0.7,
    stacking=None,
    description='The classic Glock 9mm handgun, famous for its simplicity and reliability',
    usable_properties=GunMagFed(
        compatible_magazine_type='glock9mm',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 60, 'semi-auto rapid fire': 180},
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

glock_frame_weight = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Frame Weight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='gun_accessory',
                                   compatible_items=(glock_17,),
                                   material={steel: 1},
                                   recoil=0.90,
                                   close_range_accuracy=0.94,
                                   ),
    description='Adds weight towards the muzzle end of the firearm. Reduces muzzle flip.'
)

glock17dict = {
    "guns": {
        "pistols": {
            "Glock 17": {
                "required parts": {
                    "glock17_frame": 1,
                    "glock17_barrel": 1,
                    "glock17_slide": 1,
                },
                "compatible parts": {
                    "glock_trigger": 1,
                    "glock_stock": 1,
                    "glock_optics_mount": 1,
                    "glock_base_plate": 1,
                    "gun_accessory": 1,
                    "muzzle_device_9mm": 1,
                    "optic": 1
                                     },
                "parts names": ["Frame",
                                "Slide",
                                "Barrel",
                                "Stock",
                                "Muzzle Device"
                                ],
                "item": glock_17
            },
        }
    },
    "gun parts": {
        "Glock": {


            # Frames
            "Frames": {
                "Glock 17/34 Frame": {
                    "required parts": {
                        "polymer": 2,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17_frame
                },
                "Glock 17/34 Frame - Stippled": {
                    "required parts": {
                        "polymer": 2,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17_frame_stippled
                },
            },


            # Barrels
            "Barrels": {
                "Glock 17 Barrel": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17_barrel
                },
                "Glock 17L Barrel": {
                    "required parts": {
                        "steel": 2,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17l_barrel
                },
                "Glock 9mm 9'' Barrel": {
                    "required parts": {
                        "steel": 3,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17l_barrel
                },
                "Glock 17 Ported Barrel": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17_barrel_ported
                },
                "Glock 17L Ported Barrel": {
                    "required parts": {
                        "steel": 2,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17l_barrel_ported
                },
            },


            # Slides
            "Slides": {
                "Glock 17 Slide": {
                    "required parts": {
                        "steel": 2,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17_slide
                },
                "Glock 17L Slide": {
                    "required parts": {
                        "steel": 3,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17l_slide
                },
                "Glock 17 Slide - Ported": {
                    "required parts": {
                        "steel": 3,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17_slide_ported
                },
                "Glock 17L Slide - Ported": {
                    "required parts": {
                        "steel": 3,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17l_slide_ported
                },
                "Glock 17 Slide - Custom Milled": {
                    "required parts": {
                        "steel": 3,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17_slide_custom
                },
                "Glock 17L Slide - Custom Milled": {
                    "required parts": {
                        "steel": 3,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock17l_slide_custom
                },
            },


            # Stocks
            "Stocks": {
                "Glock G-Stock": {
                    "required parts": {
                        "polymer": 3,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_9mm_compensator
                },
                "Glock PDW Kit": {
                    "required parts": {
                        "polymer": 2,
                        "steel": 3,

                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_kit_pdw
                },
                "Flux Defense Glock Pistol Brace": {
                    "required parts": {
                        "steel": 3,
                        "polymer": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_pistol_brace
                },
            },


            # Accessories
            "Accessories": {
                "Glock Autosear": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_switch
                },
                "Glock Compensator - 9mm": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_9mm_compensator
                },
                "Glock Flared Magwell": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_flared_magwell
                },
                "Glock Picatinny Optics Mount": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_pic_rail
                },
                "Glock Night Sights": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_night_sights
                },
                "Glock Slide Charging Handle": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_charging_handle
                },
                "Glock Competition Trigger": {
                    "required parts": {
                        "steel": 1,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_competition_trigger
                },
                "Glock Frame Weight": {
                    "required parts": {
                        "steel": 2,
                    },
                    "compatible parts": {},
                    "parts names": ["Material"],
                    "item": glock_frame_weight
                },
            }
        }
    },
}
