from __future__ import annotations

import os
from copy import deepcopy
from typing import Optional, TYPE_CHECKING, Union
from math import ceil, floor
import textwrap

import tcod.event

from entity import Item
import actions
from components.weapons.gundict import guns_dict
from components.consumables import Gun, GunIntegratedMag, GunMagFed, Bullet, Magazine, ComponentPart, Wearable, \
    Weapon, HealingConsumable
#from components.weapons.bullets import bullet_crafting_dict
#from components.weapons.magazines import magazine_crafting_dict
from actions import (
    Action,
    BumpAction,
    PickupAction,
    WaitAction
)

import colour
import exceptions
from scrolling_map import Camera


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

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        raise NotImplementedError

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()


class PopupMessage(BaseEventHandler):
    """Display a popup text window."""

    def __init__(self, parent_handler: BaseEventHandler, text: str):
        self.parent = parent_handler
        self.text = text

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        """Render the parent and dim the result, then print the message on top."""
        self.parent.on_render(console, camera)
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

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        self.engine.render(console, camera)


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
            return CraftingEventHandler(self.engine)

        elif key == tcod.event.K_i:
            return InventoryEventHandler(self.engine)
        elif key == tcod.event.K_e:
            return EquipmentEventHandler(self.engine)
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

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        super().on_render(console, camera)

        longest_option_name = 0

        for option in self.options:
            if isinstance(option, Item):
                if len(option.name) > longest_option_name:
                    longest_option_name = len(option.name)
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
            width=width + 6,
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
            return self.on_option_selected(selected_option)
        return super().ev_keydown(event)

    def on_option_selected(self, option):
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

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render(console, camera)

        number_of_options = len(self.options)

        width = len(self.TITLE)
        height = number_of_options + 2

        if number_of_options > self.max_list_length:
            height = self.max_list_length + 2

        x = 1
        y = 2

        index_range = self.page * self.max_list_length

        longest_name_len = 0

        for item in self.options[index_range:index_range+self.max_list_length]:

            if isinstance(item, Item):
                if item.stacking:
                    if len(item.name) + len(str(item.stacking.stack_size)) > longest_name_len:
                        longest_name_len = len(item.name) + len(str(item.stacking.stack_size))
                else:
                    if len(item.name) > longest_name_len:
                        longest_name_len = len(item.name)

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
                          f"Page {self.page + 1}/{ceil(len(self.options)/self.max_list_length)}")

            for i, item in enumerate(self.options[index_range:index_range+self.max_list_length]):
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
                selected_item = self.options[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", colour.RED)
                return None
            return self.on_option_selected(selected_item)
        return super().ev_keydown(event)

    def on_option_selected(self, option):
        return NotImplementedError


class TypeAmountEventHandler(AskUserEventHandler):

    def __init__(self, item: Item, prompt_string: str, engine: Engine):
        super().__init__(engine)
        self.item = item
        self.engine = engine
        self.pick_up_amount = 0
        self.buffer = ''
        self.prompt_string = prompt_string

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        super().on_render(console, camera)

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

                            if self.buffer == '':
                                self.buffer = f'{self.item.stacking.stack_size}'

                            return self.on_option_selected()

                    except AttributeError:
                        pass

            else:
                self.buffer = '1'
                return self.on_option_selected()

        else:
            self.buffer = '1'
            return self.on_option_selected()

    def on_option_selected(self):
        return NotImplementedError


class InventoryEventHandler(UserOptionsWithPages):

    def __init__(self, engine: Engine):
        title = "Inventory" + f" - {engine.player.inventory.current_item_weight()}" \
                                  f"/{engine.player.inventory.capacity}kg"

        super().__init__(engine=engine, options=engine.player.inventory.items, page=0, title=title)

    def on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        options = ['Use', 'Equip', 'Drop', 'Inspect']

        if isinstance(item.usable_properties, Gun):
            options.append('Disassemble')

        return ItemInteractionHandler(item=item, options=options, engine=self.engine)


class ItemInteractionHandler(UserOptionsEventHandler):  # options for interacting with an item

    def __init__(self, item, options: list, engine: Engine):
        self.item = item
        super().__init__(engine=engine, options=options, title=item.name)

    def on_option_selected(self, option) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        if option == 'Use':
            try:
                if type(self.item.usable_properties) is Magazine:
                    return MagazineOptionsHandler(engine=self.engine, magazine=self.item)
                elif isinstance(self.item.usable_properties, Gun):
                    return GunOptionsHandler(engine=self.engine, gun=self.item)
                else:
                    return self.item.usable_properties.get_action(self.engine.player)

            except AttributeError:
                self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'Equip':
            #try:
            self.item.usable_properties.equip()
            self.engine.handle_enemy_turns()
            return MainGameEventHandler(self.engine)

            #except AttributeError:
            #    self.engine.message_log.add_message("Invalid entry", colour.RED)

        elif option == 'Unequip':
            try:
                self.item.usable_properties.unequip()
                self.engine.handle_enemy_turns()
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
                turns_taken = 0
                while turns_taken < 5:
                    turns_taken += 1
                    self.engine.handle_enemy_turns()
                return MainGameEventHandler(self.engine)

        elif option == 'Inspect':
            return InspectItemViewer(engine=self.engine, item=self.item)

        else:
            self.engine.message_log.add_message("Invalid entry", colour.RED)


class EquipmentEventHandler(AskUserEventHandler):
    # used for equipment screen
    TITLE = "Equipment"

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.equipped_list = []  # equipped items

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render(console, camera)

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
        return ItemInteractionHandler(item=item, options=['Unequip', 'Inspect'], engine=self.engine)


class DropItemEventHandler(TypeAmountEventHandler):

    def __init__(self, item, engine: Engine):
        super().__init__(engine=engine, item=item, prompt_string="amount to drop (leave blank for all):")

    def on_option_selected(self) -> Optional[ActionOrHandler]:

        actions.DropAction(entity=self.engine.player, item=self.item, drop_amount=int(self.buffer)).perform()

        self.engine.handle_enemy_turns()
        return MainGameEventHandler(self.engine)


class PickUpEventHandler(UserOptionsWithPages):
    def __init__(self, engine: Engine):

        items_at_location = []

        actor_location_x = engine.player.x
        actor_location_y = engine.player.y

        for item in engine.game_map.items:
            if actor_location_x == item.x and actor_location_y == item.y:
                items_at_location.append(item)

        super().__init__(engine=engine, page=0, options=items_at_location, title="Pick Up Items")

    def on_option_selected(self, item):
        if item.stacking:
            if item.stacking.stack_size > 1:
                return AmountToPickUpMenu(item=item, engine=self.engine)
            else:
                PickupAction(entity=self.engine.player, item=item, pickup_amount=1).perform()
                self.engine.handle_enemy_turns()
                return MainGameEventHandler(engine=self.engine)
        else:
            PickupAction(entity=self.engine.player, item=item, pickup_amount=1).perform()
            self.engine.handle_enemy_turns()
            return MainGameEventHandler(engine=self.engine)


class AmountToPickUpMenu(TypeAmountEventHandler):

    def __init__(self, item, engine: Engine):
        super().__init__(engine=engine, item=item, prompt_string="amount to pick up (leave blank for all):")

    def on_option_selected(self) -> Optional[ActionOrHandler]:

        try:
            actions.PickupAction(entity=self.engine.player, item=self.item, pickup_amount=int(self.buffer)).perform()
            self.engine.handle_enemy_turns()

        except AttributeError:
            self.engine.message_log.add_message("Invalid entry", colour.RED)

        return MainGameEventHandler(self.engine)


class ChangeTargetActor(AskUserEventHandler):

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.engine = engine
        self.targets = []
        self.target_index = None
        self.distance_target = None
        self.selected_bodypart = None
        self.bodypart_index = 0
        self.bodypartlist = []

        self.camera = None
        self.console = None

        self.item = self.engine.player.inventory.held

    def on_render(self, console: tcod.Console, camera: Camera):
        super().on_render(console, camera)  # Draw the main state as the background.

        self.console = console
        self.camera = camera

        player = self.engine.player
        target_visible = False
        closest_distance = 40
        closest_actor = None

        for actor in self.engine.game_map.actors:
            if actor is not player and self.engine.game_map.visible[actor.x, actor.y]:
                self.targets.append(actor)
                distance = player.distance(actor.x, actor.y)

                if player.target_actor == actor:
                    target_visible = True

                elif distance < closest_distance:
                    closest_actor = actor

        if not target_visible:
            player.target_actor = closest_actor

        if not self.selected_bodypart:
            try:
                self.selected_bodypart = player.target_actor.bodyparts[0]
            except AttributeError:
                return MainGameEventHandler(self.engine)

        if player.target_actor:
            self.distance_target = floor(player.distance(player.target_actor.x, player.target_actor.y))
            self.target_index = self.targets.index(player.target_actor)
            console.print(x=player.target_actor.x, y=player.target_actor.y, string="X", fg=colour.YELLOW, bg=(0, 0, 0))
            console.draw_rect(x=0, y=45, width=80, height=1, ch=0, fg=(0, 0, 0), bg=(0, 0, 0))
            console.print(x=1, y=45, string=f"Targeting: {player.target_actor.name} - {self.selected_bodypart.name}",
                          fg=colour.WHITE)

            for bodypart in player.target_actor.bodyparts:
                if bodypart.functional:
                    self.bodypartlist.append(bodypart)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        player = self.engine.player
        key = event.sym

        if key == tcod.event.K_SPACE:  # change target
            try:
                player.target_actor = self.targets[self.target_index + 1]
                self.selected_bodypart = player.target_actor.bodyparts[0]
                self.bodypart_index = 0
                self.target_index += 1
            except IndexError:
                player.target_actor = self.targets[0]
                self.selected_bodypart = player.target_actor.bodyparts[0]
                self.bodypart_index = 0
                self.target_index = 0

            self.bodypartlist = []
            for bodypart in player.target_actor.bodyparts:
                if bodypart.functional:
                    self.bodypartlist.append(bodypart)

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

        elif key == tcod.event.K_RETURN:  # atttack selected target

            if player.target_actor and self.item is not None:

                actions.WeaponAttackAction(distance=self.distance_target, item=self.item, entity=player,
                                           targeted_actor=player.target_actor,
                                           targeted_bodypart=self.selected_bodypart).attack()
                self.engine.handle_enemy_turns()
                self.engine.render(console=self.console, camera=self.camera)
                return MainGameEventHandler(self.engine)

            else:
                return MainGameEventHandler(self.engine)

        elif key == tcod.event.K_ESCAPE:
            return MainGameEventHandler(self.engine)


class QuitEventHandler(AskUserEventHandler):

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        super().on_render(console, camera)  # Draw the main state as the background.

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

    def on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        player = self.engine.player

        if option == 'load bullets':
            return SelectBulletsToLoadHandler(engine=self.engine, magazine=self.magazine)

        elif option == 'unload bullets':
            self.engine.handle_enemy_turns()
            self.magazine.usable_properties.unload_magazine()

        elif option == 'add to loadout':
            player.inventory.add_to_magazines(magazine=self.magazine)
            self.engine.handle_enemy_turns()

        elif option == 'remove from loadout':
            player.inventory.remove_from_magazines(magazine=self.magazine)
            self.engine.handle_enemy_turns()

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

    def on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
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

        self.engine.handle_enemy_turns()
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

    def on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        # takes appropriate amount of turns to load magazine into gun
        turns_used = 0
        while turns_used < item.usable_properties.turns_to_load:
            turns_used += 1
            self.engine.handle_enemy_turns()

        self.gun.usable_properties.load_gun(item)
        return MainGameEventHandler(engine=self.engine)


class SelectBulletsToLoadHandler(UserOptionsWithPages):

    TITLE = "Select Bullets"

    def __init__(self, engine: Engine, magazine: Item):
        self.magazine = magazine
        ammo_list = []

        for item in self.engine.player.inventory.items:
            if isinstance(item.usable_properties, Bullet):
                if item.usable_properties.bullet_type == self.magazine.usable_properties.compatible_bullet_type:
                    ammo_list.append(item)

        title = f"Load {self.magazine.name} - ({len(self.magazine.usable_properties.magazine)}/" \
                f"{self.magazine.usable_properties.mag_capacity})"

        super().__init__(engine=engine, page=0, title=title, options=ammo_list)

    def on_option_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        return SelectNumberOfBulletsToLoadHandler(engine=self.engine, magazine=self.magazine, ammo=item)


class SelectNumberOfBulletsToLoadHandler(TypeAmountEventHandler):

    def __init__(self, engine: Engine, magazine: Item, ammo: Item):
        self.ammo = ammo
        super().__init__(engine=engine, item=magazine, prompt_string="amount to load (leave blank for maximum):")

    def on_option_selected(self):

        try:
            self.item.usable_properties.load_magazine(ammo=self.ammo, load_amount=int(self.buffer))

        except ValueError:
            self.engine.message_log.add_message("Invalid entry", colour.RED)

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

    def on_option_selected(self, option):
        return MagazineOptionsHandler(engine=self.engine, magazine=option)


class CraftingEventHandler(UserOptionsEventHandler):
    def __init__(self, engine: Engine):
        super().__init__(engine=engine, options=['guns', 'gun parts', 'ammo', 'ammo parts', 'magazines', 'armour'],
                         title='crafting')

    def on_option_selected(self, option: str) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""

        if option == 'guns':
            return SelectItemToCraft(engine=self.engine, item_dict=deepcopy(guns_dict), title='gun crafting')

        """
        elif option == 'gun parts':
            return SelectItemToCraft(engine=self.engine, item_dict=, title='gun part crafting')

        elif option == 'ammo':
            return SelectItemToCraft(engine=self.engine, item_dict=bullet_crafting_dict, title='ammo crafting')

        elif option == 'ammo parts':
            return SelectItemToCraft(engine=self.engine, item_dict=, title='ammo part crafting')

        elif option == 'magazines':
            return SelectItemToCraft(engine=self.engine, item_dict=magazine_crafting_dict, title='magazine crafting')

        elif option == 'armour':
            return SelectItemToCraft(engine=self.engine, item_dict=, title='armour crafting')
        """


class SelectItemToCraft(UserOptionsWithPages):
    def __init__(self, engine: Engine, title: str, item_dict: dict):
        super().__init__(engine=engine, options=list(item_dict.keys()), page=0, title=title)
        self.item_dict = item_dict

    def on_option_selected(self, option):

        # dictionary has parts list, can proceed with creating item
        if 'required parts' in list(self.item_dict[option].keys()):
            part_dict = {}

            available_compatible_parts = []

            for part in self.item_dict[option]["compatible parts"]:
                for item in self.engine.player.inventory.items:
                    if isinstance(item.usable_properties, ComponentPart):
                        if item.usable_properties.part_type == part:
                            available_compatible_parts.append(part)

            # all required and compatible parts
            parts = self.item_dict[option]["required parts"] + available_compatible_parts

            # adds all required and compatible parts to the dictionary and sets
            # their value to None before player selects
            for part in parts:
                part_dict[part] = None
            return CraftItem(engine=self.engine, item_to_craft=option, current_part_index=0, parts=parts,
                             item_dict=self.item_dict)

        # dictionary selected does not have parts list
        else:
            return SelectItemToCraft(engine=self.engine, title=option, item_dict=self.item_dict[option])


class CraftItem(UserOptionsWithPages):
    def __init__(self, engine: Engine, item_to_craft: str, current_part_index: int, parts: list, item_dict: dict):

        self.item_name = item_to_craft
        self.item_to_craft = item_dict[item_to_craft]

        # all parts with their values
        self.item_dict = item_dict

        # all part keys in list format
        self.parts = parts

        # index of current part to be selected set to first part
        self.current_part_selection = current_part_index

        title = self.item_dict[item_to_craft]["parts names"][current_part_index]

        # parts of a given type available in inventory
        options = []

        # if part is not required, gives the option to select none
        if self.parts[self.current_part_selection] in self.item_dict[self.item_name]["compatible parts"]:
            options.append('none')

        for item in engine.player.inventory.items:
            if isinstance(item.usable_properties, ComponentPart):
                if item.usable_properties.part_type == self.parts[self.current_part_selection]:
                    options.append(item)

        super().__init__(engine=engine, options=options, page=0, title=title)

    def on_option_selected(self, option):

        if not option == 'none':
            # sets part in part dict to be the selected part
            self.item_dict[self.parts[self.current_part_selection]] = option

        if self.parts[self.current_part_selection] == self.parts[-1]:
            item = self.item_dict[self.item_name]['item']

            for key, value in self.item_dict.items():
                if value is not None:
                    if value in self.engine.player.inventory.items:
                        self.engine.player.inventory.items.remove(value)
                    setattr(item.usable_properties.parts, key, value)

            item.usable_properties.parts.update_partlist()
            item.parent = self.engine.player.inventory
            self.engine.player.inventory.items.append(item)

            turns_taken = 0
            while turns_taken < 5:
                turns_taken += 1
                self.engine.handle_enemy_turns()
            return MainGameEventHandler(engine=self.engine)

        else:
            self.current_part_selection += 1
            return CraftItem(engine=self.engine, current_part_index=self.current_part_selection,
                             item_to_craft=self.item_name, parts=self.parts, item_dict=self.item_dict)


class InspectItemViewer(AskUserEventHandler):

    def __init__(self, engine, item):
        super().__init__(engine=engine)

        self.TITLE = item.name
        self.description = item.description

        item_info = {
            "description": item.description,
            "weight": item.weight,
        }

        if isinstance(item.usable_properties, Weapon):

            weapon_info = {
                "damage": item.usable_properties.base_meat_damage,
                "armour damage": item.usable_properties.base_armour_damage,
                "accuracy": item.usable_properties.base_accuracy,
                "equip time": item.usable_properties.equip_time,
            }

            item_info.update(weapon_info)

            if isinstance(item.usable_properties, Gun):

                fire_modes = ""

                for key, value in item.usable_properties.fire_modes.items():
                    if key == "single shot":
                        fire_modes += f"single shot,"
                    else:
                        fire_modes += f"{key} - {value}RPM,"

                part_str = ""
                for part in item.usable_properties.parts.part_list:
                    part_str += f"{part.name}, "

                gun_info = {
                    "damage": item.usable_properties.base_meat_damage,
                    "armour damage": item.usable_properties.base_armour_damage,
                    "effective short range accuracy": item.usable_properties.close_range_accuracy,
                    "effective range": item.usable_properties.range_accuracy_dropoff,
                    "equip time": item.usable_properties.equip_time,
                    "recoil": item.usable_properties.recoil,
                    "fire modes": fire_modes,
                    "shot sound radius": item.usable_properties.sound_radius,
                    "parts": part_str
                }

                item_info.update(gun_info)

                if isinstance(item.usable_properties, GunMagFed):

                    gun_info = {
                        "magazine type": item.usable_properties.compatible_magazine_type,
                    }

                    item_info.update(gun_info)

                for key, value in item.usable_properties.parts.__dict__.items():
                    if value in item.usable_properties.parts.part_list:
                        gun_info[key] = value.name

        if isinstance(item.usable_properties, Magazine):
            mag_info = {
                "magazine capacity": item.usable_properties.mag_capacity,
                "round type": item.usable_properties.compatible_bullet_type,
            }

            if not isinstance(item.usable_properties, GunIntegratedMag):
                item_info["magazine type"] = item.usable_properties.magazine_type
                item_info["magazine size"] = item.usable_properties.magazine_size

            item_info.update(mag_info)

        if isinstance(item.usable_properties, Wearable):
            armour_info = {
                "fits bodypart": item.usable_properties.fits_bodypart,
                "protection": item.usable_properties.protection,
                "large mag slots": item.usable_properties.large_mag_slots,
                "medium mag slots": item.usable_properties.medium_mag_slots,
                "small mag slots": item.usable_properties.small_mag_slots,
            }

            item_info.update(armour_info)

        if isinstance(item.usable_properties, Bullet):
            bullet_info = {
                "round type": item.usable_properties.bullet_type,
                "damage modifier": item.usable_properties.meat_damage_factor,
                "armour damage modifier": item.usable_properties.armour_damage_factor,
                "sound radius modifier": item.usable_properties.sound_modifier,
                "recoil modifier": item.usable_properties.recoil_modifier
            }

            item_info.update(bullet_info)

        # TODO: show part info for component parts / rework to make more general

        if isinstance(item.usable_properties, HealingConsumable):
            item_info["healing amount"] = item.usable_properties.amount

        self.item_info = item_info

    def on_render(self, console: tcod.Console, camera: Camera) -> None:
        super().on_render(console, camera)  # Draw the main state as the background.

        height = len(self.item_info) + 2

        for key, value in self.item_info.items():
            if len(key) + len(str(value)) + 3 > 35:
                height += ceil((len(key) + len(str(value))) / 35)

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
            wrapper = textwrap.TextWrapper(width=32 - len(key))
            word_list = wrapper.wrap(text=str(value))
            console.print(x=2, y=y, string=f"{key} - ", fg=colour.LIGHT_GREEN)
            for string in word_list:
                console.print(x=2 + len(key) + 3, y=y, string=string)
                y += 1
