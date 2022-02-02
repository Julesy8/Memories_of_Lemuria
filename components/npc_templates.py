from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from entity import Entity, Actor
    from engine import Engine
    from game_map import GameMap


class BaseComponent:
    parent: Entity  # Owning entity instance.

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        return self.gamemap.engine


class Fighter(BaseComponent):
    parent: Actor

    # basic class for entities that fight
    def __init__(self,
                 unarmed_meat_damage,
                 unarmed_armour_damage,
                 melee_accuracy: float = 1.0,
                 ranged_accuracy: float = 1.0,
                 ):

        # unarmed melee attack damage
        self.unarmed_meat_damage = unarmed_meat_damage
        self.unarmed_armour_damage = unarmed_armour_damage

        # the base accuracy of the etity. 1 by defualt.
        self.melee_accuracy = melee_accuracy
        self.ranged_accuracy = ranged_accuracy

        # accuracy prior to any status effects being applied
        self.melee_accuracy_original = melee_accuracy
        self.ranged_accuracy_original = ranged_accuracy
