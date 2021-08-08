from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entity import Actor


class AttacksAndMovement:
    parent: Actor

    def __init__(self,
                 attack_interval: int = 0,
                 attacks_per_turn: int = 1,
                 move_interval: int = 0,
                 moves_per_turn: int = 1
                 ):

        # original values before changes occur i.e. crippled limbs
        self.attack_interval_original = attack_interval,
        self.attacks_per_turn_original = attacks_per_turn,
        self.move_interval_original = move_interval,
        self.moves_per_turn_original = moves_per_turn,

        self.attack_interval = attack_interval,  # how many turns the entity waits before attacking
        self.attacks_per_turn = attacks_per_turn,  # when the entity attacks, how many times?
        self.move_interval = move_interval,  # how many turns the entity waits before moving
        self.moves_per_turn = moves_per_turn,  # when the entity moves, how many times?
