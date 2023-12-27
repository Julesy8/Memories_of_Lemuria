import colour
from entity import Item, Stacking
from components.consumables import Bullet

# TODO - new specialised types of bullets particularly armour piercing

# drag coefficients by projectile type
cd_wadcutter = 0.8333
cd_jhp = 0.441511  # assumes expansion, if not expanded default to different value
cd_fmj_round_nose = 0.573576
cd_cruciform_flat_nose = 0.597175
cd_truncated_cone = 0.551937
cd_sem_wadcutter = 0.551937
cd_60_degree_conical = 0.5
cd_round_ball = 0.414214

cd_spitzer = 0.53

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
cf_spitzer = 0.6385

"""
9MM
"""

# source: 2020 Alliant Powder Catalog
# test barrel length: 4 inches
# powder: sport pistol

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
        spread_modifier=0.05,
        ballistic_coefficient=0.155,
        bullet_length=0.55,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.192,
        bullet_length=0.55,
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
        proj_config=cf_truncated_cone,
        drag_coefficient=cd_truncated_cone,
        spread_modifier=0.05,
        ballistic_coefficient=0.2,
        bullet_length=0.55,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.155,
        bullet_length=0.55,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.22,
        bullet_length=0.55,
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
        proj_config=cf_truncated_cone,
        drag_coefficient=cd_truncated_cone,
        spread_modifier=0.05,
        ballistic_coefficient=0.2,
        bullet_length=0.55,
    )
)

# HP

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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.13,
        bullet_length=0.55,
        bullet_expands=True,
        max_expansion=1.57,
        max_expansion_velocity=1489,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.17,
        bullet_length=0.55,
        bullet_expands=True,
        max_expansion=1.57,
        max_expansion_velocity=1489,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.197,
        bullet_length=0.55,
        bullet_expands=True,
        max_expansion=1.57,
        max_expansion_velocity=1489,
    )
)

# HP +P

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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.13,
        bullet_length=0.55,
        bullet_expands=True,
        max_expansion=1.57,
        max_expansion_velocity=1489,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.17,
        bullet_length=0.55,
        bullet_expands=True,
        max_expansion=1.57,
        max_expansion_velocity=1489,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.197,
        bullet_length=0.55,
        bullet_expands=True,
        max_expansion=1.57,
        max_expansion_velocity=1489,
    )
)

"""
45 
"""

# source: 2020 Alliant Powder Catalog
# test barrel length: 5 inches
# powder: sport pistol

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
        spread_modifier=0.05,
        ballistic_coefficient=0.09,
        bullet_length=0.602,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.07,
        bullet_length=0.602,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.1,
        bullet_length=0.602,
        bullet_expands=True,
        max_expansion=1.55,
        max_expansion_velocity=1150,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.15,
        bullet_length=0.602,
        bullet_expands=True,
        max_expansion=1.55,
        max_expansion_velocity=1150,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.205,
        bullet_length=0.602,
        bullet_expands=True,
        max_expansion=1.55,
        max_expansion_velocity=1150,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.15,
        bullet_length=0.602,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.205,
        bullet_length=0.602,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.09,
        bullet_length=0.602,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.07,
        bullet_length=0.602,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.1,
        bullet_length=0.602,
        bullet_expands=True,
        max_expansion=1.55,
        max_expansion_velocity=1150,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.205,
        bullet_length=0.602,
        bullet_expands=True,
        max_expansion=1.55,
        max_expansion_velocity=1150,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.15,
        bullet_length=0.602,
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
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.205,
        bullet_length=0.602,
    )
)

"""
10mm
"""

# source: 2020 Alliant Powder Catalog
# test barrel length: 5 inches
# powder: sport pistol

round_10mm_155_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='10mm - 155gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='10mm Automatic 155gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='10mm',
        mass=155,
        charge_mass=8.5,
        diameter=0.4,
        velocity=1246,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.137,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.64,
        max_expansion_velocity=1155,
    )
)

round_10mm_180_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='10mm - 180gr FMJ',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='10mm Automatic 180gr full metal jacket round nose ammunition',
    usable_properties=Bullet(
        bullet_type='10mm',
        mass=180,
        charge_mass=8.3,
        diameter=0.4,
        velocity=1265,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.138,
        bullet_length=0.525,
    )
)

round_10mm_190_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='10mm - 190gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='10mm Automatic 190gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='10mm',
        mass=190,
        charge_mass=7.4,
        diameter=0.4,
        velocity=1182,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.138,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.64,
        max_expansion_velocity=1155,
    )
)

