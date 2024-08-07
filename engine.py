from __future__ import annotations
import lzma
import pickle
from typing import TYPE_CHECKING
from random import choices, randint

from tcod import tileset

from numpy import logical_or

from tcod.console import Console
from tcod.map import compute_fov
from math import ceil
from components.weapons.gun_maker import crafting_dict
import colour

import exceptions
from level_parameters import level_names
from message_log import MessageLog
from render_functions import render_names_at_mouse_location, render_part

if TYPE_CHECKING:
    from entity import Actor, Item
    from game_map import GameMap


class GraveYard:
    def __init__(self):
        self.player_characters: list[Actor] = []
        self.guns: list[Item] = []


class Engine:
    game_map: GameMap

    def __init__(self, player: Actor):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.current_level = 0  # denotes the floor type
        self.current_floor = 0  # denotes the sublevel of the floor type
        self.player = player
        self.players: list[Actor] = [player]
        self.crafting_recipes = crafting_dict
        self.game_won = False
        self.game_over = False
        self.selected_players_attack = False

        self.keyboard_cursor = False
        self.keyboard_cursor_x: int = 0
        self.keyboard_cursor_y: int = 0

        self.bestiary = {}

        self.squad_mode: bool = False

        self.floor_str = f"{level_names[self.current_level]} [Floor {self.current_floor}]"

    def handle_queued_actions(self) -> None:
        for player in self.players:
            try:
                player.ai.perform()
            except exceptions.Impossible as exc:
                if not exc.args[0] == "Silent":  # if error is "Silent" as arg, doesn't print error to message log
                    self.message_log.add_message(exc.args[0], colour.RED)

    def switch_player(self) -> None:
        player_index = self.players.index(self.player)
        try:
            self.player = self.players[player_index + 1]
        except IndexError:
            self.player = self.players[0]

        self.game_map.camera_xy = (self.player.x, self.player.y + 3)

    def switch_to_player(self, index: int) -> None:
        try:
            self.player = self.players[index]
            self.game_map.camera_xy = (self.player.x, self.player.y + 3)
        except IndexError:
            pass

    def update_floor_str(self) -> None:
        self.floor_str = f"{level_names[self.current_level]} [{self.current_floor}]"

    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)

    def handle_turns(self) -> None:
        self.handle_queued_actions()
        self.update_fov()  # moved here from handle_action
        for entity in set(self.game_map.actors):
            #             if entity.ai and not entity in self.game_map.engine.players and entity.fighter.target_actor:
            if entity.ai and not entity.player:
                try:
                    if entity.fighter.active:
                        entity.ai.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible action exceptions from AI.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        fov = self.game_map.zeros

        # Could maybe make this faster by only recalculating the FOV for those players that have changed position since
        # last turn
        for player in self.players:
            player_fov = compute_fov(
                self.game_map.tiles["transparent"],
                (player.x, player.y),
                radius=self.game_map.fov_radius, )

            player.fighter.visible_tiles[:] = player_fov

            # activates entity when seen by player
            for entity in self.game_map.actors:
                if entity.ai and player.fighter.visible_tiles[entity.x, entity.y] and entity not in self.players:

                    # selects new target if inactive or no target currently
                    if not entity.fighter.active or entity.fighter.target_actor is None:
                        dx = entity.x - player.x
                        dy = entity.y - player.y
                        distance = max(abs(dx), abs(dy))  # Chebyshev distance.

                        # at 10 metres distance there's an equal chance of the enemy noticing you as not noticing you
                        sees_player = choices((True, False), weights=(10, distance))[0]
                        if sees_player:
                            entity.fighter.turns_attack_inactive = randint(2, 3)
                            entity.fighter.active = True
                            entity.fighter.target_actor = player

                    # random chance to change targets depending on distance of players from entity
                    if entity.fighter.target_actor is not None and entity.fighter.target_actor is not player:

                        dx_target = entity.x - player.x
                        dy_target = entity.y - player.y
                        distance_target = max(abs(dx_target), abs(dy_target))

                        dx_player = entity.x - player.x
                        dy_player = entity.y - player.y
                        distance_player = max(abs(dx_player), abs(dy_player))

                        if distance_player <= distance_target and choices((True, False),
                                                                          weights=(7, distance_target)):
                            entity.fighter.target_actor = player

            fov = logical_or(fov, player_fov)

        self.game_map.visible[:] = fov

        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:

        # start_time = time.time()

        self.game_map.render(console)

        if self.keyboard_cursor and not self.squad_mode:
            console.print(x=0, y=console.height - 8, string="VIEW MODE ON - PRESS [V] TO TOGGLE",
                          fg=colour.WHITE,
                          bg=(0, 0, 0))

        console.draw_rect(0, console.height - 7, console.width, 7, 219, bg=(0, 0, 0))
        console.hline(0, console.height - 7, console.width)

        if self.squad_mode:
            console.print(x=0, y=0, string=f"MODE: SQUAD │ COMBAT STYLE: {self.player.fighter.attack_style}",
                          fg=colour.WHITE, bg=(0, 0, 0))
        else:
            console.print(x=0, y=0, string=f"MODE: INDIVIDUAL │ COMBAT STYLE: {self.player.fighter.attack_style}",
                          fg=colour.WHITE, bg=(0, 0, 0))

        console.print(x=0, y=console.height - 6, string=self.player.name, fg=self.player.fg_colour,
                      bg=(0, 0, 0))

        # render message log
        self.message_log.render(console=console, x=6, y=console.height - 4,
                                width=console.width - 16, height=4)

        ap_str = f" | AP: {round(self.player.fighter.ap)}/{self.player.fighter.max_ap}"

        if self.player.ai is not None:
            if self.player.ai.queued_action:
                turns_remaining = ceil(abs(self.player.fighter.ap / self.player.fighter.ap_per_turn *
                                           self.player.fighter.ap_per_turn_modifier))
                ap_str = f" │ {self.player.ai.queued_action.action_str} ({turns_remaining} turns remain)"

        console.print(x=len(self.player.name), y=console.height - 6, string=ap_str, fg=colour.WHITE, bg=(0, 0, 0))

        # head
        render_part(console=console, x=2, y=console.height - 4, character="O",
                    current_value=self.player.bodyparts[1].hp,
                    maximum_value=self.player.bodyparts[1].max_hp)
        # body upper
        render_part(console=console, x=2, y=console.height - 3, character="┼",
                    current_value=self.player.bodyparts[0].hp,
                    maximum_value=self.player.bodyparts[0].max_hp)
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
                    current_value=self.player.bodyparts[0].hp,
                    maximum_value=self.player.bodyparts[0].max_hp)
        # right leg
        render_part(console=console, x=1, y=console.height - 1, character="/",
                    current_value=self.player.bodyparts[4].hp,
                    maximum_value=self.player.bodyparts[4].max_hp)
        # right leg
        render_part(console=console, x=3, y=console.height - 1, character=chr(tileset.CHARMAP_CP437[92]),
                    current_value=self.player.bodyparts[5].hp, maximum_value=self.player.bodyparts[5].max_hp)

        console.print(x=0, y=console.height - 4, string='R', fg=colour.WHITE)  # indicates right and left
        console.print(x=4, y=console.height - 4, string='L', fg=colour.WHITE)

        console.print(x=1, y=console.height - 7,
                      string=f"┤{self.floor_str}├", fg=colour.WHITE,
                      bg=(0, 0, 0))

        number_of_players = len(self.players)

        # squad members
        if number_of_players > 1:
            squad_display_height = (len(self.players) * 5) + 2

            longest_str = 0
            player_index = 1
            offset = 0

            for player in self.players:

                current_hp = 0
                max_hp = 0
                condition_colour = colour.GREEN
                condition_str = "UNHARMED"

                for bodypart in player.bodyparts[0:1]:
                    current_hp += bodypart.hp
                    max_hp += max_hp

                if current_hp == max_hp:
                    pass

                elif max_hp * 0.75 <= current_hp <= max_hp:
                    condition_str = "MINOR INJURY"
                    condition_colour = colour.YELLOW

                elif max_hp * 0.5 <= current_hp <= max_hp * 0.75:
                    condition_str = "INJURED"
                    condition_colour = colour.ORANGE

                elif max_hp * 0.15 <= current_hp <= max_hp * 0.50:
                    condition_str = "SERIOUSLY INJURED"
                    condition_colour = colour.LIGHT_RED

                elif 0 < current_hp <= max_hp * 0.15:
                    condition_str = "CRITICALLY INJURED"
                    condition_colour = colour.RED

                elif current_hp == 0:
                    condition_str = "DEAD"
                    condition_colour = colour.DARK_GRAY

                player_str = f"[{player_index}] {player.name}"
                player_str_len = len(player_str)

                if player_str_len > longest_str:
                    longest_str = player_str_len

                if len(condition_str) > longest_str:
                    longest_str = len(condition_str)

                weapon_str = 'UNARMED'

                if player.inventory.held is not None:

                    weapon_str = f"{player.inventory.held.name}"

                    # for magazine fed gun
                    if hasattr(player.inventory.held.usable_properties, "loaded_magazine"):
                        if player.inventory.held.usable_properties.loaded_magazine is None:
                            weapon_str += ' - No Mag'
                        else:
                            if player.inventory.held.usable_properties.chambered_bullet is not None:
                                weapon_str += (f""
                                               f" "
                                               f"({len(player.inventory.held.usable_properties.loaded_magazine.magazine) + 1}/"
                                               f"{player.inventory.held.usable_properties.loaded_magazine.mag_capacity})")
                            else:
                                weapon_str += (
                                    f" ({len(player.inventory.held.usable_properties.loaded_magazine.magazine)}/"
                                    f"{player.inventory.held.usable_properties.loaded_magazine.mag_capacity})")

                    # for gun with integrated magazine
                    elif hasattr(player.inventory.held.usable_properties, "mag_capacity"):

                        if player.inventory.held.usable_properties.chambered_bullet is not None:
                            weapon_str += (f" ({len(player.inventory.held.usable_properties.magazine) + 1}/"
                                           f"{player.inventory.held.usable_properties.mag_capacity})")
                        else:
                            weapon_str += (f" ({len(player.inventory.held.usable_properties.magazine)}/"
                                           f"{player.inventory.held.usable_properties.mag_capacity})")

                if len(weapon_str) > longest_str:
                    longest_str = len(weapon_str)

                ap_str = f" AP: {round(player.fighter.ap)}/{player.fighter.max_ap}"

                if player.ai is not None:
                    if player.ai.queued_action:
                        turns_remaining = ceil(abs(player.fighter.ap / player.fighter.ap_per_turn *
                                                   player.fighter.ap_per_turn_modifier))
                        ap_str = f" {player.ai.queued_action.action_str} ({turns_remaining})"

                if len(ap_str) > longest_str:
                    longest_str = len(ap_str)

                console.print(x=console.width - player_str_len - 1,
                              y=console.height - 7 - squad_display_height + player_index + offset,
                              string=player_str,
                              fg=player.fg_colour)

                console.print(x=console.width - len(weapon_str) - 1,
                              y=console.height - 7 - squad_display_height + player_index + offset + 1,
                              string=weapon_str,
                              fg=colour.WHITE)

                console.print(x=console.width - len(ap_str) - 1,
                              y=console.height - 7 - squad_display_height + player_index + offset + 2,
                              string=ap_str,
                              fg=colour.WHITE)

                console.print(x=console.width - len(condition_str) - 1,
                              y=console.height - 7 - squad_display_height + player_index + offset + 3,
                              string=condition_str,
                              fg=condition_colour,
                              )

                player_index += 1
                offset = 4

        # displays current ammo
        if self.player.inventory.held is not None:

            weapon_str = f"Held: {self.player.inventory.held.name}"

            # for magazine fed gun
            if hasattr(self.player.inventory.held.usable_properties, "loaded_magazine"):
                if self.player.inventory.held.usable_properties.loaded_magazine is None:
                    weapon_str += ' - No Mag'
                else:
                    if self.player.inventory.held.usable_properties.chambered_bullet is not None:
                        weapon_str += (f""
                                       f" "
                                       f"({len(self.player.inventory.held.usable_properties.loaded_magazine.magazine) + 1}/"
                                       f"{self.player.inventory.held.usable_properties.loaded_magazine.mag_capacity})")
                    else:
                        weapon_str += (f" ({len(self.player.inventory.held.usable_properties.loaded_magazine.magazine)}/"
                                       f"{self.player.inventory.held.usable_properties.loaded_magazine.mag_capacity})")

            # for gun with integrated magazine
            elif hasattr(self.player.inventory.held.usable_properties, "mag_capacity"):
                if self.player.inventory.held.usable_properties.chambered_bullet is not None:
                    weapon_str += (f" ({len(self.player.inventory.held.usable_properties.magazine) + 1}/"
                                   f"{self.player.inventory.held.usable_properties.mag_capacity})")
                else:
                    weapon_str += (f" ({len(self.player.inventory.held.usable_properties.magazine)}/"
                                   f"{self.player.inventory.held.usable_properties.mag_capacity})")

            console.print(x=console.width - len(weapon_str), y=console.height - 6, string=weapon_str,
                          fg=colour.WHITE, bg=(0, 0, 0))

        render_names_at_mouse_location(console=console, x=0, y=console.height - 5, engine=self, game_map=self.game_map)

        # end_time = time.time()
        # execution_time = start_time - end_time
        # print("Execution time:", execution_time)
