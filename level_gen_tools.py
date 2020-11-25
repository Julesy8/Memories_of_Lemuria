import random
import numpy as np

import tile_types

def generate_char_arrays(floor_fg_l, floor_bg_l, floor_chars):
    """
    From tuples representing the colours of the tiles and possible floor characters (from dictionary in
    colours_and_chars), generates a series of lists representing possible combinations of floor colours and characters,
    which are used to an array representing these tiles.

    !!! Can be expanded in future to use multiple possible colours for a single floor !!!
    """
    floor_list = []
    for x in floor_chars:
        floor_list.append(tile_types.new_floor(floor_fg_l, floor_bg_l, x))
    floor_arrays = np.array(floor_list)
    return floor_arrays


def select_random_tile(character_array):
    """
    Using an array of possible tiles from (from generate_char_arrays), selects a tile in the array at random

    !!! Possibilities can be weighted in future using multiple entries of the same tile !!!
    """
    character_index = random.randint(0, character_array.size - 1)
    character = character_array[character_index]
    return character