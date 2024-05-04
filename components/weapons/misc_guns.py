from entity import Item
from components.consumables import GunIntegratedMag, GunComponent, GunMagFed
from components.gunparts import Parts
import colour

"""
Pistols
"""

"""S&W 629 .44"""

# weights
# frame and grip - 33.1 oz
# grips weight - 0.15 kg

sw629_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W Model 629 Frame",
    weight=0.94,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W .44 Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   accuracy_part=True,
                                   ),
    description='Frame and grip for a Smith & Wesson model 629 revolver.'
)

sw629_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W 629 Classic Barrel",
    weight=0.46,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W .44 Barrel',
                                   optic_properties={'target_acquisition_ap': 0.9,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.08, },
                                   is_optic=True,
                                   suffix='Classic',
                                   barrel_length=6.5,
                                   velocity_modifier={'44 Magnum': 0.95},
                                   accuracy_part=True,
                                   ),
    description='Standard 6.5 inch Smith & Wesson Model 629 Classic .44 Magnum barrel.'
)

sw629_barrel_stealth = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W 629 Stealth Hunter Barrel",
    weight=0.63,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W .44 Barrel',
                                   ap_to_equip=1.02,
                                   optic_properties={'target_acquisition_ap': 0.905,
                                                     'ap_distance_cost_modifier': 1.065,
                                                     'sight_spread_modifier': 0.08, },
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.0},
                                   is_optic=True,
                                   suffix='Stealth Hunter',
                                   barrel_length=7.5,
                                   velocity_modifier={'44 Magnum': 0.97},
                                   accuracy_part=True,
                                   ),
    description='A 7 inch Smith & Wesson Model 629 Classic .44 Magnum barrel. It includes a weighted shroud to'
                ' reduce muzzle flip.'
)

sw629_barrel_5in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W 629 5 Inch Barrel",
    weight=0.35,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W .44 Barrel',
                                   optic_properties={'target_acquisition_ap': 0.885,
                                                     'ap_distance_cost_modifier': 1.085,
                                                     'sight_spread_modifier': 0.08, },
                                   ap_to_equip=0.98,
                                   is_optic=True,
                                   barrel_length=5,
                                   velocity_modifier={'44 Magnum': 0.89},
                                   accuracy_part=True,
                                   ),
    description='5 inch Smith & Wesson Model 629 .44 Magnum barrel.'
)

sw629_barrel_4in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W 629 4 Inch Barrel",
    weight=0.27,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W .44 Barrel',
                                   optic_properties={'target_acquisition_ap': 0.88,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.08, },
                                   suffix='Short Barrel',
                                   ap_to_equip=0.97,
                                   is_optic=True,
                                   barrel_length=4,
                                   velocity_modifier={'44 Magnum': 0.8},
                                   accuracy_part=True,
                                   ),
    description='4 inch Smith & Wesson Model 629 .44 Magnum barrel.'
)

sw629_optic_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W N-Frame Optic Mount - Pistol",
    weight=0.05,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W N-Frame Optic Mount',
                                   additional_required_parts=('Optic',),
                                   is_attachment_point_types=['Pistol Optics Mount', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.0},
                                   receiver_height_above_bore=0.26,
                                   ),
    description='A pistol optics mount for the Smith & Wesson Model 629, replacing the rear sight.'
)

sw629_optic_pistol_picrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W N-Frame Optic Mount - Picatinny",
    weight=0.025,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W N-Frame Optic Mount',
                                   additional_required_parts=('Optic',),
                                   receiver_height_above_bore=0.26,
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.0},
                                   ),
    description='A picatinny rail optics mount for the Smith & Wesson Model 629, replacing the rear sight.'
)

sw629 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="S&W Model 629",
    weight=0.7,
    stacking=None,
    description='A six-shot, double action revolver designed by Smith and Wesson chambered in .44 Magnum, first'
                ' manufactured in 1955. It was once the most powerful production handgun, before the introduction of'
                ' larger cartridges such as .50 AE.',
    usable_properties=GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=False,
        ap_to_equip=100,
        compatible_clip='S&W Model 629 Moon Clip',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type=('.44 Magnum',),
        manual_action=False,
        mag_capacity=6,
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0.55,
        sight_height_above_bore=0.31,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        gun_type='pistol',
        action_type='revolver',
        barrel_length=6.5
    )
)

m629dict = {
    "guns": {
        "rifles": {
            "S&W Model 629": {
                "required parts": {
                    "S&W .44 Frame": 1,
                    "S&W .44 Barrel": 1,
                },
                "compatible parts": {
                    "S&W N-Frame Optic Mount": 1,
                    "Optic": 1,
                },
                "item": sw629
            },
        }
    },
}

