from __future__ import annotations

from typing import Iterable, TYPE_CHECKING, Optional

import numpy as np  # type: ignore
from tcod.console import Console

import tile_types
from colours_and_chars import MapColoursChars

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class GameMap:
    def __init__(self, engine:Engine, width: int, height: int, level: int, debug_fov: bool, entities: Iterable[Entity] = ()):
        self.level = level
        self.debug_fov = debug_fov  # to disable fov, set to 'True' in level_generator
        self.engine = engine

        colours_chars = MapColoursChars(self.level)

        # defines the colours and characters used for wall tiles:
        self.wall = tile_types.new_wall(colours_chars.wall_fg_dark(),
                                        colours_chars.wall_bg_dark(),
                                        colours_chars.wall_fg_light(),
                                        colours_chars.wall_bg_light(),
                                        colours_chars.wall_tile())

        self.entities = set(entities)
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=self.wall, order="F")  # fills game map with wall tiles

        self.visible = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player can currently see

        self.explored = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player has seen before

    def get_blocking_entity_at_location(
        self, location_x: int, location_y: int,
    ) -> Optional[Entity]:
        for entity in self.entities:
            if (
                entity.blocks_movement
                and entity.x == location_x
                and entity.y == location_y
            ):
                return entity

        return None


    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        """
        if self.debug_fov == False:
            console.tiles_rgb[0: self.width, 0: self.height] = np.select(
                condlist=[self.visible, self.explored],
                choicelist=[self.tiles["light"], self.tiles["dark"]],
                default=tile_types.SHROUD,
            )
        else:
            console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["light"]

        for entity in self.entities:
            if self.debug_fov == False:
                # Only print entities that are in the FOV
                if self.visible[entity.x, entity.y]:
                    console.print(entity.x, entity.y, entity.char, entity.fg_colour, entity.bg_colour)
            else:
                console.print(entity.x, entity.y, entity.char, entity.fg_colour, entity.bg_colour)
