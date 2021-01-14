from __future__ import annotations

from entity import Actor
from render_order import RenderOrder
from input_handlers import GameOverEventHandler
from engine import Engine
import colour

class Bodypart:  # a basic bodypart

    entity: Actor
    def __init__(self,
                 owner_instance,
                 hp: int,
                 defence: int,
                 vital: bool,
                 walking: bool,
                 flying:bool,
                 grasping: bool,
                 name: str,
                 type: str, # can be 'Body', 'Head', 'Arms' or 'Legs'
                 base_chance_to_hit: int,
                functional: bool = True):
        self.owner_instance = owner_instance
        self.max_hp = hp
        self._hp = hp
        self._defence = defence
        self.vital = vital
        self.walking = walking
        self.flying = flying
        self.grasping = grasping
        self.name = name
        self.type = type
        self.base_chance_to_hit = base_chance_to_hit
        self.functional = functional

    @property
    def engine(self) -> Engine:
        return self.owner_instance.gamemap.engine

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def defence(self) -> int:
        return self._defence

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.owner_instance.ai and self.vital:
            self.die()

        elif self._hp == 0 and self.owner_instance.ai and self.vital == False:
            self.destroy()

    def die(self) -> None:

        if self.owner_instance.player:
            death_message = "You died!"
            death_message_colour = colour.MAGENTA
            self.engine.event_handler = GameOverEventHandler(self.engine)

        else:
            death_message = f"{self.owner_instance.name} is dead!"
            death_message_colour = colour.CYAN
            self.owner_instance.fg_colour = colour.WHITE
            self.owner_instance.bg_colour = colour.LIGHT_RED
            self.owner_instance.blocks_movement = False
            self.owner_instance.ai = None
            self.owner_instance.name = f"remains of {self.owner_instance.name}"
            self.owner_instance.render_order = RenderOrder.CORPSE

        self.engine.message_log.add_message(death_message, death_message_colour)

    def destroy(self) -> None:
        if self.functional:
            self.functional = False
            self.engine.message_log.add_message(f"{self.owner_instance.name}'s {self.name} is destroyed!")

    @defence.setter
    def defence(self, value):
        self._defence = value