round_10mm_220_fp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='10mm - 220gr FP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='10mm Automatic 190gr jacketed flat point ammunition',
    usable_properties=Bullet(
        bullet_type='10mm',
        mass=220,
        charge_mass=4.7,
        diameter=0.4,
        velocity=929,
        proj_config=cf_truncated_cone,
        drag_coefficient=cd_truncated_cone,
        spread_modifier=0.05,
        ballistic_coefficient=0.137,
        bullet_length=0.525,
    )
)

"""
40 S&W
"""

# source: 2020 Alliant Powder Catalog
# test barrel length: 4 inches
# powder: sport pistol

round_40sw_155_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='40 S&W - 155gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='40 S&W 155gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='40 S&W',
        mass=155,
        charge_mass=5.6,
        diameter=0.4,
        velocity=1101,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.137,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.64,
        max_expansion_velocity=1155,
    )
)

round_40sw_165_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='40 S&W - 165gr FMJ',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='40 S&W 165 gr flat point full metal jacket ammunition',
    usable_properties=Bullet(
        bullet_type='40 S&W',
        mass=165,
        charge_mass=5.6,
        diameter=0.4,
        velocity=1070,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.138,
        bullet_length=0.525,
    )
)

round_40sw_180_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='40 S&W - 180gr FMJ',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='40 S&W 180gr full metal jacket round nose ammunition',
    usable_properties=Bullet(
        bullet_type='40 S&W',
        mass=180,
        charge_mass=5.0,
        diameter=0.4,
        velocity=978,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.138,
        bullet_length=0.525,
    )
)

round_40sw_180_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='40 S&W - 180gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='40 S&W 180gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='40 S&W',
        mass=180,
        charge_mass=4.6,
        diameter=0.4,
        velocity=958,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.138,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.64,
        max_expansion_velocity=1155,
    )
)

round_40sw_220_fp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='40 S&W - 220gr FP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='40 S&W 220gr jacketed flat point ammunition',
    usable_properties=Bullet(
        bullet_type='40 S&W',
        mass=220,
        charge_mass=2.9,
        diameter=0.4,
        velocity=728,
        proj_config=cf_truncated_cone,
        drag_coefficient=cd_truncated_cone,
        spread_modifier=0.05,
        ballistic_coefficient=0.137,
        bullet_length=0.525,
    )
)

"""
.44 Magnum
"""

# source: 2020 Alliant Powder Catalog
# test barrel length: 8.275 inches

round_44_180_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='44 Magnum - 180gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='44 Magnum 180gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='44 Magnum',
        mass=180,
        charge_mass=14,
        diameter=0.429,
        velocity=1632,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.130,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.74,
        max_expansion_velocity=1300,
    )
)

round_44_200_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='44 Magnum - 200gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='44 Magnum 200gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='44 Magnum',
        mass=200,
        charge_mass=15.5,
        diameter=0.429,
        velocity=1573,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.122,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.74,
        max_expansion_velocity=1300,
    )
)

round_44_225_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='44 Magnum - 225gr SWC-JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='44 Magnum 225gr semi-wad cutter jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='44 Magnum',
        mass=225,
        charge_mass=21.4,
        diameter=0.429,
        velocity=1526,
        proj_config=cf_sem_wadcutter,
        drag_coefficient=cd_sem_wadcutter,
        spread_modifier=0.05,
        ballistic_coefficient=0.146,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.74,
        max_expansion_velocity=1300,
    )
)

round_44_240_sp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='44 Magnum - 240gr DCHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='44 Magnum 240gr "deep curl" copper plated soft point ammunition',
    usable_properties=Bullet(
        bullet_type='44 Magnum',
        mass=240,
        charge_mass=21,
        diameter=0.429,
        velocity=1434,
        proj_config=cf_sem_wadcutter,
        drag_coefficient=cd_sem_wadcutter,
        spread_modifier=0.05,
        ballistic_coefficient=0.175,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.74,
        max_expansion_velocity=1450,
    )
)

round_44_300_sp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='44 Magnum - 300gr DCHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='44 Magnum 300gr "deep curl" copper plated soft point ammunition',
    usable_properties=Bullet(
        bullet_type='44 Magnum',
        mass=300,
        charge_mass=22,
        diameter=0.429,
        velocity=1350,
        proj_config=cf_sem_wadcutter,
        drag_coefficient=cd_sem_wadcutter,
        spread_modifier=0.05,
        ballistic_coefficient=0.213,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.74,
        max_expansion_velocity=1450,
    )
)


"""
7.62x25
"""

