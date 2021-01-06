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
                 melee_accuracy: int = 80,
                 ranged_accuracy: int = 80,
                 ):

        self.power = power
