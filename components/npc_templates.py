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
                 volume_blood: int = 100,
                 bleeds: bool = True,
                 ):

        self.power = power
        self.max_volume_blood = volume_blood
        self.volume_blood = volume_blood
        self.bleeds = bleeds
