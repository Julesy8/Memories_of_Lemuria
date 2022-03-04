from numpy import array
from components.enemies.caverns import *
from components.commonitems import medkit

# this dictionary has the parameters for all the levels in the game
# NOTE: map width/height must be larger than screen size!
level_params = {
    0: array([True,   # messy tunnels (bool)
              80,    # map width
              50,     # map height
              24,     # MAX_LEAF_SIZE
              15,     # ROOM_MAX_SIZE
              9,      # ROOM_MIN_SIZE
              2,      # Max monsters per room
              10,      # Max items per room
              ])
}

level_names = {
    0: 'Caverns'
}

# these dictionaries contain lists of the enemies that should appear on a given level

Enemies_by_level = {
    0:
        (
         [giant_snake, 1],
         [large_rat, 3]
         ),

}

Items_by_level = {
    0:
        (
        [medkit, 1],
        [medkit, 1]
        ),
}
