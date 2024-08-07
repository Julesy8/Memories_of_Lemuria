import colour
from entity import Item
from components.consumables import DetachableMagazine, Clip

# TODO - add more magazines that have witness holes and are clear etc

"""
GLOCK 9mm
"""

glock_mag_9mm = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Magazine 9mm - Standard Capacity",
    weight=0.096,
    stacking=None,
    description='9mm Glock magazine - 17 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=('9mm', ),
        mag_capacity=17,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

glock_mag_9mm_33 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Magazine 9mm - Extended",
    weight=0.15,
    stacking=None,
    description='extended 9mm Glock magazine - 33 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=('9mm', ),
        mag_capacity=33,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.02,
        equip_ap_mod=1.06,
        witness=True,
        witness_check_ap=300,
    )
)

glock_mag_9mm_50 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Drum 9mm - 50 Rounds",
    weight=0.6,
    stacking=None,
    description='9mm Glock drum - 50 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=('9mm', ),
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.13,
        ap_distance_cost_mod=1.15,
        equip_ap_mod=1.18,
        failure_chance=2,
        witness=True,
        witness_check_ap=200,
    )
)

glock_mag_9mm_100 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Beta Mag 9mm - 100 Rounds",
    weight=1.36,
    stacking=None,
    description='9mm Glock Beta Mag - 100 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=('9mm', ),
        mag_capacity=100,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.21,
        ap_distance_cost_mod=1.23,
        equip_ap_mod=1.25,
        failure_chance=3,
        witness=True,
        witness_check_ap=200,
    )
)

"""Glock 10mm"""

glock_mag_10mm = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Magazine 10mm - Standard Capacity",
    weight=0.087,
    stacking=None,
    description='10mm Glock magazine - 15 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock 10mm',
        compatible_bullet_type=('10mm', ),
        mag_capacity=15,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

glock_mag_10mm_33 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Magazine 10mm - Extended",
    weight=0.215,
    stacking=None,
    description='10mm Glock-compatible Kriss vector magazine - 33 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock 10mm',
        compatible_bullet_type=('10mm', ),
        mag_capacity=33,
        magazine_size='medium',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.02,
        equip_ap_mod=1.06,
    )
)

glock_mag_10mm_50 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Drum 10mm - 50 Rounds",
    weight=0.79,
    stacking=None,
    description='10mm Glock drum - 50 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock 10mm',
        compatible_bullet_type=('10mm', ),
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.13,
        ap_distance_cost_mod=1.15,
        equip_ap_mod=1.18,
        failure_chance=2,
        witness=True,
        witness_check_ap=200,
    )
)

"""
Glock .50 GI
"""

glock_mag_50gi = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Magazine .50 GI",
    weight=0.09,
    stacking=None,
    description='.50 GI Glock magazine - 9 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock .50 GI',
        compatible_bullet_type=('.50 GI', ),
        mag_capacity=9,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

"""
Glock .40 S&W
"""

glock_mag_40 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Magazine .40 S&W - Standard Capacity",
    weight=0.08,
    stacking=None,
    description='.40 S&W Glock magazine - 15 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock .40 S&W',
        compatible_bullet_type=('40 S&W', ),
        mag_capacity=15,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

glock_mag_40_22 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Magazine .40 S&W - Extended",
    weight=0.136,
    stacking=None,
    description='.40 S&W Glock magazine - 31 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock .40 S&W',
        compatible_bullet_type=('40 S&W', ),
        mag_capacity=31,
        magazine_size='medium',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.02,
        equip_ap_mod=1.06,
    )
)

glock_mag_40_50 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Glock Drum .40 S&W - 50 Rounds",
    weight=0.68,
    stacking=None,
    description='.40 S&W Glock drum - 50 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='Glock .40 S&W',
        compatible_bullet_type=('40 S&W', ),
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.13,
        ap_distance_cost_mod=1.15,
        equip_ap_mod=1.18,
        failure_chance=2,
        witness=True,
        witness_check_ap=200,
    )
)

"""
1911 45
"""

