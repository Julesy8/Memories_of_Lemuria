import numpy as np  # type: ignore
from tcod.console import Console
from random import randint

import tile_types
import level_importer


class GameMap:
    def __init__(self, width: int, height: int, level: int):
        self.level = level
        colours_and_characters = level_importer.level_dependent_import(level)

        # floor colours
        self.floor_fg_light = colours_and_characters[2][0]
        self.floor_bg_light = colours_and_characters[2][1]
        self.floor_fg_dark = colours_and_characters[2][2]
        self.floor_bg_dark = colours_and_characters[2][3]

        # wall colours
        self.wall_fg_light = colours_and_characters[1][0]
        self.wall_bg_light = colours_and_characters[1][1]
        self.wall_fg_dark = colours_and_characters[1][2]
        self.wall_bg_dark = colours_and_characters[1][3]
        self.wall_tile = colours_and_characters[3][0]

        def generate_random_tile(colours_and_tiles):
            if colours_and_tiles[4][0] == 1:
                char = colours_and_tiles[4][1]
            else:
                rand_tile = randint(1, colours_and_tiles[4][0])
                char = colours_and_tiles[4][rand_tile]
            return char

        self.floor = tile_types.new_floor(self.floor_bg_light, self.floor_fg_light,
                                          generate_random_tile(colours_and_characters))
        self.wall = tile_types.new_wall(self.wall_bg_light, self.wall_fg_light, self.wall_tile)
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=self.wall, order="F")  # fills game map with wall tiles

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