"""S&W 610"""

sw610_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W Model 610 Frame",
    weight=0.87,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W 10mm Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   accuracy_part=True,
                                   ),
    description='Frame and grip for a Smith & Wesson model 610 revolver.'
)

sw610_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W 610 Classic Barrel",
    weight=0.55,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W 10mm Barrel',
                                   optic_properties={'target_acquisition_ap': 0.9,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.08, },
                                   is_optic=True,
                                   suffix='Classic',
                                   barrel_length=6.5,
                                   velocity_modifier={'10mm': 1.016, '40 S&W': 1.093},
                                   accuracy_part=True,
                                   ),
    description='Standard 6.5 inch Smith & Wesson Model 610 barrel.'
)


sw610_barrel_4in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="S&W 610 4 Inch Barrel",
    weight=0.34,
    stacking=None,
    usable_properties=GunComponent(part_type='S&W 10mm Barrel',
                                   optic_properties={'target_acquisition_ap': 0.88,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.08, },
                                   velocity_modifier={'10mm': 0.93, '40 S&W': 1.0},
                                   ap_to_equip=0.98,
                                   suffix='Short Barrel',
                                   is_optic=True,
                                   barrel_length=4,
                                   accuracy_part=True,
                                   ),
    description='4 inch Smith & Wesson Model 610 barrel.'
)

sw610 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="S&W Model 610",
    weight=0.7,
    stacking=None,
    description='A six-shot, double action revolver designed by Smith and Wesson chambered in 10mm Auto. '
                'Can also fire .40 S&W.',
    usable_properties=GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=False,
        ap_to_equip=100,
        compatible_clip='S&W Model 610 Moon Clip',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type=('10mm', '40 S&W'),
        manual_action=False,
        mag_capacity=6,
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0.55,
        sight_height_above_bore=0.31,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        gun_type='pistol',
        action_type='revolver',
        barrel_length=6.5
    )
)

m610dict = {
    "guns": {
        "rifles": {
            "S&W Model 610": {
                "required parts": {
                    "S&W 10mm Frame": 1,
                    "S&W 10mm Frame Barrel": 1,
                },
                "compatible parts": {
                    "S&W N-Frame Optic Mount": 1,
                    "Optic": 1,
                },
                "item": sw610
            },
        }
    },
}

"""Desert Eagle XIX .44 Magnum"""

# frames

de44_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="DE XIX .44 Magnum Frame",
    weight=0.78,
    stacking=None,
    usable_properties=GunComponent(part_type='DE .44 Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_magazine_type=('Desert Eagle .44',),
                                   functional_part=True,
                                   ),
    description='Frame for a Desert Eagle XIX .44 Magnum pistol.'
)

# barrels

de44_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="DE XIX .44 Magnum Barrel",
    weight=0.516,
    stacking=None,
    usable_properties=GunComponent(part_type='DE .44 Barrel',
                                   optic_properties={'target_acquisition_ap': 0.9,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.08, },
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.0},
                                   is_optic=True,
                                   barrel_length=6,
                                   velocity_modifier=0.92,
                                   functional_part=True,
                                   accuracy_part=True,
                                   ),
    description='Standard 6 inch Desert Eagle XIX .44 Magnum barrel.'
)

de44_barrel_imb = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="DE XIX .44 Magnum Barrel - IMB",
    weight=0.533,
    stacking=None,
    usable_properties=GunComponent(part_type='DE .44 Barrel',
                                   optic_properties={'target_acquisition_ap': 0.9,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.08, },
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.0},
                                   suffix='IMB',
                                   barrel_length=6,
                                   velocity_modifier=0.92,
                                   muzzle_break_efficiency=0.5,
                                   sound_radius=1.11,
                                   functional_part=True,
                                   accuracy_part=True,
                                   ),
    description='A 6 inch Desert Eagle XIX .44 Magnum barrel with an integrated muzzle brake.'
)

de44_barrel_10in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="DE XIX .44 Magnum Long Barrel",
    weight=0.64,
    stacking=None,
    usable_properties=GunComponent(part_type='DE .44 Barrel',
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.0},
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.04,
                                                     'sight_spread_modifier': 0.07, },
                                   suffix='Long Barrel',
                                   barrel_length=10,
                                   ap_to_equip=1.06,
                                   velocity_modifier=1.057,
                                   functional_part=True,
                                   accuracy_part=True,
                                   target_acquisition_ap_mod=1.05,
                                   ap_distance_cost_mod=1.03,
                                   equip_ap_mod=1.1,
                                   ),
    description='An extended 10 inch Desert Eagle XIX .44 Magnum barrel.'
)

