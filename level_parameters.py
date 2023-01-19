from numpy import array
from components.enemies.caverns import *
from components.commonitems import medkit
# from components.weapons.glock17 import glock17_frame, glock17_barrel, glock17_slide, glock_switch
from components.weapons.bullets import round_9mm_124_fmj
from components.weapons.magazines import glock_mag_9mm

# this dictionary has the parameters for all the levels in the game
level_params = {

    # sewers
    0: array([False,  # messy tunnels (bool)
              70,  # map width
              70,  # map height
              30,  # MAX_LEAF_SIZE
              10,  # ROOM_MAX_SIZE
              7,  # ROOM_MIN_SIZE
              1,  # Max items per room
              20,  # fov radius
              ]),

    # caves
    1: array([True,
              60,
              60,
              26,
              15,
              9,
              1,
              15,
              ]),

    # the nexion
    2: array([False,
              70,
              70,
              30,
              18,
              9,
              1,
              100,
              ]),

    # D.U.M.B
    3: array([False,
              60,
              60,
              20,
              13,
              9,
              1,
              100,
              ]),

    # reptilian hive
    4: array([True,
              60,
              60,
              11,
              17,
              9,
              1,
              30,
              ]),
}

level_names = {
    0: 'Sewers',
    1: 'Caverns',
    2: 'The Nexion',
    3: 'D.U.M.B',
    4: 'Reptilian Hive',
}

# these dictionaries contain lists of the enemies that should appear on a given level

Enemies_by_level = {
    0:
        (
            [giant_snake, 1],
            [large_rat, 3]
        ),
    1:
        (
            [giant_snake, 1],
            [large_rat, 3]
        ),
    2:
        (
            [giant_snake, 1],
            [large_rat, 3]
        ),
    3:
        (
            [giant_snake, 1],
            [large_rat, 3]
        ),
    4:
        (
            [giant_snake, 1],
            [large_rat, 3]
        ),

}

Items_by_level = {
    0:
        (
            [medkit, 1],
            [medkit, 1],
            # [glock_17, 1],
            # [round_9mm_124_fmj, 1],
            [glock_mag_9mm, 1],
            # [glock17_frame, 1],
            # [glock17_barrel, 1],
            # [glock17_slide, 1],
            # [glock_switch, 1],
        ),
    1:
        (
            [medkit, 1],
            [medkit, 1],
            # [glock_17, 1],
            # [round_9mm_124_fmj, 1],
            [glock_mag_9mm, 1],
            # [glock17_frame, 1],
            # [glock17_barrel, 1],
            # [glock17_slide, 1],
            # [glock_switch, 1],
        ),
    2:
        (
            [medkit, 1],
            [medkit, 1],
            # [glock_17, 1],
            # [round_9mm_124_fmj, 1],
            [glock_mag_9mm, 1],
            # [glock17_frame, 1],
            # [glock17_barrel, 1],
            # [glock17_slide, 1],
            # [glock_switch, 1],
        ),
    3:
        (
            [medkit, 1],
            [medkit, 1],
            # [glock_17, 1],
            # [round_9mm_124_fmj, 1],
            [glock_mag_9mm, 1],
            # [glock17_frame, 1],
            # [glock17_barrel, 1],
            # [glock17_slide, 1],
            # [glock_switch, 1],
        ),
    4:
        (
            [medkit, 1],
            [medkit, 1],
            # [glock_17, 1],
            # [round_9mm_124_fmj, 1],
            [glock_mag_9mm, 1],
            # [glock17_frame, 1],
            # [glock17_barrel, 1],
            # [glock17_slide, 1],
            # [glock_switch, 1],
        ),
}