m1911_mag_45_8 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="1911 .45 ACP Magazine - Standard Capacity",
    weight=0.0907,
    stacking=None,
    description='Steel 1911 .45 ACP magazine - 8 round standard capacity',
    usable_properties=DetachableMagazine(
        magazine_type='1911 .45 ACP',
        compatible_bullet_type=('.45 ACP',),
        mag_capacity=8,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

m1911_mag_45_10 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="1911 .45 ACP Magazine - 10 Rounds",
    weight=0.1,
    stacking=None,
    description='Extended 10 round capacity steel .45 ACP magazine for 1911 pistols designed by Wilson Combat. '
                'The polymer base plate has been extended such that it sits flush seamlessly with the magazine well.',
    usable_properties=DetachableMagazine(
        magazine_type='1911 .45 ACP',
        compatible_bullet_type=('.45 ACP',),
        mag_capacity=10,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

m1911_mag_45_15 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="1911 .45 ACP Extended Magazine - 15 Rounds",
    weight=0.17,
    stacking=None,
    description='Steel 1911 15 round extended magazine designed by ProMag',
    usable_properties=DetachableMagazine(
        magazine_type='1911 .45 ACP',
        compatible_bullet_type=('.45 ACP',),
        mag_capacity=15,
        magazine_size='medium',
        ap_to_load=330,
        witness=True,
        witness_check_ap=300,
    )
)

m1911_mag_45_40 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="1911 .45 ACP Drum Magazine - 40 Rounds",
    weight=0.85,
    stacking=None,
    description='Polymer .45 ACP 40 round drum magazine designed by ProMag.',
    usable_properties=DetachableMagazine(
        magazine_type='1911 .45 ACP',
        compatible_bullet_type=('.45 ACP',),
        mag_capacity=40,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.13,
        ap_distance_cost_mod=1.15,
        equip_ap_mod=1.18,
        failure_chance=2,
        witness=True,
        witness_check_ap=300,
    )
)

"""
1911 9
"""

m1911_mag_9_10 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="1911 9mm Magazine - Standard Capacity",
    weight=0.075,
    stacking=None,
    description='Steel 1911 9mm magazine - 10 round standard capacity',
    usable_properties=DetachableMagazine(
        magazine_type='1911 9mm',
        compatible_bullet_type=('9mm',),
        mag_capacity=10,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

"""
1911 10mm
"""

m1911_mag_10_8 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="1911 10mm Magazine - Standard Capacity",
    weight=0.073,
    stacking=None,
    description='Steel 1911 9mm magazine - 8 round standard capacity',
    usable_properties=DetachableMagazine(
        magazine_type='1911 10mm',
        compatible_bullet_type=('10mm',),
        mag_capacity=8,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

"""
1911 10mm
"""

m1911_mag_40sw_8 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="1911 40 S&W Magazine - Standard Capacity",
    weight=0.073,
    stacking=None,
    description='Steel 1911 9mm magazine - 8 round standard capacity',
    usable_properties=DetachableMagazine(
        magazine_type='1911 40 S&W',
        compatible_bullet_type=('40 S&W',),
        mag_capacity=8,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

"""
Tokarev TT-33
"""

tt33_magazine = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Tokarev TT-33 Magazine",
    weight=0.073,
    stacking=None,
    description='A steel TT-33 7.62x25 Tokarev magazine - 8 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='TT-33',
        compatible_bullet_type=('7.62x25 Tokarev',),
        mag_capacity=8,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

"""
PPSh-41
"""

ppsh_mag_35rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="PPSh 35 Round Magazine",
    weight=0.38,
    stacking=None,
    description='A steel, 35 round capacity 7.62x25 Tokarev magazine made for the PPSh-41',
    usable_properties=DetachableMagazine(
        magazine_type='PPSh-41',
        compatible_bullet_type=('7.62x25 Tokarev', '9mm'),
        mag_capacity=35,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.02,
        ap_distance_cost_mod=1.03,
        equip_ap_mod=1.03,
        witness_check_ap=200,
    )
)

ppsh_71rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="PPSh 71 Round Drum",
    weight=0.68,
    stacking=None,
    description='71 round capacity 7.62x25 Tokarev drum magazine designed for the PPSh-41',
    usable_properties=DetachableMagazine(
        magazine_type='PPSh-41',
        compatible_bullet_type=('7.62x25 Tokarev', '9mm'),
        mag_capacity=71,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.16,
        ap_distance_cost_mod=1.18,
        equip_ap_mod=1.22,
        failure_chance=2,
        witness_check_ap=200,
    )
)

"""
Desert Eagle .44
"""

de44_mag = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="DE XIX .44 Magazine",
    weight=0.127,
    stacking=None,
    description='A standard capacity, 8 round magazine for the Desert Eagle .44 Magnum.',
    usable_properties=DetachableMagazine(
        magazine_type='Desert Eagle .44',
        compatible_bullet_type=('.44 Magnum',),
        mag_capacity=8,
        magazine_size='small',
        ap_to_load=300,
        witness=True,
        witness_check_ap=300,
    )
)

