from __future__ import annotations

from engine import Engine
from entity import Entity, Actor

from components.bodyparts import Bodypart

class BaseComponent:
    entity: Entity  # Owning entity instance.

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine


class Fighter(BaseComponent):
    # basic class for entities that fight
    def __init__(self,
                 power: int = 0,
                 volume_blood: int = 100,
                 energy: int = 100,
                 move_cost:int = 100,
                 attack_cost:int = 100,
                 bleeds: bool = True,
                 ):

        self.power = power
        self.max_volume_blood = volume_blood
        self.volume_blood = volume_blood
        self.max_energy = energy
        self.energy = energy
        self.move_cost = move_cost
        self.attack_cost = attack_cost
        self.bleeds = bleeds

class Basic(Actor):
    # basic body class for normal bipeds/quadropeds
    def __init__(self,
                 x: int,
                 y: int,
                 char: str,
                 fg_colour,
                 bg_colour,
                 name: str,
                 head: Bodypart,
                 body: Bodypart,
                 limb_1: Bodypart,
                 limb_2: Bodypart,
                 limb_3: Bodypart,
                 limb_4: Bodypart,
                 fighter: Fighter = None,
                 ai=None
                 ):
        self.head = head
        self.body = body
        self.limb_1 = limb_1
        self.limb_2 = limb_2
        self.limb_3 = limb_3
        self.limb_4 = limb_4

        self.x = x
        self.y = y
        self.char = char
        self.fg_colour = fg_colour
        self.bg_colour = bg_colour
        self.name = name
        self.fighter = fighter
        self.ai = ai
        super().__init__(x,
                         y,
                         char,
                         fg_colour,
                         bg_colour,
                         name,
                         fighter=fighter,
                         ai=ai
                         )
