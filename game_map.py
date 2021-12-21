from __future__ import annotations

from typing import Iterable, Iterator, Optional, TYPE_CHECKING

import numpy as np  # type: ignore
from tcod.console import Console

import tile_types
from colours_and_chars import MapColoursChars
from entity import Actor, Item
from scrolling_map import Camera

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class GameMap:
    def __init__(self, engine: Engine, width: int, height: int, level: int, debug_fov: bool,
                 entities: Iterable[Entity] = ()):
        self.level = level
        self.debug_fov = debug_fov  # to disable fov, set to 'True' in level_generator
        self.engine = engine

        self.colours_chars = MapColoursChars(self.level)

        # defines the colours and characters used for wall tiles:
        self.wall = tile_types.new_wall(self.colours_chars.wall_fg_dark(),
                                        self.colours_chars.wall_bg_dark(),
                                        self.colours_chars.wall_fg_light(),
                                        self.colours_chars.wall_bg_light(),
                                        self.colours_chars.wall_tile())

        self.entities = set(entities)
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=self.wall, order="F")  # fills game map with wall tiles

        self.visible = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player can currently see

        self.explored = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles the player has seen before

        self.downstairs_location = (0, 0)

    @property
    def gamemap(self) -> GameMap:
        return self

    @property
    def actors(self) -> Iterator[Actor]:
        """Iterate over this maps living actors."""
        yield from (
            entity
            for entity in self.entities
            if isinstance(entity, Actor) and entity.is_alive
        )

    @property
    def items(self) -> Iterator[Item]:
        yield from (entity for entity in self.entities if isinstance(entity, Item))

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

    def get_actor_at_location(self, x: int, y: int) -> Optional[Actor]:
        for actor in self.actors:
            if actor.x == x and actor.y == y:
                return actor

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console, camera: Camera) -> None:

        for screen_y in range(camera.screen_height):
            for screen_x in range(camera.screen_width):
                map_x, map_y = camera.screen_to_map(screen_x, screen_y)

                if self.visible[map_x, map_y]:
                    console.print(screen_x, screen_y,
                                  chr(self.tiles[map_x, map_y]["light"]["ch"]),
                                  tuple(self.tiles[map_x, map_y]["light"]["fg"]),
                                  tuple(self.tiles[map_x, map_y]["light"]["bg"]))

                elif self.explored[map_x, map_y]:
                    console.print(screen_x, screen_y,
                                  chr(self.tiles[map_x, map_y]["dark"]["ch"]),
                                  tuple(self.tiles[map_x, map_y]["dark"]["fg"]),
                                  tuple(self.tiles[map_x, map_y]["dark"]["bg"]))

        entities_sorted_for_rendering = sorted(
            self.entities, key=lambda x: x.render_order.value
        )

        for entity in entities_sorted_for_rendering:

            if self.visible[entity.x, entity.y]:
                screen_x, screen_y = camera.map_to_screen(entity.x, entity.y)
                if 0 <= screen_x < camera.screen_width and 0 <= screen_y < camera.screen_height:
                    console.print(screen_x, screen_y, entity.char, entity.fg_colour, entity.bg_colour)
                    entity.active = True

    def generate_level(self) -> None:
        from level_generator import MessyBSPTree
        from level_parameters import level_params

        self.engine.current_floor += 1

        self.engine.game_map = MessyBSPTree(
            messy_tunnels=level_params[self.engine.current_level][0],
            map_width=level_params[self.engine.current_level][1],
            map_height=level_params[self.engine.current_level][2],
            max_leaf_size=level_params[self.engine.current_level][3],
            room_max_size=level_params[self.engine.current_level][4],
            room_min_size=level_params[self.engine.current_level][5],
            max_monsters_per_room=level_params[self.engine.current_level][6],
            max_items_per_room=level_params[self.engine.current_level][7],
            engine=self.engine,
            current_level=self.engine.current_level,
            ).generateLevel()
