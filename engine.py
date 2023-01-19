from __future__ import annotations
import lzma
import pickle
from typing import TYPE_CHECKING

from tcod import tileset

from tcod.console import Console
from tcod.map import compute_fov
import colour

import exceptions
from level_parameters import level_names
from message_log import MessageLog
from render_functions import render_names_at_mouse_location, render_part

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap


class Engine:
    game_map: GameMap

    def __init__(self, player: Actor, current_level: int, current_floor: int):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.current_level = current_level  # denotes the floor type
        self.current_floor = current_floor  # denotes the sublevel of the floor type
        self.player = player
        self.crafting_recipes = {
            "guns": {},
            "gun parts": {},
        }

        self.floor_str = f"{level_names[self.current_level]} {self.current_floor + 1}"

    def update_floor_str(self) -> None:
        self.floor_str = f"{level_names[self.current_level]} {self.current_floor + 1}"

    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)

    def handle_enemy_turns(self) -> None:

        self.player.fighter.ap += round(self.player.fighter.ap_per_turn * self.player.fighter.ap_per_turn_modifier)

        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    if entity.active:
                        entity.ai.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible action exceptions from AI.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=self.game_map.fov_radius,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:
        self.game_map.render(console)
        console.draw_rect(0, console.height - 4, console.width, 4, 219, bg=(0, 0, 0))

        # render message log
        self.message_log.render(console=console, x=6, y=console.height - 4,
                                width=console.width - 16, height=4)

        # head
        render_part(console=console, x=2, y=console.height - 4, character="O",
                    current_value=self.player.bodyparts[0].hp,
                    maximum_value=self.player.bodyparts[0].max_hp)
        # body upper
        render_part(console=console, x=2, y=console.height - 3, character="┼",
                    current_value=self.player.bodyparts[1].hp,
                    maximum_value=self.player.bodyparts[1].max_hp)
        # right arm
        render_part(console=console, x=1, y=console.height - 3, character="─",
                    current_value=self.player.bodyparts[2].hp,
                    maximum_value=self.player.bodyparts[2].max_hp)
        # left arm
        render_part(console=console, x=3, y=console.height - 3, character="─",
                    current_value=self.player.bodyparts[3].hp,
                    maximum_value=self.player.bodyparts[3].max_hp)
        # body lower
        render_part(console=console, x=2, y=console.height - 2, character="│",
                    current_value=self.player.bodyparts[1].hp,
                    maximum_value=self.player.bodyparts[1].max_hp)
        # right leg
        render_part(console=console, x=1, y=console.height - 1, character="/",
                    current_value=self.player.bodyparts[4].hp,
                    maximum_value=self.player.bodyparts[4].max_hp)
        # right leg
        render_part(console=console, x=3, y=console.height - 1, character=chr(tileset.CHARMAP_CP437[92]),
                    current_value=self.player.bodyparts[5].hp, maximum_value=self.player.bodyparts[5].max_hp)

        console.print(x=0, y=console.height - 4, string='R', fg=colour.WHITE)  # indicates right and left
        console.print(x=4, y=console.height - 4, string='L', fg=colour.WHITE)

        console.print(x=console.width - len(self.floor_str), y=0,
                      string=f"{level_names[self.current_level]} {self.current_floor + 1}", fg=colour.WHITE, bg_blend=1)

        # displays current ammo
        if self.player.inventory.held is not None:

            # for magazine fed gun
            if hasattr(self.player.inventory.held.usable_properties, "loaded_magazine"):
                if self.player.inventory.held.usable_properties.loaded_magazine is None:
                    console.print(x=66, y=console.height - 3, string="No Mag", fg=colour.WHITE, bg_blend=1)

            # for gun with integrated magazine
            elif hasattr(self.player.inventory.held.usable_properties, "mag_capacity"):
                chamber = 0
                if self.player.inventory.held.usable_properties.chambered_bullet is not None:
                    chamber = 1
                gun = self.player.inventory.held.usable_properties
                console.print(x=66, y=console.height - 3, string=f"{len(gun.magazine) + chamber}/{gun.mag_capacity}",
                              fg=colour.WHITE, bg_blend=1)

        render_names_at_mouse_location(console=console, x=1, y=console.height - 5, engine=self)
