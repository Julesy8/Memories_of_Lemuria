from __future__ import annotations

import os
from copy import deepcopy
from typing import Optional, TYPE_CHECKING, Union
from math import ceil
import textwrap

import tcod.event

from entity import Item
import actions
from components.consumables import Gun, GunIntegratedMag, GunMagFed, Bullet, Magazine, GunComponent, Wearable
from actions import (
    Action,
    BumpAction,
    PickupAction,
    WaitAction
)

import colour
import exceptions

if TYPE_CHECKING:
    from engine import Engine

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

    def __init__(self, parent_handler: BaseEventHandler, text: str):
        self.parent = parent_handler
        self.text = text

    def on_render(self, console: tcod.Console) -> None:
        """Render the parent and dim the result, then print the message on top."""
        self.parent.on_render(console)
        console.tiles_rgb["fg"] //= 8
        console.tiles_rgb["bg"] //= 8

        console.print(
            console.width // 2,
            console.height // 2,
            self.text,
            fg=colour.WHITE,
            bg=(0, 0, 0),
            alignment=tcod.CENTER,
        )

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

            # checks if previous target actor is still visible, if not resets to None
            if self.engine.player.previous_target_actor is not None:
                if not self.engine.game_map.visible[self.engine.player.previous_target_actor.x,
                                                    self.engine.player.previous_target_actor.y]:
                    self.engine.player.previous_target_actor = None

            return MainGameEventHandler(self.engine)  # Return to the main handler.
        return self

    def handle_action(self, action: Optional[Action]) -> bool:
        """Handle actions returned from event methods.

        Returns True if the action will advance a turn.
        """

        if action is None:
            return False

        try:
            action.perform()
        except exceptions.Impossible as exc:
            if not exc.args[0] == "Silent":  # if error is "Silent" as arg, doesn't print error to message log
                self.engine.message_log.add_message(exc.args[0], colour.RED)
            return False  # Skip enemy turn on exceptions.

        self.engine.handle_enemy_turns()

        self.engine.update_fov()
        return True

    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:
        if self.engine.game_map.in_bounds(event.tile.x, event.tile.y):
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
            action = WaitAction(player)
        elif key == tcod.event.K_v:
            return HistoryViewer(self.engine)
        elif key == tcod.event.K_SPACE:
            return ChangeTargetActor(engine=self.engine)
        elif key == tcod.event.K_g:
            return PickUpEventHandler(engine=self.engine)
        elif key == tcod.event.K_r:
            return LoadoutEventHandler(engine=self.engine)
        elif key == tcod.event.K_q:
            try:
                return GunOptionsHandler(engine=self.engine, gun=player.inventory.held)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
        elif key == tcod.event.K_ESCAPE:
            return QuitEventHandler(self.engine)

        elif key == tcod.event.K_c:
            return SelectItemToCraft(engine=self.engine, item_dict=self.engine.crafting_recipes, title='Crafting')

        elif key == tcod.event.K_i:
            return InventoryEventHandler(self.engine)
        elif key == tcod.event.K_e:
            return EquipmentEventHandler(self.engine)
        elif key == tcod.event.K_s:
            return AttackStyleMenu(self.engine)
        # No valid key was pressed
        return action


class GameOverEventHandler(EventHandler):

    def on_quit(self) -> None:
        """Handle exiting out of a finished game."""
        if os.path.exists("savegame.sav"):
            os.remove("savegame.sav")  # Deletes the active save file.
        raise exceptions.QuitWithoutSaving()  # Avoid saving a finished game.

    def ev_quit(self, event: tcod.event.Quit) -> None:
        self.on_quit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        if event.sym == tcod.event.K_ESCAPE:
            self.on_quit()


CURSOR_Y_KEYS = {
    tcod.event.K_UP: -1,
    tcod.event.K_DOWN: 1,
    tcod.event.K_PAGEUP: -10,
    tcod.event.K_PAGEDOWN: 10,
}


