import colour
from entity import Item, Stacking
from components.consumables import Bullet

# ammunition specifications from Alliant powder catalogue 2020

# drag coefficients by projectile type
cd_wadcutter = 0.8333
cd_jhp = 0.441511
cd_fmj_round_nose = 0.573576
cd_cruciform_flat_nose = 0.597175
cd_truncated_cone = 0.551937
cd_sem_wadcutter = 0.551937
cd_60_degree_conical = 0.5
cd_round_ball = 0.414214

cd_spitzer = 0.24

# Cf = Cd / 0.83333

# projectile configuration factor
cf_wadcutter = 1
cf_jhp = 0.819152
cf_fmj_round_nose = 0.688292
cf_cruciform_flat_nose = 0.71661
cf_truncated_cone = 0.662324
cf_sem_wadcutter = 0.662324
cf_60_degree_conical = 0.6
cf_round_ball = 0.497056

cf_spitzer = 0.28


"""
9MM
"""

# powder - sport pistol

# FMJ
round_9mm_115_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 115gr FMJ',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='9x19mm 115gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=115,
        charge_mass=4.8,
        diameter=0.355,
        velocity=1151,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.0,
        sound_modifier=23.54,
        ballistic_coefficient=0.155
    )
)

round_9mm_124_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 124gr FMJ',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='9x19mm 124gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=124,
        charge_mass=4.5,
        diameter=0.355,
        velocity=1089,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.0,
        sound_modifier=24.02,
        ballistic_coefficient=0.192
    )
)

round_9mm_147_fp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 147gr FP',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='9x19mm 147gr jacketed flat point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=147,
        charge_mass=3.5,
        diameter=0.355,
        velocity=890,
        proj_config=cf_cruciform_flat_nose,
        drag_coefficient=cd_cruciform_flat_nose,
        spread_modifier=0.0,
        sound_modifier=23.27,
        ballistic_coefficient=0.2
    )
)

# FMJ +P
round_9mm_115_fmj_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 115gr FMJ +P',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='Overpressure 9x19mm 115gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=115,
        charge_mass=5.1,
        diameter=0.355,
        velocity=1200,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.0,
        sound_modifier=24.54,
        ballistic_coefficient=0.155
    )
)

round_9mm_124_fmj_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 124gr FMJ +P',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='Overpressure 9x19mm 124gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=124,
        charge_mass=4.8,
        diameter=0.355,
        velocity=1140,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.0,
        sound_modifier=25.14,
        ballistic_coefficient=0.22
    )
)

round_9mm_147_fp_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 147gr FP +P',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='Overpressure 9x19mm 147gr jacketed flat point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=147,
        charge_mass=3.7,
        diameter=0.355,
        velocity=956,
        proj_config=cf_cruciform_flat_nose,
        drag_coefficient=cd_cruciform_flat_nose,
        spread_modifier=0.0,
        sound_modifier=24.99,
        ballistic_coefficient=0.2
    )
)

#HP

round_9mm_115_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 115gr JHP',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='9x19mm 115gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=115,
        charge_mass=4.7,
        diameter=0.355,
        velocity=1147,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=23.46,
        ballistic_coefficient=0.13
    )
)

round_9mm_124_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 124gr JHP',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='9x19mm 124gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=124,
        charge_mass=4.4,
        diameter=0.355,
        velocity=1087,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=23.97,
        ballistic_coefficient=0.17
    )
)

round_9mm_147_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 147gr JHP',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='9x19mm 147gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=147,
        charge_mass=3.6,
        diameter=0.355,
        velocity=894,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=23.37,
        ballistic_coefficient=0.197
    )
)

#HP +P

round_9mm_115_jhp_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 115gr JHP +P',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='Overpressure 9x19mm 115gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=115,
        charge_mass=5.1,
        diameter=0.355,
        velocity=1208,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=24.71,
        ballistic_coefficient=0.13
    )
)

round_9mm_124_jhp_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 124gr JHP +P',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='Overpressure 9x19mm 124gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=124,
        charge_mass=4.7,
        diameter=0.355,
        velocity=1140,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=25.14,
        ballistic_coefficient=0.17
    )
)

