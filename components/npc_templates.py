from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from entity import Entity, Actor
    from engine import Engine
    from game_map import GameMap


class BaseComponent:
    parent: Entity  # Owning entity instance.

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        return self.gamemap.engine


class Fighter(BaseComponent):
    parent: Actor

    # basic class for entities that fight
    def __init__(self,
                 unarmed_damage: int = 0,
                 melee_accuracy: float = 1.0,
                 ranged_accuracy: float = 1.0,
                 bleeds: bool = True,
                 ):

        # unarmed melee attack damage
        self.unarmed_damage = unarmed_damage

        # the base accuracy of the etity. 1 by defualt.
        self.melee_accuracy = melee_accuracy
        self.ranged_accuracy = ranged_accuracy

        # whether or not the entity bleeds
        self.bleeds = bleeds

        # TODO: make bleeding matter

        if self.bleeds is not None:
            self.blood = 100  # the amount of blood an entity has out of 100

        self.bleeding_turns: int = 0