"""
MAC 10 45
"""

mac10_mag_45 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M10/45 Magazine",
    weight=0.34,
    stacking=None,
    description='M10/45 magazine .45 ACP - 30 round capacity. Originally made for the M3 grease gun and '
                'later retrofitted for the M10/45.',
    usable_properties=DetachableMagazine(
        magazine_type='M10/45',
        compatible_bullet_type=('.45 ACP',),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

mac10_mag_45_extended = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M10/45 Extended Magazine",
    weight=0.4,
    stacking=None,
    description='M10/45 magazine .45 ACP - 40 round capacity. An original magazine modified for greater capacity',
    usable_properties=DetachableMagazine(
        magazine_type='M10/45',
        compatible_bullet_type=('.45 ACP',),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.05,
        ap_distance_cost_mod=1.05,
        equip_ap_mod=1.05,
        witness_check_ap=300,
    )
)

mac10_mag_9 = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M10/9 Magazine",
    weight=0.32,
    stacking=None,
    description='M10/9 Magazine 9mm - 32 round capacity',
    usable_properties=DetachableMagazine(
        magazine_type='M10/9',
        compatible_bullet_type=('9mm',),
        mag_capacity=32,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

"""
Grease Gun
"""

greasegun_mag = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M3 Grease Gun Magazine",
    weight=0.34,
    stacking=None,
    description='A steel, 30 round capacity .45 ACP magazine made for the M3 Grease Gun',
    usable_properties=DetachableMagazine(
        magazine_type='Grease Gun',
        compatible_bullet_type=('.45 ACP',),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

"""
Mosin Nagant
"""

mosin_nagant = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Mosin-Nagant Magazine",
    weight=0.23,
    stacking=None,
    description='An aftermarket "Archangel" 10 round capacity polymer magazine for 7.62x54R Mosin-Nagant rifles '
                'designed by ProMag',
    usable_properties=DetachableMagazine(
        magazine_type='Mosin-Nagant',
        compatible_bullet_type=('7.62x54R', ),
        mag_capacity=10,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.03,
        equip_ap_mod=1.06,
        witness_check_ap=300,
    )
)

mosin_clip = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Mosin-Nagant Clip",
    weight=0.0085,
    stacking=None,
    description='A 5 round capacity clip for Mosin-Nagant rifles',
    usable_properties=Clip(
        magazine_type='Mosin-Nagant Clip',
        compatible_bullet_type=('7.62x54R', ),
        mag_capacity=5,
        magazine_size='small',
        ap_to_load=500,
    )
)

"""
SVT-40
"""

svt_10rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="SVT-40 10 Round Magazine",
    weight=0.28,
    stacking=None,
    description='10 round capacity 7.62x54R magazine designed for the SVT-40 rifle.',
    usable_properties=DetachableMagazine(
        magazine_type='SVT-40',
        compatible_bullet_type=('7.62x54R', ),
        mag_capacity=10,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=200,
    )
)

svt_clip = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="SVT-40 Clip",
    weight=0.0085,
    stacking=None,
    description='A 5 round capacity clip for SVT-40 rifles',
    usable_properties=Clip(
        magazine_type='SVT-40 Clip',
        compatible_bullet_type=('7.62x54R', ),
        mag_capacity=5,
        magazine_size='small',
        ap_to_load=500,
    )
)


"""
SKS
"""

sks_clip = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="SKS Clip",
    weight=0.011,
    stacking=None,
    description='A 10 round capacity stripper clip for SKS rifles',
    usable_properties=Clip(
        magazine_type='SKS Clip',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=10,
        magazine_size='small',
        ap_to_load=500,
    )
)

sks_mag_20rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="SKS 20 Round Magazine",
    weight=0.112,
    stacking=None,
    description='An aftermarket polymer duckbill magazine designed by ProMag for SKS rifles. It holds 20 rounds '
                'and is compatible with unmodified SKS magazine wells.',
    usable_properties=DetachableMagazine(
        magazine_type='SKS Magazine',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=20,
        magazine_size='medium',
        ap_to_load=400,
        target_acquisition_ap_mod=1.04,
        ap_distance_cost_mod=1.04,
        equip_ap_mod=1.05,
        witness_check_ap=300,
    )
)

