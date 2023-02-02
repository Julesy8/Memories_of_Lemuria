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
                 #faction_allegiance: tuple,
                 unarmed_ap_cost: int = 100,
                 move_ap_cost: int = 100,
                 ap: int = 100,
                 ap_per_turn: int = 100,
                 melee_accuracy: float = 1.0,  # more = more accurate
                 ranged_accuracy: float = 1.0,  # less = more accurate
                 move_success_chance: float = 1.0,
                 responds_to_sound: bool = True,
                 ):

        self.target_actor = None
        self.previous_target_actor = None

        self.max_ap = ap
        self._ap = ap
        self.ap_per_turn = ap_per_turn

        self.unarmed_ap_cost = unarmed_ap_cost
        self.move_ap_cost = move_ap_cost
        self.move_ap_original = move_ap_cost

        self._action_ap_modifier = 1.0
        self.ap_per_turn_modifier = 1.0

        # unarmed melee attack damage
        self.unarmed_meat_damage = unarmed_meat_damage
        self.unarmed_armour_damage = unarmed_armour_damage

        # the base accuracy of the entity. 1 by defualt.
        self.melee_accuracy = melee_accuracy
        self._ranged_accuracy = ranged_accuracy

        # accuracy prior to any status effects being applied
        self.melee_accuracy_original = melee_accuracy
        self.ranged_accuracy_original = ranged_accuracy

        # move success chance changes when limb crippled - i.e. chance to fail moving when leg crippled
        self.move_success_original = move_success_chance
        self.move_success_chance = move_success_chance

        self.style_range_accuracy = 1.0
        self.style_action_ap = 1.0

        # whether entity paths towards gunshot sounds
        self.responds_to_sound = responds_to_sound

        # allegiance of the entity. hostile to entities of different factions.
        #self.faction_allegiance = faction_allegiance

    @property
    def ap(self) -> int:
        return self._ap

    @property
    def attack_ap_modifier(self) -> float:
        return self.action_ap_modifier

    @property
    def ranged_accuracy(self) -> float:
        return self._ranged_accuracy * self.style_range_accuracy

    @property
    def action_ap_modifier(self) -> float:
        return self._action_ap_modifier * self.style_action_ap

    @ranged_accuracy.setter
    def ranged_accuracy(self, value: float) -> None:
        self._ranged_accuracy = value

    @action_ap_modifier.setter
    def action_ap_modifier(self, value: float) -> None:
        self._action_ap_modifier = value

    @ap.setter
    def ap(self, value: int) -> None:
        self._ap = min(value, self.max_ap)


class GunFighter(Fighter):
    def __init__(self,
                 unarmed_meat_damage,
                 unarmed_armour_damage,
                 unarmed_ap_cost: int = 100,
                 move_ap_cost: int = 100,
                 ap: int = 100,
                 ap_per_turn: int = 100,
                 melee_accuracy: float = 1.0,
                 ranged_accuracy: float = 1.0,
                 move_success_chance: float = 1.0,
                 responds_to_sound: bool = True,
                 automatic_fire_duration: float = 0.5
                 ):

        # how long (in seconds) an automatic burst of fire should last
        self.automatic_fire_duration = automatic_fire_duration

        super().__init__(unarmed_meat_damage, unarmed_armour_damage, unarmed_ap_cost, move_ap_cost, ap, ap_per_turn,
                         melee_accuracy, ranged_accuracy, move_success_chance, responds_to_sound,)

    def attack_style_precision(self):
        self.style_range_accuracy = 0.7
        self.automatic_fire_duration = 0.2
        self.style_action_ap = 1.3

    def attack_style_cqc(self):
        self.style_range_accuracy = 1.3
        self.automatic_fire_duration = 0.7
        self.style_action_ap = 0.7

    def attack_style_measured(self):
        self.style_range_accuracy = 1.0
        self.automatic_fire_duration = 0.5
        self.style_action_ap = 1.0
