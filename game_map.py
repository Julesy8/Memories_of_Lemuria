import numpy as np  # type: ignore
from tcod.console import Console
from random import randint

import tile_types
import level_importer


class GameMap:
    def __init__(self, width: int, height: int, level: int):
        self.level = level
        colours_and_characters = level_importer.level_dependent_import(level)

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

        # floor colours
        self.floor_fg_light = colours_and_characters[2][0]
        self.floor_bg_light = colours_and_characters[2][1]
        self.floor_fg_dark = colours_and_characters[2][2]
        self.floor_bg_dark = colours_and_characters[2][3]
        self.floor_tile = colours_and_characters[4]

        # wall colours
        self.wall_fg_light = colours_and_characters[1][0]
        self.wall_bg_light = colours_and_characters[1][1]
        self.wall_fg_dark = colours_and_characters[1][2]
        self.wall_bg_dark = colours_and_characters[1][3]
        self.wall_tile = colours_and_characters[3][0]

        char_arrays = generate_char_arrays(self.floor_fg_dark, self.floor_bg_dark, self.floor_tile)

        self.floor = select_random_tile(char_arrays)
        self.wall = tile_types.new_wall(self.wall_fg_dark, self.wall_bg_dark, self.wall_tile)
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=self.wall, order="F")  # fills game map with wall tiles

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
