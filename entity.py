from __future__ import annotations

from typing import Optional, Tuple, Type, TypeVar, TYPE_CHECKING, Union
import copy
import math

if TYPE_CHECKING:
    from game_map import GameMap
    from components.consumables import Consumable, Weapon, Wearable
    from components.inventory import Inventory

from render_order import RenderOrder

T = TypeVar("T", bound="Entity")


class Entity:  # generic entity

    parent: Union[GameMap, Inventory]

    def __init__(self,
                 x: int,
                 y: int,
                 char: str,
                 fg_colour,
                 bg_colour,
                 name: str,
                 blocks_movement=False,
                 parent: Optional[GameMap] = None,
                 render_order: RenderOrder = RenderOrder.CORPSE,
                 active: bool = False,
                 ):
        self.x = x
        self.y = y
        self.char = char
        self.hidden_char = char
        self.fg_colour = fg_colour
        self.bg_colour = bg_colour
        self.name = name
        self.render_order = render_order
        self.blocks_movement = blocks_movement
        self.active = active
        if parent:
            # If parent isn't provided now then it will be set later.
            self.parent = parent
            parent.entities.add(self)

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.parent = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location.  Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "parent"):  # Possibly uninitialized.
                if self.parent is self.gamemap:
                    self.gamemap.entities.remove(self)
            self.parent = gamemap
            gamemap.entities.add(self)

    def distance(self, x: int, y: int) -> float:
        """
        Return the distance between the current entity and the given (x, y) coordinate.
        """
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)


class Actor(Entity):
    def __init__(
            self,
            x: int,
            y: int,
            char: str,
            fg_colour,
            bg_colour,
            name: str,
            ai,
            fighter,
            bodyparts,  # list of bodyparts belonging to the entity
            inventory: Inventory,
            attack_interval=0,  # how many turns the entity waits before attacking
            attacks_per_turn=1,  # when the entity attacks, how many times?
            move_interval=0,  # how many turns the entity waits before moving
            moves_per_turn=1,  # when the entity moves, how many times?
            active_radius=10,
            player: bool = False,
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            fg_colour=fg_colour,
            bg_colour=bg_colour,
            name=name,
            blocks_movement=True,
            render_order=RenderOrder.ACTOR,
            active=False,
        )

        self.ai = ai(self)
        self.fighter = fighter
        self.fighter.parent = self
        self.targeting = ['Body', 'Head', 'Arms', 'Legs']
        self.selected_target = self.targeting[0]
        self.player = player
        self.bodyparts = copy.deepcopy(bodyparts)
        self.active_radius = active_radius
        self.turn_counter = 0
        self.last_move_turn = 0
        self.last_attack_turn = 0
        self.attack_interval = attack_interval
        self.attacks_per_turn = attacks_per_turn
        self.move_interval = move_interval
        self.moves_per_turn = moves_per_turn
        self.inventory = inventory
        self.inventory.parent = self
        for bodypart in self.bodyparts:
            bodypart.parent = self

    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)


class Item(Entity):
    def __init__(
        self,
        *,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        fg_colour,
        bg_colour,
        name: str = "<Unnamed>",
        weight: int,
        stacking: Optional[Stacking],
        consumable: Optional[Consumable],
        weapon: Optional[Weapon],
        wearable: Optional[Wearable]
    ):

        self.weight = weight
        self.stacking = stacking

        self.consumable = consumable
        if consumable:
            self.consumable.parent = self

        self.weapon = weapon
        if weapon:
            self.weapon.parent = self

        self.wearable = wearable
        if wearable:
            self.wearable.parent = self

        super().__init__(
            x=x,
            y=y,
            char=char,
            fg_colour=fg_colour,
            bg_colour=bg_colour,
            name=name,
            blocks_movement=False,
            render_order=RenderOrder.ITEM,
        )


class Stacking:  # class for stacks of items
    def __init__(self, stack_size):
        self.stack_size = stack_size
