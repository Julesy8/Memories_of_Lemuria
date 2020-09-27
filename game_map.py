import numpy as np  # type: ignore
from tcod.console import Console

import tile_types
from colours_and_chars import MapColoursChars


class GameMap:
    def __init__(self, width: int, height: int, level: int):
        self.level = level

        colours_chars = MapColoursChars(self.level)
        self.wall = tile_types.new_wall(colours_chars.wall_fg_dark(),
                                        colours_chars.wall_bg_dark(),
                                        colours_chars.wall_tile())
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=self.wall, order="F")  # fills game map with wall tiles

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
