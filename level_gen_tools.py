import random
import numpy as np

import tile_types


def generate_char_arrays(floor_fg_d, floor_bg_d, floor_fg_l, floor_bg_l, floor_chars):
    """
    From tuples representing the colours of the tiles and possible floor characters (from dictionary in
    colours_and_chars), generates a series of lists representing possible combinations of floor colours and characters,
    which are used to an array representing these tiles.

    !!! Can be expanded in future to use multiple possible colours for a single floor !!!
    """
    floor_list = []
    for x in floor_chars:
        floor_list.append(tile_types.new_floor(floor_fg_d, floor_bg_d, floor_fg_l, floor_bg_l, x))
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


class Rect:  # used for the tunneling algorithm
    def __init__(self, x, y, w, h):
        self.x1 = int(x)
        self.y1 = int(y)
        self.x2 = int(x) + int(w)
        self.y2 = int(y) + int(h)

    def centre(self):
        centerX = (self.x1 + self.x2) / 2
        centerY = (self.y1 + self.y2) / 2
        centerX = int(centerX)
        centerY = int(centerY)
        return centerX, centerY

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)