round_9mm_147_jhp_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='9x19mm - 147gr JHP +P',
    weight=0.006,
    stacking=Stacking(stack_size=10),
    description='Overpressure 9x19mm 147gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=147,
        charge_mass=3.8,
        diameter=0.355,
        velocity=934,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=24.42,
        ballistic_coefficient=0.197
    )
)


"""
45
"""

# swc

round_45_185_swc = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 185gr Jacketed SWC',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='45 Automatic 185gr copper jacketed semi wad cutter ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=185,
        charge_mass=5.9,
        diameter=0.452,
        velocity=1038,
        proj_config=cf_sem_wadcutter,
        drag_coefficient=cd_sem_wadcutter,
        spread_modifier=0.0,
        sound_modifier=34.15,
        ballistic_coefficient=0.09
    )
)

round_45_200_swc = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 200gr Jacketed SWC',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='45 Automatic 200gr copper jacketed semi wad cutter ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=200,
        charge_mass=5.2,
        diameter=0.452,
        velocity=956,
        proj_config=cf_sem_wadcutter,
        drag_coefficient=cd_sem_wadcutter,
        spread_modifier=0.0,
        sound_modifier=34.0,
        ballistic_coefficient=0.07
    )
)

# JHP

round_45_185_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 185gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='45 Automatic 185gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=185,
        charge_mass=6.7,
        diameter=0.452,
        velocity=1071,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=35.24,
        ballistic_coefficient=0.1
    )
)

round_45_200_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 200gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='45 Automatic 200gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=200,
        charge_mass=6.2,
        diameter=0.452,
        velocity=980,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=34.86,
        ballistic_coefficient=0.15
    )
)

round_45_230_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 230gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='45 Automatic 230gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=230,
        charge_mass=5.3,
        diameter=0.452,
        velocity=867,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=35.46,
        ballistic_coefficient=0.205
    )
)

# FMJ

round_45_200_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 200gr FMJ',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='45 Automatic 200gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=200,
        charge_mass=6.4,
        diameter=0.355,
        velocity=986,
        proj_config=0.688292,
        drag_coefficient=0.573576,
        spread_modifier=0.0,
        sound_modifier=35.07,
        ballistic_coefficient=0.15
    )
)

round_45_230_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 230gr FMJ',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='45 Automatic 230gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=230,
        charge_mass=5.9,
        diameter=0.355,
        velocity=914,
        proj_config=0.688292,
        drag_coefficient=0.573576,
        spread_modifier=0.0,
        sound_modifier=37.39,
        ballistic_coefficient=0.205
    )
)

# swc +P

round_45_185_swc_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 185gr Jacketed SWC +P',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='Overpressure 45 Automatic 185gr copper jacketed semi wad cutter ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=185,
        charge_mass=6.2,
        diameter=0.452,
        velocity=1025,
        proj_config=cf_sem_wadcutter,
        drag_coefficient=cd_sem_wadcutter,
        spread_modifier=0.0,
        sound_modifier=33.72,
        ballistic_coefficient=0.09
    )
)

round_45_200_swc_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 200gr Jacketed SWC +P',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='Overpressure 45 Automatic 200gr copper jacketed semi wad cutter ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=200,
        charge_mass=5.4,
        diameter=0.452,
        velocity=983,
        proj_config=cf_sem_wadcutter,
        drag_coefficient=cd_sem_wadcutter,
        spread_modifier=0.0,
        sound_modifier=34.96,
        ballistic_coefficient=0.07
    )
)


# JHP +P

round_45_185_jhp_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 185gr JHP +P',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='Overpressure 45 Automatic 185gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=185,
        charge_mass=7.0,
        diameter=0.452,
        velocity=1111,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=36.55,
        ballistic_coefficient=0.1
    )
)

round_45_230_jhp_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 230gr JHP +P',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='Overpressure 45 Automatic 230gr full metal jacket hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='.45 ACP',
        mass=230,
        charge_mass=5.6,
        diameter=0.452,
        velocity=910,
        proj_config=cf_jhp,
        drag_coefficient=cd_jhp,
        spread_modifier=0.0,
        sound_modifier=37.22,
        ballistic_coefficient=0.205
    )
)

