from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entity import Actor
    from engine import Engine

from render_order import RenderOrder
from input_handlers import GameOverEventHandler
import colour


# in the future split into separate classes for distinct bodyparts
class Bodypart:

    entity: Actor

    def __init__(self,
                 owner_instance,           # the entity that 'owns' the body part
                 hp: int,
                 defence: int,
                 vital: bool,              # whether when the body part gets destroyed, the entity should die
                 walking: bool,            # whether the body part is required for walking
                 flying: bool,
                 grasping: bool,
                 name: str,
                 type: str,                # can be 'Body', 'Head', 'Arms' or 'Legs'
                 base_chance_to_hit: int,  # base modifier of how likely the body part is to be hit when attacked
                 functional: bool = True   # whether the body part should be working or not
                 ):

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

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def take_damage(self, amount: int) -> None:
        self.hp -= amount

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

        elif self._hp == 0 and self.owner_instance.ai and self.vital is False:
            # this is broke
            self.destroy()

    @defence.setter
    def defence(self, value):
        self._defence = value

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
            self.owner_instance.hidden_char = '%'
            self.owner_instance.blocks_movement = False
            self.owner_instance.ai = None
            self.owner_instance.name = f"remains of {self.owner_instance.name}"
            self.owner_instance.render_order = RenderOrder.CORPSE

        self.engine.message_log.add_message(death_message, death_message_colour)

    def destroy(self) -> None:
        if self.functional:
            self.functional = False
            self.engine.message_log.add_message(f"{self.owner_instance.name}'s {self.name} is destroyed!")
