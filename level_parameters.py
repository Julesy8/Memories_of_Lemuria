from numpy import array
from components.enemies.caverns import *
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
    0: {large_rat: 1,
        giant_snake: 1,
        maniac: 1,
        rat_king: 1,
        grunt: 1,
        soldier: 1,
        officer: 1,
        },

    # caverns
    1: {zombie: 1,
        fast_zombie: 1,
        maniac: 1,
        grunt: 1,
        soldier: 1,
        officer: 1,
        },

    # the temple
    2: {zombie: 1,
        fast_zombie: 1,
        hulk_zombie: 1,
        zombie_soldier: 1,
        grunt: 1,
        soldier: 1,
        officer: 1,
        },

    # D.U.M.B
    3: {grunt: 1,
        soldier: 1,
        officer: 1,
        reptilian: 1,
        soldier_gov: 1,
        reptilian_soldier: 1,
        },

    # the labs
    4: {grunt: 1,
        soldier: 1,
        officer: 1,
        blob: 1,
        soldier_gov: 1,
        reptilian: 1,
        reptilian_soldier: 1,
        },

    # the hive
    5: {grunt: 1,
        soldier: 1,
        officer: 1,
        soldier_gov: 1,
        reptilian_soldier: 1,
        wyrm: 1,
        },
}

Items_by_level = {
    0: {None: 100,
        medkit: 5,
        bandages: 10,
        repair_kit: 5,
        },
    1: {None: 100,
        medkit: 5,
        bandages: 10,
        repair_kit: 5,
        },
    2: {None: 100,
        medkit: 5,
        bandages: 10,
        repair_kit: 5,
        },
    3: {None: 100,
        medkit: 5,
        bandages: 10,
        repair_kit: 5,
        },
    4: {None: 100,
        medkit: 5,
        bandages: 10,
        repair_kit: 5,
        },
    5: {None: 100,
        medkit: 5,
        bandages: 10,
        repair_kit: 5,
        },
}