# FMJ +P

round_45_200_fmj_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 200gr FMJ  +P',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='Overpressure 45 Automatic 200gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=200,
        charge_mass=6.7,
        diameter=0.355,
        velocity=1035,
        proj_config=0.688292,
        drag_coefficient=0.573576,
        spread_modifier=0.0,
        sound_modifier=36.81,
        ballistic_coefficient=0.15
    )
)

round_45_230_fmj_pp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='45 ACP - 230gr FMJ  +P',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='Overpressure 45 Automatic 230gr full metal jacket round point ammunition',
    usable_properties=Bullet(
        bullet_type='9mm',
        mass=230,
        charge_mass=6.2,
        diameter=0.355,
        velocity=958,
        proj_config=0.688292,
        drag_coefficient=0.573576,
        spread_modifier=0.0,
        sound_modifier=39.19,
        ballistic_coefficient=0.205
    )
)

"""
7.62 x 39
"""
# 16 inch barrel length
# powder - N130 or closest

#FMJ

round_76239_123_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x39mm - 123gr FMJ',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='7.62x39mm 123gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x39',
        mass=123,
        charge_mass=27.3,
        diameter=0.311,
        velocity=2361,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=51.65,
        ballistic_coefficient=0.282
    )
)

round_76239_150_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x39mm - 150gr FMJ',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='7.62x39mm 150gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x39',
        mass=150,
        charge_mass=24.4,
        diameter=0.311,
        velocity=2185,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=58.29,
        ballistic_coefficient=0.341
    )
)

# SST (21 in barrel)

round_76239_123_sst = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x39mm - 123gr SST',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='7.62x39mm 123gr copper jacketed "super shock tip" polymer tipped ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x39',
        mass=123,
        charge_mass=27.3,
        diameter=0.311,
        velocity=2445,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=53.48,
        ballistic_coefficient=0.295
    )
)

# soft point (21 in barrel)

round_76239_150_sp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x39mm - 150gr SP',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='7.62x39mm 150gr copper jacketed soft point ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x39',
        mass=150,
        charge_mass=23.6,
        diameter=0.311,
        velocity=2109,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=56.26,
        ballistic_coefficient=0.341
    )
)

"""
5.56 
"""
# 14 inch barrel length
# powder - XMR-2015

round_556_55_sp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.56 NATO - 55gr SP',
    weight=0.012,
    stacking=Stacking(stack_size=10),
    description='5.56x45mm NATO 55gr jacketed soft point ammunition',
    usable_properties=Bullet(
        bullet_type='5.56x45',
        mass=55,
        charge_mass=21.7,
        diameter=0.224,
        velocity=3067,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=30.0,
        ballistic_coefficient=0.204
    )
)

round_556_60_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.56 NATO - 60gr V-Max',
    weight=0.012,
    stacking=Stacking(stack_size=10),
    description='5.56x45mm NATO 60gr jacketed VMAX ammunition',
    usable_properties=Bullet(
        bullet_type='5.56x45',
        mass=60,
        charge_mass=24.5,
        diameter=0.224,
        velocity=3217,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=34.33,
        ballistic_coefficient=0.323
    )
)

round_556_75_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.56 NATO - 75gr A-Max',
    weight=0.012,
    stacking=Stacking(stack_size=10),
    description='5.56x45mm NATO 75gr jacketed A-MAX polymer tipped ammunition',
    usable_properties=Bullet(
        bullet_type='5.56x45',
        mass=75,
        charge_mass=22.6,
        diameter=0.224,
        velocity=2798,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=37.32,
        ballistic_coefficient=0.435
    )
)

round_556_69_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.56 NATO - 69gr HPBT',
    weight=0.012,
    stacking=Stacking(stack_size=10),
    description='5.56x45mm NATO 69gr copper jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='5.56x45',
        mass=69,
        charge_mass=24.0,
        diameter=0.224,
        velocity=2936,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=36.03,
        ballistic_coefficient=0.301
    )
)

