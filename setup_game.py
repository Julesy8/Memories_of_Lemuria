"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

from typing import Optional

import tcod
import numpy as np
import lzma
import pickle
import traceback

import colour
from engine import Engine
from scrolling_map import Camera
import input_handlers
from entity import Actor
from level_generator import MessyBSPTree
from level_parameters import level_params
from components.inventory import Inventory
from components.ai import HostileEnemy
from components.npc_templates import Fighter
from components.bodyparts import Bodypart


def new_game() -> Engine:
    """Return a brand new game session as an Engine instance."""
    current_level = 0

    # initialises player entity
    fighter_component = Fighter(power=6)

    head = Bodypart(hp=15, defence=15, vital=True, walking=False, grasping=False,
                    connected_to=[], equipped=None, name='Head', part_type='Head', base_chance_to_hit=80)
    body = Bodypart(hp=15, defence=15, vital=True, walking=False, grasping=False,
                    connected_to=[], equipped=None, name='Body', part_type='Body', base_chance_to_hit=90)
    r_arm = Bodypart(hp=15, defence=15, vital=False, walking=False, grasping=True,
                     connected_to=[], equipped=None, name='Right Arm', part_type='Arms', base_chance_to_hit=80)
    l_arm = Bodypart(hp=15, defence=15, vital=False, walking=False, grasping=True,
                     connected_to=[], equipped=None, name='Left Arm', part_type='Arms', base_chance_to_hit=80)
    r_leg = Bodypart(hp=15, defence=15, vital=False, walking=False, grasping=False,
                     connected_to=[], equipped=None, name='Right Leg', part_type='Legs', base_chance_to_hit=80)
    l_leg = Bodypart(hp=15, defence=15, vital=False, walking=False, grasping=False,
                     connected_to=[], equipped=None, name='Left Leg', part_type='Legs', base_chance_to_hit=80)

    body_parts = (body, head, r_arm, l_arm, r_leg, l_leg)

    player = Actor(0, 0,
                   '@',
                   colour.WHITE,
                   None,
                   'Player',
                   ai=HostileEnemy,
                   fighter=fighter_component,
                   bodyparts=body_parts,
                   attack_interval=0,
                   attacks_per_turn=1,
                   move_interval=0,
                   moves_per_turn=1,
                   player=True,
                   inventory=Inventory(capacity=15, held=None)
                   )

    engine = Engine(player=player, current_level=current_level, current_floor=0)

    engine.game_map = MessyBSPTree(level_params[current_level][0],  # messy tunnels
                                   level_params[current_level][1],  # map width
                                   level_params[current_level][2],  # map height
                                   level_params[current_level][3],  # max leaf size
                                   level_params[current_level][4],  # max room size
                                   level_params[current_level][5],  # room min size
                                   level_params[current_level][6],  # max monsters per room
                                   level_params[current_level][7],  # max items per room
                                   engine,
                                   current_level,
                                   ).generateLevel()

    engine.update_fov()

    engine.message_log.add_message(
        "You lose your footing and fall deep into the caverns below... You can't see any way to get back to the surface"
        , colour.LIGHT_MAGENTA
    )

    return engine


def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine


class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        """Render the main menu on a background image."""

        console2 = tcod.Console(32, 32, order="F")

        path = "new_logo.xp"  # REXPaint file with one layer.
        # Load a REXPaint file with a single layer.
        # The comma after console is used to unpack a single item tuple.
        console2, = tcod.console.load_xp(path, order="F")

        # Convert tcod's Code Page 437 character mapping into a NumPy array.
        CP437_TO_UNICODE = np.asarray(tcod.tileset.CHARMAP_CP437)

        # Convert from REXPaint's CP437 encoding to Unicode in-place.
        console2.ch[:] = CP437_TO_UNICODE[console2.ch]

        # Apply REXPaint's alpha key color.
        KEY_COLOR = (255, 0, 255)
        is_transparent = (console2.rgb["bg"] == KEY_COLOR).all(axis=2)
        console2.rgba[is_transparent] = (ord(" "), (0,), (0,))

        console2.blit(dest=console, dest_x=24, dest_y=6, src_x=0, src_y=0, width=32, height=32)

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "DEEP UNDERGROUND ROGUELIKE",
            fg=colour.WHITE,
            alignment=tcod.CENTER,
        )
        console.print(
            console.width // 2,
            console.height - 2,
            "Submit bug reports and suggestions to DeepUndergroundRL@protonmail.com",
            fg=colour.WHITE,
            alignment=tcod.CENTER,
        )
        console.print(
            1,
            1,
            "Pre-alpha",
            fg=colour.WHITE,
        )

        menu_width = 24
        for i, text in enumerate(
            ["[N] Play a new game", "[C] Continue last game", "[Q] Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=colour.RED,
                bg=colour.BLACK,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),
            )

    def ev_keydown(
        self, event: tcod.event.KeyDown
    ) -> Optional[input_handlers.BaseEventHandler]:
        if event.sym in (tcod.event.K_q, tcod.event.K_ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.K_c:
            try:
                return input_handlers.MainGameEventHandler(load_game("savegame.sav"))
            except FileNotFoundError:
                return input_handlers.PopupMessage(self, "No saved game to load.")
            except Exception as exc:
                traceback.print_exc()  # Print to stderr.
                return input_handlers.PopupMessage(self, f"Failed to load save:\n{exc}")
            pass
        elif event.sym == tcod.event.K_n:
            return input_handlers.MainGameEventHandler(new_game())

        return None
