from entity import Item
from components import consumables
import colour

# TODO - chest rigs and belt

"""
Body armour standards:

VPAM 1 - 0.13 inches mild steel - 22 LR
VPAM 2 - 0.16 - 123 gr 9mm
VPAM 3 - 0.2 - 9mm +P
VPAM 4 - 0.28 - 357 / 44 mag
VPAM 5 - 0.3 - 357 +P 
VPAM 6 - 0.56 - 7.62x39
VPAM 7 - 0.83 5.56/7.62x51
VPAM 10 - 0.93 7.62x54r
"""

helmet_ssh68 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Ssh-68 Steel Helmet",
    weight=1.3,
    stacking=None,
    description='A cold war era steel helmet originating from the Soviet Union. Provides protection against shrapnel '
                'and handgun rounds.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.4,
        coverage_d=0.6,
        coverage_l=0.6,
        coverage_r=0.6,
        equip_ap_cost=400,
        ballistic_protection_level="PM 3",
        protection_ballistic=0.2,
        protection_physical=5,
        fits_bodypart_type='Head',
    ))
)

helmet_m1 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="M1 Steel Helmet",
    weight=1.36,
    stacking=None,
    description='A WWII era steel helmet originating from the USA. It saw service in the US military until 1985. ',
    usable_properties=(consumables.Wearable(
        coverage_v=0.4,
        coverage_d=0.6,
        coverage_l=0.6,
        coverage_r=0.6,
        equip_ap_cost=400,
        ballistic_protection_level="PM 2",
        protection_ballistic=0.16,
        protection_physical=5,
        fits_bodypart_type='Head',
    ))
)

helmet_pasgt = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="PASGT Ballistic Helmet",
    weight=1.4,
    stacking=None,
    description='A kevlar helmet adopted by the US military in the 1980s and used until the mid 2000s.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.4,
        coverage_d=0.7,
        coverage_l=0.7,
        coverage_r=0.7,
        equip_ap_cost=400,
        ballistic_protection_level="PM 3",
        protection_ballistic=0.2,
        protection_physical=4,
        fits_bodypart_type='Head',
    ))
)

helmet_ech = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Enhanced Combat Helmet",
    weight=1.5,
    stacking=None,
    description='A combat helmet developed by the US Marine Corps and Army to replace the advanced combat helmet,'
                ' with improved ballistic protection through the use of advanced thermoplastics rather than ballistic '
                'fibres.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.4,
        coverage_d=0.7,
        coverage_l=0.7,
        coverage_r=0.7,
        equip_ap_cost=400,
        ballistic_protection_level="PM 4",
        protection_ballistic=0.28,
        protection_physical=4,
        fits_bodypart_type='Head',
    ))
)

helmet_ronin = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="DEVTAC Ronin Helmet",
    weight=2.17,
    stacking=None,
    description='A ballsitic combat helmet with full face mask produced by DEVTAC. '
                'It has a menacing skull-like visage.',
    usable_properties=(consumables.Wearable(
        coverage_v=1,
        coverage_d=1,
        coverage_l=1,
        coverage_r=1,
        equip_ap_cost=800,
        ballistic_protection_level="PM 4",
        protection_ballistic=0.28,
        protection_physical=4,
        fits_bodypart_type='Head',
    ))
)

helmet_altyn = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Altyn Ballistic Helmet",
    weight=3.5,
    stacking=None,
    description='A large titanium helmet developed for the Soviet military. It has seen continued use with Russian '
                'special forces.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.5,
        coverage_d=0.8,
        coverage_l=0.8,
        coverage_r=0.8,
        equip_ap_cost=800,
        ballistic_protection_level="PM 7",
        protection_ballistic=0.83,
        protection_physical=7,
        fits_bodypart_type='Head',
    ))
)

bodyarmour_pasgt = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="PASGT Vest",
    weight=11.4,
    stacking=None,
    description='A kevlar ballistic vest developed for the US military in the 1980s.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.8,
        coverage_d=0.8,
        coverage_l=0,
        coverage_r=0,
        ballistic_protection_level="PM 2",
        protection_ballistic=0.16,
        protection_physical=5,
        fits_bodypart_type='Body',
        equip_ap_cost=1000,
    ))
)

bodyarmour_interceptor = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Interceptor Outer Tactical Vest",
    weight=7.4,
    stacking=None,
    description='A kevlar ballistic vest developed for the US military in the 2000s to replace the older PASGT design.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.8,
        coverage_d=0.8,
        coverage_l=0,
        coverage_r=0,
        ballistic_protection_level="PM 3",
        protection_ballistic=0.2,
        protection_physical=6,
        fits_bodypart_type='Body',
        equip_ap_cost=1000,
    ))
)

bodyarmour_improved = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Improved Outer Tactical Vest",
    weight=14,
    stacking=None,
    description='A kevlar ballistic vest developed for the US military in the early 2010s to replace the Interceptor '
                'OTV, featuring greater ballsitic protection.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.8,
        coverage_d=0.8,
        coverage_l=0,
        coverage_r=0,
        ballistic_protection_level="PM 7",
        protection_ballistic=0.2,
        protection_physical=7,
        fits_bodypart_type='Body',
        equip_ap_cost=1000,
    ))
)

platecarrier_3a = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Plate Carrier - Level IIIa",
    weight=1.7,
    stacking=None,
    description='A plate carrier with level IIIA plates, rated to protect against pistol calibre rounds up to '
                '.44 Magnum.',
    usable_properties=(consumables.Wearable(
        coverage_v=0.7,
        coverage_d=0.0,
        coverage_l=0.05,
        coverage_r=0.05,
        ballistic_protection_level="PM 4",
        protection_ballistic=0.28,
        protection_physical=5,
        fits_bodypart_type='Body',
        equip_ap_cost=1000,
    ))
)

platecarrier_3 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Plate Carrier - Level III",
    weight=3.85,
    stacking=None,
    description='A plate carrier with level IIIA plates, rated to protect against rifle calibre rounds up to 7.62 NATO',
    usable_properties=(consumables.Wearable(
        coverage_v=0.7,
        coverage_d=0.0,
        coverage_l=0.05,
        coverage_r=0.05,
        ballistic_protection_level="PM 7",
        protection_ballistic=0.28,
        protection_physical=7,
        fits_bodypart_type='Body',
        equip_ap_cost=1000,
    ))
)

platecarrier_4 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    name="Plate Carrier - Level IV",
    weight=4.3,
    stacking=None,
    description='A plate carrier with level IV plates, rated to protect against rifle calibre rounds up to armour'
                ' piercing 30-06',
    usable_properties=(consumables.Wearable(
        coverage_v=0.7,
        coverage_d=0.0,
        coverage_l=0.05,
        coverage_r=0.05,
        ballistic_protection_level="PM 10",
        protection_ballistic=0.93,
        protection_physical=10,
        fits_bodypart_type='Body',
        equip_ap_cost=1000,
    ))
)
