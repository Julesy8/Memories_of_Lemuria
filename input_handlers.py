from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        # Arrow movement
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        # Numpad movement
        if key == tcod.event.K_KP_1:
            action = MovementAction(dx=-1, dy=1)
        elif key == tcod.event.K_KP_2:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_KP_3:
            action = MovementAction(dx=1, dy=1)
        elif key == tcod.event.K_KP_4:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_KP_5:
            action = MovementAction(dx=0, dy=0)
        elif key == tcod.event.K_KP_6:
            action = MovementAction(dx=1, dy=0)
        elif key == tcod.event.K_KP_7:
            action = MovementAction(dx=-1, dy=-1)
        elif key == tcod.event.K_KP_8:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_KP_9:
            action = MovementAction(dx=1, dy=-1)

        # Keyboard movement
        elif key == tcod.event.K_h:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_j:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_k:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_l:
            action = MovementAction(dx=1, dy=0)
        elif key == tcod.event.K_y:
            action = MovementAction(dx=-1, dy=-1)
        elif key == tcod.event.K_u:
            action = MovementAction(dx=1, dy=-1)
        elif key == tcod.event.K_b:
            action = MovementAction(dx=-1, dy=1)
        elif key == tcod.event.K_n:
            action = MovementAction(dx=1, dy=1)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action
