from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import tcod.event

from actions import Action, BumpAction, EscapeAction

if TYPE_CHECKING:
    from engine import Engine

class EventHandler(tcod.event.EventDispatch[Action]):

    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov()  # Update the FOV before the players next action.


    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        # Arrow movement
        if key == tcod.event.K_UP:
            action = BumpAction(player, dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(player, dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(player, dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(player, dx=1, dy=0)

        # Numpad movement
        if key == tcod.event.K_KP_1:
            action = BumpAction(player, dx=-1, dy=1)
        elif key == tcod.event.K_KP_2:
            action = BumpAction(player, dx=0, dy=1)
        elif key == tcod.event.K_KP_3:
            action = BumpAction(player, dx=1, dy=1)
        elif key == tcod.event.K_KP_4:
            action = BumpAction(player, dx=-1, dy=0)
        elif key == tcod.event.K_KP_5:
            action = BumpAction(player, dx=0, dy=0)
        elif key == tcod.event.K_KP_6:
            action = BumpAction(player, dx=1, dy=0)
        elif key == tcod.event.K_KP_7:
            action = BumpAction(player, dx=-1, dy=-1)
        elif key == tcod.event.K_KP_8:
            action = BumpAction(player, dx=0, dy=-1)
        elif key == tcod.event.K_KP_9:
            action = BumpAction(player, dx=1, dy=-1)

        # Keyboard movement
        elif key == tcod.event.K_h:
            action = BumpAction(player, dx=-1, dy=0)
        elif key == tcod.event.K_j:
            action = BumpAction(player, dx=0, dy=1)
        elif key == tcod.event.K_k:
            action = BumpAction(player, dx=0, dy=-1)
        elif key == tcod.event.K_l:
            action = BumpAction(player, dx=1, dy=0)
        elif key == tcod.event.K_y:
            action = BumpAction(player, dx=-1, dy=-1)
        elif key == tcod.event.K_u:
            action = BumpAction(player, dx=1, dy=-1)
        elif key == tcod.event.K_b:
            action = BumpAction(player, dx=-1, dy=1)
        elif key == tcod.event.K_n:
            action = BumpAction(player, dx=1, dy=1)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)

        # No valid key was pressed
        return action