sks_mag_35rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="SKS 35 Round Magazine",
    weight=0.23,
    stacking=None,
    description='An aftermarket polymer duckbill magazine designed by ProMag for SKS rifles. It holds 35 rounds '
                'and is compatible with unmodified SKS magazine wells.',
    usable_properties=DetachableMagazine(
        magazine_type='SKS Magazine',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=20,
        magazine_size='medium',
        ap_to_load=500,
        target_acquisition_ap_mod=1.05,
        ap_distance_cost_mod=1.05,
        equip_ap_mod=1.06,
        witness_check_ap=300,
    )
)

sks_mag_75rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="SKS 75 Round Drum Magazine",
    weight=1.043,
    stacking=None,
    description='An aftermarket 75 round capacity steel drum magazine for the SKS in the style of an Kalashnikov drum '
                'magazine. It is compatible with unmodified SKS magazine wells.',
    usable_properties=DetachableMagazine(
        magazine_type='SKS Magazine',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=75,
        magazine_size='large',
        ap_to_load=600,
        target_acquisition_ap_mod=1.11,
        ap_distance_cost_mod=1.12,
        equip_ap_mod=1.15,
        failure_chance=3,
        witness_check_ap=300,
    )
)


"""
Model 629
"""

m629_clip = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Model 629 Moon Clip",
    weight=0.005,
    stacking=None,
    description='A 6 round capacity moon clip for the Smith & Wesson Model 629 .44 Magnum revolver.',
    usable_properties=Clip(
        magazine_type='S&W Model 629 Moon Clip',
        compatible_bullet_type=('.44 Magnum', ),
        mag_capacity=6,
        magazine_size='small',
        ap_to_load=300,
        requires_gun_empty=True
    )
)

""" 
Model 610
"""

m610_clip = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Model 610 Moon Clip",
    weight=0.005,
    stacking=None,
    description='A 6 round capacity moon clip for the Smith & Wesson Model 610 10mm / 40 S&W revolver.',
    usable_properties=Clip(
        magazine_type='S&W Model 629 Moon Clip',
        compatible_bullet_type=('10mm', '40 S&W'),
        mag_capacity=6,
        magazine_size='small',
        ap_to_load=300,
        requires_gun_empty=True
    )
)

"""
AK 7.62x39
"""

ak762_10rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 7.62x39 10 Round Magazine",
    weight=0.205,
    stacking=None,
    description='A polymer 10 round capacity 7.62x39 AK magazine',
    usable_properties=DetachableMagazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=10,
        magazine_size='small',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

ak762_20rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 7.62x39 20 Round Magazine",
    weight=0.281,
    stacking=None,
    description='A steel 20 round capacity 7.62x39 AK magazine of hungarian origin',
    usable_properties=DetachableMagazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=20,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

ak762_30rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 7.62x39 30 Round Magazine",
    weight=0.37,
    stacking=None,
    description='A steel 30 round capacity 7.62x39 AK magazine',
    usable_properties=DetachableMagazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

ak762_40rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 7.62x39 40 Round Magazine",
    weight=0.46,
    stacking=None,
    description='A steel 40 round capacity 7.62x39 AK magazine designed for RPK light machine guns',
    usable_properties=DetachableMagazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=40,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.04,
        ap_distance_cost_mod=1.03,
        equip_ap_mod=1.05,
        witness_check_ap=300,
    )
)

ak762_60rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AC-Unity AK 7.62x39 Quad Magazine",
    weight=0.35,
    stacking=None,
    description='A polymer 60 round capacity 7.62x39 AK quad stack magazine',
    usable_properties=DetachableMagazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=60,
        magazine_size='medium',
        ap_to_load=500,
        target_acquisition_ap_mod=1.07,
        ap_distance_cost_mod=1.08,
        equip_ap_mod=1.06,
        failure_chance=2,
        witness_check_ap=300,
    )
)

ak762_75rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 7.62x39 75 Round Drum Magazine",
    weight=0.2,
    stacking=None,
    description='75 round capacity 7.62x39 AK drum magazine',
    usable_properties=DetachableMagazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=75,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.11,
        ap_distance_cost_mod=1.12,
        equip_ap_mod=1.15,
        failure_chance=3,
        witness_check_ap=300,
    )
)

