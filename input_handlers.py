from __future__ import annotations

from typing import Optional, TYPE_CHECKING
from math import ceil
from copy import deepcopy

import tcod.event

import actions
from actions import (
    Action,
    BumpAction,
    PickupAction,
    ChangeTarget,
    WaitAction
)

import colour
import exceptions
from scrolling_map import Camera


if TYPE_CHECKING:
    from engine import Engine
    from entity import Item

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

CHANGE_TARGET = {
    tcod.event.K_t
}


class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self, event: tcod.event.Event) -> None:
        self.handle_action(self.dispatch(event))

    def handle_action(self, action: Optional[Action]) -> bool:
        """Handle actions returned from event methods.

        Returns True if the action will advance a turn.
        """
        if action is None:
            return False

        try:
            action.perform()
        except exceptions.Impossible as exc:
            self.engine.message_log.add_message(exc.args[0], colour.RED)
            return False  # Skip enemy turn on exceptions.

        self.engine.handle_enemy_turns()

        self.engine.update_fov()
        return True

    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:
        if self.engine.game_map.in_bounds(event.tile.x, event.tile.y):
            self.engine.mouse_location = event.tile.x, event.tile.y

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        self.engine.render(console, camera)


class MainGameEventHandler(EventHandler):

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy)
        elif key in WAIT_KEYS:
            action = WaitAction(player)
        elif key in CHANGE_TARGET:
            action = ChangeTarget(player)
        elif key == tcod.event.K_v:
            self.engine.event_handler = HistoryViewer(self.engine)
        elif key == tcod.event.K_g:
            action = PickupAction(player)
        elif key == tcod.event.K_ESCAPE:
            raise SystemExit()

        elif key == tcod.event.K_i:
            self.engine.event_handler = InventoryInteractHandler(self.engine, 0)
        elif key == tcod.event.K_e:
            self.engine.event_handler = EquipmentInteractHandler(self.engine)
        # No valid key was pressed
        return action


class GameOverEventHandler(EventHandler):
    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        if event.sym == tcod.event.K_ESCAPE:
            raise SystemExit()


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

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        super().on_render(console, camera)  # Draw the main state as the background.

        log_console = tcod.Console(console.width - 6, console.height - 6)

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

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
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
            self.engine.event_handler = MainGameEventHandler(self.engine)


class AskUserEventHandler(EventHandler):
    """Handles user input for actions which require special input."""

    def handle_action(self, action: Optional[Action]) -> bool:
        """Return to the main event handler when a valid action was performed."""
        if super().handle_action(action):
            self.engine.event_handler = MainGameEventHandler(self.engine)
            return True
        return False

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
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

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[Action]:
        """By default any mouse click exits this input handler."""
        return self.on_exit()

    def on_exit(self) -> Optional[Action]:
        """Called when the user is trying to exit or cancel an action.

        By default this returns to the main event handler.
        """
        self.engine.event_handler = MainGameEventHandler(self.engine)
        return None


