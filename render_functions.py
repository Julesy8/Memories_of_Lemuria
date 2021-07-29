from __future__ import annotations

from typing import TYPE_CHECKING

import tcod

import colour

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ", ".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )
    return names.capitalize()


def render_names_at_mouse_location(
    console: Console, x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=mouse_x, y=mouse_y, game_map=engine.game_map
    )

    console.print(x=x, y=y, string=names_at_mouse_location, fg=colour.WHITE, bg=(0, 0, 0))


def render_mouse_location(console: Console, engine: Engine, game_map: GameMap) -> None:
    mouse_x, mouse_y = engine.mouse_location

    if game_map.in_bounds(mouse_x, mouse_y):
        tcod.console_put_char_ex(console, mouse_x, mouse_y, 43, colour.YELLOW, colour.BLACK)

    else:
        return


def render_bar(
    console: Console, x: int, y: int, text: str, current_value: int, maximum_value: int, total_width: int
) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(x=x, y=y, width=total_width, height=1, ch=1, bg=colour.RED)

    if bar_width > 0:
        console.draw_rect(
            x=x, y=y, width=bar_width, height=1, ch=1, bg=colour.GREEN
        )

    console.print(
        x=x, y=y, string=f"{text}", fg=colour.WHITE
    )


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

    elif maximum_value * 0.25 <= current_value <= maximum_value * 0.50:
        console.print(x, y, character, colour.LIGHT_RED)

    elif 0 < current_value <= maximum_value * 0.50:
        console.print(x, y, character, colour.RED)

    elif current_value == 0:
        console.print(x, y, character, colour.DARK_GRAY)
