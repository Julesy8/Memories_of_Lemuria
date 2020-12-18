from __future__ import annotations

from typing import Optional, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

from RenderOrder import RenderOrder
from random import randint

T = TypeVar("T", bound="Entity")

import copy
import math


class Entity:  # generic entity

    gamemap: GameMap

    def __init__(self,
                 x,
                 y,
                 char,
                 fg_colour,
                 bg_colour,
                 name,
                 blocks_movement=False,
                 gamemap: Optional[GameMap] = None,
                 render_order = RenderOrder.CORPSE):
        self.x = x
        self.y = y
        self.spawn_x = x
        self.spawn_y = y
        self.char = char
        self.fg_colour = fg_colour
        self.bg_colour = bg_colour
        self.name = name
        self.blocks_movement = blocks_movement
        self.render_order = render_order
        if gamemap:
            # If gamemap isn't provided now then it will be set later.
            self.gamemap = gamemap
            gamemap.entities.add(self)

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
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location.  Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "gamemap"):  # Possibly uninitialized.
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)

class Actor(Entity):
    def __init__(
        self,
        x,
        y,
        char,
        fg_colour,
        bg_colour,
        name,
        ai,
        fighter,
        bodyparts # list of bodyparts belonging to the entity
    ):
        self.identifier = randint(1,999)
        super().__init__(
            x=x,
            y=y,
            char=char,
            fg_colour=fg_colour,
            bg_colour=bg_colour,
            name=name + ' (' + str(self.identifier) + ')',
            # just gives the entity a random number its associated with so it can be easily identified
            blocks_movement=True,
        )

        self.ai = ai(self)
        self.fighter = fighter
        self.fighter.entity = self
        self.targeting = ['Body', 'Head', 'Arms', 'Legs']
        self.selected_target = self.targeting[0]
        self.bodyparts = bodyparts

    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)
