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
                 automatic_fire_duration: float = 0.5,
                 felt_recoil: float = 1.0,
                 target_acquisition_ap: float = 1.0,
                 firing_ap_cost: float = 1.0,
                 ap_distance_cost_modifier: float = 1.0,
                 ):

        # how long (in seconds) an automatic burst of fire should last
        self.automatic_fire_duration = automatic_fire_duration
        self._felt_recoil = felt_recoil
        self._target_acquisition_ap = target_acquisition_ap
        self._firing_ap_cost = firing_ap_cost
        self._ap_distance_cost_modifier = ap_distance_cost_modifier

        self.felt_recoil_original = felt_recoil
        self.target_acquisition_ap_original = target_acquisition_ap
        self.firing_ap_cost_original = firing_ap_cost
        self.ap_distance_cost_modifier_original = ap_distance_cost_modifier

        super().__init__(unarmed_meat_damage, unarmed_armour_damage, unarmed_ap_cost, move_ap_cost, ap, ap_per_turn,
                         melee_accuracy, ranged_accuracy, move_success_chance, responds_to_sound,)

    @property
    def felt_recoil(self):
        return self._felt_recoil

    @property
    def target_acquisition_ap(self):
        return self._target_acquisition_ap

    @property
    def firing_ap_cost(self):
        return self._firing_ap_cost

    @property
    def ap_distance_cost_modifier(self):
        return self._ap_distance_cost_modifier

    @felt_recoil.setter
    def felt_recoil(self, value: float):
        self._felt_recoil = value

    @target_acquisition_ap.setter
    def target_acquisition_ap(self, value: float):
        self._target_acquisition_ap = value

    @firing_ap_cost.setter
    def firing_ap_cost(self, value: float):
        self._firing_ap_cost = value

    @ap_distance_cost_modifier.setter
    def ap_distance_cost_modifier(self, value: float):
        self._ap_distance_cost_modifier = value

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


class PlayerFighter(GunFighter):
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
                 automatic_fire_duration: float = 0.5,
                 felt_recoil: float = 1.0,
                 target_acquisition_ap: float = 1.0,
                 firing_ap_cost: float = 1.0,
                 ap_distance_cost_modifier: float = 1.0,
                 skill_marksmanship: int = 0,
                 skill_pistol_proficiency: int = 0,
                 skill_smg_proficiency: int = 0,
                 skill_rifle_proficiency: int = 0,
                 skill_bolt_action_proficiency: int = 0,
                 ):

        self._skill_marksmanship = skill_marksmanship
        self._skill_pistol_proficiency = skill_pistol_proficiency
        self._skill_smg_proficiency = skill_smg_proficiency
        self._skill_rifle_proficiency = skill_rifle_proficiency
        self._skill_bolt_action_proficiency = skill_bolt_action_proficiency

        super().__init__(unarmed_meat_damage, unarmed_armour_damage, unarmed_ap_cost, move_ap_cost, ap, ap_per_turn,
                         melee_accuracy, ranged_accuracy, move_success_chance, responds_to_sound,
                         automatic_fire_duration, felt_recoil, target_acquisition_ap, firing_ap_cost,
                         ap_distance_cost_modifier)

    @property
    def skill_marksmanship(self):
        return self._skill_marksmanship

    @skill_marksmanship.setter
    def skill_marksmanship(self, value):
        self._skill_marksmanship = min(value, 1000)

    @property
    def skill_pistol_proficiency(self):
        return self._skill_pistol_proficiency

    @skill_pistol_proficiency.setter
    def skill_pistol_proficiency(self, value):
        self._skill_pistol_proficiency = min(value, 1000)

    @property
    def skill_smg_proficiency(self):
        return self._skill_smg_proficiency

    @skill_smg_proficiency.setter
    def skill_smg_proficiency(self, value):
        self._skill_smg_proficiency = min(value, 1000)

    @property
    def skill_rifle_proficiency(self):
        return self._skill_rifle_proficiency

    @skill_rifle_proficiency.setter
    def skill_rifle_proficiency(self, value):
        self._skill_rifle_proficiency = min(value, 1000)

    @property
    def skill_bolt_action_proficiency(self):
        return self._skill_bolt_action_proficiency

    @skill_bolt_action_proficiency.setter
    def skill_bolt_action_proficiency(self, value):
        self._skill_bolt_action_proficiency = min(value, 1000)
