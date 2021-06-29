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
                 power: int = 0,
                 melee_accuracy: float = 0.9,
                 ranged_accuracy: float = 0.9,
                 ):

        self.power = power
        self.melee_accuracy = melee_accuracy
        self.ranged_accuracy = ranged_accuracy