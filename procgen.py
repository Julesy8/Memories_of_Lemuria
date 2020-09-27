from typing import Tuple
from random import randint
import numpy as np

import tile_types
from game_map import GameMap
from colours_and_chars import MapColoursChars


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
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


def generate_char_arrays(floor_fg_l, floor_bg_l, floor_chars):
    floor_list = []
    for x in floor_chars:
        floor_list.append(tile_types.new_floor(floor_fg_l, floor_bg_l, x))
    floor_arrays = np.array(floor_list)
    return floor_arrays


def select_random_tile(character_array):
    character_index = randint(0, character_array.size - 1)
    character = character_array[character_index]
    return character


def generate_dungeon(map_width, map_height, current_level) -> GameMap:
    dungeon = GameMap(map_width, map_height, current_level)

    colours_chars = MapColoursChars(current_level)

    floor_tiles = generate_char_arrays(colours_chars.floor_fg_dark(),
                                       colours_chars.floor_bg_dark(),
                                       colours_chars.floor_tile())

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    # dungeon.tiles[room_1.inner] = dungeon.floor
    # dungeon.tiles[room_2.inner] = dungeon.floor

    for x in range(int(room_1.x1) + 1, int(room_1.x2)):
        for y in range(int(room_1.y1) + 1, int(room_1.y2)):
            dungeon.tiles[x, y] = floor_tiles

    for x in range(int(room_2.x1) + 1, int(room_2.x2)):
        for y in range(int(room_2.y1) + 1, int(room_2.y2)):
            dungeon.tiles[x, y] = floor_tiles

    return dungeon