de44_barrel_10in_threaded = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="DE XIX .44 Magnum Threaded Long Barrel",
    weight=0.64,
    stacking=None,
    usable_properties=GunComponent(part_type='DE .44 Barrel',
                                   is_attachment_point_types=['Picrail Optics Mount - Long', 'Barrel Thread 5/8x24'],
                                   optic_mount_properties={'receiver_height_above_bore': 0.0},
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.04,
                                                     'sight_spread_modifier': 0.07, },
                                   suffix='Long Barrel',
                                   barrel_length=10,
                                   ap_to_equip=1.06,
                                   velocity_modifier=1.057,
                                   functional_part=True,
                                   accuracy_part=True,
                                   target_acquisition_ap_mod=1.05,
                                   ap_distance_cost_mod=1.03,
                                   equip_ap_mod=1.1,
                                   ),
    description='An extended 10 inch Desert Eagle XIX .44 Magnum barrel. The barrel has been threaded to accept a '
                'muzzle device.'
)


# slides

de44_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="DE XIX .44 Magnum Slide",
    weight=0.595,
    stacking=None,
    usable_properties=GunComponent(part_type='DE .44 Slide',
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard TT-33 slide.'
)

de44 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Desert Eagle XIX .44 Magnum",
    weight=0.62,
    stacking=None,
    description='The Desert Eagle is a semi-automatic magnum pistol developed by the American company Magnum '
                'Research. Models are produced in .375 Magnum, .44 Magnum and .50 AE. It uses a gas piston and a '
                'rotating bolt which is reminiscent of the AR-15. While heavy and impractical, it has gained infamy '
                'for its roles in countless movies and video games.',
    usable_properties=GunMagFed(
        compatible_magazine_type=('Desert Eagle .44',),
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=100,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        current_fire_mode='single shot',
        parts=Parts(),
        velocity_modifier={'single projectile': 1.0},
        compatible_bullet_type=('.44 Magnum',),
        felt_recoil=1.0,
        load_time_modifier=1.0,
        receiver_height_above_bore=0.32,
        sight_height_above_bore=0.3,
        sound_modifier=1.0,
        zero_range=25,
        target_acquisition_ap=30,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        gun_type='pistol',
        barrel_length=4.6,
        action_type='semi-auto pistol',
    )
)

de44_dict = {
    "guns": {
        "pistols": {
            "Desert Eagle XIX .44 Magnum": {
                "required parts": {
                    "DE .44 Frame": 1,
                    "DE .44 Barrel": 1,
                    "DE .44 Slide": 1,
                },
                "compatible parts": {
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": de44
            },
        }
    },
}


"""TT-33"""

# frames

tt33_frame = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33 Frame",
    weight=0.129,
    stacking=None,
    usable_properties=GunComponent(part_type='Tokarev TT Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_magazine_type=('TT-33',),
                                   functional_part=True,
                                   ),
    description='A standard Russian TT-33 frame.'
)

# barrels

tt33_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33 Barrel",
    weight=0.06,
    stacking=None,
    usable_properties=GunComponent(part_type='Tokarev TT Barrel',
                                   is_attachment_point_types=['Tokarev TT-33 Barrel', ],
                                   velocity_modifier={'7.62x25 Tokarev': 1.0},
                                   barrel_length=4.6,
                                   functional_part=True,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='Standard 4.6 inch TT-33 barrel.'
)

# slides

tt33_slide = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33 Slide",
    weight=0.595,
    stacking=None,
    usable_properties=GunComponent(part_type='Tokarev TT Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A standard TT-33 slide.'
)

tt33_slide_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33 Slide - Tactical",
    weight=0.645,
    stacking=None,
    usable_properties=GunComponent(part_type='Tokarev TT Slide',
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.36},
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A TT-33 slide which has been fitted with a C&R rails picatinny rail for optics mounting.'
)


# grips

tt33_grip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33 Grip Panels",
    weight=0.07,
    stacking=None,
    usable_properties=GunComponent(part_type='Tokarev TT-33 Grip Panels',
                                   target_acquisition_ap=0.97,
                                   ),
    description='Original grip panels for TT-33 pistols.'
)

tt33_grip_rubberised = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33 Rubber Grip",
    weight=0.077,
    stacking=None,
    usable_properties=GunComponent(part_type='Tokarev TT-33 Grip Panels',
                                   felt_recoil=0.96,
                                   ),
    description='Ergonomic rubber pistol grip for TT-33 pistols. Includes ergonomic finger grooves which wrap around '
                'the front of the grip.'
)