class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated."""

    def __init__(self, engine: Engine):
        super().__init__(engine)
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

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[MainGameEventHandler]:
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
            return MainGameEventHandler(self.engine)
        return None


class AskUserEventHandler(EventHandler):
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
        return MainGameEventHandler(self.engine)


class UserOptionsEventHandler(AskUserEventHandler):

    def __init__(self, engine: Engine, options: list, title: str):
        self.options = options
        self.TITLE = title
        super().__init__(engine)

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
            return MainGameEventHandler(self.engine)

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

    def __init__(self, engine: Engine, page: int, options: list, title: str):
        super().__init__(engine)
        self.max_list_length = 15  # defines the maximum amount of items to be displayed in the menu
        self.page = page
        self.options = options
        self.TITLE = title

        super().__init__(engine)

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

            if isinstance(item, Item):
                stack_size = 0

                if item.stacking:
                    stack_size = 3 + item.stacking.stack_size
                if len(item.name) + stack_size > longest_name_len:
                    longest_name_len = len(item.name) + stack_size
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


class TypeAmountEventHandler(AskUserEventHandler):

    def __init__(self, item: Item, prompt_string: str, engine: Engine):
        super().__init__(engine)
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

        if self.item.stacking:
            if self.item.stacking.stack_size > 1:

                for event in tcod.event.wait():
                    try:
                        if isinstance(event, tcod.event.TextInput):
                            self.buffer += event.text

                        elif event.scancode == tcod.event.SCANCODE_ESCAPE:
                            return MainGameEventHandler(self.engine)

                        elif event.scancode == tcod.event.SCANCODE_BACKSPACE:
                            self.buffer = self.buffer[:-1]

                        elif event.scancode == tcod.event.SCANCODE_RETURN:

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

    def __init__(self, engine: Engine):
        title = "Inventory" + f" - {round(engine.player.inventory.current_item_weight(), 2)}" \
                              f"/{engine.player.inventory.capacity}kg"

        super().__init__(engine=engine, options=engine.player.inventory.items, page=0, title=title)

    def ev_on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        options = ['Drop', 'Inspect']

        if hasattr(item, 'usable_properties'):
            options.append('Use')

        if isinstance(item.usable_properties, Wearable):
            options.append('Equip')

        if isinstance(item.usable_properties, Gun):
            options += ['Equip', 'Disassemble']

        return ItemInteractionHandler(item=item, options=options, engine=self.engine)


class ItemInteractionHandler(UserOptionsEventHandler):  # options for interacting with an item

    def __init__(self, item, options: list, engine: Engine):
        self.item = item
        super().__init__(engine=engine, options=options, title=item.name)

    def ev_on_option_selected(self, option) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        if option == 'Use':
            try:
                if isinstance(self.item.usable_properties, Magazine):
                    return MagazineOptionsHandler(engine=self.engine, magazine=self.item)
                elif isinstance(self.item.usable_properties, Gun):
                    return GunOptionsHandler(engine=self.engine, gun=self.item)
                else:
                    return self.item.usable_properties.get_action(self.engine.player)

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'Equip':
            try:
                self.item.usable_properties.equip()
                return MainGameEventHandler(self.engine)

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'Unequip':
            try:
                self.item.usable_properties.unequip()
                return MainGameEventHandler(self.engine)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'Drop':
            try:
                return DropItemEventHandler(item=self.item, engine=self.engine)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'Disassemble':
            if hasattr(self.item.usable_properties, 'parts'):
                self.item.usable_properties.parts.disassemble(entity=self.engine.player)
                for i in range(5):
                    self.engine.handle_enemy_turns()
                return MainGameEventHandler(self.engine)

        elif option == 'Inspect':
            return InspectItemViewer(engine=self.engine, item=self.item)

        else:
            self.engine.message_log.add_message("Invalid entry", colour.RED)


class AmountToScrap(TypeAmountEventHandler):
    def __init__(self, engine: Engine, item: Item):
        super().__init__(engine=engine, item=item, prompt_string="amount to scrap (leave blank for all):")

    def ev_on_option_selected(self) -> Optional[ActionOrHandler]:

        stack_size = 1
        successful = True
        if self.item.stacking:
            stack_size = self.item.stacking.stack_size

        if stack_size < int(self.buffer):
            successful = False

        scrap_dict = deepcopy(self.item.usable_properties.material)

        if successful:

            for key, value in scrap_dict.items():
                scrap_item = key
                scrap_item.stacking.stack_size = value
                scrap_item.parent = self.engine.player.inventory
                scrap_item.stacking.stack_size = stack_size * int(self.buffer)
                self.engine.player.inventory.add_to_inventory(item=scrap_item, item_container=None, amount=1)

            if stack_size == int(self.buffer):
                self.engine.player.inventory.items.remove(self.item)

            else:
                stack_size -= int(self.buffer)

            if self.item.stacking:
                self.item.stacking.stack_size = stack_size

            return MainGameEventHandler(self.engine)

        else:
            self.engine.message_log.add_message("Invalid entry", colour.RED)


class EquipmentEventHandler(AskUserEventHandler):
    # used for equipment screen
    TITLE = "Equipment"

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.equipped_list = []  # equipped items

    def on_render(self, console: tcod.Console) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
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

                self.equipped_list.append(bodypart.equipped)
                equipment_dictionary[bodypart.equipped.name] = bodypart.part_type

                if len(bodypart.equipped.name) > longest_name_len:
                    longest_name_len = len(bodypart.equipped.name)

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
                return EquipmentEventHandler(engine=self.engine)
            return self.on_item_selected(selected_item)
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        options = ['Unequip', 'Inspect']

        return ItemInteractionHandler(item=item, options=options, engine=self.engine)


class DropItemEventHandler(TypeAmountEventHandler):

    def __init__(self, item, engine: Engine):
        super().__init__(engine=engine, item=item, prompt_string="amount to drop (leave blank for all):")

    def ev_on_option_selected(self) -> Optional[ActionOrHandler]:
        return actions.DropAction(entity=self.engine.player, item=self.item, drop_amount=int(self.buffer))


class PickUpEventHandler(UserOptionsWithPages):
    def __init__(self, engine: Engine):

        items_at_location = []

        actor_location_x = engine.player.x
        actor_location_y = engine.player.y

        for item in engine.game_map.items:
            if actor_location_x == item.x and actor_location_y == item.y:
                items_at_location.append(item)

        super().__init__(engine=engine, page=0, options=items_at_location, title="Pick Up Items")

    def ev_on_option_selected(self, item):
        if item.stacking:
            if item.stacking.stack_size > 1:
                return AmountToPickUpMenu(item=item, engine=self.engine)
            else:
                return PickupAction(entity=self.engine.player, item=item, amount=1)
        else:
            return PickupAction(entity=self.engine.player, item=item, amount=1)


class AmountToPickUpMenu(TypeAmountEventHandler):

    def __init__(self, item, engine: Engine):
        super().__init__(engine=engine, item=item, prompt_string="amount to pick up (leave blank for all):")

    def ev_on_option_selected(self) -> Optional[ActionOrHandler]:

        try:
            return actions.PickupAction(entity=self.engine.player, item=self.item, amount=int(self.buffer))

        except AttributeError:
            self.engine.message_log.add_message("Invalid entry", colour.RED)

        return MainGameEventHandler(self.engine)


class ChangeTargetActor(AskUserEventHandler):

    def __init__(self, engine: Engine):
        super().__init__(engine)
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

        self.get_targets()

    def get_targets(self) -> None:

        player = self.engine.player
        target_visible = False
        closest_distance = 1000
        closest_actor = None

        self.targets = []

        for actor in set(self.engine.game_map.actors) - {player}:
            if self.engine.game_map.visible[actor.x, actor.y]:
                self.targets.append(actor)

                # checks if previous target is still visible
                if player.target_actor == actor:
                    target_visible = True

                # checks for closest actor incase previous target not visible
                distance = player.distance(actor.x, actor.y)

                if distance < closest_distance:
                    closest_actor = actor

        # sets target actor to closest actor
        if not target_visible:
            player.target_actor = closest_actor

        if player.target_actor is not None:
            # centres camera on target
            self.engine.game_map.camera_xy = (player.target_actor.x, player.target_actor.y)

            # selects bodypart
            self.selected_bodypart = player.target_actor.bodyparts[0]

            self.update_bodypart_list()

            # sets targets index in target list
            self.target_index = self.targets.index(player.target_actor)

            self.update_part_str_colour()

    def on_render(self, console: tcod.Console):
        super().on_render(console)  # Draw the main state as the background.

        self.console = console

        screen_shape = console.rgb.shape
        cam_x, cam_y = self.engine.game_map.get_left_top_pos(screen_shape)

        player = self.engine.player

        console.print(x=1, y=1, string="ATTACK MODE - [ESC] TO EXIT", fg=colour.WHITE, bg=(0, 0, 0))

        if player.target_actor is not None:

            target_x, target_y = player.target_actor.x - cam_x, player.target_actor.y - cam_y

            if 0 <= target_x < console.width and 0 <= target_y < console.height:
                console.tiles_rgb[["ch", "fg"]][target_x, target_y] = ord('X'), colour.YELLOW

            target_str = f"Targeting: {player.target_actor.name} - {self.selected_bodypart.name}".upper()
            ap_str = f"AP: {player.fighter.ap}/{player.fighter.max_ap}"

            console.print(x=1, y=console.height-8, string=ap_str, fg=colour.WHITE, bg=(0, 0, 0))

            console.print(x=1, y=console.height-7, string=target_str, fg=colour.WHITE, bg=(0, 0, 0))

            console.print(x=1, y=console.height-6, string="PART CONDITION:", fg=colour.WHITE, bg=(0, 0, 0))

            console.print(x=17, y=console.height-6, string=f"{self.part_cond_str}", fg=self.part_cond_colour,
                          bg=(0, 0, 0))

        else:
            console.print(x=1, y=2, string="NO TARGET", fg=colour.LIGHT_RED, bg=(0, 0, 0))

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        player = self.engine.player
        key = event.sym

        if key == tcod.event.K_SPACE:  # change target

            try:
                player.target_actor = self.targets[self.target_index + 1]
                self.selected_bodypart = player.target_actor.bodyparts[0]
                self.bodypart_index = 0
                self.target_index += 1
                # centres camera on target
                self.engine.game_map.camera_xy = (player.target_actor.x, player.target_actor.y)
            except IndexError:
                player.target_actor = self.targets[0]
                self.selected_bodypart = player.target_actor.bodyparts[0]
                self.bodypart_index = 0
                self.target_index = 0
                self.engine.game_map.camera_xy = (player.target_actor.x, player.target_actor.y)
            except TypeError:
                return MainGameEventHandler(self.engine)

            self.target_index = self.targets.index(player.target_actor)

            # updates list of target bodyparts
            self.update_bodypart_list()
            self.update_part_str_colour()

        elif key == tcod.event.K_TAB:  # change limb targetted
            try:
                self.selected_bodypart = self.bodypartlist[self.bodypart_index + 1]
                self.bodypart_index += 1

            except IndexError:
                try:
                    self.selected_bodypart = self.bodypartlist[0]
                    self.bodypart_index = 0
                except IndexError:
                    return MainGameEventHandler(self.engine)

            self.update_part_str_colour()

        elif key == tcod.event.K_RETURN:  # atttack selected target

            if player.target_actor:

                distance_target = round(player.distance(player.target_actor.x, player.target_actor.y))

                # attack with weapon
                if self.item is not None:

                    actions.WeaponAttackAction(distance=distance_target, item=self.item, entity=player,
                                               targeted_actor=player.target_actor,
                                               targeted_bodypart=self.selected_bodypart).attack()

                # unarmed attack
                else:
                    actions.UnarmedAttackAction(distance=distance_target, entity=player,
                                                targeted_actor=player.target_actor,
                                                targeted_bodypart=self.selected_bodypart).attack()

                self.get_targets()
                self.engine.render(console=self.console)

            else:
                return MainGameEventHandler(self.engine)

        elif key in WAIT_KEYS:
            self.engine.handle_enemy_turns()

        elif key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            self.engine.game_map.move_camera(dx, dy)

        elif key == tcod.event.K_ESCAPE:
            self.engine.game_map.camera_xy = (self.engine.player.x, self.engine.player.y)
            return MainGameEventHandler(self.engine)

    def update_bodypart_list(self) -> None:
        # updates bodypart list
        self.bodypartlist = []
        for bodypart in self.engine.player.target_actor.bodyparts:
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


class QuitEventHandler(AskUserEventHandler):

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        console.draw_frame(
            x=24,
            y=22,
            width=32,
            height=4,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        console.print(x=25, y=23, string="Are you sure you want to quit?", fg=colour.WHITE, bg=(0, 0, 0))
        console.print(x=32, y=24, string="(Y) Yes, (N) No", fg=colour.WHITE, bg=(0, 0, 0))

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        key = event.sym
        if key == tcod.event.K_y:
            raise SystemExit()

        elif key == tcod.event.K_n:
            return MainGameEventHandler(self.engine)


class MagazineOptionsHandler(UserOptionsEventHandler):

    def __init__(self, engine: Engine, magazine: Item):

        self.magazine = magazine

        title = f"{magazine.name} - ({len(self.magazine.usable_properties.magazine)}/" \
                f"{self.magazine.usable_properties.mag_capacity})"

        options = ['load bullets', 'unload bullets']

        inventory = engine.player.inventory
        loadout = inventory.small_magazines + inventory.medium_magazines + inventory.large_magazines

        if magazine in loadout:
            options.append('remove from loadout')
        else:
            options.append('add to loadout')

        super().__init__(engine=engine, options=options, title=title)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        player = self.engine.player

        if option == 'load bullets':
            return SelectBulletsToLoadHandler(engine=self.engine, magazine=self.magazine)

        elif option == 'unload bullets':
            self.magazine.usable_properties.unload_magazine()

        elif option == 'add to loadout':
            player.inventory.add_to_magazines(magazine=self.magazine)

        elif option == 'remove from loadout':
            player.inventory.remove_from_magazines(magazine=self.magazine)

        return MainGameEventHandler(engine=self.engine)


class GunOptionsHandler(UserOptionsEventHandler):
    def __init__(self, engine: Engine, gun: Item):
        self.gun = gun

        title = gun.name
        options = []

        self.firemodes = self.gun.usable_properties.fire_modes

        if type(self.gun.usable_properties) is GunMagFed:
            options += ["load magazine", "unload magazine"]

        elif type(self.gun.usable_properties) is GunIntegratedMag:
            options += ["load rounds", "unload rounds"]

        for firemode in self.firemodes:
            if not firemode == self.gun.usable_properties.current_fire_mode:
                options.append(firemode)

        super().__init__(engine=engine, options=options, title=title)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        if option == 'load magazine':
            return SelectMagazineToLoadIntoGun(engine=self.engine, gun=self.gun)

        elif option == 'unload magazine':
            self.gun.usable_properties.unload_gun()

        elif option == 'load rounds':
            return SelectBulletsToLoadHandler(engine=self.engine, magazine=self.gun)

        elif option == 'unload rounds':
            self.gun.usable_properties.unload_magazine()

        elif option in self.firemodes:
            self.gun.usable_properties.current_fire_mode = option

        return MainGameEventHandler(engine=self.engine)


class SelectMagazineToLoadIntoGun(UserOptionsWithPages):

    def __init__(self, engine: Engine, gun: Item):
        self.gun = gun

        mag_list = []
        title = gun.name

        loadout = self.engine.player.inventory.small_magazines + self.engine.player.inventory.medium_magazines \
                  + self.engine.player.inventory.large_magazines

        for item in self.engine.player.inventory.items:
            if item in loadout:
                if item.usable_properties.magazine_type == self.gun.usable_properties.compatible_magazine_type:
                    mag_list.append(item)

        super().__init__(engine=engine, options=mag_list, page=0, title=title)

    def ev_on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        self.gun.usable_properties.load_gun(item)
        return MainGameEventHandler(engine=self.engine)


class SelectBulletsToLoadHandler(UserOptionsWithPages):
    TITLE = "Select Bullets"

    def __init__(self, engine: Engine, magazine: Item):
        self.magazine = magazine
        ammo_list = []

        for item in engine.player.inventory.items:
            if isinstance(item.usable_properties, Bullet):
                if item.usable_properties.bullet_type == self.magazine.usable_properties.compatible_bullet_type:
                    ammo_list.append(item)

        title = f"Load {self.magazine.name} - ({len(self.magazine.usable_properties.magazine)}/" \
                f"{self.magazine.usable_properties.mag_capacity})"

        super().__init__(engine=engine, page=0, title=title, options=ammo_list)

    def ev_on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        return SelectNumberOfBulletsToLoadHandler(engine=self.engine, magazine=self.magazine, ammo=item)


class SelectNumberOfBulletsToLoadHandler(TypeAmountEventHandler):

    def __init__(self, engine: Engine, magazine: Item, ammo: Item):
        self.magazine = magazine
        self.ammo = ammo
        super().__init__(engine=engine, item=ammo, prompt_string="amount to load (leave blank for maximum):")

    def ev_on_option_selected(self):
        self.magazine.usable_properties.load_magazine(ammo=self.ammo, load_amount=int(self.buffer))
        return MainGameEventHandler(self.engine)


class LoadoutEventHandler(UserOptionsWithPages):

    def __init__(self, engine: Engine):
        title = "Loadout"

        loadout_items = []

        inventory = self.engine.player.inventory

        items = inventory.small_magazines + inventory.medium_magazines + inventory.large_magazines

        for item in items:
            if item in inventory.items:
                loadout_items.append(item)

        super().__init__(engine=engine, options=loadout_items, page=0, title=title)

    def ev_on_option_selected(self, option):
        return MagazineOptionsHandler(engine=self.engine, magazine=option)


class SelectItemToCraft(UserOptionsWithPages):
    def __init__(self, engine: Engine, title: str, item_dict: dict):

        super().__init__(engine=engine, options=list(item_dict.keys()), page=0, title=title)
        self.item_dict = item_dict

    def ev_on_option_selected(self, option):

        # dictionary has parts list, can proceed with creating item
        if 'required parts' in list(self.item_dict[option].keys()):
            part_dict = {}

            # all required and compatible parts
            parts = list(self.item_dict[option]["required parts"].keys()) + \
                    list(self.item_dict[option]["compatible parts"].keys())

            # adds all required and compatible parts to the dictionary and sets
            # their value to None before player selects
            for part in parts:
                part_dict[part] = None

            if isinstance(self.item_dict[option]["item"].usable_properties, Gun):
                return CraftGun(engine=self.engine, item_to_craft=option, current_part_index=0,
                                item_dict=self.item_dict,
                                compatible_parts={},
                                part_dict=part_dict,
                                prevent_suppression=False,
                                attachment_points=[]
                                )
            else:
                return MainGameEventHandler(engine=self.engine)

        # dictionary selected does not have parts list
        else:
            return SelectItemToCraft(engine=self.engine, title=option, item_dict=self.item_dict[option])


class CraftItem(UserOptionsWithPages):
    def __init__(self,
                 engine: Engine,
                 item_to_craft: str,
                 current_part_index: int,
                 item_dict: dict,
                 compatible_parts: dict,
                 part_dict: dict,
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

        super().__init__(engine=engine, options=self.options, page=0, title=title)

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
                 attachment_points: list
                 ):

        self.prevent_suppression = prevent_suppression
        self.attachment_points = attachment_points

        super().__init__(engine=engine,
                         item_to_craft=item_to_craft,
                         current_part_index=current_part_index,
                         item_dict=item_dict,
                         compatible_parts=compatible_parts,
                         part_dict=part_dict,
                         )

    def add_options(self):

        # checks if current part selection is the same as the type an item in the prerequisite parts
        # if it is, only adds parts to options that are in prerequisites
        add_only_compatible = False
        for part_type in self.compatible_parts.keys():
            if part_type == self.parts[self.current_part_selection]:
                add_only_compatible = True
                break

        for item in self.engine.player.inventory.items:
            if isinstance(item.usable_properties, GunComponent):

                if item.usable_properties.part_type == self.parts[self.current_part_selection]:

                    add_option = True

                    # checks if there is an attachment point compatible with the attachment
                    if hasattr(item.usable_properties, 'attachment_point_required'):
                        attachment_point = getattr(item.usable_properties, 'attachment_point_required')
                        if any(item in attachment_point for item in self.attachment_points):
                            if attachment_point not in self.attachment_points:
                                add_option = False

                    if hasattr(item.usable_properties, 'incompatibilities'):
                        all_parts = []
                        for value in self.part_dict.values():
                            if hasattr(value, 'tags'):
                                all_parts += value.tags
                        incompatibilities = getattr(item.usable_properties, 'incompatibilities')
                        for setups in incompatibilities:
                            for items in setups:
                                if all(item in all_parts for item in items):
                                    add_option = False

                    # checks suppressor compatibility
                    if item.usable_properties.is_suppressor:
                        if self.prevent_suppression:
                            add_option = False

                    if add_option:
                        if add_only_compatible and item.name in \
                                self.compatible_parts[self.parts[self.current_part_selection]]:
                            self.options.append(item)
                        elif not add_only_compatible:
                            self.options.append(item)

        if self.parts[self.current_part_selection] in self.item_dict[self.item_name]["compatible parts"]:
            # if part is not required and there are no parts of this type available,
            # skips to the next part type
            if len(self.options) == 0 and self.parts[self.current_part_selection] != self.parts[-1]:
                self.options = ['none', ] + self.options
                self.current_part_selection += 1
                return CraftGun(engine=self.engine,
                                current_part_index=self.current_part_selection,
                                item_to_craft=self.item_name,
                                item_dict=self.item_dict,
                                part_dict=self.part_dict,
                                compatible_parts=self.compatible_parts,
                                prevent_suppression=self.prevent_suppression,
                                attachment_points=self.attachment_points
                                )

            # part is not required, adds the option to select no part
            else:
                self.options = ['none', ] + self.options

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

        if hasattr(option.usable_properties, 'additional_required_parts'):
            for i in option.usable_properties.additional_required_parts:
                if i in self.item_dict[self.item_name]["compatible parts"]:
                    del self.item_dict[self.item_name]["compatible parts"][i]

        if option.usable_properties.prevents_suppression:
            self.prevent_suppression = True

    def ev_on_option_selected(self, option):

        if not option == 'none':
            # sets part in part dict to be the selected part
            self.part_dict[self.parts[self.current_part_selection]] = option
            self.update_crafting_properties(option)

        # part is last part to select
        if self.parts[self.current_part_selection] == self.parts[-1]:
            item = self.item_dict[self.item_name]['item']

            craftable = True

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
                    item.usable_properties.parts.update_partlist()
                item.parent = self.engine.player.inventory

                for i in range(5):
                    self.engine.handle_enemy_turns()

                self.engine.player.inventory.add_to_inventory(item=item, item_container=None, amount=1)
                return MainGameEventHandler(engine=self.engine)

            else:
                return MainGameEventHandler(engine=self.engine)

        else:
            self.current_part_selection += 1
            return CraftGun(engine=self.engine,
                            current_part_index=self.current_part_selection,
                            item_to_craft=self.item_name,
                            item_dict=self.item_dict,
                            part_dict=self.part_dict,
                            compatible_parts=self.compatible_parts,
                            prevent_suppression=self.prevent_suppression,
                            attachment_points=self.attachment_points
                            )


class InspectItemViewer(AskUserEventHandler):

    def __init__(self, engine, item):
        super().__init__(engine=engine)

        self.item = item
        self.TITLE = item.name
        self.description = item.description

        self.inspect_parts_option = False

        if hasattr(item.usable_properties, 'parts'):
            self.inspect_parts_option = True

        item_info = {
            "description": item.description,
            "weight": item.weight,
        }

        additonal_info = {

            "attachment point": 'attachment_point_required',

            # healing consumable
            "healing amount": 'amount',

            # weapon
            "maximum range": 'maximum_range',
            "equip turns": 'ap_to_equip',

            # melee weapon
            "base damage": 'base_meat_damage',
            "base armour damage": 'base_armour_damage',
            "accuracy modifier": 'base_accuracy',

            # bullet
            "round type": 'bullet_type',
            "bullet mass (grains)": 'mass',
            "charge mass (grains)": 'charge_mass',
            "bullet diameter (inches)": 'diameter',
            "bullet velocity (fps)": 'velocity',
            "sound modifier": 'sound_modifier',
            "spread modifier": 'spread_modifier',
            "ballistic coefficient": 'ballistic_coefficient',
            "drag coefficient": 'drag_coefficient',
            "projectile amount": 'projectile_no',

            # magazine
            "magazine type": 'magazine_type',
            "magazine size": 'magazine_size',
            "magazine capacity": 'mag_capacity',
            "compatible round": 'compatible_bullet_type',
            "turns to load": 'ap_to_load',

            # gun
            "felt recoil": 'felt_recoil',
            "reload time modifier": 'load_time_modifier',
            "fire rate modifier": 'fire_rate_modifier',
            "barrel length": 'barrel_length',
            "zero range": 'zero_range',
            "sight height over bore": 'sight_height_above_bore',
            "receiver height above bore": 'receiver_height_above_bore',
            "AP cost distance modifier": 'ap_distance_cost_modifier',
            "target acquisition AP cost": 'target_acquisition_ap',
            "AP cost to fire": 'firing_ap_cost',
            "muzzle break efficiency": 'muzzle_break_efficiency',
            "shot sound modifier": 'sound_modifier',
            "bullet velocity modifier": 'velocity_modifier',
            "bullet spread": 'spread_modifier',

            # mag fed
            "compatible magazine": 'compatible_magazine_type',

            # wearable
            "fits bodypart": 'fits_bodypart',
            "protection": 'protection',
            "large mag slots": 'large_mag_slots',
            "medium mag slots": 'medium_mag_slots',
            "small mag slots": 'small_mag_slots',

            # component part
            "part type": 'part_type',
            "prevents suppression": 'prevents_suppression',

            # gun component
            "compatible parts": 'compatible_parts',
            "has attachment points": 'is_attachment_point_types',
            "requires additional parts": 'additional_required_parts',
            "requires attachment point": 'attachment_point_required',
        }

        for key, value in additonal_info.items():
            if hasattr(item.usable_properties, value):
                item_info[key] = getattr(item.usable_properties, value)

                if isinstance(value, dict):
                    for key_2, value_2 in value:
                        item_info[key] = f"{key_2:}"
                        for string in value_2:
                            item_info[key] += f" {string}"
                            if not string == value_2[-1]:
                                item_info[key] += ', '

                elif type(value) in (list, tuple):
                    item_info[key] = ''
                    for x in value:
                        item_info[key] += f"{x}"
                        if not x == value[-1]:
                            item_info[key] += ', '

        if isinstance(item.usable_properties, Gun):
            fire_modes = {"fire modes": ''}
            for key, value in item.usable_properties.fire_modes.items():
                if key == "single shot":
                    fire_modes["fire modes"] += 'single shot, '
                elif key == "rapid fire (semi-auto)":
                    pass
                else:
                    fire_modes["fire modes"] += f"{key} - {value}RPM, "

            item_info.update(fire_modes)

        self.item_info = item_info

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        height = len(self.item_info) * 2 + 2

        for key, value in self.item_info.items():
            if len(str(value)) > 36:
                height += ceil((len(str(value))) / 36)

        console.draw_frame(
            x=1,
            y=1,
            width=40,
            height=height,
            title=self.TITLE,
            clear=True,
            fg=colour.WHITE,
            bg=(0, 0, 0),
        )

        y = 2

        for key, value in self.item_info.items():
            wrapper = textwrap.TextWrapper(width=36)
            word_list = wrapper.wrap(text=str(value))
            console.print(x=2, y=y, string=f"{key}", fg=colour.LIGHT_GREEN)
            y += 1
            for string in word_list:
                console.print(x=2, y=y, string=string)
                y += 1

        if self.inspect_parts_option:
            console.print(x=2, y=y + 1, string=f"(i) show parts")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[BaseEventHandler]:

        key = event.sym

        if key == tcod.event.K_i:
            if self.inspect_parts_option:
                return ShowParts(engine=self.engine, item=self.item)

        elif key == tcod.event.K_ESCAPE:
            return MainGameEventHandler(self.engine)


class ShowParts(UserOptionsWithPages):

    def __init__(self, engine, item):
        title = f"parts - {item.name}"

        super().__init__(engine=engine, options=item.usable_properties.parts.part_list, page=0, title=title)

    def ev_on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        return InspectItemViewer(item=item, engine=self.engine)


class AttackStyleMenu(UserOptionsEventHandler):

    def __init__(self, engine: Engine):

        title = "Change Attack Style"
        options = ['Precise', 'Measured', 'Close Quarters']

        super().__init__(engine=engine, options=options, title=title)

    def ev_on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        player = self.engine.player

        if option == 'Precise':
            player.fighter.attack_style_precision()

        elif option == 'Measured':
            player.fighter.attack_style_measured()

        elif option == 'Close Quarters':
            player.fighter.attack_style_cqc()

        return MainGameEventHandler(engine=self.engine)