ak762_100rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 7.62x39 100 Round Drum",
    weight=1.3,
    stacking=None,
    description='100 round capacity 7.62x39 AK drum magazine',
    usable_properties=DetachableMagazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=('7.62x39', ),
        mag_capacity=100,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.2,
        ap_distance_cost_mod=1.22,
        equip_ap_mod=1.25,
        failure_chance=3,
        witness_check_ap=300,
    )
)

"""
AK 5.45x39
"""

ak545_30rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 5.45x39 Magazine",
    weight=0.215,
    stacking=None,
    description='Standard 30 round capacity 5.45x39 AK magazine',
    usable_properties=DetachableMagazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=('5.45x39', ),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

ak545_45rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="RPK-74 5.45x39 Magazine",
    weight=0.3,
    stacking=None,
    description='45 round capacity 5.45x39 AK magazine designed for RPK-74 light machine guns',
    usable_properties=DetachableMagazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=('5.45x39', ),
        mag_capacity=45,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.05,
        ap_distance_cost_mod=1.04,
        equip_ap_mod=1.07,
        witness_check_ap=300,
    )
)

ak545_60rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 5.45x39 Quad Magazine",
    weight=0.3,
    stacking=None,
    description='60 round capacity 5.45x39 AK quad stack magazine',
    usable_properties=DetachableMagazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=('5.45x39', ),
        mag_capacity=60,
        magazine_size='medium',
        ap_to_load=500,
        target_acquisition_ap_mod=1.06,
        ap_distance_cost_mod=1.06,
        equip_ap_mod=1.05,
        failure_chance=2,
        witness_check_ap=300,
    )
)

ak545_100rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="RPK-16 5.45x39 95 Round Drum",
    weight=0.68,
    stacking=None,
    description='95 round capacity 5.45x39 AK drum magazine intended for the RPK-16',
    usable_properties=DetachableMagazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=('5.45x39', ),
        mag_capacity=95,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.19,
        ap_distance_cost_mod=1.2,
        equip_ap_mod=1.25,
        failure_chance=3,
        witness_check_ap=300,
    )
)

"""
AK 5.56x45
"""

ak556_30rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AK 5.56x45 Magazine",
    weight=0.215,
    stacking=None,
    description='Standard 30 round capacity 5.56x45 AK magazine made for the AK-101',
    usable_properties=DetachableMagazine(
        magazine_type='AK 5.56x45',
        compatible_bullet_type=('5.56x45', ),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

"""
STANAG
"""

stanag_10rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="STANAG 10 Round Magazine",
    weight=0.070,
    stacking=None,
    description='10 round capacity polymer STANAG magazine',
    usable_properties=DetachableMagazine(
        magazine_type='STANAG',
        compatible_bullet_type=('5.56x45', '.300 Blackout'),
        mag_capacity=10,
        magazine_size='small',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

stanag_20rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="STANAG 20 Round Magazine",
    weight=0.090,
    stacking=None,
    description='20 round capacity polymer STANAG magazine',
    usable_properties=DetachableMagazine(
        magazine_type='STANAG',
        compatible_bullet_type=('5.56x45', '.300 Blackout'),
        mag_capacity=20,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

stanag_30rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="STANAG 30 Round Magazine",
    weight=0.117,
    stacking=None,
    description='Standard 30 round capacity STANAG magazine',
    usable_properties=DetachableMagazine(
        magazine_type='STANAG',
        compatible_bullet_type=('5.56x45', '.300 Blackout'),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

stanag_40rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="STANAG 40 Round Magazine",
    weight=0.2,
    stacking=None,
    description='40 round capacity STANAG magazine',
    usable_properties=DetachableMagazine(
        magazine_type='STANAG',
        compatible_bullet_type=('5.56x45', '.300 Blackout'),
        mag_capacity=40,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.02,
        equip_ap_mod=1.04,
        witness_check_ap=300,
    )
)

stanag_50rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="STANAG 50 Round Drum Magazine",
    weight=0.9,
    stacking=None,
    description='50 round capacity STANAG drum magazine designed by F5-MFG',
    usable_properties=DetachableMagazine(
        magazine_type='STANAG',
        compatible_bullet_type=('5.56x45', '.300 Blackout'),
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=400,
        target_acquisition_ap_mod=1.06,
        ap_distance_cost_mod=1.06,
        equip_ap_mod=1.09,
        failure_chance=1,
        witness_check_ap=300,
    )
)

stanag_60rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="STANAG 60 Round Magazine",
    weight=0.18,
    stacking=None,
    description='60 round capacity STANAG quad stack magazine designed by SureFire',
    usable_properties=DetachableMagazine(
        magazine_type='STANAG',
        compatible_bullet_type=('5.56x45', '.300 Blackout'),
        mag_capacity=60,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.07,
        ap_distance_cost_mod=1.07,
        equip_ap_mod=1.07,
        failure_chance=2,
        witness_check_ap=300,
    )
)

stanag_100rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="STANAG Beta C 100 Round Drum Magazine",
    weight=1.81,
    stacking=None,
    description='100 round capacity STANAG Beta C drum magazine',
    usable_properties=DetachableMagazine(
        magazine_type='STANAG',
        compatible_bullet_type=('5.56x45', '.300 Blackout'),
        mag_capacity=100,
        magazine_size='large',
        ap_to_load=600,
        target_acquisition_ap_mod=1.18,
        ap_distance_cost_mod=1.18,
        equip_ap_mod=1.25,
        failure_chance=3,
        witness=True,
        witness_check_ap=300,
    )
)