round_556_80_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.56 NATO - 80gr HPBT',
    weight=0.012,
    stacking=Stacking(stack_size=10),
    description='5.56x45mm NATO 80gr copper jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='5.56x45',
        mass=80,
        charge_mass=22.2,
        diameter=0.224,
        velocity=2742,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=39.01,
        ballistic_coefficient=0.461
    )
)


"""
300 blackout
"""

# barrel - 16 inch
# powder - accurate 1680

round_300aac_150_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='.300 Blackout - 150gr HPBT',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='.300 AAC Blackout 150 gr copper jacketed hollow point boat tail ammunition',
    usable_properties=Bullet(
        bullet_type='.300 Blackout',
        mass=150,
        charge_mass=21.6,
        diameter=0.308,
        velocity=2086,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=55.65,
        ballistic_coefficient=0.397
    )
)

round_300aac_150_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='.300 Blackout - 150gr FMJ',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='.300 AAC Blackout 150 gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='.300 Blackout',
        mass=150,
        charge_mass=21.7,
        diameter=0.308,
        velocity=2057,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=54.87,
        ballistic_coefficient=0.397
    )
)

round_300aac_210_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='.300 Blackout - 210gr FMJ',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='.300 AAC Blackout 210 gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='.300 Blackout',
        mass=210,
        charge_mass=16,
        diameter=0.308,
        velocity=1582,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=59.08,
        ballistic_coefficient=0.65
    )
)

round_300aac_210_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='.300 Blackout - 210gr HPBT',
    weight=0.016,
    stacking=Stacking(stack_size=10),
    description='.300 AAC Blackout 210 gr copper jacketed hollow point boat tail ammunition',
    usable_properties=Bullet(
        bullet_type='.300 Blackout',
        mass=210,
        charge_mass=12,
        diameter=0.308,
        velocity=1263,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=47.17,
        ballistic_coefficient=0.65
    )
)

"""
5.45
"""

# barrel length - 26 inches

round_545_56_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.45x39 - 56gr FMJ',
    weight=0.01,
    stacking=Stacking(stack_size=10),
    description='5.45x39 56 gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='5.45x39',
        mass=56,
        charge_mass=19.5,
        diameter=0.22,
        velocity=2980,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=29.68,
        ballistic_coefficient=0.209
    )
)

round_545_63_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.45x39 - 63gr FMJ',
    weight=0.01,
    stacking=Stacking(stack_size=10),
    description='5.45x39 63 gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='5.45x39',
        mass=63,
        charge_mass=19.3,
        diameter=0.22,
        velocity=2798,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=31.35,
        ballistic_coefficient=0.235
    )
)

round_545_60_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='5.45x39 - 60gr JHP',
    weight=0.01,
    stacking=Stacking(stack_size=10),
    description='5.45x39 60 gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='5.45x39',
        mass=60,
        charge_mass=18.5,
        diameter=0.22,
        velocity=2787,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=29.74,
        ballistic_coefficient=0.240
    )
)

"""
7.62x51 
"""

round_308_130_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x51 - 130gr JHP',
    weight=0.024,
    stacking=Stacking(stack_size=10),
    description='7.62x51 130 gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x51',
        mass=130,
        charge_mass=47.6,
        diameter=0.308,
        velocity=3182,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=73.57,
        ballistic_coefficient=0.263
    )
)

round_308_150_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x51 - 150gr FMJ',
    weight=0.024,
    stacking=Stacking(stack_size=10),
    description='7.62x51 150 gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x51',
        mass=150,
        charge_mass=44.5,
        diameter=0.308,
        velocity=2929,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=78.14,
        ballistic_coefficient=0.38
    )
)

round_308_165_sp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x51 - 165gr FMJ',
    weight=0.024,
    stacking=Stacking(stack_size=10),
    description='7.62x51 130 gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x51',
        mass=150,
        charge_mass=42.1,
        diameter=0.308,
        velocity=2751,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=73.39,
        ballistic_coefficient=0.404
    )
)

