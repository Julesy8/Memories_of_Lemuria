from __future__ import annotations

from typing import Optional, TypeVar, TYPE_CHECKING, Type
import copy
import math

if TYPE_CHECKING:
    from game_map import GameMap

from render_order import RenderOrder

T = TypeVar("T", bound="Entity")


class Entity:  # generic entity

    gamemap: GameMap

    def __init__(self,
                 x: int,
                 y: int,
                 char: str,
                 fg_colour,
                 bg_colour,
                 name: str,
                 blocks_movement=False,
                 gamemap: Optional[GameMap] = None,
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
        self.blocks_movement = blocks_movement
        self.render_order = render_order
        self.active = active
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
            x: int,
            y: int,
            char: str,
            fg_colour,
            bg_colour,
            name: str,
            ai,
            fighter,
            bodyparts,  # list of bodyparts belonging to the entity
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
        self.fighter.entity = self
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
        for bodypart in self.bodyparts:
            bodypart.owner_instance = self

    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)