"""
MCR 
"""

mcr_100rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="MCR 200 Round Linked Ammunition Magazine",
    weight=0.63,
    stacking=None,
    description='200 round capacity soft ammo pack for holding linked 5.56x45 ammunition.',
    usable_properties=DetachableMagazine(
        magazine_type='MCR Linked Ammunition Magazine',
        compatible_bullet_type=('5.56x45',),
        mag_capacity=200,
        magazine_size='large',
        ap_to_load=800,
        target_acquisition_ap_mod=1.22,
        ap_distance_cost_mod=1.22,
        equip_ap_mod=1.25,
        witness=True,
        witness_check_ap=20,
    )
)

"""
AR-10
"""

ar10_10rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AR-10 7.62x51 10 Round Magazine",
    weight=0.11,
    stacking=None,
    description='A polymer 10 round 7.62x51 magazine for AR-10 type rifles',
    usable_properties=DetachableMagazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=10,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

ar10_20rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AR-10 7.62x51 20 Round Magazine",
    weight=0.17,
    stacking=None,
    description='A polymer 20 round 7.62x51 magazine for AR-10 type rifles',
    usable_properties=DetachableMagazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=20,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=300,
    )
)

ar10_25rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AR-10 7.62x51 25 Round Magazine",
    weight=0.206,
    stacking=None,
    description='A polymer 25 round 7.62x51 magazine for AR-10 type rifles',
    usable_properties=DetachableMagazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=25,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.02,
        ap_distance_cost_mod=1.01,
        equip_ap_mod=1.02,
        witness_check_ap=300,
    )
)

ar10_40rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AR-10 7.62x51 40 Round Magazine",
    weight=0.226,
    stacking=None,
    description='A polymer 40 round 7.62x51 magazine for AR-10 type rifles',
    usable_properties=DetachableMagazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=40,
        magazine_size='large',
        ap_to_load=400,
        target_acquisition_ap_mod=1.05,
        ap_distance_cost_mod=1.04,
        equip_ap_mod=1.06,
        failure_chance=1,
        witness_check_ap=300,
    )
)

ar10_50rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="AR-10 7.62x51 50 Round Drum Magazine",
    weight=0.771,
    stacking=None,
    description='A polymer 50 round 7.62x51 drum magazine for AR-10 type rifles',
    usable_properties=DetachableMagazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.07,
        ap_distance_cost_mod=1.06,
        equip_ap_mod=1.12,
        failure_chance=2,
        witness_check_ap=300,
    )
)

"""
Calico
"""

calico_9mm_50rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Calico 9mm 50 Round Magazine",
    weight=0.5,
    stacking=None,
    description='50 round capacity 9mm helical magazine by Calico',
    usable_properties=DetachableMagazine(
        magazine_type='Calico 9mm',
        compatible_bullet_type=('9mm', ),
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.13,
        ap_distance_cost_mod=1.17,
        equip_ap_mod=1.14,
        failure_chance=1,
        witness_check_ap=200,
    )
)