# other

tt33_compensator = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33 Muzzle Brake / Compensator",
    weight=0.066,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('Tokarev TT-33 Barrel',),
                                   muzzle_break_efficiency=0.24,
                                   target_acquisition_ap=1.02,
                                   sound_radius=1.08,
                                   ),
    description='A compensator / muzzle brake for TT-33 pistols.'
)

tt33 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_MAGENTA,
    name="TT-33",
    weight=0.62,
    stacking=None,
    description='The TT-33 is a semi-automatic WWII-era pistol originating from the Soviet union. It uses a short '
                'recoil tilting bolt mechanism, similar to 1911 pistols. It fires the 7.62x25 Tokarev cartridge. '
                'While it fires a small 30 calibre bullet, it is typically high velocity, '
                'and is known to defeat body armour that would not typically be penetrable by pistol rounds.',
    usable_properties=GunMagFed(
        compatible_magazine_type=('TT-33',),
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=100,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        current_fire_mode='single shot',
        parts=Parts(),
        velocity_modifier={'single projectile': 1.0},
        compatible_bullet_type=('7.62x25 Tokarev',),
        felt_recoil=1.0,
        load_time_modifier=1.1,
        receiver_height_above_bore=0.33,
        sight_height_above_bore=0.22,
        sound_modifier=1.0,
        zero_range=27,
        target_acquisition_ap=30,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        gun_type='pistol',
        action_type='semi-auto pistol',
        barrel_length=4.6
    )
)

tt33_dict = {
    "guns": {
        "pistols": {
            "TT-33": {
                "required parts": {
                    "Tokarev TT Frame": 1,
                    "Tokarev TT Barrel": 1,
                    "Tokarev TT Slide": 1,
                    "Tokarev TT-33 Grip Panels": 1,
                },
                "compatible parts": {
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": tt33
            },
        }
    },
}

"""
Shotguns
"""

"""H015"""

# Winchester Model 37

single_shot_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Henry H015 Reciever",
    weight=1.22,
    stacking=None,
    usable_properties=GunComponent(part_type='H015 Reciever',
                                   grip_properties={
                                       'felt_recoil': 0.86,
                                       'ap_distance_cost_modifier': 0.92,
                                       'handling_spread_modifier': 0.92,
                                       'target_acquisition_ap': 0.81},
                                   ),
    description='Receiver for a Henry H015 single shot shotgun.'
)

# barrels

single_shot_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Henry H015 Barrel",
    weight=1.41,
    stacking=None,
    usable_properties=GunComponent(part_type='H015 Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier={'12 Gauge': 1.0, 'single projectile': 1.0, 'buckshot': 1.0},
                                   is_attachment_point_types=['Remington 12 Ga Choke', ],
                                   optic_properties={'target_acquisition_ap': 0.95,
                                                     'ap_distance_cost_modifier': 1.20,
                                                     'sight_spread_modifier': 0.1, },
                                   barrel_length=28,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description='28 inch 12 Guage barrel with bead front sight for the Henry H015.'
)

single_shot_barrel_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Henry H015 Short Barrel",
    weight=0.67,
    stacking=None,
    usable_properties=GunComponent(part_type='H015 Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier={'12 Gauge': 1.0, 'single projectile': 0.9, 'buckshot': 0.92},
                                   optic_properties={'target_acquisition_ap': 0.95,
                                                     'ap_distance_cost_modifier': 1.20,
                                                     'sight_spread_modifier': 0.1, },
                                   suffix='Short Barrel',
                                   ap_to_equip=0.94,
                                   barrel_length=14,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description='A cut down 14 inch 12 Guage barrel with bead front sight for the Henry H015.'
)

# stocks

single_shot_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Henry H015 Stock",
    weight=0.476,
    stacking=None,
    usable_properties=GunComponent(part_type='H015 Stock',
                                   felt_recoil=0.5,
                                   ap_distance_cost_modifier=0.69,
                                   handling_spread_modifier=0.85,
                                   target_acquisition_ap=0.77,
                                   ap_to_equip=1.3,
                                   has_stock=True,
                                   ),
    description='A wooden buttstock for the Henry H015.'
)

h015_birdshead = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="H015 Cut Down Stock",
    weight=0.3,
    stacking=None,
    usable_properties=GunComponent(part_type='H015 Stock',
                                   felt_recoil=0.92,
                                   ap_distance_cost_modifier=0.9,
                                   suffix='Pistol Grip',
                                   handling_spread_modifier=0.89,
                                   target_acquisition_ap=0.7,
                                   ),
    description='A wooden, cut down birds head type pistol grip for the Henry H015 shotgun.'
)

