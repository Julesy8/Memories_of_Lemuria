from __future__ import annotations
import lzma
import pickle
from typing import TYPE_CHECKING

from tcod import tileset

from tcod.console import Console
from tcod.map import compute_fov
from scrolling_map import Camera
import colour

import exceptions
from level_parameters import level_params
from message_log import MessageLog
from render_functions import render_names_at_mouse_location, render_part

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap


class Engine:
    game_map: GameMap

    def __init__(self, player: Actor, current_level: int):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.current_level = current_level
        self.player = player

    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)

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
        camera.update(entity=self.player, map_width=self.game_map.width, map_height=self.game_map.height)
        self.game_map.render(console, camera)
        console.draw_rect(0, 46, 80, 4, 219)
        self.message_log.render(console=console, x=6, y=46, width=60, height=4)

        # head
        render_part(console=console, x=2, y=46, character="O", current_value=self.player.bodyparts[0].hp,
                    maximum_value=self.player.bodyparts[0].max_hp)
        # body upper
        render_part(console=console, x=2, y=47, character="┼", current_value=self.player.bodyparts[1].hp,
                    maximum_value=self.player.bodyparts[1].max_hp)
        # right arm
        render_part(console=console, x=1, y=47, character="─", current_value=self.player.bodyparts[2].hp,
                    maximum_value=self.player.bodyparts[2].max_hp)
        # left arm
        render_part(console=console, x=3, y=47, character="─", current_value=self.player.bodyparts[3].hp,
                    maximum_value=self.player.bodyparts[3].max_hp)
        # body lower
        render_part(console=console, x=2, y=48, character="│", current_value=self.player.bodyparts[1].hp,
                    maximum_value=self.player.bodyparts[1].max_hp)
        # right leg
        render_part(console=console, x=1, y=49, character="/", current_value=self.player.bodyparts[4].hp,
                    maximum_value=self.player.bodyparts[4].max_hp)
        # right leg
        render_part(console=console, x=3, y=49, character=chr(tileset.CHARMAP_CP437[92]),
                    current_value=self.player.bodyparts[5].hp, maximum_value=self.player.bodyparts[5].max_hp)
        console.print(x=0, y=46, string='R', fg=colour.WHITE)  # indicates right and left
        console.print(x=4, y=46, string='L', fg=colour.WHITE)

        render_names_at_mouse_location(console=console, x=1, y=45, engine=self)
        # render_mouse_location(console=console, engine=self, game_map=self.game_map)
