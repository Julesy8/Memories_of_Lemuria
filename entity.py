from __future__ import annotations

from typing import Optional, TypeVar, TYPE_CHECKING, Union, Type
from random import choice
import copy
import math

if TYPE_CHECKING:
    from game_map import GameMap
    from components.consumables import Usable
    from components.ai import BaseAI
    from components.inventory import Inventory

from render_order import RenderOrder

T = TypeVar("T", bound="Entity")


class Entity:  # generic entity

    parent: Union[GameMap, Inventory]

    def __init__(self,
                 x: int,
                 y: int,
                 char: str,
                 fg_colour: tuple[int, int, int],
                 name: str,
                 blocks_movement=False,
                 parent: Optional[GameMap] = None,
                 render_order: RenderOrder = RenderOrder.CORPSE,
                 ):

        self.x = x
        self.y = y
        self.char = char
        self.fg_colour = fg_colour
        self.name = name
        self.render_order = render_order
        self.blocks_movement = blocks_movement
        self.seen = False
        self.ghost_x = x
        self.ghost_y = y

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
            fg_colour: tuple[int, int, int],
            name: str,
            ai: Type[BaseAI],
            fighter,
            bodyparts: tuple,  # list of bodyparts belonging to the entity
            inventory: Inventory,
            bleeds=True,
            player: bool = False,
            speaks: bool = False,
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            fg_colour=fg_colour,
            name=name,
            blocks_movement=True,
            render_order=RenderOrder.ACTOR,
        )

        self.orientation = choice((0,  # east
                                   0.785,  # north east
                                   1.57,  # north
                                   2.356,  # north west
                                   3.141,  # west
                                   3.926,  # south west
                                   4.712,  # south
                                   5.497  # south east
                                   ))
        self.ai = ai(self)
        self.speaks = speaks
        self.bleeds = bleeds
        self.fighter = fighter
        self.fighter.parent = self
        self.player = player
        self.bodyparts = copy.deepcopy(bodyparts)
        self.inventory = inventory
        self.inventory.parent = self
        self.identifier: int = 0
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
            fg_colour: tuple[int, int, int],
            name: str = "<Unnamed>",
            weight: float,
            stacking: Optional[Stacking],
            usable_properties: Optional[Usable],
            description: str,
    ):
        self.weight = weight
        self.stacking = stacking

        self.usable_properties = usable_properties
        if usable_properties:
            self.usable_properties.parent = self

        self.description = description

        super().__init__(
            x=x,
            y=y,
            char=char,
            fg_colour=fg_colour,
            name=name,
            blocks_movement=False,
            render_order=RenderOrder.ITEM,
        )


class Stacking:  # class for stacks of items
    def __init__(self, stack_size, spawn_amount_min: int = 1, spawn_amount_max: int = 1):
        self.stack_size = stack_size
        self.spawn_amount_min = spawn_amount_min
        self.spawn_amount_max = spawn_amount_max