# accessories

h015_scope_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Henry H015 Picatinny Rail Optics Mount",
    weight=0.048,
    stacking=None,
    usable_properties=GunComponent(part_type='H015 Optic Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Long'],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.2},
                                   ),
    description='A picatinny rail for mounting optics and other accessories to Henry H015 shotguns.'
)


singleshot = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_MAGENTA,
    name="Henry H015",
    weight=1,
    stacking=None,
    description='A single shot 12 guage shotgun manufactured by Henry USA.',
    usable_properties=GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=False,
        ap_to_equip=100,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type=('12 Gauge',),
        velocity_modifier={'single projectile': 1.0, 'buckshot': 1.0},
        felt_recoil=1.0,
        mag_capacity=1,
        target_acquisition_ap=50,
        manual_action=True,
        action_cycle_ap_cost=300,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0.63,
        sight_height_above_bore=0.12,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0, 'buckshot': 1.0},
        gun_type='rifle',
        action_type='break action',
        barrel_length=20
    )
)

h015_dict = {
    "guns": {
        "shotguns": {
            "Winchester H015": {
                "required parts": {
                    "H015 Reciever": 1,
                    "H015 Barrel": 1,
                    "H015 Stock": 1,
                    "Model 870 Choke": 1,
                },
                "compatible parts": {
                    "H015 Optic Mount": 1,
                    "Optic": 1
                },
                "item": singleshot
            },
        }
    },
}

"""
Submachineguns
"""

"""M3"""

# reciever

m3_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M3 Receiver",
    weight=3.27,
    stacking=None,
    usable_properties=GunComponent(part_type='M3 Reciever',
                                   incompatibilities=(("Iron Sight",),),
                                   optic_properties={'target_acquisition_ap': 1.05,
                                                     'ap_distance_cost_modifier': 1.12,
                                                     'sight_spread_modifier': 0.16, },
                                   is_optic=True,
                                   compatible_magazine_type=('Grease Gun',),
                                   functional_part=True,
                                   optic_mount_properties={'receiver_height_above_bore': 0.4},
                                   grip_properties={
                                       'felt_recoil': 0.96,
                                       'ap_distance_cost_modifier': 0.8,
                                       'handling_spread_modifier': 0.77,
                                       'target_acquisition_ap': 0.95}
                                   ),
    description='Receiver for an M3 submachine gun.'
)

m3_reciever_picrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M3 Receiver - Tactical",
    weight=3.43,
    stacking=None,
    usable_properties=GunComponent(part_type='M3 Reciever',
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   compatible_magazine_type=('Grease Gun',),
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.36},
                                   additional_required_parts=('Optic',),
                                   grip_properties={
                                       'felt_recoil': 0.96,
                                       'ap_distance_cost_modifier': 0.8,
                                       'handling_spread_modifier': 0.77,
                                       'target_acquisition_ap': 0.95}
                                   ),
    description='Receiver for an M3 submachine gun. A picatinny rail has been attached for optics mounting.'
)

# barrel

m3_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M3 Submachine Gun Barrel",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='M3 Barrel',
                                   velocity_modifier={'.45 ACP': 1.078},
                                   compatible_bullet_type=('.45 ACP',),
                                   barrel_length=8,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A standard 8 inch .45 calibre M3 submachine gun barrel')

m3_barrel_threaded = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M3 Submachine Gun Barrel - Threaded",
    weight=0.15,
    stacking=None,
    usable_properties=GunComponent(part_type='M3 Barrel',
                                   velocity_modifier={'.45 ACP': 1.078},
                                   compatible_bullet_type=('.45 ACP',),
                                   is_attachment_point_types=['Barrel Thread .578x28', ],
                                   barrel_length=8,
                                   accuracy_part=True,
                                   short_barrel=True,
                                   ),
    description='A standard 8 inch .45 calibre M3 submachine gun barrel. It has been threaded to accept muzzle '
                'devices.')


# stock

m3_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M10 Stock",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='M3 Stock',
                                   felt_recoil=0.8,
                                   ap_distance_cost_modifier=0.9,
                                   handling_spread_modifier=0.74,
                                   target_acquisition_ap=0.78,
                                   has_stock=True,
                                   pdw_stock=True,
                                   ),
    description='The collapsing wire buttstock for the M3 submachine gun'
)

