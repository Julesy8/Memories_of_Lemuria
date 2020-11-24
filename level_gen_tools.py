from math import floor
from typing import Tuple, Iterator
import random
import numpy as np

import tcod

import tile_types


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.width = width
        self.height = height
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    def intersects(self, other) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )


def make_tunnel_right_angle(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:  # 50% chance.
        # Move horizontally, then vertically.
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y


def round_up(n):
    return floor(n + 0.5)


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