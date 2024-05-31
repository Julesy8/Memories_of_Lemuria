from numpy import array
from components.enemies.caverns import *
import components.weapons.bullets as bullets
from components.armour import *
from components.commonitems import medkit, bandages, repair_kit


# this dictionary has the parameters for all the levels in the game
level_params = {

    0: array([False,  # messy tunnels (bool)
              90,
              90,
              25,
              21,
              5,
              1,
              100,
              6,  # min caverns
              8,  # max caverns
              150,  # cavern size
              4,  # custom room chance
              3,  # enclose room chance
              ]),

    # the caverns
    1: array([True,  # messy tunnels (bool)
              100,  # map width
              100,  # map height
              40,  # MAX_LEAF_SIZE
              14,  # ROOM_MAX_SIZE
              7,  # ROOM_MIN_SIZE
              1,  # Max items per room
              100,  # fov radius
              3,  # min caverns
              3,  # max caverns
              500,  # cavern size
              4,  # custom room chance
              3,  # enclose room chance
              ]),

    # the temple
    2: array([False,
              90,
              90,
              25,
              21,
              5,
              1,
              100,
              6,  # min caverns
              8,  # max caverns
              150,  # cavern size
              4,  # custom room chance
              3,  # enclose room chance
              ]),

    # the base
    3: array([False,
              120,  # map width
              120,  # map height
              70,  # MAX_LEAF_SIZE
              14,  # ROOM_MAX_SIZE
              3,  # ROOM_MIN_SIZE
              1,  # Max items per room
              100,  # fov radius
              3,  # min caverns
              5,  # max caverns
              500,  # cavern size
              4,  # custom room chance
              3,  # enclose room chance
              ]),

    # the labs
    4: array([True,
              100,  # map width
              100,  # map height
              25,  # MAX_LEAF_SIZE
              20,  # ROOM_MAX_SIZE
              4,  # ROOM_MIN_SIZE
              1,  # Max items per room
              100,  # fov radius
              5,  # min caverns
              5,  # max caverns
              150,  # cavern size
              4,  # custom room chance
              3,  # enclose room chance
              ]),

    # the hive
    5: array([True,
              100,  # map width
              100,  # map height
              25,  # MAX_LEAF_SIZE
              20,  # ROOM_MAX_SIZE
              4,  # ROOM_MIN_SIZE
              1,  # Max items per room
              100,  # fov radius
              8,  # min caverns
              10,  # max caverns
              50,  # cavern size
              4,  # custom room chance
              3,  # enclose room chance
              ]),
}

level_names = {
    0: 'The Tunnels',
    1: 'The Caverns',
    2: 'The Temple',
    3: 'The Base',
    4: 'The Labs',
    5: 'The Hive',
}

# these dictionaries contain lists of the enemies that should appear on a given level

Enemies_by_level = {

    # tunnels
    0: {large_rat: 10,
        giant_snake: 8,
        grunt: 5,
        maniac: 6,
        soldier: 3,
        officer: 1,
        rat_king: 2,
        },

    # caverns
    1: {zombie: 2,
        grunt: 10,
        fast_zombie: 1,
        maniac: 4,
        soldier: 4,
        officer: 1,
        },

    # the temple
    2: {zombie: 10,
        fast_zombie: 5,
        grunt: 6,
        hulk_zombie: 1,
        zombie_soldier: 6,
        soldier: 4,
        officer: 2,
        },

    # D.U.M.B
    3: {grunt: 8,
        soldier: 6,
        officer: 4,
        reptilian: 5,
        soldier_gov: 6,
        reptilian_soldier: 1,
        },

    # the labs
    4: {grunt: 3,
        soldier: 4,
        officer: 2,
        blob: 1,
        soldier_gov: 2,
        reptilian: 3,
        reptilian_soldier: 1,
        },

    # the hive
    5: {grunt: 4,
        soldier: 8,
        officer: 2,
        reptilian_soldier: 2,
        wyrm: 1,
        },
}