m3_greasegun = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_MAGENTA,
    name="M3 Submachine Gun",
    weight=1,
    stacking=None,
    description='The M3 submachine gun, better known as the "Grease Gun" due to its resemblance to the tool, '
                'is a cheaply produced submachine gun chambered for .45 ACP. It was produced for the US Army during '
                'WWII intended as a replacement for the Thompson submachine gun. It lacks the ergonomics of more '
                'modern designs and has rudimentary iron sights.',
    usable_properties=GunMagFed(
        compatible_magazine_type=('Grease Gun',),
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        ap_to_equip=100,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'automatic': {'fire rate': 450, 'automatic': True}},
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type=('.45 ACP',),
        firing_ap_cost=50,
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        ap_distance_cost_modifier=1.1,
        sight_height_above_bore=0.4,
        receiver_height_above_bore=0.97,
        sound_modifier=1.0,
        target_acquisition_ap=50,
        zero_range=100,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        gun_type='pdw',
        action_type='semi-auto rifle',
        barrel_length=8
    )
)

m3_dict = {
    "guns": {
        "submachineguns": {
            "M3 Submachine Gun": {
                "required parts": {
                    "M3 Reciever": 1,
                    "M3 Barrel": 1,
                },
                "compatible parts": {
                    "M3 Stock": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": m3_greasegun
            },
        },
    }
}

"""PPSh"""

# reciever

ppsh_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Receiver",
    weight=0.96,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Reciever',
                                   grip_properties={
                                       'felt_recoil': 0.96,
                                       'ap_distance_cost_modifier': 0.82,
                                       'handling_spread_modifier': 0.8,
                                       'target_acquisition_ap': 0.95},
                                   is_optic=True,
                                   compatible_magazine_type=('PPSh-41',),
                                   functional_part=True,
                                   ),
    description='Receiver for a PPSh-41 submachine gun.'
)

# barrel

ppsh_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Barrel",
    weight=0.51,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Barrel',
                                   velocity_modifier={'7.62x25 Tokarev': 1.08},
                                   compatible_parts={'PPSh Dust Cover': ["PPSh-41 Dust Cover",
                                                                         "PPSh-41 Dust Cover - Tactical"]},
                                   barrel_length=10.59,
                                   accuracy_part=True,
                                   ),
    description='A standard 10.6 inch 7.62x25 Tokarev PPSh-41 barrel')

ppsh_barrel_obrez = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Obrez Barrel",
    weight=0.23,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Barrel',
                                   suffix='Obrez',
                                   compatible_parts={'PPSh Dust Cover': ["PPSh-41 Obrez Dust Cover",
                                                                         "PPSh-41 Obrez Dust Cover - Tactical"]},
                                   velocity_modifier={'7.62x25 Tokarev': 1.01},
                                   barrel_length=4.6,
                                   accuracy_part=True,
                                   ),
    description='A shortened "obrez"-style 4.6 inch 7.62x25 Tokarev PPSh-41 barrel')

ppsh_barrel_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 9mm Barrel",
    weight=0.51,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Barrel',
                                   velocity_modifier={'9mm': 1.159},
                                   compatible_bullet_type=('9mm',),
                                   compatible_parts={'PPSh Dust Cover': ["PPSh-41 Dust Cover",
                                                                         "PPSh-41 Dust Cover - Tactical"]},
                                   barrel_length=10.59,
                                   accuracy_part=True,
                                   ),
    description='A 10.6 inch PPSh-41 barrel chambered in 9mm')

ppsh_barrel_obrez_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 9mm Obrez Barrel",
    weight=0.23,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Barrel',
                                   compatible_bullet_type=('9mm',),
                                   suffix='Obrez',
                                   compatible_parts={'PPSh Dust Cover': ["PPSh-41 Obrez Dust Cover",
                                                                         "PPSh-41 Obrez Dust Cover - Tactical"]},
                                   velocity_modifier={'9mm': 1.033},
                                   barrel_length=4.6,
                                   accuracy_part=True,
                                   ),
    description='A shortened "obrez"-style 4.6 inch PPSh-41 barrel chambered in 9mm')

# dust cover

ppsh_cover = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Dust Cover",
    weight=1.1,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Dust Cover',
                                   muzzle_break_efficiency=0.36,
                                   sound_radius=1.07,
                                   optic_properties={'target_acquisition_ap': 1.08,
                                                     'ap_distance_cost_modifier': 0.96,
                                                     'sight_spread_modifier': 0.1, },
                                   is_optic=True,
                                   ),
    description='A dust cover and barrel shroud for a PPSh-41')