class InventoryEventHandler(AskUserEventHandler):
    """This handler lets the user select an item.

    What happens then depends on the subclass.
    """

    TITLE = "<missing title>"

    def __init__(self, engine: Engine, page: int):
        super().__init__(engine)
        self.max_list_length = 5  # defines the maximum amount of items to be displayed in the menu
        self.page = page

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render(console, camera)
        number_of_items_in_inventory = len(self.engine.player.inventory.items)

        longest_name_len = None
        if len(self.engine.player.inventory.items) > 0:
            longest_name_len = self.engine.player.inventory.items[0]

        width = len(self.TITLE) + 4
        height = number_of_items_in_inventory + 2

        if number_of_items_in_inventory > self.max_list_length:
            height = self.max_list_length + 2

        x = 1
        y = 1

        index_range = self.page * self.max_list_length

        for item in self.engine.player.inventory.items[index_range:index_range+self.max_list_length]:
            try:
                if len(item.name) > len(longest_name_len.name) + len(str(longest_name_len.stacking.stack_size)) + 2:
                    longest_name_len = item
            except AttributeError:
                if len(item.name) > len(longest_name_len.name):
                    longest_name_len = item

            if item.stacking:
                try:
                    if len(item.name) + len(str(item.stacking.stack_size)) > \
                            len(longest_name_len.name) + len(str(longest_name_len.stacking.stack_size)):
                        longest_name_len = item
                except AttributeError:
                    if len(item.name) + len(str(item.stacking.stack_size)) + 2 > len(longest_name_len.name):
                        longest_name_len = item

        if longest_name_len:
            if len(longest_name_len.name) + 6 > width:
                width = len(longest_name_len.name) + 6

        stack_str_len = 0

        if longest_name_len:
            if longest_name_len.stacking:
                stack_str_len = len(str(longest_name_len.stacking.stack_size)) + 2

        console.draw_frame(
            x=x,
            y=y,
            width=width + stack_str_len,
            height=height,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
        )

        if number_of_items_in_inventory > 0:
            console.print(x + 1, y + height - 1,
                          f"Page {self.page + 1}/{ceil(len(self.engine.player.inventory.items)/self.max_list_length)}")

            for i, item in enumerate(self.engine.player.inventory.items[index_range:index_range+self.max_list_length]):
                item_key = chr(ord("a") + i)
                if item.stacking:
                    console.print(x + 1, y + i + 1, f"({item_key}) {item.name} ({item.stacking.stack_size})")
                else:
                    console.print(x + 1, y + i + 1, f"({item_key}) {item.name}")
        else:
            console.print(x + 1, y + 1, "(Empty)")

    def ev_keydown(self, event: tcod.event.KeyDown):
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a

        if key == tcod.event.K_DOWN:
            if len(self.engine.player.inventory.items) > (self.page + 1) * self.max_list_length:
                self.engine.event_handler = InventoryInteractHandler(self.engine, self.page + 1)
                return

        if key == tcod.event.K_UP:
            if self.page > 0:
                self.engine.event_handler = InventoryInteractHandler(self.engine, self.page - 1)
                return

        if 0 <= index <= self.max_list_length - 1:
            try:
                selected_item = player.inventory.items[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.on_item_selected(selected_item)
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[Action]:
        """Called when the user selects a valid item."""
        raise NotImplementedError()


class InventoryInteractHandler(InventoryEventHandler):
    """Handle using an inventory item."""

    TITLE = "Inventory"

    def on_item_selected(self, item: Item) -> None:
        options = ('Use', 'Equip', 'Drop')
        self.engine.event_handler = ItemInteractionHandler(item=item, options=options, engine=self.engine)


class ItemInteractionHandler(AskUserEventHandler):  # options for interacting with an item

    TITLE = "Item Options"

    def __init__(self, item, options: tuple, engine: Engine):
        super().__init__(engine)
        self.item = item
        self.options = options

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        """
        Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render(console, camera)
        if self.item is not None:
            x = 1
            y = 1

            longest_option_len = 0

            height = len(self.options) + 2

            for option in self.options:
                if len(option) > longest_option_len:
                    longest_option_len = len(option)

            if len(self.TITLE) + 4 > longest_option_len + 6:
                width = longest_option_len + 6
            else:
                width = len(self.TITLE) + 4

            console.draw_frame(
                x=x,
                y=y,
                width=width,
                height=height,
                title=self.item.name,
                clear=True,
                fg=(255, 255, 255),
                bg=(0, 0, 0),
            )

            for i, option in enumerate(self.options):
                option_key = chr(ord("a") + i)
                console.print(x + 1, y + i + 1, f"({option_key}) {option}")

        else:
            self.engine.message_log.add_message("Invalid entry.", colour.RED)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        key = event.sym
        index = key - tcod.event.K_a

        if 0 <= index <= 26:
            try:
                selected_option = self.options[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.on_option_selected(selected_option)
        return super().ev_keydown(event)

    def on_option_selected(self, option) -> Optional[Action]:
        """Called when the user selects a valid item."""
        if option == 'Use':
            try:
                if self.item.consumable:
                    return self.item.consumable.get_action(self.engine.player)
                elif self.item.weapon:
                    return self.item.weapon.get_action(self.engine.player)

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)

        elif option == 'Equip':
            try:
                if self.item.weapon:
                    return actions.EquipWeapon(self.engine.player, self.item)
                elif self.item.wearable:
                    return actions.EquipArmour(self.engine.player, self.item)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)

        elif option == 'Unequip':
            try:
                if self.item.weapon:
                    return actions.UnequipWeapon(self.engine.player, self.item)
                elif self.item.wearable:
                    return actions.UnequipArmour(self.engine.player, self.item)
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)

        elif option == 'Drop':
            try:
                self.engine.event_handler = DropItemEventHandler(item=self.item, engine=self.engine)
                return
            except AttributeError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)

        else:
            self.engine.message_log.add_message("Invalid entry.", colour.RED)


class EquipmentEventHandler(AskUserEventHandler):
    # used for equipment screen
    TITLE = "<missing title>"

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render(console, camera)

        equipped_list = []  # equipped items

        equipment_dictionary = {}  # dictionary containing bodypart associated with the item equipped

        # adds held item to the equipped list
        if self.engine.player.inventory.held is not None:
            equipped_list.append(self.engine.player.inventory.held)

        longest_part_len = 4  # set to 4 by defualt because of 'Held'
        longest_name_len = 0  # for items

        # adds all items equipped by bodyparts of the entity to the equipped list
        for bodypart in self.engine.player.bodyparts:
            if bodypart.equipped:
                equipped_list.append(bodypart)
                # from the item gives the name of the bodypart that it is equipped by, adds it to equipment_dictionary

                equipment_dictionary[bodypart.name] = bodypart.equipped.name

                if len(bodypart.name) > longest_part_len:
                    longest_part_len = len(bodypart.name)
                if len(bodypart.equipped.name) > longest_name_len:
                    longest_name_len = len(bodypart.equipped.name)

        width = len(self.TITLE) + 4
        height = len(equipped_list) + 2

        x = 1
        y = 1

        if longest_name_len + longest_part_len + 9 > width:
            width = longest_name_len + longest_part_len + 11

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=height,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
        )

        if len(equipped_list) > 0:
            for i, item in enumerate(equipped_list):

                item_key = chr(ord("a") + i)

                if item == self.engine.player.inventory.held:
                    console.print(x + 1, y + i + 1, f"({item_key}) | Held | {item.name}")

                else:
                    console.print(x + 1, y + i + 1, f"({item_key}) | {item.name} | {item.equipped.name}")

        else:
            console.print(x + 1, y + 1, "(Empty)")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a

        if 0 <= index <= 26:
            try:
                selected_item = player.bodyparts[index].equipped
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.on_item_selected(selected_item)
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[Action]:
        """Called when the user selects a valid item."""
        raise NotImplementedError()


class EquipmentInteractHandler(EquipmentEventHandler):  # equipment screen
    TITLE = "Equipment"

    def on_item_selected(self, item: Item) -> None:
        options = ('Unequip',)
        self.engine.event_handler = ItemInteractionHandler(item=item, options=options, engine=self.engine)


class DropItemEventHandler(AskUserEventHandler):

    def __init__(self, item, engine: Engine):
        super().__init__(engine)
        self.item = item
        self.engine = engine
        self.drop_amount = 0
        self.buffer = ''
        self.console = None
        self.camera = None

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        super().on_render(console, camera)

        self.console = console
        self.camera = camera

        if self.item.stacking:
            if self.item.stacking.stack_size > 1:
                console.draw_frame(
                    x=1,
                    y=1,
                    width=18 + len(self.buffer),
                    height=3,
                    clear=True,
                    fg=(255, 255, 255),
                    bg=(0, 0, 0),
                )
                console.print(x=2, y=2, string=f"amount to drop: {self.buffer}")

    def ev_keydown(self, event):

        if self.item.stacking:
            if self.item.stacking.stack_size > 1:

                for event in tcod.event.wait():

                    if isinstance(event, tcod.event.TextInput):
                        self.buffer += event.text

                    elif event.scancode == tcod.event.SCANCODE_ESCAPE:
                        self.engine.event_handler = MainGameEventHandler(self.engine)
                        return

                    elif event.scancode == tcod.event.SCANCODE_BACKSPACE:
                        print('backspace')
                        self.buffer = self.buffer[:-1]

                    elif event.scancode == tcod.event.SCANCODE_RETURN:
                        # buffer is ready to be used.
                        try:

                            # copy of the item to be dropped
                            dropped_item = deepcopy(self.item)

                            self.drop_amount = int(self.buffer, base=0)
                            # sets dropped item to have correct stack size
                            dropped_item.stacking.stack_size = self.drop_amount

                            # more than 1 stack left in after drop
                            if self.item.stacking.stack_size - self.drop_amount > 1:
                                if self.item in self.engine.player.inventory.items:
                                    self.item.stacking.stack_size -= self.drop_amount
                                    dropped_item.place(self.engine.player.x, self.engine.player.y, self.engine.game_map)
                                    self.engine.message_log.add_message(f"You dropped the {self.item.name}.")
                                    self.engine.event_handler = MainGameEventHandler(self.engine)

                            # no stacks left after drop
                            elif self.item.stacking.stack_size - self.drop_amount <= 0:
                                self.drop_item(self.item)

                        # invalid input
                        except ValueError:
                            self.engine.message_log.add_message(f"Invalid Input", fg=colour.RED)
                            self.engine.event_handler = MainGameEventHandler(self.engine)
                            return

            else:  # item stacking, stack size = 1
                self.drop_item(self.item)

        else:  # item not stacking
            self.drop_item(self.item)

    def drop_item(self, item):
        """
        Removes an item from the inventory and restores it to the game map, at the player's current location.
        """
        if item in self.engine.player.inventory.items:
            self.engine.player.inventory.items.remove(item)

        item.place(self.engine.player.x, self.engine.player.y, self.engine.game_map)

        self.engine.message_log.add_message(f"You dropped the {item.name}.")
        self.engine.event_handler = MainGameEventHandler(self.engine)
        return