Items_by_level = {
    0: {None: 300,
        medkit: 15,
        bandages: 30,
        repair_kit: 5,
        bullets.round_9mm_115_fmj: 10,
        bullets.round_9mm_115_jhp: 5,
        bullets.round_76225_85_rn: 10,
        bullets.round_30carb_110_fmj: 8,
        bullets.round_40sw_165_fmj: 6,
        bullets.round_45_185_swc: 5,
        bullets.round_556_60_fmj: 5,
        bullets.round_76239_123_fmj: 5,
        bullets.round_308_130_jhp: 4,
        bullets.round_54r_200_fmj: 7,
        bullets.round_44_180_jhp: 4,
        bullets.round_10mm_155_jhp: 3,
        bullets.round_12ga_00buck: 3,
        helmet_ssh68: 2,
        helmet_m1: 2,
        platecarrier_3a: 2
        },

    1: {None: 300,
        medkit: 10,
        bandages: 20,
        repair_kit: 5,
        bullets.round_9mm_115_fmj: 10,
        bullets.round_9mm_115_jhp: 5,
        bullets.round_76225_85_rn: 10,
        bullets.round_30carb_110_fmj: 8,
        bullets.round_40sw_155_jhp: 6,
        bullets.round_45_200_swc: 5,
        bullets.round_54r_200_fmj: 7,
        bullets.round_76239_123_fmj: 10,
        bullets.round_556_55_sp: 10,
        bullets.round_545_56_fmj: 6,
        bullets.round_308_130_jhp: 5,
        bullets.round_44_200_jhp: 4,
        bullets.round_10mm_180_fmj: 4,
        bullets.round_12ga_00buck: 3,
        bullets.round_300aac_150_fmj: 3,
        bodyarmour_pasgt: 1,
        helmet_pasgt: 1,
        helmet_m1: 2,
        platecarrier_3a: 2,
        platecarrier_3: 1,
        },

    2: {None: 300,
        medkit: 15,
        bandages: 30,
        repair_kit: 5,
        bullets.round_76239_123_fmj: 10,
        bullets.round_556_75_fmj: 10,
        bullets.round_54r_200_fmj: 8,
        bullets.round_545_63_fmj: 8,
        bullets.round_30carb_110_jhp: 7,
        bullets.round_9mm_124_fmj: 4,
        bullets.round_9mm_124_jhp: 3,
        bullets.round_76225_90_jhp: 6,
        bullets.round_40sw_180_fmj: 6,
        bullets.round_45_185_jhp: 5,
        bullets.round_308_150_fmj: 5,
        bullets.round_44_225_jhp: 4,
        bullets.round_10mm_180_fmj: 4,
        bullets.round_300aac_150_fmj: 3,
        bullets.round_12ga_00buck: 3,
        bodyarmour_pasgt: 1,
        helmet_pasgt: 1,
        helmet_m1: 2,
        platecarrier_3a: 2,
        platecarrier_3: 1,
        },

    3: {None: 300,
        medkit: 15,
        bandages: 30,
        repair_kit: 5,
        bullets.round_76239_150_fmj: 10,
        bullets.round_556_75_fmj: 10,
        bullets.round_545_60_jhp: 8,
        bullets.round_54r_200_fmj: 7,
        bullets.round_308_150_fmj: 8,
        bullets.round_30carb_110_jhp: 7,
        bullets.round_9mm_124_fmj_pp: 4,
        bullets.round_9mm_124_jhp_pp: 3,
        bullets.round_76225_90_jhp: 6,
        bullets.round_40sw_180_jhp: 6,
        bullets.round_45_200_jhp: 6,
        bullets.round_44_225_jhp: 5,
        bullets.round_10mm_180_fmj: 4,
        bullets.round_12ga_00buck: 4,
        bullets.round_300aac_150_fmj: 4,
        bodyarmour_pasgt: 2,
        helmet_pasgt: 3,
        platecarrier_3a: 3,
        platecarrier_3: 2,
        helmet_altyn: 1,
        },

    4: {None: 300,
        medkit: 15,
        bandages: 30,
        repair_kit: 5,
        bullets.round_76239_150_fmj: 10,
        bullets.round_556_69_jhp: 10,
        bullets.round_545_60_jhp: 9,
        bullets.round_308_165_sp: 9,
        bullets.round_54r_200_fmj: 8,
        bullets.round_300aac_210_fmj: 8,
        bullets.round_9mm_147_fp: 5,
        bullets.round_9mm_147_jhp: 3,
        bullets.round_30carb_110_jhp: 7,
        bullets.round_40sw_180_jhp: 7,
        bullets.round_45_230_fmj: 7,
        bullets.round_76225_100_jhp: 7,
        bullets.round_44_240_sp: 6,
        bullets.round_10mm_190_jhp: 6,
        bullets.round_12ga_00buck: 4,
        helmet_pasgt: 3,
        helmet_ech: 2,
        bodyarmour_improved: 2,
        platecarrier_3: 3,
        helmet_altyn: 1,
        helmet_ronin: 1,
        },

    5: {None: 300,
        medkit: 15,
        bandages: 30,
        repair_kit: 5,
        bullets.round_76239_150_sp: 10,
        bullets.round_556_80_jhp: 10,
        bullets.round_545_60_jhp: 10,
        bullets.round_308_165_sp: 9,
        bullets.round_54r_200_fmj: 9,
        bullets.round_9mm_147_fp: 5,
        bullets.round_9mm_147_jhp: 3,
        bullets.round_30carb_110_jhp: 7,
        bullets.round_300aac_210_jhp: 7,
        bullets.round_45_230_jhp: 7,
        bullets.round_40sw_220_fp: 7,
        bullets.round_76225_100_jhp: 6,
        bullets.round_44_300_sp: 5,
        bullets.round_10mm_190_jhp: 5,
        bullets.round_12ga_00buck: 5,
        helmet_ech: 3,
        bodyarmour_interceptor: 2,
        platecarrier_4: 2,
        helmet_ronin: 2,
        helmet_altyn: 2,
        },
}
