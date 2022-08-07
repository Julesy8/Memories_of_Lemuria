from typing import Tuple

import numpy as np  # type: ignore

import colour

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
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), colour.WHITE, (0,0,0)), dtype=graphic_dt)


def new_floor(fg_colour_d: Tuple[int, int, int], bg_colour_d: Tuple[int, int, int],
              fg_colour_l: Tuple[int, int, int], bg_colour_l: Tuple[int, int, int], tile: int):
    floor = new_tile(
        walkable=True, transparent=True, dark=(tile, fg_colour_d, bg_colour_d), light=(tile, fg_colour_l, bg_colour_l)
    )
    return floor


def new_wall(fg_colour_d: Tuple[int, int, int], bg_colour_d: Tuple[int, int, int],
             fg_colour_l: Tuple[int, int, int], bg_colour_l: Tuple[int, int, int], tile: int):
    wall = new_tile(
        walkable=False, transparent=False, dark=(tile, fg_colour_d, bg_colour_d), light=(tile, fg_colour_l, bg_colour_l)
    )
    return wall


down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), colour.DARK_GRAY, colour.BLACK),
    light=(ord(">"), colour.LIGHT_GRAY, colour.BLACK),
)