calico_9mm_100rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Calico 9mm 100 Round Magazine",
    weight=1.03,
    stacking=None,
    description='100 round capacity 9mm helical magazine by Calico',
    usable_properties=DetachableMagazine(
        magazine_type='Calico 9mm',
        compatible_bullet_type=('9mm', ),
        mag_capacity=100,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.23,
        ap_distance_cost_mod=1.25,
        equip_ap_mod=1.3,
        failure_chance=1,
        witness_check_ap=200,
    )
)

"""
Suomi M31
"""

m31_9mm_36rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Suomi M31 9mm 36 Round Magazine",
    weight=0.34,
    stacking=None,
    description='36 round capacity 9mm magazine designed for the Suomi M31 submachinegun',
    usable_properties=DetachableMagazine(
        magazine_type='Suomi M31',
        compatible_bullet_type=('9mm', ),
        mag_capacity=36,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.02,
        ap_distance_cost_mod=1.03,
        equip_ap_mod=1.03,
        witness=True,
        witness_check_ap=200,
    )
)

m31_9mm_71rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Suomi M31 9mm 71 Round Drum",
    weight=0.68,
    stacking=None,
    description='71 round capacity 9mm drum magazine designed for the Suomi M31 submachinegun',
    usable_properties=DetachableMagazine(
        magazine_type='Suomi M31',
        compatible_bullet_type=('9mm', ),
        mag_capacity=71,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.16,
        ap_distance_cost_mod=1.18,
        equip_ap_mod=1.22,
        failure_chance=2,
        witness_check_ap=200,
    )
)

"""
M1 Carbine
"""

m1_carbine_15rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M1/M2 Carbine 15 Round Magazine",
    weight=0.0765,
    stacking=None,
    description='15 round capacity .30 carbine magazine designed for the M1 and M2 carbine',
    usable_properties=DetachableMagazine(
        magazine_type='M1/M2 Carbine',
        compatible_bullet_type=('.30 Carbine', ),
        mag_capacity=15,
        magazine_size='small',
        ap_to_load=300,
        target_acquisition_ap_mod=1.02,
        ap_distance_cost_mod=1.03,
        equip_ap_mod=1.03,
        witness_check_ap=200,
    )
)

m1_carbine_30rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M1/M2 Carbine 30 Round Magazine",
    weight=0.09,
    stacking=None,
    description='30 round capacity .30 carbine magazine designed for the M1 and M2 carbine',
    usable_properties=DetachableMagazine(
        magazine_type='M1/M2 Carbine',
        compatible_bullet_type=('.30 Carbine', ),
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=330,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.02,
        equip_ap_mod=1.03,
        witness_check_ap=200,
    )
)

"""
M14
"""

m14_10rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M14/M1A 10 Round Magazine",
    weight=0.159,
    stacking=None,
    description='10 round capacity 7.62x51 NATO magazine designed for the M14 and M1A rifles',
    usable_properties=DetachableMagazine(
        magazine_type='M14/M1A',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=10,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=200,
    )
)

m14_20rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M14/M1A 20 Round Magazine",
    weight=0.233,
    stacking=None,
    description='20 round capacity 7.62x51 NATO magazine designed for the M14 and M1A rifles',
    usable_properties=DetachableMagazine(
        magazine_type='M14/M1A',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=20,
        magazine_size='medium',
        ap_to_load=300,
        witness_check_ap=200,
    )
)

m14_50rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="M14/M1A ProMag 50 Round Drum Magazine",
    weight=0.771,
    stacking=None,
    description='50 round capacity 7.62x51 NATO polymer drum magazine designed by ProMag for the M14 and M1A rifles',
    usable_properties=DetachableMagazine(
        magazine_type='M14/M1A',
        compatible_bullet_type=('7.62x51', ),
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.07,
        ap_distance_cost_mod=1.06,
        equip_ap_mod=1.12,
        failure_chance=2,
        witness_check_ap=200,
    )
)

"""
R870 DM
"""

r870_6rd = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_BROWN,
    name="Model 870 DM 6 Round Magazine",
    weight=0.21,
    stacking=None,
    description='6 round box magazine for the magazine fed DM model of the Remington 870',
    usable_properties=DetachableMagazine(
        magazine_type='R870 DM',
        compatible_bullet_type=('12 Gauge', ),
        mag_capacity=6,
        magazine_size='medium',
        ap_to_load=400,
        witness_check_ap=200,
    )
)