# source: https://www.shootingtimes.com/editorial/handloading-the-762x25-tokarev/374699
# test barrel length: 4.5 inches
# powder: power pistol

round_76225_85_rn = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x25 Tokarev - 85gr RN',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='7.62x25 Tokarev 85gr jacketed round nose ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x25 Tokarev',
        mass=85,
        charge_mass=6.0,
        diameter=0.309,
        velocity=1272,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.113,
        bullet_length=0.525,
    )
)

round_76225_90_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x25 Tokarev - 90gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='7.62x25 Tokarev 90gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x25 Tokarev',
        mass=90,
        charge_mass=6.0,
        diameter=0.309,
        velocity=1231,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.115,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.57,
        max_expansion_velocity=1500,
    )
)

round_76225_100_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='7.62x25 Tokarev - 100gr JHP',
    weight=0.015,
    stacking=Stacking(stack_size=10),
    description='7.62x25 Tokarev 90gr jacketed hollow point ammunition',
    usable_properties=Bullet(
        bullet_type='7.62x25 Tokarev',
        mass=90,
        charge_mass=5.8,
        diameter=0.309,
        velocity=1231,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.115,
        bullet_length=0.525,
        bullet_expands=True,
        max_expansion=1.57,  # No data, educated guess
        max_expansion_velocity=1500,
    )
)

"""
7.62 x 39
"""
# source: shootersreference.com
# test barrel length: 24 inches
# powder: 1680 Accurate (Closest to N130)

# FMJ

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
        velocity=2445,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.282,
        bullet_length=0.796,
        bullet_yaws=True,
        bullet_fragments=True,
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
        charge_mass=23.6,
        diameter=0.311,
        velocity=2109,
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.341,
        bullet_length=0.796,
        bullet_yaws=True,
        bullet_fragments=True,
    )
)

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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.295,
        bullet_length=0.796,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1800,
    )
)

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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.341,
        bullet_length=0.796,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=2000,
    )
)

"""
5.56 
"""
# source: Lyman 48th Ed.
# test barrel length: 24 inches
# powder: IMR-4198 or closest (Closest to N130)

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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.204,
        bullet_length=0.810,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=2000,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.323,
        bullet_length=0.810,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1800,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.435,
        bullet_length=0.810,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1800,
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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.301,
        bullet_length=0.810,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1900,
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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.461,
        bullet_length=0.810,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1900,
    )
)

"""
300 blackout
"""
# source: shootersreference.com
# test barrel length: 16 inches
# powder: accurate 1680

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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.397,
        bullet_length=1.013,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1900,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.397,
        bullet_length=1.013,
        bullet_yaws=True,
        bullet_fragments=True,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.65,
        bullet_length=1.013,
        bullet_yaws=True,
        bullet_fragments=True,
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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.65,
        bullet_length=1.013,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1900,
    )
)

"""
5.45
"""

# based on .222 remington loading data
# source: Lyman 48th Ed.
# test barrel length: 26 inches
# powder: IMR-4198

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
        spread_modifier=0.05,
        ballistic_coefficient=0.209,
        bullet_length=1.0,
        bullet_yaws=True,
        bullet_fragments=True,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.235,
        bullet_length=1.0,
        bullet_yaws=True,
        bullet_fragments=True,
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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.240,
        bullet_length=1.0,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1900,
    )
)

"""
7.62x51 
"""

# source: Alliant 2020
# test barrel length: 24 inches
# powder: AR-Comp

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
        spread_modifier=0.05,
        ballistic_coefficient=0.263,
        bullet_length=1.4,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=1900,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.38,
        bullet_length=1.4,
        bullet_yaws=True,
        bullet_fragments=True,
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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.404,
        bullet_length=1.4,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=2000,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.484,
        bullet_length=1.4,
        bullet_yaws=True,
    )
)

"""
7.62x54R
"""

# source: Lyman 48th Ed.
# test barrel length: 26 inches
# powder: IMR-4198

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
        spread_modifier=0.05,
        ballistic_coefficient=0.262,
        bullet_length=1.4,
        bullet_yaws=True,
        bullet_fragments=True,
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
        proj_config=cf_spitzer,
        drag_coefficient=cd_spitzer,
        spread_modifier=0.05,
        ballistic_coefficient=0.411,
        bullet_length=1.4,
        bullet_yaws=True,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.5,
        max_expansion_velocity=2000,
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
        spread_modifier=0.05,
        ballistic_coefficient=0.344,
        bullet_length=1.4,
        bullet_yaws=True,
        bullet_fragments=True,
    )
)

"""
.30 Carbine
"""