round_308_180_tsx = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x51 - 180gr TSX',
    weight=0.024,
    stacking=Stacking(stack_size=10),
    description='7.62x51 180 gr all-copper ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x51',
        mass=180,
        charge_mass=40.5,
        diameter=0.308,
        velocity=2572,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=82.34,
        ballistic_coefficient=0.484
    )
)


"""
7.62x54R
"""

# 'original' ammunition, 210gr projectile travelling 2200fps, muzzle energy 2257
round_54r_174_jrn = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x54R - 174gr Jacketed RN',
    weight=0.024,
    stacking=Stacking(stack_size=10),
    description='7.62x54R 174 gr jacketed round nose ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x54R',
        mass=174,
        charge_mass=45.5,
        diameter=0.3105,
        velocity=2496,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.0,
        sound_modifier=77.24,
        ballistic_coefficient=0.262
    )
)

round_54r_180_jsp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x54R - 180gr Jacketed SP',
    weight=0.024,
    stacking=Stacking(stack_size=10),
    description='7.62x54R 150 gr jacketed soft point ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x54R',
        mass=180,
        charge_mass=45.5,
        diameter=0.3105,
        velocity=2488,
        proj_config=cd_jhp,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=79.65,
        ballistic_coefficient=0.411
    )
)

round_54r_200_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x54R - 200gr Jacketed RN',
    weight=0.024,
    stacking=Stacking(stack_size=10),
    description='7.62x54R 200 gr full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x54R',
        mass=200,
        charge_mass=32.5,
        diameter=0.3105,
        velocity=2108,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.0,
        sound_modifier=74.98,
        ballistic_coefficient=0.344
    )
)

"""
12 guage
"""
"""
# 54gr projectile travelling 1200fps, muzzle energy 1,547
round_buckshot_12 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='12 Guage Buckshot',
    weight=0.0,
    stacking=Stacking(stack_size=10),
    description='12 guage buckshot round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='9mm',
        meat_damage=9,
        armour_damage=5,
        accuracy_factor=0.9,
        recoil_modifier=12,
        sound_modifier=20,
        projectile_no=9,
        range_modifier=0.082,
    )
)

# 437.5gr projectile travelling 1560fps, muzzle energy 2363
round_slug_12 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='12 Guage Buckshot',
    weight=0.0,
    stacking=Stacking(stack_size=10),
    description='12 guage buckshot round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='9mm',
        meat_damage=100,
        armour_damage=28,
        accuracy_factor=0.95,
        recoil_modifier=18.4,
        sound_modifier=24,
        range_modifier=0.24,
    )
)
"""

bullet_list = (round_9mm_115_fmj, round_9mm_124_fmj, round_9mm_147_fp, round_9mm_115_fmj_pp,
               round_9mm_124_fmj_pp, round_9mm_147_fp_pp, round_9mm_115_jhp, round_9mm_124_jhp,
               round_9mm_147_jhp, round_9mm_115_jhp_pp, round_9mm_124_jhp_pp, round_9mm_147_jhp_pp, round_45_185_swc,
               round_45_200_swc, round_45_185_jhp, round_45_200_jhp, round_45_230_jhp, round_45_200_fmj,
               round_45_230_fmj, round_45_185_swc_pp, round_45_200_swc_pp, round_45_185_jhp_pp, round_45_230_jhp_pp,
               round_45_200_fmj_pp, round_45_230_fmj_pp, round_76239_123_fmj, round_76239_150_fmj,
               round_76239_123_sst, round_76239_150_sp, round_556_55_sp, round_556_60_fmj,
               round_556_75_fmj, round_556_69_jhp, round_556_80_jhp, round_300aac_150_jhp, round_300aac_150_fmj,
               round_300aac_210_fmj, round_300aac_210_jhp, round_545_56_fmj, round_545_63_fmj, round_545_60_jhp,
               round_308_130_jhp, round_308_150_fmj, round_308_165_sp, round_308_180_tsx, round_54r_174_jrn,
               round_54r_180_jsp, round_54r_200_fmj
               )


