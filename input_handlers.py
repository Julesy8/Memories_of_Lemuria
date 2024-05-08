from __future__ import annotations

import os
from copy import deepcopy
from typing import Optional, TYPE_CHECKING, Union, Callable
from configparser import ConfigParser
from math import ceil
import numpy as np
import tcod
import textwrap
import tcod.event

from entity import Item, Actor, Entity
import actions
from actions import (
    Action,
    BumpAction,
    PickupAction,
    ReloadMagFed,
    LoadBulletsIntoMagazine,
    GunAttackAction
)

import colour
import exceptions

if TYPE_CHECKING:
    from engine import Engine
    from components.consumables import Magazine, Bullet, Gun, GunMagFed, GunIntegratedMag, Clip, DetachableMagazine
    from components.bodyparts import Bodypart

config = ConfigParser()
config.read('settings.ini')
max_fps = config.getint('settings', 'max_fps')

MOVE_KEYS = {
    # Arrow keys.
    tcod.event.K_UP: (0, -1),
    tcod.event.K_DOWN: (0, 1),
    tcod.event.K_LEFT: (-1, 0),
    tcod.event.K_RIGHT: (1, 0),
    tcod.event.K_HOME: (-1, -1),
    tcod.event.K_END: (-1, 1),
    tcod.event.K_PAGEUP: (1, -1),
    tcod.event.K_PAGEDOWN: (1, 1),
    # Numpad keys.
    tcod.event.K_KP_1: (-1, 1),
    tcod.event.K_KP_2: (0, 1),
    tcod.event.K_KP_3: (1, 1),
    tcod.event.K_KP_4: (-1, 0),
    tcod.event.K_KP_6: (1, 0),
    tcod.event.K_KP_7: (-1, -1),
    tcod.event.K_KP_8: (0, -1),
    tcod.event.K_KP_9: (1, -1),
    # Vi keys.
    tcod.event.K_h: (-1, 0),
    tcod.event.K_j: (0, 1),
    tcod.event.K_k: (0, -1),
    tcod.event.K_l: (1, 0),
    tcod.event.K_y: (-1, -1),
    tcod.event.K_u: (1, -1),
    tcod.event.K_b: (-1, 1),
    tcod.event.K_n: (1, 1),
}

WAIT_KEYS = {
    tcod.event.K_PERIOD,
    tcod.event.K_KP_5,
    tcod.event.K_CLEAR,
}

ActionOrHandler = Union[Action, "BaseEventHandler"]
"""An event handler return value which can trigger an action or switch active handlers.

If a handler is returned then it will become the active handler for future events.
If an action is returned it will be attempted and if it's valid then
MainGameEventHandler will become the active handler.
"""


class BaseEventHandler(tcod.event.EventDispatch[ActionOrHandler]):
    def handle_events(self, event: tcod.event.Event) -> BaseEventHandler:
        """Handle an event and return the next active event handler."""
        state = self.dispatch(event)
        if isinstance(state, BaseEventHandler):
            return state
        assert not isinstance(state, Action), f"{self!r} can not handle actions."
        return self

    def on_render(self, console: tcod.Console) -> None:
        raise NotImplementedError

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()


class PopupMessage(BaseEventHandler):
    """Display a popup text window."""

    def __init__(self, parent_handler: BaseEventHandler, text: str, title: str):
        self.parent = parent_handler
        self.text = text
        self.title = title

    def on_render(self, console: tcod.Console) -> None:
        """Render the parent and dim the result, then print the message on top."""
        self.parent.on_render(console)

        wrapper = textwrap.TextWrapper(width=37)
        wrapped_text = wrapper.wrap(text=self.text)

        lines_text = len(wrapped_text)

        # Draw a frame with a custom banner title.
        console.draw_frame(console.width // 2 - 20, console.height // 2 - 1, 40,
                           lines_text + 3, bg=(0, 0, 0), fg=colour.WHITE)
        console.print_box(console.width // 2 - 20, console.height // 2 - 1, 40,
                          lines_text + 3, f"┤{self.title}├", alignment=tcod.CENTER, bg=(0, 0, 0), fg=colour.WHITE)

        y = console.height // 2

        for line in wrapped_text:
            console.print(
                console.width // 2 - 19,
                y,
                line,
                fg=colour.WHITE,
                bg=(0, 0, 0),
                # alignment=tcod.CENTER,
            )

            y += 1

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[BaseEventHandler]:
        """Any key returns to the parent handler."""
        return self.parent


class EventHandler(BaseEventHandler):

    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self, event: tcod.event.Event) -> BaseEventHandler:
        """Handle events for input handlers with an engine."""
        action_or_state = self.dispatch(event)
        if isinstance(action_or_state, BaseEventHandler):
            return action_or_state
        if self.handle_action(action_or_state):
            # A valid action was performed.
            if not self.engine.player.is_alive:
                # The player was killed sometime during or after the action.
                return GameOverEventHandler(self.engine)
            if self.engine.game_won:
                return GameWonEventHandler(self.engine)

            # checks if previous target actor is still visible, if not resets to None
            if self.engine.player.fighter.previous_target_actor is not None:
                if not self.engine.game_map.visible[self.engine.player.fighter.previous_target_actor.x,
                self.engine.player.fighter.previous_target_actor.y]:
                    self.engine.player.fighter.previous_target_actor = None
                    self.engine.player.fighter.previously_targeted_part = None

                elif not isinstance(action_or_state, GunAttackAction) or not isinstance(action_or_state, BumpAction):
                    self.engine.player.fighter.previous_target_actor = None
                    self.engine.player.fighter.previously_targeted_part = None

            return MainGameEventHandler(self.engine)  # Return to the main handler.
        return self

    def handle_action(self, action: Optional[Action]) -> bool:
        """Handle actions returned from event methods.

        Returns True if the action will advance a turn.
        """

        if action is None:
            return False

        try:
            action.handle_action()
        except exceptions.Impossible as exc:
            if not exc.args[0] == "Silent":  # if error is "Silent" as arg, doesn't print error to message log
                self.engine.message_log.add_message(exc.args[0], colour.RED)
            return False  # Skip enemy turn on exceptions.

        if not self.engine.squad_mode:
            self.engine.handle_turns()

        # self.engine.update_fov() moved to handle_turns

        return True

    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:
        self.engine.mouse_location = event.tile.x, event.tile.y

    def on_render(self, console: tcod.Console) -> None:
        self.engine.render(console)


class MainGameEventHandler(EventHandler):

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        action: Optional[Action] = None

        key = event.sym
        modifier = event.mod

        player = self.engine.player

        if key == tcod.event.K_PERIOD and modifier & (
                tcod.event.KMOD_LSHIFT | tcod.event.KMOD_RSHIFT
        ):
            return actions.TakeStairsAction(player)

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy)
        elif key in WAIT_KEYS:
            self.engine.handle_turns()
            # action = WaitAction(player)
        elif key == tcod.event.K_v:
            return HistoryViewer(self.engine, parent_handler=self)
        elif key == tcod.event.K_g:
            return PickUpEventHandler(engine=self.engine, parent_handler=self)
        elif key == tcod.event.K_r:
            return LoadoutEventHandler(engine=self.engine, parent_handler=self)
        elif key == tcod.event.K_q:
            try:
                # held gun is mag fed
                if hasattr(player.inventory.held.usable_properties, 'loaded_magazine'):
                    return GunOptionsMagFed(engine=self.engine, gun=player.inventory.held.usable_properties,
                                            parent_handler=self)
                # held gun is integrated magazine
                elif hasattr(player.inventory.held.usable_properties, 'magazine'):
                    return GunOptionsIntegratedMag(engine=self.engine, gun=player.inventory.held.usable_properties,
                                                   parent_handler=self)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry: no held weapon", colour.RED)
        elif key == tcod.event.K_ESCAPE:
            return QuitEventHandler(self.engine, parent_handler=self)
        elif key == tcod.event.K_c:
            return SelectItemToCraft(engine=self.engine, item_dict=self.engine.crafting_recipes, title='Crafting',
                                     parent_handler=self)
        elif key == tcod.event.K_i:
            return InventoryEventHandler(self.engine, parent_handler=self)
        elif key == tcod.event.K_e:
            return EquipmentEventHandler(self.engine, parent_handler=self)
        elif key == tcod.event.K_s:
            return AttackStyleMenu(self.engine, parent_handler=self)
        elif key == tcod.event.K_t:
            return Bestiary(self.engine, parent_handler=self)
        elif key == tcod.event.K_p:
            return ViewPlayer(self.engine, parent_handler=self)

        elif key == tcod.event.K_SPACE:
            return ChangeTargetActor(engine=self.engine, in_squad_mode=self.engine.squad_mode, parent_handler=self)

        elif key == tcod.event.K_TAB:
            return self.engine.switch_player()
        elif key == tcod.event.K_RALT:
            if self.engine.squad_mode:
                self.engine.squad_mode = False
            else:
                self.engine.squad_mode = True
        # No valid key was pressed
        return action


def on_quit() -> None:
    """Handle exiting out of a finished game."""
    if os.path.exists("savegame.sav"):
        os.remove("savegame.sav")  # Deletes the active save file.
    raise exceptions.QuitWithoutSaving()  # Avoid saving a finished game.


