from numpy import array
from components.enemies.caverns import *

# this dictionary has the parameters for all the levels in the game
level_params = {
    0: array([0,   # tunnel type (0 = drunkard, 1 = straight)
              80,  # map width
              50,  # map height
              24,  # MAX_LEAF_SIZE
              15,  # ROOM_MAX_SIZE
              6,   # ROOM_MIN_SIZE
              2    # Max monsters per room
              ])
}

# these dictionaries contain lists of the enemies that should appear on a given level
# note enemy rarity can be made even more granular beyond the rarity system by placing multiple instances of an entity
# in a given list
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
