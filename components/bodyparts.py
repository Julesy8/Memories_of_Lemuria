from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from entity import Actor
from render_order import RenderOrder
import colour

if TYPE_CHECKING:
    from entity import Item
    from engine import Engine


class Bodypart:

    parent: Actor

    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 part_type: str,
                 base_chance_to_hit: int,  # base modifier of how likely the body part is to be hit when attacked
                 equipped: Optional[Item] = None,  # equipped item for the given body part
                 functional: bool = True,  # whether the body part should be working or not
                 vital: bool = False,  # whether when the body part gets destroyed, the entity should die
                 walking: bool = False,  # whether the body part is required for walking
                 grasping: bool = False,
                 ):

        self.max_hp = hp
        self._hp = hp
        self._defence = defence
        self.vital = vital
        self.walking = walking
        self.grasping = grasping
        self.equipped = equipped
        self.name = name
        self.type = part_type
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
            self.cripple()  # TODO: change how this works for implementation of crippling + limb destruction

            if self.vital:
                self.die()

    @defence.setter
    def defence(self, value):
        self._defence = value

    def die(self) -> None:

        self.parent.fg_colour = colour.WHITE
        self.parent.bg_colour = colour.LIGHT_RED
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE

        if self.parent.player:
            death_message = "You died!"
            death_message_colour = colour.MAGENTA

        else:
            death_message = f"{self.parent.name} is dead!"
            self.engine.player.level.add_xp(self.parent.level.xp_given)
            death_message_colour = colour.CYAN

        self.engine.message_log.add_message(death_message, death_message_colour)

    def cripple(self) -> None:
        self.functional = False
        self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} is destroyed!")

        if self.walking:

            total_legs = 0
            functional_legs = 0

            for parts in self.parent.bodyparts:
                if parts.walking:
                    total_legs += 1
                    if parts.functional:
                        functional_legs += 1

            if self.parent.moves_per_turn > 1:
                self.parent.moves_per_turn = 1

            if self.parent.move_interval == 1:
                self.parent.move_interval = 2

            if functional_legs == 0:
                self.parent.move_interval = 2 * self.parent.move_interval

        if self.grasping:

            total_arms = 0
            functional_arms = 0

            for parts in self.parent.bodyparts:
                if parts.grasping:
                    total_arms += 1
                    if parts.functional:
                        functional_arms += 1

            if self.parent.attacks_per_turn > 1:
                self.parent.attacks_per_turn = 1

            if self.parent.attack_interval == 1:
                self.parent.attack_interval = 2

            if functional_arms == 0:
                self.parent.attack_interval = 2 * self.parent.attack_interval

    def destroy(self):

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def restore(self):

        # restores original attack and movement stats
        self.parent.movement_and_attack.attack_interval = self.parent.movement_and_attack.attack_interval_original
        self.parent.movement_and_attack.attacks_per_turn = self.parent.movement_and_attack.attacks_per_turn_original
        self.parent.movement_and_attack.move_interval = self.parent.movement_and_attack.move_interval_original
        self.parent.movement_and_attack.moves_per_turn = self.parent.movement_and_attack.moves_per_turn_original
