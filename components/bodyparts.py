from __future__ import annotations

from entity import Actor
from render_order import RenderOrder
from input_handlers import GameOverEventHandler
from engine import Engine
import colour


class Bodypart:

    parent: Actor

    def __init__(self,
                 hp: int,
                 defence: int,
                 vital: bool,              # whether when the body part gets destroyed, the entity should die
                 walking: bool,            # whether the body part is required for walking
                 grasping: bool,
                 name: str,
                 type: str,
                 base_chance_to_hit: int,  # base modifier of how likely the body part is to be hit when attacked
                 functional: bool = True   # whether the body part should be working or not
                 ):

        self.max_hp = hp
        self._hp = hp
        self._defence = defence
        self.vital = vital
        self.walking = walking
        self.grasping = grasping
        self.name = name
        self.type = type
        self.base_chance_to_hit = base_chance_to_hit
        self.functional = functional

    @property
    def engine(self) -> Engine:
        return self.parent.gamemap.engine

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def defence(self) -> int:
        return self._defence

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))

        if self._hp == 0 and self.parent.ai and self.functional:
            self.destroy()

            if self.vital:
                self.die()

    @defence.setter
    def defence(self, value):
        self._defence = value

    def die(self) -> None:

        if self.parent.player:
            death_message = "You died!"
            death_message_colour = colour.MAGENTA
            self.engine.event_handler = GameOverEventHandler(self.engine)

        else:
            death_message = f"{self.parent.name} is dead!"
            death_message_colour = colour.CYAN
            self.parent.fg_colour = colour.WHITE
            self.parent.bg_colour = colour.LIGHT_RED
            self.parent.blocks_movement = False
            self.parent.ai = None
            self.parent.name = f"remains of {self.parent.name}"
            self.parent.render_order = RenderOrder.CORPSE

        self.engine.message_log.add_message(death_message, death_message_colour)

    def destroy(self) -> None:
        self.functional = False
        self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} is destroyed!")

        '''
        if self.walking:

            total_legs = 1
            functional_legs = 1

            for parts in self.owner_instance.bodyparts:
                if parts.walking:
                    total_legs += 1
                    if parts.functional:
                        functional_legs += 1
            movement_penalty = (total_legs - functional_legs) / functional_legs

            if self.owner_instance.moves_per_turn > 1:
                self.owner_instance.moves_per_turn = math.ceil(movement_penalty * self.owner_instance.moves_per_turn)

            else:
                self.owner_instance.move_interval = math.ceil(movement_penalty * self.owner_instance.move_interval)
        '''

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def cripple(self) -> None:
        pass

    def restore(self):
        pass