class GameOverEventHandler(EventHandler):

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        console.draw_frame(
            x=console.width // 2 - 18,
            y=console.height // 2 - 4,
            width=36,
            height=5,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        console.print(x=console.width // 2 - 16, y=console.height // 2 - 2, string="Your team perished in the depths",
                      fg=colour.MAGENTA, bg=(0, 0, 0))

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:

        key = event.sym

        if key == tcod.event.K_v:
            return HistoryViewer(self.engine, parent_handler=self)
        elif key == tcod.event.K_ESCAPE:
            os.remove('savegame.sav')
            return QuitEventHandler(self.engine, parent_handler=self)
        elif key == tcod.event.K_t:
            return Bestiary(self.engine, parent_handler=self)


class GameWonEventHandler(EventHandler):

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        path = "win_screen.xp"  # REXPaint file with one layer.
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

        console.draw_frame(
            x=console.width // 2 - 46,
            y=console.height // 2 - 27,
            width=92,
            height=29,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        console2.blit(dest=console, dest_x=console.width // 2 - 43, dest_y=console.height // 2 - 24, src_x=0, src_y=0,
                      width=86,
                      height=52)

        console.print(x=console.width // 2 - 38, y=console.height // 2 - 4,
                      string="YOUR TEAM DESTROYED THE EVIL EXTRATERRESTRIAL FORCES AND SAVED THE COUNTRY!",
                      fg=colour.MAGENTA, bg=(0, 0, 0))

        console.print(x=console.width // 2 - 14, y=console.height // 2 - 2, string="PRESS [ESC] TO QUIT TO MENU.",
                      fg=colour.WHITE, bg=(0, 0, 0))

    def ev_keydown(self, event: tcod.event.KeyDown):

        key = event.sym

        if key == tcod.event.K_ESCAPE:
            raise exceptions.QuitToMenu

CURSOR_Y_KEYS = {
    tcod.event.K_UP: -1,
    tcod.event.K_DOWN: 1,
    tcod.event.K_PAGEUP: -10,
    tcod.event.K_PAGEDOWN: 10,
}


class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated."""

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler, ):
        super().__init__(engine)
        self.parent_handler = parent_handler
        self.log_length = len(engine.message_log.messages)
        self.cursor = self.log_length - 1

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        log_console = tcod.Console(console.width - 6, console.height - 6, order="F")

        # Draw a frame with a custom banner title.
        log_console.draw_frame(0, 0, log_console.width, log_console.height)
        log_console.print_box(
            0, 0, log_console.width, 1, "┤Message history├", alignment=tcod.CENTER
        )

        # Render the message log using the cursor parameter.
        self.engine.message_log.render_messages(
            log_console,
            1,
            1,
            log_console.width - 2,
            log_console.height - 2,
            self.engine.message_log.messages[: self.cursor + 1],
        )
        log_console.blit(console, 3, 3)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[BaseEventHandler]:
        # Fancy conditional movement to make it feel right.
        if event.sym in CURSOR_Y_KEYS:
            adjust = CURSOR_Y_KEYS[event.sym]
            if adjust < 0 and self.cursor == 0:
                # Only move from the top to the bottom when you're on the edge.
                self.cursor = self.log_length - 1
            elif adjust > 0 and self.cursor == self.log_length - 1:
                # Same with bottom to top movement.
                self.cursor = 0
            else:
                # Otherwise move while staying clamped to the bounds of the history log.
                self.cursor = max(0, min(self.cursor + adjust, self.log_length - 1))
        elif event.sym == tcod.event.K_HOME:
            self.cursor = 0  # Move directly to the top message.
        elif event.sym == tcod.event.K_END:
            self.cursor = self.log_length - 1  # Move directly to the last message.
        else:  # Any other key moves back to the main game state.
            return self.parent_handler
        return None


class AskUserEventHandler(EventHandler):

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):
        super().__init__(engine)
        self.parent_handler = parent_handler

    """Handles user input for actions which require special input."""

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        """By default any key exits this input handler."""
        if event.sym in {  # Ignore modifier keys.
            tcod.event.K_LSHIFT,
            tcod.event.K_RSHIFT,
            tcod.event.K_LCTRL,
            tcod.event.K_RCTRL,
            tcod.event.K_LALT,
            tcod.event.K_RALT,
        }:
            return None
        return self.on_exit()

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        """By default any mouse click exits this input handler."""
        return self.on_exit()

    def on_exit(self) -> Optional[ActionOrHandler]:
        """Called when the user is trying to exit or cancel an action.

        By default this returns to the main event handler.
        """
        return self.parent_handler


class UserOptionsEventHandler(AskUserEventHandler):

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler, options: list, title: str):
        self.options = options
        self.TITLE = title
        super().__init__(engine, parent_handler)

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        longest_option_name = 0

        for option in self.options:

            if isinstance(option, Item):
                stack_size = 0

                if option.stacking:
                    stack_size = 3 + option.stacking.stack_size
                if len(option.name) + stack_size > longest_option_name:
                    longest_option_name = len(option.name) + stack_size
            else:
                if len(option) > longest_option_name:
                    longest_option_name = len(option)

        width = len(self.TITLE)

        if longest_option_name > width:
            width = longest_option_name

        x = 1
        y = 2

        console.draw_frame(
            x=x,
            y=y,
            width=width + 8,
            height=len(self.options) + 2,
            title=self.TITLE,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        for i, option in enumerate(self.options):
            option_key = chr(ord("a") + i)
            if isinstance(option, Item):
                console.print(x + 1, y + i + 1, f"({option_key}) {option.name}")
            else:
                console.print(x + 1, y + i + 1, f"({option_key}) {option}")

    def ev_keydown(self, event: tcod.event.KeyDown):
        key = event.sym
        index = key - tcod.event.K_a

        if event.sym == tcod.event.K_ESCAPE:
            return self.parent_handler

        if 0 <= index <= 26:
            try:
                selected_option = self.options[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)
                return self
            return self.ev_on_option_selected(selected_option)
        return super().ev_keydown(event)

    def ev_on_option_selected(self, option):
        return NotImplementedError


class UserOptionsWithPages(AskUserEventHandler):
    TITLE = "<missing title>"

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler, page: int, options: list, title: str):
        self.max_list_length = 15  # defines the maximum amount of items to be displayed in the menu
        self.page = page
        self.options = options
        self.TITLE = title

        super().__init__(engine, parent_handler)

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        number_of_options = len(self.options)

        width = len(self.TITLE)
        height = number_of_options + 2

        if number_of_options > self.max_list_length:
            height = self.max_list_length + 2

        x = 1
        y = 2

        index_range = self.page * self.max_list_length

        longest_name_len = 0

        for item in self.options[index_range:index_range + self.max_list_length]:

            # item is of the Item class
            if isinstance(item, Item):
                stack_size = 0

                if item.stacking:
                    stack_size = 3 + item.stacking.stack_size
                if len(item.name) + stack_size > longest_name_len:
                    longest_name_len = len(item.name) + stack_size

            # item is a string
            else:
                if len(item) > longest_name_len:
                    longest_name_len = len(item)

        if longest_name_len:
            if longest_name_len > width:
                width = longest_name_len

        console.draw_frame(
            x=x,
            y=y,
            width=width + 8,
            height=height,
            title=self.TITLE,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        if number_of_options > 0:
            console.print(x + 1, y + height - 1,
                          f"Page {self.page + 1}/{ceil(len(self.options) / self.max_list_length)}")

            for i, item in enumerate(self.options[index_range:index_range + self.max_list_length]):
                item_key = chr(ord("a") + i)

                if isinstance(item, Item):

                    if item.stacking:
                        console.print(x + 1, y + i + 1, f"({item_key}) {item.name} ({item.stacking.stack_size})")
                    else:
                        console.print(x + 1, y + i + 1, f"({item_key}) {item.name}")

                else:
                    console.print(x + 1, y + i + 1, f"({item_key}) {item}")

        else:
            console.print(x + 1, y + 1, "(Empty)")

    def ev_keydown(self, event: tcod.event.KeyDown):
        key = event.sym
        index = key - tcod.event.K_a

        if key == tcod.event.K_DOWN:
            if len(self.options) > (self.page + 1) * self.max_list_length:
                self.page += 1
                return self

        if key == tcod.event.K_UP:
            if self.page > 0:
                self.page -= 1
                return self

        if 0 <= index <= self.max_list_length - 1:
            try:
                selected_item = self.options[index + (self.page * self.max_list_length)]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.ev_on_option_selected(selected_item)
        return super().ev_keydown(event)

    def ev_on_option_selected(self, option):
        return NotImplementedError


class TypeInputEventHandler(AskUserEventHandler):
    def __init__(self, item: Entity, parent_handler: BaseEventHandler, prompt_string: str, engine: Engine):
        super().__init__(engine, parent_handler)
        self.item = item
        self.engine = engine
        self.buffer = ''
        self.prompt_string = prompt_string

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        console.draw_frame(
            x=1,
            y=1,
            width=len(self.prompt_string) + len(self.buffer) + 3,
            height=3,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )
        console.print(x=2, y=2, string=f"{self.prompt_string} {self.buffer}", fg=colour.WHITE, bg=(0, 0, 0))

    def ev_keydown(self, event):
        key = event.sym

        try:
            for event in tcod.event.wait():
                if isinstance(event, tcod.event.TextInput):
                    if len(self.buffer) < 21:
                        self.buffer += event.text

            if not event.repeat:
                if key == tcod.event.K_ESCAPE:
                    return self.parent_handler

                elif key == tcod.event.K_BACKSPACE:
                    self.buffer = self.buffer[:-1]

                elif key == tcod.event.K_RETURN:
                    return self.ev_on_option_selected()

        except AttributeError:
            pass

    def ev_on_option_selected(self):
        return NotImplementedError


class TypeAmountEventHandler(TypeInputEventHandler):

    def ev_keydown(self, event):

        key = event.sym

        if self.item.stacking:
            if self.item.stacking.stack_size > 1:
                try:

                    for event in tcod.event.wait():
                        if isinstance(event, tcod.event.TextInput):
                            if event.text.isdigit():
                                self.buffer += event.text

                    if key == tcod.event.K_ESCAPE:
                        return self.parent_handler

                    elif key == tcod.event.K_BACKSPACE:
                        self.buffer = self.buffer[:-1]

                    elif key == tcod.event.K_RETURN:

                        if self.buffer == '' or int(self.buffer) < 1:
                            self.buffer = f'{self.item.stacking.stack_size}'

                        return self.ev_on_option_selected()

                except AttributeError:
                    self.buffer = f'{self.item.stacking.stack_size}'

            else:
                self.buffer = '1'
                return self.ev_on_option_selected()

        else:
            self.buffer = '1'
            return self.ev_on_option_selected()

    def ev_on_option_selected(self):
        return NotImplementedError


class InventoryEventHandler(UserOptionsWithPages):

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):
        title = "Inventory" + f" - {round(engine.player.inventory.current_item_weight(), 2)}" \
                              f"/{engine.player.inventory.capacity}kg"

        super().__init__(engine=engine, parent_handler=parent_handler,
                         options=engine.player.inventory.items, page=0, title=title)

    def ev_on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        options = []

        if hasattr(item, 'usable_properties'):
            options.append('use')

        if hasattr(item.usable_properties, 'fits_bodypart'):
            options.append('equip')

        options += ['drop', 'inspect']

        if hasattr(item.usable_properties, 'gun_type'):
            options += ['equip to primary', 'equip to secondary', 'disassemble', 'rename']

        return ItemInteractionHandler(item=item, options=options, engine=self.engine, parent_handler=self)


class ItemInteractionHandler(UserOptionsEventHandler):  # options for interacting with an item

    def __init__(self, item, options: list, engine: Engine, parent_handler: BaseEventHandler):
        self.item = item
        super().__init__(engine=engine, parent_handler=parent_handler, options=options, title=item.name)

    def ev_on_option_selected(self, option) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        if option == 'use':
            try:
                if hasattr(self.item.usable_properties, 'mag_capacity'):
                    if hasattr(self.item.usable_properties, 'gun_type'):
                        return GunOptionsIntegratedMag(engine=self.engine, gun=self.item.usable_properties,
                                                       parent_handler=self)
                    else:
                        return MagazineOptionsHandler(engine=self.engine, magazine=self.item.usable_properties,
                                                      parent_handler=self)
                elif hasattr(self.item.usable_properties, 'loaded_magazine'):
                    return GunOptionsMagFed(engine=self.engine, gun=self.item.usable_properties,
                                            parent_handler=self)
                else:
                    return self.item.usable_properties.get_action(self.engine.player)

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)
            except NotImplementedError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'pick up':
            if self.item.stacking:
                if self.item.stacking.stack_size > 1:
                    return AmountToPickUpMenu(item=self.item, engine=self.engine, parent_handler=self)
                else:
                    return PickupAction(entity=self.engine.player, item=self.item, amount=1)
            else:
                return PickupAction(entity=self.engine.player, item=self.item, amount=1)

        elif option == 'rename':
            return RenameItem(item=self.item, prompt_string='New Name:', engine=self.engine,
                              parent_handler=self)

        elif option == 'equip':
            try:
                self.item.usable_properties.equip(user=self.engine.player)
                return self.parent_handler

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'equip to primary':
            try:
                self.item.usable_properties.equip_to_primary(user=self.engine.player)
                return self.parent_handler

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'equip to secondary':
            try:
                self.item.usable_properties.equip_to_secondary(user=self.engine.player)
                return self.parent_handler

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'unequip':
            try:
                self.item.usable_properties.unequip(user=self.engine.player)
                return self.parent_handler
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'drop':
            try:
                return DropItemEventHandler(item=self.item, engine=self.engine, parent_handler=self.parent_handler)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'disassemble':
            if hasattr(self.item.usable_properties, 'parts'):
                self.item.usable_properties.parts.disassemble(entity=self.engine.player)
                for i in range(5):
                    self.engine.handle_turns()
                return MainGameEventHandler(self.engine)

        elif option == 'inspect':
            return InspectItemViewer(engine=self.engine, item=self.item, parent_handler=self.parent_handler)

        else:
            self.engine.message_log.add_message("Invalid entry", colour.RED)


class EquipmentEventHandler(AskUserEventHandler):
    # used for equipment screen
    TITLE = "Equipment"

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):
        super().__init__(engine, parent_handler)
        self.equipped_list = []  # equipped items

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        equipment_dictionary = {}  # dictionary containing bodypart associated with the item equipped

        longest_name_len = 0  # longest name of item

        if self.engine.player.inventory.held is not None:
            equipment_dictionary[self.engine.player.inventory.held.name] = "Held"
            self.equipped_list.append(self.engine.player.inventory.held)
            longest_name_len = len(self.engine.player.inventory.held.name)

        # adds all items equipped by bodyparts of the entity to the equipped list
        for bodypart in self.engine.player.bodyparts:

            if bodypart.equipped is not None:

                self.equipped_list.append(bodypart.equipped.parent)
                equipment_dictionary[bodypart.equipped.parent.name] = bodypart.part_type

                if len(bodypart.equipped.parent.name) > longest_name_len:
                    longest_name_len = len(bodypart.equipped.parent.name)

        self.equipped_list = list(dict.fromkeys(self.equipped_list))

        width = len(self.TITLE) + 4
        height = len(self.equipped_list) + 2

        x = 1
        y = 2

        if longest_name_len + 15 > width:
            width = longest_name_len + 16

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=height,
            title=self.TITLE,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        if len(self.equipped_list) > 0:
            for i, item in enumerate(self.equipped_list):
                item_key = chr(ord("a") + i)
                console.print(x + 1, y + i + 1, f"({item_key}) {equipment_dictionary[item.name]} | {item.name}")

        else:
            console.print(x + 1, y + 1, "(Empty)")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        key = event.sym
        index = key - tcod.event.K_a

        if 0 <= index <= 26:
            try:
                selected_item = self.equipped_list[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)
                return EquipmentEventHandler(engine=self.engine, parent_handler=self)
            return self.on_item_selected(selected_item)
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        options = ['unequip', 'inspect']

        return ItemInteractionHandler(item=item, options=options, engine=self.engine,
                                      parent_handler=self.parent_handler)


class ViewPlayer(UserOptionsEventHandler):

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):
        self.options = ['Rename', 'View Player Stats [z]', 'Inventory [i]', 'Equipment [e]',
                        'Loadout [r]', 'Held Weapon [q]', 'Attack Style [s]', 'Crafting [c]']
        super().__init__(engine, parent_handler, options=self.options, title=engine.player.name)

    def ev_on_option_selected(self, option):

        player = self.engine.player

        if option == 'Rename':
            return RenamePlayer(engine=self.engine, parent_handler=self)
        elif option == 'View Player Stats [z]':
            return ViewPlayerStats(engine=self.engine, parent_handler=self)
        elif option == 'Inventory [i]':
            return InventoryEventHandler(engine=self.engine, parent_handler=self)
        elif option == 'Equipment [e]':
            return EquipmentEventHandler(engine=self.engine, parent_handler=self)
        elif option == 'Loadout [r]':
            return LoadoutEventHandler(engine=self.engine, parent_handler=self)
        elif option == 'Held Weapon [q]':
            try:
                # held gun is mag fed
                if hasattr(player.inventory.held.usable_properties, 'loaded_magazine'):
                    return GunOptionsMagFed(engine=self.engine, gun=player.inventory.held, parent_handler=self)
                # held gun is integrated magazine
                elif hasattr(player.inventory.held.usable_properties, 'magazine'):
                    return GunOptionsIntegratedMag(engine=self.engine, gun=player.inventory.held, parent_handler=self)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry: no held weapon", colour.RED)
        elif option == 'Attack Style [s]':
            return AttackStyleMenu(engine=self.engine, parent_handler=self)
        elif option == 'Crafting [c]':
            return SelectItemToCraft(engine=self.engine, item_dict=self.engine.crafting_recipes, title='Crafting',
                                     parent_handler=self)
        elif option == 'Journal [t]':
            return Bestiary(engine=self.engine, parent_handler=self)


class RenamePlayer(TypeInputEventHandler):
    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):
        super().__init__(prompt_string="Rename Character", engine=engine, item=engine.player,
                         parent_handler=parent_handler)

    def ev_on_option_selected(self) -> Optional[ActionOrHandler]:
        if not self.buffer == '':
            self.item.name = self.buffer

        return self.parent_handler


class DropItemEventHandler(TypeAmountEventHandler):

    def __init__(self, item, engine: Engine, parent_handler: BaseEventHandler):
        super().__init__(engine=engine, parent_handler=parent_handler, item=item,
                         prompt_string="amount to drop (leave blank for all):")

    def ev_on_option_selected(self) -> Optional[ActionOrHandler]:
        return actions.DropAction(entity=self.engine.player, item=self.item, drop_amount=int(self.buffer))


class PickUpEventHandler(UserOptionsWithPages):
    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):

        items_at_location = []

        actor_location_x = engine.player.x
        actor_location_y = engine.player.y

        for item in engine.game_map.items:
            if actor_location_x == item.x and actor_location_y == item.y:
                items_at_location.append(item)

        super().__init__(engine=engine, page=0, options=items_at_location, title="Pick Up/Inspect Items",
                         parent_handler=parent_handler)

    def ev_on_option_selected(self, item):
        return ItemInteractionHandler(item=item, options=['pick up', 'inspect'], engine=self.engine,
                                      parent_handler=self.parent_handler)


class AmountToPickUpMenu(TypeAmountEventHandler):

    def __init__(self, item, engine: Engine, parent_handler: BaseEventHandler):
        super().__init__(engine=engine, item=item, prompt_string="amount to pick up (leave blank for all):",
                         parent_handler=parent_handler)

    def ev_on_option_selected(self) -> Optional[ActionOrHandler]:

        try:
            return actions.PickupAction(entity=self.engine.player, item=self.item, amount=int(self.buffer))

        except AttributeError:
            self.engine.message_log.add_message("Invalid entry", colour.RED)

        return self.parent_handler


class DestinationMarker:
    def __int__(self, x: int, y: int, colours: list[tuple[int, int, int]]):
        self.x = x
        self.y = y
        self.colours = colours


class ChangeTargetActor(AskUserEventHandler):

    def __init__(self, engine: Engine, in_squad_mode: bool, parent_handler: BaseEventHandler):
        super().__init__(engine, parent_handler)
        self.in_squad_mode = in_squad_mode
        self.tick_counter = 0
        self.max_tick = max_fps * 3
        self.players_selected = []
        # self.destinations = []
        self.engine = engine
        self.targets = []
        self.target_index = None
        self.selected_bodypart = None
        self.bodypart_index: int = 0
        self.bodypartlist: list = []

        # string and colour associated with the condition of the selected body part
        self.part_cond_str: str = "Unharmed"
        self.part_cond_colour: tuple[int, int, int] = colour.GREEN

        self.console = None

        self.item = self.engine.player.inventory.held

        self.engine.squad_mode = True

        self.get_targets()

    def get_targets(self) -> None:

        player = self.engine.player
        target_visible = False
        closest_distance = 1000
        closest_actor = None

        self.targets: list[Actor] = []

        for actor in set(self.engine.game_map.actors) - {player}:
            if self.engine.player.fighter.visible_tiles[actor.x, actor.y] and not actor.player:
                self.targets.append(actor)

                # checks if previous target is still visible
                if player.fighter.target_actor == actor:
                    target_visible = True

                # checks for closest actor incase previous target not visible
                distance = player.distance(actor.x, actor.y)

                if distance < closest_distance:
                    closest_actor = actor

        # sets target actor to closest actor
        if not target_visible:
            player.fighter.target_actor = closest_actor

        if player.fighter.target_actor is not None:
            # centres camera on target
            self.engine.game_map.camera_xy = (player.fighter.target_actor.x, player.fighter.target_actor.y + 3)

            # selects bodypart
            if self.selected_bodypart is None or not self.selected_bodypart in player.fighter.target_actor.bodyparts:
                self.selected_bodypart = player.fighter.target_actor.bodyparts[0]

            self.update_bodypart_list()
            self.update_part_str_colour()


            # sets targets index in target list
            self.target_index: int = self.targets.index(player.fighter.target_actor)

    def on_render(self, console: tcod.Console):

        super().on_render(console)  # Draw the main state as the background.

        blink_on = True

        self.console = console

        screen_shape = console.rgb.shape
        cam_x, cam_y = self.engine.game_map.get_left_top_pos(screen_shape)

        self.tick_counter += 1

        if self.tick_counter > self.max_tick - max_fps:
            blink_on = False
        if self.tick_counter > self.max_tick:
            self.tick_counter = 0

        player_name_list = []

        if len(self.players_selected) > 0:
            console.print(x=0, y=4, string="[PERIOD] - ADVANCE TURN", fg=colour.WHITE, bg=(0, 0, 0))

        for player in self.players_selected:
            player_name_list.append(player.name)
            player_x = player.x - cam_x
            player_y = player.y - cam_y
            if blink_on:
                console.print(player_x, player_y, player.char, player.fg_colour, (170, 255, 0))

        if len(player_name_list) > 0:
            console.print(x=0, y=3, string=f"PLAYERS SELECTED: {', '.join(player_name_list)}",
                          fg=colour.WHITE, bg=(0, 0, 0))

        # for destination in self.destinations:
        #     dest_x = destination[0] - cam_x
        #     dest_y = destination[1] - cam_y
        #     console.print(x=0, y=4, string="[PERIOD] - ADVANCE TURN", fg=colour.WHITE, bg=(0, 0, 0))
        #
        #     if blink_on and 0 <= dest_x < console.width and 0 <= dest_y < console.height:
        #         console.print(dest_x, dest_y, "X", colour.WHITE)

        player = self.engine.player

        console.print(x=0, y=1, string="SQUAD CONTROL - [ESC] TO EXIT", fg=colour.WHITE, bg=(0, 0, 0))

        # if gun is jammed, prints a message on the screen and instructs player on how to clear
        if self.item is not None:
            if hasattr(self.item.usable_properties, 'jammed'):
                if self.item.usable_properties.jammed:
                    console.print(x=0, y=console.height - 7, string="GUN JAMMED: [ENTER] TO CLEAR",
                                  fg=colour.RED, bg=(0, 0, 0))
                    return

        if player.fighter.target_actor is not None:

            target_x, target_y = player.fighter.target_actor.x - cam_x, player.fighter.target_actor.y - cam_y

            if (0 <= target_x < console.width and 0 <= target_y < console.height and blink_on
                    and self.engine.game_map.visible[player.fighter.target_actor.x, player.fighter.target_actor.y]):
                console.tiles_rgb[["ch", "fg"]][target_x, target_y] = ord('▼'), colour.LIGHT_RED

            distance_target = round(player.distance(player.fighter.target_actor.x, player.fighter.target_actor.y))

            target_str = (f"Targeting: {player.fighter.target_actor.name} "
                          f"[ID {player.fighter.target_actor.identifier}] - {self.selected_bodypart.name} "
                          f"│ Distance: {distance_target}M").upper()
            # ap_str = f"AP: {player.fighter.ap}/{player.fighter.max_ap}"

            offset = 0

            # if wearing armour, shows what body armour the enemy is wearing
            # if displaying armour, offsets other display information
            if self.selected_bodypart.equipped is not None:
                console.print(x=0, y=console.height - 6, string=f"ARMOUR: "
                                                                f"{self.selected_bodypart.equipped.parent.name}",
                              fg=colour.WHITE, bg=(0, 0, 0))
                offset = 1

            # displays AP and enemy information
            # console.print(x=1, y=console.height - 8 + offset, string=ap_str, fg=colour.WHITE, bg=(0, 0, 0))
            console.print(x=0, y=console.height - 9 + offset, string=target_str, fg=colour.WHITE, bg=(0, 0, 0))
            console.print(x=0, y=console.height - 8 + offset, string="PART CONDITION: ", fg=colour.WHITE, bg=(0, 0, 0))
            console.print(x=16, y=console.height - 8 + offset, string=f"{self.part_cond_str}", fg=self.part_cond_colour,
                          bg=(0, 0, 0))
            console.print(x=0, y=2, string="PRESS [K] FOR ENEMY INFO", fg=colour.WHITE, bg=(0, 0, 0))

        else:
            console.print(x=0, y=2, string="NO TARGET", fg=colour.WHITE, bg=(0, 0, 0))

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> None:
        screen_shape = self.console.rgb.shape
        cam_x, cam_y = self.engine.game_map.get_left_top_pos(screen_shape)

        mouse_x, mouse_y = self.engine.mouse_location
        mouse_x += cam_x
        mouse_y += cam_y

        # button 1 = LMB
        # button 3 = RMB

        if self.engine.game_map.in_bounds(mouse_x, mouse_y):

            # selects players or enemies to attack
            if event.button == 1:
                for entity in self.engine.game_map.actors:
                    if entity.x == mouse_x and entity.y == mouse_y:
                        # player selected
                        if entity.player:
                            if entity not in self.players_selected:
                                self.players_selected.append(entity)
                            else:
                                self.players_selected.remove(entity)
                        # enemy selected
                        else:
                            if self.engine.game_map.check_los(self.engine.player.x, self.engine.player.y, entity.x,
                                                              entity.y):
                                self.engine.player.fighter.target_actor = entity
                                self.selected_bodypart = self.engine.player.fighter.target_actor.bodyparts[0]
                                self.bodypart_index = 0
                                self.target_index = 0

            # moves players
            elif event.button == 3:

                for player in self.players_selected:

                    if self.engine.game_map.explored[mouse_x, mouse_y]:
                        player.ai.path_to_xy = (mouse_x, mouse_y)
                        # player.ai.path = player.ai.get_path_to(mouse_x, mouse_y)
                        # self.destinations.append([mouse_x, mouse_y])
                        self.players_selected = []

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        player = self.engine.player
        key = event.sym
        modifier = event.mod

        if key == tcod.event.K_SPACE:  # change target

            try:
                player.fighter.target_actor = self.targets[self.target_index + 1]
                self.selected_bodypart = player.fighter.target_actor.bodyparts[0]
                self.bodypart_index = 0
                self.target_index += 1
                # centres camera on target
                self.engine.game_map.camera_xy = (player.fighter.target_actor.x, player.fighter.target_actor.y + 3)
            except IndexError:
                if len(self.targets) > 0:
                    player.fighter.target_actor = self.targets[0]
                    self.selected_bodypart = player.fighter.target_actor.bodyparts[0]
                    self.bodypart_index = 0
                    self.target_index = 0
                    self.engine.game_map.camera_xy = (player.fighter.target_actor.x, player.fighter.target_actor.y + 3)
            except TypeError:
                if not self.in_squad_mode:
                    self.engine.squad_mode = False
                return self.parent_handler

            if len(self.targets) > 0:
                self.target_index = self.targets.index(player.fighter.target_actor)

            # updates list of target bodyparts
            self.update_bodypart_list()
            self.update_part_str_colour()

        elif key == tcod.event.K_LALT or key == tcod.event.K_RALT:  # change limb targetted
            try:
                self.selected_bodypart = self.bodypartlist[self.bodypart_index + 1]
                self.bodypart_index += 1

            except IndexError:
                try:
                    self.selected_bodypart = self.bodypartlist[0]
                    self.bodypart_index = 0
                except IndexError:
                    if not self.in_squad_mode:
                        self.engine.squad_mode = False
                    return self.parent_handler

            self.update_part_str_colour()

        elif key == tcod.event.K_RETURN:  # atttack selected target
            print(self.bodypart_index)

            if self.item is not None:
                if hasattr(self.item.usable_properties, 'jammed'):
                    if self.item.usable_properties.jammed:
                        return actions.ClearJam(entity=player, gun=self.item.usable_properties).handle_action()

            if player.fighter.target_actor:

                distance_target = round(player.distance(player.fighter.target_actor.x, player.fighter.target_actor.y))

                # attack with weapon
                if self.item is not None:
                    (self.item.usable_properties.get_attack_action(distance=distance_target, entity=player,
                                                                   targeted_actor=player.fighter.target_actor,
                                                                   targeted_bodypart=self.selected_bodypart).
                     handle_action())

                # unarmed attack
                else:
                    actions.UnarmedAttackAction(distance=distance_target, entity=player,
                                                targeted_actor=player.fighter.target_actor,
                                                targeted_bodypart=self.selected_bodypart,
                                                handle_now=True).handle_action()

                self.get_targets()
                self.engine.render(console=self.console)

        elif key == tcod.event.K_TAB:
            self.engine.switch_player()
            return self.get_targets()
        elif key == tcod.event.K_c:
            return SelectItemToCraft(engine=self.engine, item_dict=self.engine.crafting_recipes, title='Crafting',
                                     parent_handler=self)
        elif key == tcod.event.K_i:
            return InventoryEventHandler(self.engine, parent_handler=self)
        elif key == tcod.event.K_e:
            return EquipmentEventHandler(self.engine, parent_handler=self)
        elif key == tcod.event.K_s:
            return AttackStyleMenu(self.engine, parent_handler=self)
        elif key == tcod.event.K_t:
            return Bestiary(self.engine, parent_handler=self)
        elif key == tcod.event.K_z:
            return ViewPlayerStats(self.engine, parent_handler=self)
        elif key == tcod.event.K_r:
            return LoadoutEventHandler(engine=self.engine, parent_handler=self)
        elif key == tcod.event.K_PERIOD and modifier & (tcod.event.KMOD_LSHIFT | tcod.event.KMOD_RSHIFT):
            return actions.TakeStairsAction(player)
        elif key == tcod.event.K_q:
            try:
                # held gun is mag fed
                if hasattr(player.inventory.held.usable_properties, 'loaded_magazine'):
                    return GunOptionsMagFed(engine=self.engine, gun=player.inventory.held.usable_properties,
                                            parent_handler=self)
                # held gun is integrated magazine
                elif hasattr(player.inventory.held.usable_properties, 'magazine'):
                    return GunOptionsIntegratedMag(engine=self.engine, gun=player.inventory.held.usable_properties,
                                                   parent_handler=self)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
        elif key == tcod.event.K_v:
            return HistoryViewer(self.engine, parent_handler=self)
        elif key == tcod.event.K_g:
            return PickUpEventHandler(engine=self.engine, parent_handler=self)

        # displays enemy info
        elif key == tcod.event.K_k and player.fighter.target_actor is not None:
            return ShowEnemyInfo(self.engine, entity=player.fighter.target_actor, parent_handler=self)

        elif key in WAIT_KEYS:
            self.get_targets()
            self.engine.handle_turns()

        elif key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            self.engine.game_map.move_camera(dx, dy)

        elif key == tcod.event.K_ESCAPE:

            for player in self.engine.players:
                player.ai.path_to_xy = None
            self.engine.game_map.camera_xy = (self.engine.player.x, self.engine.player.y + 3)
            # if not self.in_squad_mode:
            self.engine.squad_mode = False
            return self.parent_handler

    def update_bodypart_list(self) -> None:
        # updates bodypart list
        self.bodypartlist = []
        if self.engine.player.fighter.target_actor is not None:
            for bodypart in self.engine.player.fighter.target_actor.bodyparts:
                self.bodypartlist.append(bodypart)

    def update_part_str_colour(self) -> None:

        string: str = "UNHARMED"
        str_colour: tuple[int, int, int] = colour.GREEN

        current_value = getattr(self.selected_bodypart, "hp")
        maximum_value = getattr(self.selected_bodypart, "max_hp")

        if maximum_value == current_value:
            pass

        elif maximum_value * 0.75 <= current_value <= maximum_value:
            string = "MINOR DAMAGE"
            str_colour = colour.YELLOW

        elif maximum_value * 0.5 <= current_value <= maximum_value * 0.75:
            string = "DAMAGED"
            str_colour = colour.ORANGE

        elif maximum_value * 0.15 <= current_value <= maximum_value * 0.50:
            string = "CRITICAL DAMAGE"
            str_colour = colour.LIGHT_RED

        elif 0 < current_value <= maximum_value * 0.15:
            string = "MANGLED"
            str_colour = colour.RED

        elif current_value == 0:
            string = "DESTROYED"
            str_colour = colour.DARK_GRAY

        self.part_cond_str = string
        self.part_cond_colour = str_colour


class ShowEnemyInfo(EventHandler):

    def __init__(self, engine: Engine, entity: Actor, parent_handler: BaseEventHandler):
        super().__init__(engine)
        self.parent_handler = parent_handler
        self.entity = entity
        self.title = f"Info - {entity.name}"
        self.strings = []

        if entity.inventory.held is not None:
            self.strings.append(f"Held Weapon: {entity.inventory.held.name}")

        equipped_armour = []

        for part in entity.bodyparts:
            string: str = "UNHARMED"

            current_value = getattr(part, "hp")
            maximum_value = getattr(part, "max_hp")

            if maximum_value == current_value:
                pass

            elif maximum_value * 0.75 <= current_value <= maximum_value:
                string = "Minor Damage"

            elif maximum_value * 0.5 <= current_value <= maximum_value * 0.75:
                string = "Injured"

            elif maximum_value * 0.15 <= current_value <= maximum_value * 0.50:
                string = "Critically Injured"

            elif 0 < current_value <= maximum_value * 0.15:
                string = "Mangled"

            elif current_value == 0:
                string = "Destroyed"

            self.strings.append(f"{part.name}: {string}")

            if part.equipped is not None:
                if part.equipped.name not in equipped_armour:
                    equipped_armour.append(f"Worn - {part.equipped.name}")

            self.strings += equipped_armour

    def on_render(self, console: tcod.Console) -> None:
        """Render the parent and dim the result, then print the message on top."""
        super().on_render(console)

        longest_str_len = 0

        for string in self.strings:
            if len(string) > longest_str_len:
                longest_str_len = len(string)

        width = len(self.title)
        height = len(self.strings) + 2

        if longest_str_len > width:
            width = longest_str_len

        x = 1
        y = 2

        console.draw_frame(
            x=x,
            y=y,
            width=width + 7,
            height=height,
            title=self.title,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        for i, string in enumerate(self.strings):
            console.print(x + 1, y + i + 1, string)

        if hasattr(self.entity, 'description'):
            console.print(x, height + 2, "PRESS [D] FOR DESCRIPTION")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        key = event.sym

        if key == tcod.event.K_d:
            if hasattr(self.entity, 'description'):
                return PopupMessage(text=self.entity.description, parent_handler=self, title=self.entity.name)

        elif key == tcod.event.K_ESCAPE:
            return self.parent_handler


class QuitEventHandler(AskUserEventHandler):

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        console.draw_frame(
            x=console.width // 2 - 11,
            y=console.height // 2 - 2,
            width=22,
            height=5,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        console.print(x=console.width // 2 - 9, y=console.height // 2 - 1, string="1) Return to Game",
                      fg=colour.WHITE, bg=(0, 0, 0))

        console.print(x=console.width // 2 - 9, y=console.height // 2, string="2) Quit to Menu",
                      fg=colour.WHITE, bg=(0, 0, 0))

        console.print(x=console.width // 2 - 9, y=console.height // 2 + 1, string="3) Abandon Mission",
                      fg=colour.WHITE, bg=(0, 0, 0))

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        key = event.sym
        if key == tcod.event.K_2:
            raise exceptions.QuitToMenu

        elif key == tcod.event.K_1:
            return self.parent_handler

        elif key == tcod.event.K_3:
            if os.path.exists("savegame.sav"):
                os.remove("savegame.sav")  # Deletes the active save file.
            raise exceptions.QuitToMenuWithoutSaving


class MagazineOptionsHandler(UserOptionsEventHandler):

    def __init__(self, engine: Engine, magazine: Union[DetachableMagazine, Clip], parent_handler: BaseEventHandler):

        self.magazine = magazine

        title = f"{magazine.parent.name} - ({len(self.magazine.magazine)}/" \
                f"{self.magazine.mag_capacity})"

        options = ['load bullets', 'unload bullets']

        inventory = engine.player.inventory
        loadout = inventory.small_magazines + inventory.medium_magazines + inventory.large_magazines

        if not hasattr(magazine, 'gun_type'):
            if magazine.parent in loadout:
                options.append('remove from loadout')
            else:
                options.append('add to loadout')

        super().__init__(engine=engine, options=options, title=title, parent_handler=parent_handler)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        player = self.engine.player

        if option == 'load bullets':
            return SelectBulletsToLoadHandler(engine=self.engine, magazine=self.magazine,
                                              parent_handler=self.parent_handler)

        elif option == 'unload bullets':
            self.magazine.unload_magazine(entity=self.engine.player)

        elif option == 'add to loadout':
            player.inventory.add_to_magazines(magazine=self.magazine)

        elif option == 'remove from loadout':
            player.inventory.remove_from_magazines(magazine=self.magazine)

        return MainGameEventHandler(engine=self.engine)


class GunOptionsMagFed(UserOptionsEventHandler):
    def __init__(self, engine: Engine, gun: GunMagFed, parent_handler: BaseEventHandler):
        self.gun = gun

        title = gun.parent.name
        options = ['rename', ]

        self.firemodes = self.gun.fire_modes

        if self.gun.jammed:
            options.append('clear jam')

        if self.gun.loaded_magazine:
            options += ["load magazine", "unload magazine", "check rounds in mag"]
        else:
            options.append("load magazine")

        if self.gun.compatible_clip is not None:
            options.append("load from clip")

        for firemode in self.firemodes:
            if not firemode == self.gun.current_fire_mode:
                options.append(firemode)

        super().__init__(engine=engine, options=options, title=title, parent_handler=parent_handler)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        if option == 'load magazine':
            return SelectMagazineToLoadIntoGun(engine=self.engine, gun=self.gun, parent_handler=self)

        elif option == 'unload magazine':
            self.gun.unload_gun()

        elif option == 'load from clip':
            return SelectClipToLoadIntoGun(engine=self.engine, gun=self.gun, parent_handler=self)

        elif option == 'rename':
            return RenameItem(item=self.gun.parent, prompt_string='New Name:', engine=self.engine,
                              parent_handler=self)

        elif option == 'clear jam':
            return actions.ClearJam(entity=self.engine.player, gun=self.gun).handle_action()

        elif option == 'check rounds in mag':
            return actions.CheckRoundsInMag(entity=self.engine.player, weapon=self.gun).handle_action()

        elif option in self.firemodes:
            self.gun.current_fire_mode = option

        return self.parent_handler


class GunOptionsIntegratedMag(UserOptionsEventHandler):
    def __init__(self, engine: Engine, gun: GunIntegratedMag, parent_handler: BaseEventHandler):
        self.gun = gun

        title = gun.parent.name
        options = ['rename', "load rounds", "unload rounds"]

        self.firemodes = self.gun.fire_modes

        if self.gun.jammed:
            options.append('clear jam')

        if self.gun.compatible_clip is not None:
            options.append("load from clip")

        for firemode in self.firemodes:
            if not firemode == self.gun.current_fire_mode:
                options.append(firemode)

        super().__init__(engine=engine, options=options, title=title, parent_handler=parent_handler)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        if option == 'load rounds':
            return SelectBulletsToLoadHandler(engine=self.engine, magazine=self.gun, parent_handler=self)

        elif option == 'unload rounds':
            self.gun.unload_magazine(entity=self.engine.player)

        elif option == 'load from clip':
            return SelectClipToLoadIntoGun(engine=self.engine, gun=self.gun, parent_handler=self)

        elif option == 'rename':
            return RenameItem(item=self.gun.parent, prompt_string='New Name:', engine=self.engine,
                              parent_handler=self)

        elif option == 'clear jam':
            return actions.ClearJam(entity=self.engine.player, gun=self.gun).handle_action()

        elif option in self.firemodes:
            self.gun.current_fire_mode = option

        return self.parent_handler


class RenameItem(TypeInputEventHandler):

    def __init__(self, item: Item, prompt_string: str, engine: Engine, parent_handler: BaseEventHandler):
        super().__init__(prompt_string=prompt_string, engine=engine, item=item, parent_handler=parent_handler)

    def ev_on_option_selected(self) -> Optional[ActionOrHandler]:
        if not self.buffer == '':
            self.item.name = self.buffer

        return self.parent_handler


class SelectMagazineToLoadIntoGun(UserOptionsWithPages):

    def __init__(self, engine: Engine, gun: GunMagFed, parent_handler: BaseEventHandler):
        self.gun = gun

        mag_list = []
        title = gun.parent.name

        loadout = \
            engine.player.inventory.small_magazines + engine.player.inventory.medium_magazines + \
            engine.player.inventory.large_magazines

        for item in loadout:
            if hasattr(item.usable_properties, 'magazine_type') and hasattr(self.gun, 'compatible_magazine_type'):
                if item.usable_properties.magazine_type not in self.gun.compatible_magazine_type:
                    mag_list.append(item)

        super().__init__(engine=engine, options=mag_list, page=0, title=title, parent_handler=parent_handler)

    def ev_keydown(self, event: tcod.event.KeyDown):
        key = event.sym
        index = key - tcod.event.K_a

        if key == tcod.event.K_DOWN:
            if len(self.options) > (self.page + 1) * self.max_list_length:
                self.page += 1
                return self

        if key == tcod.event.K_UP:
            if self.page > 0:
                self.page -= 1
                return self

        if 0 <= index <= self.max_list_length - 1:
            try:
                selected_item = self.options[index + (self.page * self.max_list_length)]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.ev_on_option_selected(selected_item.usable_properties)
        return super().ev_keydown(event)

    def ev_on_option_selected(self, item: DetachableMagazine) -> Optional[ActionOrHandler]:
        ReloadMagFed(entity=self.engine.player, gun=self.gun, magazine_to_load=item).handle_action()
        return self.parent_handler


class SelectClipToLoadIntoGun(UserOptionsWithPages):

    def __init__(self, engine: Engine, gun: Gun, parent_handler: BaseEventHandler):
        self.gun = gun

        mag_list = []
        title = gun.parent.name

        loadout = \
            engine.player.inventory.small_magazines + engine.player.inventory.medium_magazines + \
            engine.player.inventory.large_magazines

        for item in loadout:
            if hasattr(item.usable_properties, 'magazine_type') and hasattr(self.gun, 'compatible_clip'):
                if item.usable_properties.magazine_type == self.gun.compatible_clip:
                    mag_list.append(item)

        super().__init__(engine=engine, options=mag_list, page=0, title=title, parent_handler=parent_handler)

    def ev_keydown(self, event: tcod.event.KeyDown):
        key = event.sym
        index = key - tcod.event.K_a

        if key == tcod.event.K_DOWN:
            if len(self.options) > (self.page + 1) * self.max_list_length:
                self.page += 1
                return self

        if key == tcod.event.K_UP:
            if self.page > 0:
                self.page -= 1
                return self

        if 0 <= index <= self.max_list_length - 1:
            try:
                selected_item = self.options[index + (self.page * self.max_list_length)]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.ev_on_option_selected(selected_item.usable_properties)
        return super().ev_keydown(event)

    def ev_on_option_selected(self, item: Clip) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        self.gun.load_from_clip(clip=item)
        return self.parent_handler


class SelectPartToRepair(UserOptionsWithPages):

    def __init__(self, engine: Engine, options: list, callback: Callable[[Item], Optional[Action]],
                 parent_handler: BaseEventHandler):

        self.callback = callback

        title = 'Select Part to Repair'

        super().__init__(engine=engine, options=options, page=0, title=title, parent_handler=parent_handler)

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        number_of_options = len(self.options)

        width = len(self.TITLE)
        height = number_of_options + 2

        if number_of_options > self.max_list_length:
            height = self.max_list_length + 2

        x = 1
        y = 2

        index_range = self.page * self.max_list_length

        longest_name_len = 0

        for item in self.options[index_range:index_range + self.max_list_length]:

            if len(item.name) > longest_name_len:
                longest_name_len = len(item.name)

        if longest_name_len:
            if longest_name_len > width:
                width = longest_name_len + 7

        console.draw_frame(
            x=x,
            y=y,
            width=width + 8,
            height=height,
            title=self.TITLE,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        if number_of_options > 0:
            console.print(x + 1, y + height - 1,
                          f"Page {self.page + 1}/{ceil(len(self.options) / self.max_list_length)}")

            for i, item in enumerate(self.options[index_range:index_range + self.max_list_length]):
                item_key = chr(ord("a") + i)
                if item.usable_properties.accuracy_part and not item.usable_properties.functional_part:
                    console.print(x + 1, y + i + 1, f"({item_key}) {item.name} - "
                                                    f"{round(item.usable_properties.condition_accuracy / 5 * 100)}%")

                elif item.usable_properties.functional_part and not item.usable_properties.accuracy_part:
                    console.print(x + 1, y + i + 1, f"({item_key}) {item.name} - "
                                                    f"{round(item.usable_properties.condition_function / 5 * 100)}%")

                elif item.usable_properties.functional_part and item.usable_properties.accuracy_part:
                    condition = round(item.usable_properties.condition_function +
                                      item.usable_properties.condition_accuracy / 10 * 100)
                    console.print(x + 1, y + i + 1, f"({item_key}) {item.name} - {condition}%")

        else:
            console.print(x + 1, y + 1, "No Repairable Parts")

    def ev_on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        return self.callback(item)


class SelectPartToHeal(AskUserEventHandler):
    def __init__(self, engine: Engine, options: list[Bodypart],
                 callback: Callable[[Bodypart], Optional[Action]], parent_handler: BaseEventHandler):

        self.callback = callback

        title = 'Select Body Part to Heal'

        self.options = options
        self.TITLE = title

        super().__init__(engine=engine, parent_handler=parent_handler)

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        longest_option_name = 0

        for option in self.options:

            if len(option.name) > longest_option_name:
                longest_option_name = len(option.name)

        width = len(self.TITLE)

        if longest_option_name > width:
            width = longest_option_name

        x = 1
        y = 2

        console.draw_frame(
            x=x,
            y=y,
            width=width + 29,
            height=len(self.options) + 2,
            title=self.TITLE,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        for i, option in enumerate(self.options):
            option_key = chr(ord("a") + i)

            maximum_value = option.max_hp
            current_value = option.hp

            damage_str = ''
            str_colour = colour.YELLOW

            if maximum_value * 0.75 <= current_value <= maximum_value:
                damage_str = "Minor Damage"

            elif maximum_value * 0.5 <= current_value <= maximum_value * 0.75:
                damage_str = "Injured"
                str_colour = colour.ORANGE

            elif maximum_value * 0.15 <= current_value <= maximum_value * 0.50:
                damage_str = "Critically Injured"
                str_colour = colour.LIGHT_RED

            elif 0 < current_value <= maximum_value * 0.15:
                damage_str = "Mangled"
                str_colour = colour.RED

            console.print(x + 1, y + i + 1, f"({option_key}) {option.name} - {damage_str}", fg=str_colour)

    def ev_keydown(self, event: tcod.event.KeyDown):
        key = event.sym
        index = key - tcod.event.K_a

        if event.sym == tcod.event.K_ESCAPE:
            return self.parent_handler

        if 0 <= index <= 26:
            try:
                selected_option = self.options[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)
                return self
            return self.ev_on_option_selected(selected_option)
        return super().ev_keydown(event)

    def ev_on_option_selected(self, bodypart: Bodypart) -> Optional[ActionOrHandler]:
        return self.callback(bodypart)


class SelectBulletsToLoadHandler(UserOptionsWithPages):
    TITLE = "Select Bullets"

    def __init__(self, engine: Engine, magazine: Magazine, parent_handler: BaseEventHandler):
        self.magazine = magazine
        ammo_list = []

        for item in engine.player.inventory.items:
            if hasattr(item.usable_properties, 'bullet_type'):
                if item.usable_properties.bullet_type in self.magazine.compatible_bullet_type:
                    ammo_list.append(item)

        title = f"Load {self.magazine.parent.name} - ({len(self.magazine.magazine)}/" \
                f"{self.magazine.mag_capacity})"

        super().__init__(engine=engine, page=0, title=title, options=ammo_list, parent_handler=parent_handler)

    def ev_keydown(self, event: tcod.event.KeyDown):
        key = event.sym
        index = key - tcod.event.K_a

        if key == tcod.event.K_DOWN:
            if len(self.options) > (self.page + 1) * self.max_list_length:
                self.page += 1
                return self

        if key == tcod.event.K_UP:
            if self.page > 0:
                self.page -= 1
                return self

        if 0 <= index <= self.max_list_length - 1:
            try:
                selected_item = self.options[index + (self.page * self.max_list_length)]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.ev_on_option_selected(selected_item.usable_properties)
        return super().ev_keydown(event)

    def ev_on_option_selected(self, item: Bullet) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        return SelectNumberOfBulletsToLoadHandler(engine=self.engine, magazine=self.magazine, ammo=item,
                                                  parent_handler=self.parent_handler)


class SelectNumberOfBulletsToLoadHandler(TypeAmountEventHandler):

    def __init__(self, engine: Engine, magazine: Magazine, ammo: Bullet, parent_handler: BaseEventHandler):
        self.magazine = magazine
        self.ammo = ammo
        super().__init__(engine=engine, item=ammo.parent, prompt_string="amount to load (leave blank for maximum):",
                         parent_handler=parent_handler)

    def ev_on_option_selected(self):
        LoadBulletsIntoMagazine(entity=self.engine.player, bullet_type=self.ammo, bullets_to_load=int(self.buffer),
                                magazine=self.magazine).handle_action()
        return self.parent_handler


class LoadoutEventHandler(UserOptionsWithPages):

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):
        title = "Loadout"

        loadout_items = []

        if engine.player.inventory.primary_weapon is not None:
            loadout_items.append(engine.player.inventory.primary_weapon)
        if engine.player.inventory.secondary_weapon is not None:
            loadout_items.append(engine.player.inventory.secondary_weapon)

        inventory = engine.player.inventory

        items = inventory.small_magazines + inventory.medium_magazines + inventory.large_magazines

        for item in items:
            if item in inventory.items:
                loadout_items.append(item)

        super().__init__(engine=engine, options=loadout_items, page=0, title=title, parent_handler=parent_handler)

    def ev_keydown(self, event: tcod.event.KeyDown):
        key = event.sym
        index = key - tcod.event.K_a

        if key == tcod.event.K_DOWN:
            if len(self.options) > (self.page + 1) * self.max_list_length:
                self.page += 1
                return self

        if key == tcod.event.K_UP:
            if self.page > 0:
                self.page -= 1
                return self

        if 0 <= index <= self.max_list_length - 1:
            try:
                selected_item = self.options[index + (self.page * self.max_list_length)]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.ev_on_option_selected(selected_item.usable_properties)
        return super().ev_keydown(event)

    def ev_on_option_selected(self, item: Union[Clip, DetachableMagazine]):

        if hasattr(item, 'mag_capacity') and not hasattr(item, 'gun_type'):
            return MagazineOptionsHandler(engine=self.engine, magazine=item, parent_handler=self)

        elif hasattr(item, 'gun_type'):

            options = ['equip', 'unequip', 'use', 'inspect']
            return ItemInteractionHandler(item=item.parent, options=options, engine=self.engine,
                                          parent_handler=self)


class SelectItemToCraft(UserOptionsWithPages):
    def __init__(self, engine: Engine, title: str, item_dict: dict, parent_handler: BaseEventHandler):

        super().__init__(engine=engine, options=list(item_dict.keys()), page=0, title=title,
                         parent_handler=parent_handler)
        self.item_dict = item_dict

    def ev_on_option_selected(self, option):

        # dictionary has parts list, can proceed with creating item
        if 'required parts' in list(self.item_dict[option].keys()):
            part_dict = {}

            # all required and compatible parts
            parts = \
                list(self.item_dict[option]["required parts"].keys()) \
                + list(self.item_dict[option]["compatible parts"].keys())

            # adds all required and compatible parts to the dictionary and sets
            # their value to None before player selects
            for part in parts:
                part_dict[part] = None

            if hasattr(self.item_dict[option]["item"].usable_properties, 'gun_type'):
                return CraftGun(engine=self.engine, item_to_craft=option, current_part_index=0,
                                item_dict=self.item_dict,
                                compatible_parts={},
                                part_dict=part_dict,
                                prevent_suppression=False,
                                attachment_points=[],
                                has_optic=False,
                                attachments_dict={},
                                parent_handler=self.parent_handler
                                )
            else:
                return self.parent_handler

        # dictionary selected does not have parts list
        else:
            return SelectItemToCraft(engine=self.engine, title=option, item_dict=self.item_dict[option],
                                     parent_handler=self)


class CraftItem(UserOptionsWithPages):
    def __init__(self,
                 engine: Engine,
                 item_to_craft: str,
                 current_part_index: int,
                 item_dict: dict,
                 compatible_parts: dict,
                 part_dict: dict,
                 parent_handler: BaseEventHandler
                 ):
        self.engine = engine

        # values of all parts
        self.part_dict = part_dict

        self.item_name = item_to_craft

        # item crafting dict
        self.item_dict = deepcopy(item_dict)

        # all part keys in list format
        self.parts = list(part_dict.keys())

        # index of current part to be selected set to first part
        self.current_part_selection = current_part_index

        title = self.parts[current_part_index]

        # parts of a given type available in inventory
        self.options = []

        self.compatible_parts = compatible_parts
        self.add_options()

        super().__init__(engine=engine, options=self.options, page=0, title=title, parent_handler=parent_handler)

    def add_options(self):
        return NotImplementedError


class CraftGun(CraftItem):
    def __init__(self,
                 engine: Engine,
                 item_to_craft: str,
                 current_part_index: int,
                 item_dict: dict,
                 compatible_parts: dict,
                 part_dict: dict,
                 prevent_suppression: bool,
                 attachment_points: list,
                 attachments_dict: dict,
                 has_optic: bool,
                 parent_handler: BaseEventHandler
                 ):

        self.prevent_suppression = prevent_suppression
        self.attachment_points = attachment_points
        self.attachments_dict = attachments_dict
        self.has_optic = has_optic

        super().__init__(engine=engine,
                         item_to_craft=item_to_craft,
                         current_part_index=current_part_index,
                         item_dict=item_dict,
                         compatible_parts=compatible_parts,
                         part_dict=part_dict,
                         parent_handler=parent_handler
                         )

    def add_options(self):

        # checks if current part selection is the same as the type as item in the prerequisite parts
        # if it is, only adds parts to options that are in prerequisites
        add_only_compatible = False
        for part_type in self.compatible_parts.keys():
            if part_type == self.parts[self.current_part_selection]:
                add_only_compatible = True
                break

        for item in self.engine.player.inventory.items:
            # is gun part
            if hasattr(item.usable_properties, 'prevents_suppression'):

                if item.usable_properties.part_type == self.parts[self.current_part_selection]:

                    # if the item is an optic, and if any of the current parts require an optic to be mounted,
                    # prevents attachment item from being added as an option if it is incompatible with the part that
                    # requires optics attachment
                    if item.usable_properties.part_type == 'Optic':
                        for part in self.part_dict.values():
                            if part is not None:
                                if hasattr(part.usable_properties, 'additional_required_parts'):
                                    if 'Optic' in part.usable_properties.additional_required_parts \
                                            and hasattr(item.usable_properties, 'attachment_point_required'):
                                        if not any(attach_point in item.usable_properties.attachment_point_required
                                                   for attach_point in
                                                   part.usable_properties.is_attachment_point_types):
                                            continue

                    # checks if there is an attachment point compatible with the attachment
                    if hasattr(item.usable_properties, 'attachment_point_required'):
                        attachment_point = getattr(item.usable_properties, 'attachment_point_required')
                        if not any(item in attachment_point for item in self.attachment_points):
                            continue

                    if hasattr(item.usable_properties, 'incompatibilities'):
                        all_parts = []
                        for value in self.part_dict.values():
                            if hasattr(value, 'tags'):
                                all_parts += value.tags
                        incompatibilities = getattr(item.usable_properties, 'incompatibilities')
                        for setups in incompatibilities:
                            for items in setups:
                                if all(item in all_parts for item in items):
                                    continue

                    # checks suppressor compatibility
                    if item.usable_properties.is_suppressor:
                        if self.prevent_suppression:
                            continue

                    if add_only_compatible:
                        if item.name in self.compatible_parts[self.parts[self.current_part_selection]]:
                            self.options.append(item)
                            continue

                        has_compatible_tag = False
                        tags = [item.usable_properties.part_type, ]

                        if hasattr(item.usable_properties, 'tags'):
                            tags.extend(getattr(item.usable_properties, 'tags'))

                        # commented out below line - appears depricated
                        # for tag in getattr(item.usable_properties, 'tags'):
                        for tag in tags:
                            if tag in self.compatible_parts[self.parts[self.current_part_selection]]:
                                has_compatible_tag = True
                                break

                        if not has_compatible_tag:
                            continue

                    self.options.append(item)

        if self.parts[self.current_part_selection] in self.item_dict[self.item_name]["compatible parts"]:
            # if part is not required and there are no parts of this type available,
            # skips to the next part type
            # if len(self.options) == 0 and self.parts[self.current_part_selection] != self.parts[-1]:
            self.options = ['none', ] + self.options
            # self.current_part_selection += 1
            #     print('test 1')
            #     return CraftGun(engine=self.engine,
            #                     current_part_index=self.current_part_selection,
            #                     item_to_craft=self.item_name,
            #                     item_dict=self.item_dict,
            #                     part_dict=self.part_dict,
            #                     compatible_parts=self.compatible_parts,
            #                     prevent_suppression=self.prevent_suppression,
            #                     attachment_points=self.attachment_points,
            #                     attachments_dict=self.attachments_dict,
            #                     has_optic=self.has_optic
            #                     )
            #
            # # part is not required, adds the option to select no part
            # else:
            #     self.options = ['none', ] + self.options

        # if part is required but no item of this type in inventory, cancels crafting
        else:
            if len(self.options) < 1:
                self.engine.message_log.add_message(f"Missing parts: {self.parts[self.current_part_selection]}",
                                                    colour.RED)

    def update_crafting_properties(self, option):

        # updates the compatible parts dictionary
        if hasattr(option.usable_properties, 'compatible_parts'):
            part_keys = option.usable_properties.compatible_parts.keys()
            for key, value in self.compatible_parts.items():
                if key in part_keys:
                    self.compatible_parts[key] = value.extend(option.usable_properties.compatible_parts[key])
            for key, value in option.usable_properties.compatible_parts.items():
                if key not in self.compatible_parts.keys():
                    self.compatible_parts[key] = option.usable_properties.compatible_parts[key]

        if hasattr(option.usable_properties, 'is_attachment_point_types'):
            attachment_point_types = getattr(option.usable_properties, 'is_attachment_point_types')
            self.attachment_points.extend(attachment_point_types)
            item_attachment_points = {}
            for attachment_point in attachment_point_types:
                item_attachment_points[attachment_point] = None
            self.attachments_dict[option.name] = item_attachment_points

        if hasattr(option.usable_properties, 'additional_required_parts'):
            for i in option.usable_properties.additional_required_parts:
                if i in self.item_dict[self.item_name]["compatible parts"]:
                    del self.item_dict[self.item_name]["compatible parts"][i]

        if option.usable_properties.prevents_suppression:
            self.prevent_suppression = True

        if option.usable_properties.is_optic:
            self.has_optic = True

    def ev_on_option_selected(self, option):

        if not option == 'none':

            # if requires attachment point, has player select specific attachment point
            if hasattr(option.usable_properties, 'attachment_point_required'):
                return SelectItemToAttach(engine=self.engine, item=option, crafting_handler=self,
                                          parent_handler=self.parent_handler)

            # sets part in part dict to be the selected part
            self.part_dict[self.parts[self.current_part_selection]] = option
            self.update_crafting_properties(option)

        # part is last part to select
        if self.parts[self.current_part_selection] == self.parts[-1]:
            self.craft_item()
            return self.parent_handler

        else:
            self.current_part_selection += 1
            return CraftGun(engine=self.engine,
                            current_part_index=self.current_part_selection,
                            item_to_craft=self.item_name,
                            item_dict=self.item_dict,
                            part_dict=self.part_dict,
                            compatible_parts=self.compatible_parts,
                            prevent_suppression=self.prevent_suppression,
                            attachment_points=self.attachment_points,
                            attachments_dict=self.attachments_dict,
                            has_optic=self.has_optic,
                            parent_handler=self.parent_handler
                            )

    def craft_item(self) -> Optional[ActionOrHandler]:

        item = self.item_dict[self.item_name]['item']

        craftable = True

        # gun has no sights, cannot be crafted.
        if not self.has_optic:
            self.engine.message_log.add_message(f"Crafting failed - missing sights", colour.RED)
            return self.parent_handler

        # all possible components with the amount required to craft
        full_part_dict = {**self.item_dict[self.item_name]['compatible parts'],
                          **self.item_dict[self.item_name]['required parts']}

        for key, value in self.part_dict.items():
            if value is not None:
                if value in self.engine.player.inventory.items:

                    # if crafting component in inventory is stacking, removes appropriate amount of item from
                    # inventory
                    if value.stacking:
                        if value.stacking.stack_size - full_part_dict[value.usable_properties.part_type] > 0:
                            value.stacking.stack_size -= full_part_dict[value.usable_properties.part_type]
                        elif value.stacking.stack_size - full_part_dict[value.usable_properties.part_type] == 0:
                            self.engine.player.inventory.items.remove(value)
                        else:
                            craftable = False

                    # not stacking, removes from inventory
                    else:
                        self.engine.player.inventory.items.remove(value)

                    if hasattr(item.usable_properties, 'parts'):
                        setattr(item.usable_properties.parts, key, value)

        if craftable:
            if hasattr(item.usable_properties, 'parts'):
                item.usable_properties.parts.update_partlist(attachment_dict=self.attachments_dict)
            item.parent = self.engine.player.inventory

            for i in range(5):
                self.engine.handle_turns()

            self.engine.player.inventory.add_to_inventory(item=item, item_container=None, amount=1)
            return self.parent_handler

        else:
            return self.parent_handler


class SelectItemToAttach(UserOptionsWithPages):

    def __init__(self, engine: Engine, item: Item, crafting_handler: CraftGun, parent_handler: BaseEventHandler):
        title = f"Select Part to Attach to"

        self.crafting_handler = crafting_handler
        self.item = item  # item being attached to the attachment point (the accessory)

        options = []

        prevents_attachment_of = {}

        # whether the part is an optic mount which, if present, an optic must be attached
        required_optic_mount = False

        # if the accessory is an optic, iterates through parts. If an additonal optics attachment is required for any
        # of the parts, sets the attachment options to the given part.
        if self.item.usable_properties.part_type == 'Optic':
            for part in self.crafting_handler.part_dict.values():
                if part is not None:
                    if hasattr(part.usable_properties, 'additional_required_parts'):
                        if 'Optic' in part.usable_properties.additional_required_parts:
                            required_optic_mount = True
                            options = [part, ]

        if not required_optic_mount:
            # iterate over each attachment point in item attachment point required
            for attachment_point in item.usable_properties.attachment_point_required:

                # iterates over each part currently added
                for part in self.crafting_handler.part_dict.values():
                    if part is not None:
                        # part prevents attachment of certain accessories
                        if hasattr(item.usable_properties, 'prevents_attachment_of'):
                            part_prevents_attachment = getattr(item.usable_properties, 'prevents_attachment_of')
                            prevents_attachment_of_keys = prevents_attachment_of.keys()
                            for key, value in part_prevents_attachment.items():
                                # if key already in prevents_attachment_of, updates it with new values
                                if key in prevents_attachment_of_keys:
                                    if value not in prevents_attachment_of[key]:
                                        prevents_attachment_of[key] += value
                                # key not already in dict, sets key and value
                                else:
                                    prevents_attachment_of[key] = value

                        # if the given part has the attachment point and not already in options and this combination is
                        # not prevented by prevents_attachment_of, adds to options
                        if hasattr(part.usable_properties, 'is_attachment_point_types'):

                            # creates list of tags of the accessory
                            tags_item = [self.item.usable_properties.part_type, ]
                            if hasattr(self.item.usable_properties, 'tags'):
                                tags_item.extend(getattr(self.item.usable_properties, 'tags'))

                            # checks if part type or one of the accessories tags is in prevents_attachments
                            if any(tag in prevents_attachment_of.keys() for tag in tags_item):

                                # accessories tag incompatible with part type
                                for tag in tags_item:
                                    if self.item.usable_properties.part_type in prevents_attachment_of[tag]:
                                        continue

                                if hasattr(part.usable_properties, 'tags'):
                                    tags_part = getattr(part.usable_properties, 'tags')

                                    for tag in tags_part:
                                        # attachment point part type incompatible with part type of attachment
                                        if tag in prevents_attachment_of[part.usable_properties.part_type]:
                                            continue
                                        # attachment point tags incompatible with tags of item
                                        for x in tags_item:
                                            if tag in prevents_attachment_of[x]:
                                                continue

                            possible_attachment_points = getattr(part.usable_properties,
                                                                 'is_attachment_point_types')
                            if attachment_point in list(possible_attachment_points):
                                if part not in options:
                                    options.append(part)

        super().__init__(engine=engine, options=options, page=0, title=title, parent_handler=parent_handler)

    def ev_on_option_selected(self, attachment_point_item: Item) -> Optional[ActionOrHandler]:

        return SelectAttachPoint(engine=self.engine, attach_point_item=attachment_point_item, accessory=self.item,
                                 crafting_handler=self.crafting_handler, parent_handler=self.parent_handler)


class SelectAttachPoint(UserOptionsWithPages):

    def __init__(self, engine: Engine, attach_point_item: Item, accessory: Item, crafting_handler: CraftGun,
                 parent_handler: BaseEventHandler):
        title = f"Select Attachment Point"

        self.crafting_handler = crafting_handler
        self.attachment_point_item = attach_point_item
        self.accessory = accessory

        options = []

        # iterates through all possible attachment points in attachment point types dict and if they are 'None' value
        # (no attachment at this point), adds to options
        for attachment_point in attach_point_item.usable_properties.is_attachment_point_types:
            if attachment_point in self.crafting_handler.attachments_dict[attach_point_item.name].keys():
                if self.crafting_handler.attachments_dict[attach_point_item.name][attachment_point] is None:
                    options.append(attachment_point)

        super().__init__(engine=engine, options=options, page=0, title=title, parent_handler=parent_handler)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:

        # if the part converts attachment points - i.e. MLOK to picrail adapter - changes the attachment point type
        # of the part the accessory is being attached to
        if hasattr(self.accessory.usable_properties, 'converts_attachment_points'):
            self.crafting_handler.attachment_points.remove(
                self.crafting_handler.attachment_points[self.crafting_handler.attachments_dict[
                    self.attachment_point_item.name][option]])
            del self.crafting_handler.attachments_dict[self.attachment_point_item.name][option]
            self.crafting_handler.attachments_dict[self.attachment_point_item.name][
                self.accessory.usable_properties.converts_attachment_points[option]] = None
            self.crafting_handler.attachment_points.append(
                self.accessory.usable_properties.converts_attachment_points[option])

        else:
            # sets value for the given attachment point of the part to attach to be attached part
            self.crafting_handler.attachments_dict[self.attachment_point_item.name][option] = self.accessory
            self.crafting_handler.attachment_points.remove(
                self.crafting_handler.attachment_points[self.crafting_handler.attachments_dict[
                    self.attachment_point_item.name][option]])

            # sets part in part dict to be the selected part
            self.crafting_handler.part_dict[self.crafting_handler.parts[self.crafting_handler.current_part_selection]] \
                = self.accessory

            self.crafting_handler.update_crafting_properties(self.accessory)

        # part is last part to select, crafts item
        if self.crafting_handler.parts[self.crafting_handler.current_part_selection] == self.crafting_handler.parts[-1]:
            self.crafting_handler.craft_item()
            return self.parent_handler

        # still more parts, continues to next part type
        else:
            self.crafting_handler.current_part_selection += 1
            return CraftGun(engine=self.engine,
                            current_part_index=self.crafting_handler.current_part_selection,
                            item_to_craft=self.crafting_handler.item_name,
                            item_dict=self.crafting_handler.item_dict,
                            part_dict=self.crafting_handler.part_dict,
                            compatible_parts=self.crafting_handler.compatible_parts,
                            prevent_suppression=self.crafting_handler.prevent_suppression,
                            attachment_points=self.crafting_handler.attachment_points,
                            attachments_dict=self.crafting_handler.attachments_dict,
                            has_optic=self.crafting_handler.has_optic,
                            parent_handler=self.parent_handler
                            )


class InspectItemViewer(AskUserEventHandler):

    def __init__(self, engine: Engine, item: Item, parent_handler: BaseEventHandler):
        super().__init__(engine=engine, parent_handler=parent_handler)

        self.item = item
        self.TITLE = item.name
        self.description = item.description

        self.inspect_parts_option = False

        self.max_list_length = 25
        self.scroll_position = 0

        if hasattr(item.usable_properties, 'parts'):
            self.inspect_parts_option = True

        self.item_info = {
            "-- Description --": ('description', item.description),
            "-- Weight (kg)--": ('weight', round(item.weight, 2)),

            # healing consumable
            # "-- Healing Amount --": ('amount', getattr(self.item.usable_properties, 'amount', 1)),

            # weapon
            "-- AP to Equip --": ('ap_to_equip', round(getattr(self.item.usable_properties, 'ap_to_equip', 1), 3)),

            "-- Gun Type --": ('gun_type', getattr(self.item.usable_properties, 'gun_type', 1)),
            "-- Action Type --": ('action_type', getattr(self.item.usable_properties, 'action_type', 1)),

            # melee weapon
            "-- Damage --": ('base_meat_damage', getattr(self.item.usable_properties, 'base_meat_damage', 1)),
            "-- Armour Damage --": ('base_armour_damage',
                                    getattr(self.item.usable_properties, 'base_armour_damage', 1)),
            "-- Accuracy Modifier --": ('base_accuracy', getattr(self.item.usable_properties, 'base_accuracy', 1)),

            # bullet
            "-- Round Type --": ('bullet_type', getattr(self.item.usable_properties, 'bullet_type', 1)),
            "-- Bullet Mass (Grains) --": ('mass', getattr(self.item.usable_properties, 'mass', 1)),
            "-- Charge Mass (Grains) --": ('charge_mass', getattr(self.item.usable_properties, 'charge_mass', 1)),
            "-- Bullet Diameter (Inch) --": ('diameter', getattr(self.item.usable_properties, 'diameter', 1)),
            "-- Bullet Velocity (Feet/Sec) --": ('velocity', getattr(self.item.usable_properties, 'velocity', 1)),
            "-- Shot Sound --": ('sound_modifier',
                                 round(getattr(self.item.usable_properties, 'sound_modifier', 1), 3)),
            "-- Bullet Spread Modifier (MoA) --": ('spread_modifier',
                                             round(getattr(self.item.usable_properties, 'spread_modifier', 1) * 100,
                                                   3)),
            "-- Ballistic Coefficient --": ('ballistic_coefficient',
                                            getattr(self.item.usable_properties, 'ballistic_coefficient', 1)),
            "-- Drag Coefficient --": ('drag_coefficient', getattr(self.item.usable_properties, 'drag_coefficient',
                                                                   1)),
            "-- Projectile Amount --": ('projectile_no', getattr(self.item.usable_properties, 'projectile_no', 1)),

            # magazine
            "-- Magazine Type --": ('magazine_type', getattr(self.item.usable_properties, 'magazine_type', 1)),
            "-- Magazine Size --": ('magazine_size', getattr(self.item.usable_properties, 'magazine_size', 1)),
            "-- Magazine Capacity --": ('mag_capacity', getattr(self.item.usable_properties, 'mag_capacity', 1)),
            "-- Compatible Round --": ('compatible_bullet_type',
                                       getattr(self.item.usable_properties, 'compatible_bullet_type', 1)),
            "-- AP to Load --": ('ap_to_load', getattr(self.item.usable_properties, 'ap_to_load', 1)),
            "-- Failure Chance (%) --": ('failure_chance', getattr(self.item.usable_properties, 'failure_chance', 1)),

            # gun
            "-- Felt Recoil Modifier --": ('felt_recoil', round(getattr(self.item.usable_properties, 'felt_recoil',
                                                                        1), 3)),

            "-- Sight Accuracy (MoA) --": ('sight_spread_modifier',
                                           round(getattr(self.item.usable_properties, 'sight_spread_modifier',
                                                         1) * 100, 3)),

            "-- Handling Accuracy Modifier (MoA) --":
                ('handling_spread_modifier', round(getattr(self.item.usable_properties, 'handling_spread_modifier',
                                                           1) * 100, 3)),

            "-- Reload AP Modifier --": ('load_time_modifier',
                                         round(getattr(self.item.usable_properties, 'load_time_modifier', 1), 3)),
            "-- Fire Rate Modifier --": ('fire_rate_modifier',
                                         round(getattr(self.item.usable_properties, 'fire_rate_modifier', 1), 3)),
            "-- Barrel Length (Inch) --": ('barrel_length',
                                           round((getattr(self.item.usable_properties, 'barrel_length', 1)), 3)),
            "-- Zero Range (Yard) --": ('zero_range', getattr(self.item.usable_properties, 'zero_range', 1)),
            "-- Sight Height Over Mount (Inch) --": ('sight_height_above_bore',
                                                     getattr(self.item.usable_properties, 'sight_height_above_bore',
                                                             1)),
            "-- Sight Mount / Over Bore (Inch) --": ('receiver_height_above_bore',
                                                     getattr(self.item.usable_properties,
                                                             'receiver_height_above_bore', 1)),
            "-- AP Cost Distance Modifier --": ('ap_distance_cost_modifier',
                                                round(getattr(self.item.usable_properties, 'ap_distance_cost_modifier',
                                                              1), 3)),
            "-- AP Cost Target Acquisition --": ('target_acquisition_ap',
                                                 round(getattr(self.item.usable_properties, 'target_acquisition_ap',
                                                               1), 3)),
            "-- AP Cost to Fire --": ('firing_ap_cost', round(getattr(self.item.usable_properties, 'firing_ap_cost',
                                                                      1), 3)),

            "-- Action Cycling AP Cost --": ('action_cycle_ap_cost',
                                             round(getattr(self.item.usable_properties, 'action_cycle_ap_cost', 1), 3)),

            "-- Muzzle Break Efficiency (%) --": ('muzzle_break_efficiency',
                                                  (getattr(self.item.usable_properties, 'muzzle_break_efficiency',
                                                           1)) * 100),
            "-- Bullet Velocity Modifier --": ('velocity_modifier',
                                               getattr(self.item.usable_properties, 'velocity_modifier', 1), 3),

            "-- Part Condition: Accuracy (%) --": ('condition_accuracy',
                                                   round((getattr(self.item.usable_properties, 'condition_accuracy',
                                                                  1)) / 5 * 100), 3),

            "-- Part Condition: Function (%) --": ('condition_function',
                                                   round((getattr(self.item.usable_properties, 'condition_function',
                                                                  1)) / 5 * 100), 3),

            # mag fed
            "-- Compatible Magazine Type --": ('compatible_magazine_type',
                                               getattr(self.item.usable_properties, 'compatible_magazine_type', 1)),

            # wearable
            "-- Fits Bodypart --": ('fits_bodypart', getattr(self.item.usable_properties, 'fits_bodypart', 1)),
            "-- Ballistic Protection --": (
                'ballistic_protection_level', getattr(self.item.usable_properties, 'protection_ballistic', 1)),
            "-- AP Penalty (%) --": (
                'ap_penalty', round((getattr(self.item.usable_properties, 'ap_penalty', 1) - 1) * 100)),
            "-- Physical Protection --": ('protection_physical', getattr(self.item.usable_properties,
                                                                         'protection_physical', 1)),
            "-- Armour Coverage --": ('armour_coverage', getattr(self.item.usable_properties, 'armour_coverage', 1)),
            "-- Large Magazine Slots --": ('large_mag_slots',
                                           getattr(self.item.usable_properties, 'large_mag_slots', 1)),
            "-- Medium Magazine Slots --": ('medium_mag_slots',
                                            getattr(self.item.usable_properties, 'medium_mag_slots', 1)),
            "-- Small Magazine Slots --": ('small_mag_slots',
                                           getattr(self.item.usable_properties, 'small_mag_slots', 1)),

            # component part
            "-- Part Type --": ('part_type', getattr(self.item.usable_properties, 'part_type', 1)),
            "-- Prevents Suppression --": ('prevents_suppression',
                                           getattr(self.item.usable_properties, 'prevents_suppression', 1)),

            # gun component
            "-- Compatible Parts --": ('compatible_parts',
                                       getattr(self.item.usable_properties, 'compatible_parts', 1)),
            "-- Has Attachment Points --": ('is_attachment_point_types',
                                            getattr(self.item.usable_properties, 'is_attachment_point_types', 1)),
            "-- Additional Parts Required --": ('additional_required_parts',
                                                getattr(self.item.usable_properties, 'additional_required_parts', 1)),
            "-- Compatible Attachment Points --": ('attachment_point_required',
                                                   getattr(self.item.usable_properties, 'attachment_point_required',
                                                           1)),
        }

        item_properties = dir(self.item) + dir(self.item.usable_properties)

        keys_to_delete = []

        for key, value in self.item_info.items():
            if not self.item_info[key][0] in item_properties:
                keys_to_delete.append(key)

            else:

                new_string = ''

                if isinstance(value[1], dict):

                    for key_2, value_2 in value[1].items():
                        new_string += f"{key_2:}"
                        try:
                            for string in value_2:
                                new_string += f" {string}"
                                if not string == value_2[-1]:
                                    new_string += ', '
                        except TypeError:
                            new_string += f" {value_2}"

                    self.item_info[key] = ('', new_string)

                elif type(value[1]) in (list, tuple):

                    for x in value[1]:
                        new_string += f"{x}"
                        if not x == value[1][-1]:
                            new_string += ', '

                    self.item_info[key] = ('', new_string)

        if hasattr(item.usable_properties, 'fire_modes'):
            fire_modes_str = ''

            for key, value in item.usable_properties.fire_modes.items():
                if key == "single shot":
                    fire_modes_str += 'single shot, '
                elif key == "rapid fire (semi-auto)":
                    pass
                else:
                    fire_modes_str += f"{key} - {value['fire rate']}RPM, "

            fire_modes = {" -- Fire Modes -- ": ('', fire_modes_str)}
            self.item_info.update(fire_modes)

        for key in keys_to_delete:
            del self.item_info[key]

        self.menu_length = len(self.item_info.keys())
        self.menu_length_remaining = self.menu_length

        for value in self.item_info.values():
            if len(str(value)) > 36:
                self.menu_length += ceil((len(str(value))) / 36)
            else:
                self.menu_length += 1

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        height = min(self.menu_length, self.max_list_length) + 2

        console.draw_frame(
            x=1,
            y=1,
            width=40,
            height=height + 2,
            title=self.TITLE,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        y = 2

        for key, value in \
                list(self.item_info.items())[self.scroll_position:self.scroll_position + self.max_list_length]:
            wrapper = textwrap.TextWrapper(width=36)
            word_list = wrapper.wrap(text=str(value[1]))
            console.print(x=2, y=y, string=key.center(38), fg=colour.LIGHT_GREEN)
            y += 1
            for string in word_list:
                console.print(x=2, y=y, string=string)
                y += 1

            if y > 2 + self.max_list_length:
                break

        if self.inspect_parts_option:
            console.print(x=2, y=height + 3, string="(I) SHOW PARTS", bg=(0, 0, 0))

        console.print(x=2, y=height + 2, string="USE ARROW KEYS TO SCROLL", bg=(0, 0, 0))

        if not self.scroll_position == 0:
            console.print(x=1, y=2, string="▲")

        if self.scroll_position < self.menu_length_remaining - self.scroll_position:
            console.print(x=1, y=height, string="▼")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[BaseEventHandler]:

        key = event.sym

        if key == tcod.event.K_i:
            if self.inspect_parts_option:
                return ShowParts(engine=self.engine, item=self.item, parent_handler=self)

        elif key == tcod.event.K_UP:

            menu_length = \
                len(list(self.item_info.keys())[self.scroll_position:self.scroll_position + self.max_list_length])

            for value in self.item_info.values():
                if len(str(value)) > 36:
                    menu_length += ceil((len(str(value))) / 36)

            self.menu_length_remaining = menu_length

            if self.scroll_position > 0:
                self.scroll_position -= 1

        elif key == tcod.event.K_DOWN:

            menu_length = \
                len(list(self.item_info.keys())[self.scroll_position:self.scroll_position + self.max_list_length])

            for value in self.item_info.values():
                if len(str(value)) > 36:
                    menu_length += ceil((len(str(value))) / 36)

            self.menu_length_remaining = menu_length

            if self.scroll_position < menu_length - self.scroll_position:
                self.scroll_position += 1

        elif key == tcod.event.K_ESCAPE:
            return self.parent_handler


def skill_proficiency(skill_level, skill_max) -> str:
    if skill_level == 0:
        return f'Untrained'
    elif skill_level <= (skill_max * 0.1):
        return 'Novice'
    elif (skill_max * 0.1) < skill_level <= (skill_max * 0.2):
        return 'Adequate'
    elif (skill_max * 0.2) < skill_level <= (skill_max * 0.3):
        return 'Competent'
    elif (skill_max * 0.4) < skill_level <= (skill_max * 0.5):
        return 'Skilled'
    elif (skill_max * 0.5) < skill_level <= (skill_max * 0.6):
        return 'Talented'
    elif (skill_max * 0.6) < skill_level <= (skill_max * 0.7):
        return 'Professional'
    elif (skill_max * 0.7) < skill_level <= (skill_max * 0.8):
        return 'Expert'
    elif (skill_max * 0.8) < skill_level <= (skill_max * 0.9):
        return 'Great'
    elif (skill_max * 0.9) < skill_level <= skill_max:
        return 'Master'


class ViewPlayerStats(EventHandler):

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):
        super().__init__(engine)
        self.title = f'Skills - {engine.player.name}'
        self.parent_handler = parent_handler
        self.options = {
            "Ranged Marksmanship": skill_proficiency(engine.player.fighter.skill_marksmanship, 1000),
            "Pistol Proficiency": skill_proficiency(engine.player.fighter.skill_pistol_proficiency, 1000),
            "PDW & SMG Proficiency": skill_proficiency(engine.player.fighter.skill_pistol_proficiency, 1000),
            "Rifle Proficiency": skill_proficiency(engine.player.fighter.skill_rifle_proficiency, 1000),
            "Bolt Gun Proficiency": skill_proficiency(engine.player.fighter.skill_bolt_action_proficiency, 1000),
            "Recoil Control": skill_proficiency(engine.player.fighter.skill_recoil_control, 1000),
        }

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        width = len(self.title)

        for key, value in self.options.items():
            total_len = (len(key) + len(value) + 1)
            if total_len > width:
                width = total_len

        x = console.width // 2 - ((width + 8) // 2)
        y = console.height // 2 - (len(self.options) // 2)

        console.draw_frame(
            x=x,
            y=y,
            width=width + 8,
            height=len(self.options) + 2,
            title=self.title,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        for i, key in enumerate(self.options.keys()):
            console.print(x + 1, y + i + 1, f"{key} - {self.options[key]}")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        if event.sym == tcod.event.K_ESCAPE:
            return self.parent_handler


class ShowParts(UserOptionsWithPages):

    def __init__(self, engine, item, parent_handler: BaseEventHandler):
        title = f"parts - {item.name}"

        super().__init__(engine=engine, options=item.usable_properties.parts.part_list, page=0, title=title,
                         parent_handler=parent_handler)

    def ev_on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        return InspectItemViewer(item=item, engine=self.engine, parent_handler=self.parent_handler)


class AttackStyleMenu(UserOptionsEventHandler):

    def __init__(self, engine: Engine, parent_handler: BaseEventHandler):

        title = "Change Attack Style"
        options = ['precise', 'measured', 'close quarters']

        super().__init__(engine=engine, options=options, title=title, parent_handler=parent_handler)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        player = self.engine.player

        if option == 'precise':
            player.fighter.attack_style_precision()

        elif option == 'measured':
            player.fighter.attack_style_measured()

        elif option == 'close quarters':
            player.fighter.attack_style_cqc()

        return MainGameEventHandler(engine=self.engine)


class Bestiary(UserOptionsWithPages):

    def __init__(self, engine, parent_handler: BaseEventHandler):
        title = f"Journal"

        super().__init__(engine=engine, options=list(engine.bestiary.keys()), page=0, title=title,
                         parent_handler=parent_handler)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        return PopupMessage(text=self.engine.bestiary[option], parent_handler=self, title=option)
