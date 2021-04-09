from __future__ import annotations

from typing import Optional, TypeVar, TYPE_CHECKING, Union
import copy
import math

if TYPE_CHECKING:
    from game_map import GameMap
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
                 last_seen_x=None,
                 last_seen_y=None,
                 render_order: RenderOrder = RenderOrder.CORPSE,
                 active: bool = False,
                 seen: bool = False,

                 ):
        self.x = x
        self.y = y
        self.last_seen_x = last_seen_x
        self.last_seen_y = last_seen_y
        self.char = char
        self.hidden_char = char
        self.fg_colour = fg_colour
        self.bg_colour = bg_colour
        self.name = name
        self.blocks_movement = blocks_movement
        self.render_order = render_order
        self.active = active
        self.seen = seen
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


class Actor(Entity):
    def __init__(
            self,
            x: int,
            y: int,

            char: str,
            fg_colour,
            bg_colour,
            name: str,
            inventory: Inventory,
            ai,
            fighter,
            bodyparts,  # list of bodyparts belonging to the entity
            energy=100,
            attack_cost=100,
            move_cost=100,
            energy_regain=100,
            active_radius=10,
            player: bool = False,
            last_seen_x=None,
            last_seen_y=None,
            fears_death=True
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
            seen=False,
            active=False,
            last_seen_x=last_seen_x,
            last_seen_y=last_seen_y,
        )

        self.inventory = inventory
        self.inventory.parent = self
        self.ai = ai(self)
        self.fighter = fighter
        self.fighter.parent = self
        self.targeting = ['Body', 'Head', 'Arms', 'Legs']
        self.selected_target = self.targeting[0]
        self.player = player
        self.bodyparts = copy.deepcopy(bodyparts)
        self._energy = energy
        self.attack_cost = attack_cost
        self.move_cost = move_cost
        self.energy_regain = energy_regain
        self.max_energy = energy
        self.active_radius = active_radius
        self.fears_death = fears_death
        for bodypart in self.bodyparts:
            bodypart.owner_instance = self

    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)

    @property
    def energy(self) -> int:
        return self._energy

    @energy.setter
    def energy(self, value: int) -> None:
        self._energy = max(0, min(value, self.max_energy))


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
        consumable,
    ):
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

        self.consumable = consumable
        self.consumable.parent = self
