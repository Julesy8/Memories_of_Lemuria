from __future__ import annotations

from engine import Engine
from entity import Entity, Actor


class BaseComponent:
    entity: Entity  # Owning entity instance.

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine


class Fighter(BaseComponent):
    entity: Actor

    # basic class for entities that fight
    def __init__(self,
                 power: int = 0,
                 melee_accuracy: float = 0.9,
                 ranged_accuracy: float = 0.9,
                 ):

        self.power = power
        self.melee_accuracy = melee_accuracy
        self.ranged_accuracy = ranged_accuracy