ppsh_cover_obrez = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Obrez Dust Cover",
    weight=0.53,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Dust Cover',
                                   muzzle_break_efficiency=0.36,
                                   sound_radius=1.1,
                                   zero_range=27,
                                   optic_properties={'target_acquisition_ap': 1.03,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'sight_spread_modifier': 0.12, },
                                   is_optic=True,
                                   ),
    description='A shorted "obrez" style dust cover and barrel shroud for a PPSh-41, accomdating a shorter barrel')

ppsh_cover_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Dust Cover - Tactical",
    weight=1.1,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Dust Cover',
                                   muzzle_break_efficiency=0.36,
                                   sound_radius=1.07,
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.36},
                                   additional_required_parts=('Optic',),
                                   ),
    description='A dust cover and barrel shroud for a PPSh-41. A picatinny rail has been attached for optics mounting.')

ppsh_cover_obrez_tactical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Obrez Dust Cover - Tactical",
    weight=0.53,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Dust Cover',
                                   muzzle_break_efficiency=0.36,
                                   sound_radius=1.1,
                                   zero_range=27,
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.36},
                                   additional_required_parts=('Optic',),
                                   ),
    description='A shorted "obrez" style dust cover and barrel shroud for a PPSh-41, accomdating a shorter barrel. '
                'A picatinny rail has been attached for optics mounting.')


# stock

ppsh_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Stock",
    weight=1.05,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Stock',
                                   felt_recoil=0.46,
                                   ap_to_equip=1.2,
                                   ap_distance_cost_modifier=0.71,
                                   handling_spread_modifier=0.87,
                                   target_acquisition_ap=0.81,
                                   has_stock=True,
                                   ),
    description='A wooden buttstock for the PPSh-41.'
)

ppsh_stock_obrez = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41 Pistol Grip Stock",
    weight=0.766,
    stacking=None,
    usable_properties=GunComponent(part_type='PPSh Stock',
                                   suffix='Pistol Grip',
                                   felt_recoil=0.94,
                                   ap_distance_cost_modifier=0.87,
                                   handling_spread_modifier=0.87,
                                   target_acquisition_ap=0.68,
                                   has_stock=False,
                                   ),
    description='A modified "stock" for the PPSh, the buttstock has been removed and it features an AKM pistol grip.'
)

ppsh_41 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_MAGENTA,
    name="PPSh-41",
    weight=1,
    stacking=None,
    description='A WWII-era open-bolt submachine gun of soviet origin, nicknamed the "Papasha". It is known for its '
                'high rate of fire.',
    usable_properties=GunMagFed(
        compatible_magazine_type=('PPSh-41',),
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        ap_to_equip=100,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'automatic': {'fire rate': 1000, 'automatic': True}},
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type=('7.62x25 Tokarev',),
        firing_ap_cost=50,
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        ap_distance_cost_modifier=1.08,
        sight_height_above_bore=0.53,
        receiver_height_above_bore=0.53,
        sound_modifier=1.0,
        target_acquisition_ap=50,
        zero_range=109,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        gun_type='pdw',
        action_type='semi-auto rifle',
        barrel_length=8
    )
)

ppsh_dict = {
    "guns": {
        "submachineguns": {
            "PPSh-41": {
                "required parts": {
                    "PPSh Reciever": 1,
                    "PPSh Barrel": 1,
                    "PPSh Dust Cover": 1,
                    "PPSh Stock": 1,
                },
                "compatible parts": {
                    "Optic": 1
                },
                "item": ppsh_41
            },
        },
    }
}

"""
Rifles
"""

"""SVT"""

stock_svt = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SVT-40 Stock",
    weight=1.217,
    stacking=None,
    usable_properties=GunComponent(part_type='SVT Stock',
                                   felt_recoil=0.55,
                                   ap_distance_cost_modifier=0.71,
                                   handling_spread_modifier=0.86,
                                   target_acquisition_ap=0.8,
                                   ap_to_equip=1.3,
                                   accuracy_part=True,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.88,
                                       'ap_distance_cost_modifier': 0.91,
                                       'handling_spread_modifier': 0.93,
                                       'target_acquisition_ap': 0.82}),
    description='A standard wooden stock for SVT-40 rifles.'
)

svt_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SVT Reciever & Barrel Assembly",
    weight=2.94,
    stacking=None,
    usable_properties=GunComponent(part_type='SVT Reciever',
                                   compatible_magazine_type=('SVT-40',),
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier={'7.62x54R': 1.05},
                                   optic_properties={'target_acquisition_ap': 1.11,
                                                     'ap_distance_cost_modifier': 0.93,
                                                     'sight_spread_modifier': 0.04, },
                                   barrel_length=24.6,
                                   is_optic=True,
                                   target_acquisition_ap=1.04,
                                   muzzle_break_efficiency=0.47,
                                   sound_radius=1.16,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description='An SVT-40 reciever with standard 24.6 inch barrel. It comes installed with a muzzle brake.'
)

