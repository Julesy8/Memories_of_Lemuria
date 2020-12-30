from __future__ import annotations

from engine import Engine
from entity import Entity, Actor
from render_order import RenderOrder
from input_handlers import GameOverEventHandler

class BaseComponent:
    entity: Entity  # Owning entity instance.

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine


class Fighter(BaseComponent):
    entity: Actor

    # basic class for entities that fight
    def __init__(self,

                 hp: int,
                 defence: int,

                 power: int = 0,
                 volume_blood: int = 100,
                 energy: int = 100,
                 move_cost:int = 100,
                 attack_cost:int = 100,
                 bleeds: bool = True,
                 ):

        self.max_hp = hp
        self._hp = hp
        self._defence = defence
        self.power = power
        self.max_volume_blood = volume_blood
        self.volume_blood = volume_blood
        self.max_energy = energy
        self.energy = energy
        self.move_cost = move_cost
        self.attack_cost = attack_cost
        self.bleeds = bleeds

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def defence(self) -> int:
        return self._defence

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.entity.ai:
            self.die()

    def die(self) -> None:
        if self.engine.player is self.entity:
            death_message = "You died!"
            self.engine.event_handler = GameOverEventHandler

        else:
            death_message = f"{self.entity.name} is dead!"

        self.entity.fg_colour = (191,0,0)
        self.entity.bg_colour = (255,255,255)
        self.entity.blocks_movement = False
        self.entity.ai = None
        self.entity.name = f"remains of {self.entity.name}"
        self.entity.render_order = RenderOrder.CORPSE

        print(death_message)

    @defence.setter
    def defence(self, value):
        self._defence = value