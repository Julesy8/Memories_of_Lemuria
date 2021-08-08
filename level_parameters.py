from numpy import array
from components.enemies.caverns import *

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
              2,      # Max items per room
              ])
}

level_names = {
    0: 'Caverns'
}

# these dictionaries contain lists of the enemies that should appear on a given level
# note enemy rarity can be made even more granular beyond the rarity system by placing multiple instances of an entity
# in a given list

# should probably use arrays instead of lists here
Enemies_by_level = {
    0: [
        # common
        [placeholder_common],
        # uncommon
        [placeholder_uncommon],
        # rare
        [placeholder_rare],
        # very rare
        [placeholder_v_rare],
        # legendary
        [placeholder_legendary]
    ]
}


Items_by_level = {
    0: [
        # common
        [medkit, glock, helmet, greaves, chestplate, pauldron],
        # uncommon
        [medkit, glock, helmet, greaves, chestplate, pauldron],
        # rare
        [medkit, glock, helmet, greaves, chestplate, pauldron],
        # very rare
        [medkit, glock, helmet, greaves, chestplate, pauldron],
        # legendary
        [medkit, glock, helmet, greaves, chestplate, pauldron],
    ]
}
