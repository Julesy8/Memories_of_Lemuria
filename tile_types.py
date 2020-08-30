from typing import Tuple
from random import randint
import numpy as np  # type: ignore

level = 0

"""
The following dictionaries determine tile foreground and background colour and character. Dependent on what floor
the player is on, i.e. "caverns". For first dict, integers are colour values in order:
floor foreground, floor background, wall foreground, wall background.
Second dict represents hex character values in the order 
wall, multiple floor tiles or single, floor, floor, floor, where values after the second are the floor tiles
"""
tile_colour = {
    0: [(63, 63, 63, 31, 31, 31), (45, 45, 45, 63, 63, 63),  # light
        (32, 32, 32, 16, 16, 16), (23, 23, 23, 32, 32, 32)]  # dark
}

tile_character = {
    # 0 = #, 2 = dot, 3 = `, 4 = ,
    0: [35, False, 250, 96, 44]
}

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int, int, int, int], Tuple[int, int, int, int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark), dtype=tile_dt)


def random_tile():
    rand_tile = randint(1, 3)
    if rand_tile == 1:
        char = tile_character[level][2]
    elif rand_tile == 2:
        char = tile_character[level][3]
    else:
        char = tile_character[level][4]
    return char


colour_floor = tile_colour[level][0]
colour_floor_dark = tile_colour[level][1]
colour_wall = tile_colour[level][2]
colour_wall_dark = tile_colour[level][3]

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), colour_floor, colour_floor_dark),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), colour_wall, colour_wall_dark),
)
