from __future__ import annotations

from typing import TYPE_CHECKING
from math import atan2
import tcod
from entity import Item

import colour

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = []

    for entity in set(game_map.entities) - {game_map.engine.player}:
        if entity.x == x and entity.y == y:

            # omits player name from list
            try:

                weapon_name = None

                if hasattr(entity, 'inventory'):
                    if entity.inventory.held is not None:
                        weapon_name = entity.inventory.held.name

                if entity.ai:
                    if weapon_name is None:
                        names.append(f"{entity.name} │ Condition: {give_entity_condition(entity)}")
                    else:
                        names.append(f"{entity.name} │ Condition: {give_entity_condition(entity)} │ "
                                     f"Held: {weapon_name}")

                else:
                    names.append(entity.name)

            except AttributeError:
                names.append(entity.name)

            # shows stack size for stackable items
            if isinstance(entity, Item):
                if entity.stacking is not None:
                    if entity.stacking.stack_size > 1:
                        names[-1].join(f"({entity.stacking.stack_size})")

            # finds duplicate names and replaces them with a since string denoting the amount present
            name_count = 0
            for name in names:
                if name == entity.name:
                    name_count += 1
                    if name_count > 1:
                        names.remove(entity.name)

            if name_count > 1:
                names.remove(entity.name)
                names.append(f"{entity.name} x {name_count}")

    return ', '.join(map(str, names))


def give_entity_condition(entity):

    total_hp_max = 0
    total_hp = 0

    for part in entity.bodyparts:
        if part.vital:
            total_hp += part.hp
            total_hp_max += part.max_hp

    if total_hp == total_hp_max:
        return "Unscathed"

    elif total_hp_max * 0.75 <= total_hp <= total_hp_max:
        return "Damaged"

    elif total_hp_max * 0.5 <= total_hp <= total_hp_max * 0.75:
        return "Injured"

    elif total_hp_max * 0.15 <= total_hp <= total_hp_max * 0.50:
        return "Severely Injured"

    elif 0 < total_hp <= total_hp_max * 0.15:
        return "Critically Injured"


def render_names_at_mouse_location(
    console: Console, x: int, y: int, engine: Engine, game_map: GameMap
) -> None:

    screen_shape = console.rgb.shape
    cam_x, cam_y = game_map.get_left_top_pos(screen_shape)

    mouse_x, mouse_y = engine.mouse_location
    mouse_x += cam_x
    mouse_y += cam_y

    # print(mouse_x)
    # print(mouse_y)
    # print(engine.player.x)
    # print(engine.player.y)
    # orientation = atan2(engine.player.y - mouse_y,
    #                     engine.player.x - mouse_x)
    # print(orientation)

    names_at_mouse_location = ""

    if game_map.in_bounds(mouse_x, mouse_y):
        names_at_mouse_location = get_names_at_location(
            x=mouse_x, y=mouse_y, game_map=engine.game_map
        )

    names_at_player = get_names_at_location(
        x=engine.player.x, y=engine.player.y, game_map=engine.game_map
    )

    if names_at_mouse_location == "":
        console.print(x=x, y=y, string=names_at_player, fg=colour.WHITE, bg=(0, 0, 0))
    else:
        console.print(x=x, y=y, string=f"Mouse: {names_at_mouse_location}", fg=colour.WHITE, bg=(0, 0, 0))


def render_mouse_location(console: Console, engine: Engine, game_map: GameMap) -> None:
    mouse_x, mouse_y = engine.mouse_location

    if game_map.in_bounds(mouse_x, mouse_y):
        tcod.console_put_char_ex(console, mouse_x, mouse_y, 43, colour.YELLOW, colour.BLACK)
    else:
        return


def render_part(
        console: Console, x: int, y: int, character: str, current_value: int, maximum_value: int
) -> None:
    # used for graphically rendering body part health

    if current_value == maximum_value:
        console.print(x, y, character, colour.GREEN)

    elif maximum_value * 0.75 <= current_value <= maximum_value:
        console.print(x, y, character, colour.YELLOW)

    elif maximum_value * 0.5 <= current_value <= maximum_value * 0.75:
        console.print(x, y, character, colour.ORANGE)

    elif maximum_value * 0.15 <= current_value <= maximum_value * 0.50:
        console.print(x, y, character, colour.LIGHT_RED)

    elif 0 < current_value <= maximum_value * 0.15:
        console.print(x, y, character, colour.RED)

    elif current_value == 0:
        console.print(x, y, character, colour.DARK_GRAY)
