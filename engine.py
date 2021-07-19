from __future__ import annotations

from typing import TYPE_CHECKING

from tcod.console import Console
from tcod.map import compute_fov
from scrolling_map import Camera
import colour

import exceptions
from input_handlers import MainGameEventHandler
from message_log import MessageLog
from render_functions import render_names_at_mouse_location, render_bar

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap
    from input_handlers import EventHandler


class Engine:
    game_map: GameMap

    def __init__(self, player: Actor):
        self.event_handler: EventHandler = MainGameEventHandler(self)
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    entity.ai.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible action exceptions from AI.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=15,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, camera: Camera) -> None:
        self.game_map.render(console, camera)
        console.draw_rect(0, 46, 80, 4, 219, fg=colour.BLACK, bg=colour.BLACK)
        self.message_log.render(console=console, x=21, y=46, width=60, height=4)

        render_names_at_mouse_location(console=console, x=1, y=45, engine=self)
        #render_mouse_location(console=console, engine=self, game_map=self.game_map)