svt_barrel_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SVT Reciever & Barrel Assembly - Automatic",
    weight=2.94,
    stacking=None,
    usable_properties=GunComponent(part_type='SVT Reciever',
                                   compatible_magazine_type=('SVT-40',),
                                   incompatibilities=(("Iron Sight",),),
                                   suffix="Automatic",
                                   velocity_modifier={'7.62x54R': 1.05},
                                   optic_properties={'target_acquisition_ap': 1.11,
                                                     'ap_distance_cost_modifier': 0.93,
                                                     'sight_spread_modifier': 0.04, },
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   barrel_length=24.6,
                                   is_optic=True,
                                   target_acquisition_ap=1.04,
                                   muzzle_break_efficiency=0.47,
                                   sound_radius=1.16,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description='An SVT-40 reciever that has been modified to allow fully-automatic fire. It features a standard '
                '24.6 inch barrel. It comes installed with a muzzle brake.'
)

svt_pic_scope_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SVT-40 Picatinny Rail Optics Mount",
    weight=0.28,
    stacking=None,
    usable_properties=GunComponent(part_type='SVT Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Long'],
                                   additional_required_parts=['Optic', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.86}, ),
    description='A picatinny rail for mounting optics to SVT-40 rifles'
)

svt = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="SVT-40",
    weight=3.85,
    stacking=None,
    description='The SVT-40 is a WWII-era semi-automatic rifle produced by the Soviet Union, originally intended to '
                'replace the Mosin-Nagant, which which it shares the 7.62x54R cartridge, as the standard infantry '
                'rifle for the Soviet military.',
    usable_properties=GunMagFed(
        compatible_magazine_type=('SVT-40',),
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=100,
        current_fire_mode='single shot',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        parts=Parts(),
        compatible_bullet_type=('7.62x54R',),
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        sound_modifier=1.0,
        zero_range=109,
        receiver_height_above_bore=0.96,
        sight_height_above_bore=0.24,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        compatible_clip='SVT-40 Clip',
        projectile_spread_modifier={'single projectile': 1.0},
        barrel_length=24.6,
        action_type='semi-auto rifle',
        gun_type='rifle'
    )
)

svt_dict = {
    "guns": {
        "automatic rifles": {
            "SVT-40": {
                "required parts": {
                    "SVT Reciever": 1,
                    "SVT Stock": 1,
                },
                "compatible parts": {
                    "SVT Optics Mount": 1,
                    "Optic": 1
                },
                "item": svt
            },
        }
    },
}


"""
Carbines
"""

"""Calico 9mm"""

# deductions
# tactical and traditional pistol fore weighs the same
# weight difference between full and collapsing stock - 0.2 lbs
# estimated weight of 16 inch barrel - w/o mb 0.22 kg
# assuming pistol grip is roughly 0.08 kg
# assuming 8.5 inch barrel weighs roughly 0.12 kg
# assuming 6 inch barrel weighs roughly 0.11 kg

# weight diff - lib 3 and m960
# LIII minus barrel - 0.91
# M960 minus barrel and grip - 1.72 kg
# therefore collapsing stock weighs roughly 0.81 kg
# I don't think the M960 weight given is accurate to begin with, so I dont think that this number is accurate

# 9mm liberty 50T tactical carbine rifle - 6.5 lbs (full stock, tactical fore, carbine barrel)
# 9mm liberty I carbine rifle - 5 lbs (collapsing stock, old fore, 16 in barrel)
# 9mm M-960 SBR - 4.25 lbs (collapsing stock, old fore w/ foregrip, 8.5 in barrel w/ brake)
# 9mm Liberty IIT tactical carbine rifle - 6.7 lbs (full stock, tactical fore, carbine barrel w/ brake)
# 9mm Liberty IT tactical carbine rifle - 6.5 lbs (collapsing stock, tactical fore, carbine barrel w/ brake)
# 9mm libterty IIIT tactical pistol -  2.25 lbs (no stock, tactical fore, 6 inch barrel w/ brake)
# 9mm liberty III pistol - 2.25 lbs (no stock, old fore, 6 inch barrel w/ brake)
# 9mm Liberty II - 5.25 lbs (full stock, old fore, carbine barrel)