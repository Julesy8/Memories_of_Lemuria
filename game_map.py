import numpy as np  # type: ignore
from tcod.console import Console
from random import randint

import tile_types


class GameMap:
    def __init__(self, width: int, height: int, level: int):

        """
        The following dictionaries determine tile foreground and background colour and character. Dependent on what
        floor the player is on, i.e. "caverns". For first dict, integers are colour values in order:
        floor foreground, floor background, wall foreground, wall background.
        Second dict represents hex character values in the order
        wall, number of floor tiles, floor, ...
        """
        tile_colour = {
            0: ((63, 63, 63), (31, 31, 31), (45, 45, 45), (63, 63, 63),  # light
                (32, 32, 32), (16, 16, 16), (23, 23, 23), (32, 32, 32))  # dark
        }

        tile_character = {
            # 0 = #, 2 = dot, 3 = `, 4 = ,
            0: [35, 3, 46, 96, 44]
        }

        """
        Used to generate random floor tiles. Second value in tile_character list for the given level is how many
        different tiles there are that can be generated. Every integer after that represents a different tile. 
        If there is more than 1 tile that can be generated, generates a number between 2 (first tile value) and 
        the amount of different tiles that can be generated + 1. This value is assigned to char and then returned. 
        """
        def generate_random_tile(current_level):  # at some point should implement random colours too
            if tile_character[current_level][1] == 1:
                char = tile_character[current_level][2]
            else:
                rand_tile = randint(2, tile_character[current_level][1] + 1)
                char = tile_character[current_level][rand_tile]

            return char

        self.floor_fg_light = tile_colour[level][0]
        self.floor_bg_light = tile_colour[level][1]
        self.floor_fg_dark = tile_colour[level][4]
        self.floor_bg_dark = tile_colour[level][5]

        self.wall_fg_light = tile_colour[level][2]
        self.wall_bg_light = tile_colour[level][3]
        self.wall_fg_dark = tile_colour[level][6]
        self.wall_bg_dark = tile_colour[level][7]
        self.wall_tile = tile_character[level][0]

        self.floor = tile_types.new_floor(self.floor_bg_light, self.floor_fg_light, generate_random_tile(level))
        self.wall = tile_types.new_wall(self.wall_bg_light, self.wall_fg_light, self.wall_tile)
        self.width, self.height = width, height
        self.level = level
        self.tiles = np.full((width, height), fill_value=self.floor, order="F")

        self.tiles[30:33, 22] = self.wall

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