# velocity - https://shootersreference.com/reloadingdata/30-carbine/
# powder loading - https://shootersreference.com/reloadingdata/30-carbine/
# powder: accurate 1680

round_30carb_110_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='.30 Carbine - 110gr Critical Defense',
    weight=0.012,
    stacking=Stacking(stack_size=10),
    description=".30 Carbine 110gr 'Critical Defense' polymer tipped ammunition",
    usable_properties=Bullet(
        bullet_type='.30 Carbine',
        mass=110,
        charge_mass=16,
        diameter=0.3078,
        velocity=1963,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.178,
        bullet_length=0.55,  # this is not correct, couldn't find any data on .30 carbine bullet lengths
        bullet_yaws=False,
        bullet_fragments=True,
        bullet_expands=True,
        max_expansion=1.55,
        max_expansion_velocity=2000,
    )
)

round_30carb_110_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='.30 Carbine - 110gr FMJ',
    weight=0.012,
    stacking=Stacking(stack_size=10),
    description=".30 Carbine 110gr full metal jacket ammunition",
    usable_properties=Bullet(
        bullet_type='.30 Carbine',
        mass=110,
        charge_mass=16,
        diameter=0.3078,
        velocity=1980,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.05,
        ballistic_coefficient=0.154,
        bullet_length=0.55,
        bullet_yaws=False,
        bullet_fragments=True,
    )
)

"""
12 guage
"""

# velocity vs barrel length - https://www.kommandoblog.com/2017/05/16/shotgun-barrel-length-velocity/
# velocity source - alliant powder catalogue
# test barrel length - 30 inches
# with improved cylcinder choke

round_12ga_slug = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='12-Gauge - 1 Oz Slug',
    weight=0.04,  # approx 12 grams for wad, shell, primer etc
    stacking=Stacking(stack_size=10),
    description="12-gauge 2.75 inch 1 oz rifled slug shotgun shell",
    usable_properties=Bullet(
        bullet_type='12 Gauge',
        mass=437,
        charge_mass=49,
        diameter=0.69,
        velocity=1680,
        proj_config=cf_fmj_round_nose,
        drag_coefficient=cd_fmj_round_nose,
        spread_modifier=0.064,
        ballistic_coefficient=0.075,
        bullet_length=0.55,
        bullet_yaws=False,
        bullet_fragments=False,
    )
)

# TODO - more 12ga ammo types

round_12ga_00buck = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name='12-Gauge - 00 Buckshot',
    weight=0.04,  # approx 12 grams for wad, shell, primer etc
    stacking=Stacking(stack_size=10),
    description="12-gauge 2.75 inch 00 buckshot shotgun shell",
    usable_properties=Bullet(
        bullet_type='12 Gauge',
        mass=54,
        charge_mass=32,
        diameter=0.33,
        velocity=1325,
        proj_config=cf_round_ball,
        drag_coefficient=cd_round_ball,
        spread_modifier=0.111,
        ballistic_coefficient=0.045,
        projectile_type='buckshot',
        bullet_length=0.55,
        bullet_yaws=False,
        bullet_fragments=False,
        projectile_no=9
    )
)

# bullet_list = (round_9mm_115_fmj, round_9mm_124_fmj, round_9mm_147_fp, round_9mm_115_fmj_pp,
#                round_9mm_124_fmj_pp, round_9mm_147_fp_pp, round_9mm_115_jhp, round_9mm_124_jhp,
#                round_9mm_147_jhp, round_9mm_115_jhp_pp, round_9mm_124_jhp_pp, round_9mm_147_jhp_pp, round_45_185_swc,
#                round_45_200_swc, round_45_185_jhp, round_45_200_jhp, round_45_230_jhp, round_45_200_fmj,
#                round_45_230_fmj, round_45_185_swc_pp, round_45_200_swc_pp, round_45_185_jhp_pp, round_45_230_jhp_pp,
#                round_45_200_fmj_pp, round_45_230_fmj_pp, round_76239_123_fmj, round_76239_150_fmj,
#                round_76239_123_sst, round_76239_150_sp, round_556_55_sp, round_556_60_fmj,
#                round_556_75_fmj, round_556_69_jhp, round_556_80_jhp, round_300aac_150_jhp, round_300aac_150_fmj,
#                round_300aac_210_fmj, round_300aac_210_jhp, round_545_56_fmj, round_545_63_fmj, round_545_60_jhp,
#                round_308_130_jhp, round_308_150_fmj, round_308_165_sp, round_308_180_tsx, round_54r_174_jrn,
#                round_54r_180_jsp, round_54r_200_fmj
#                )
