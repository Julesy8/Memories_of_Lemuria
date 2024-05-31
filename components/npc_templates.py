from __future__ import annotations

from typing import TYPE_CHECKING
from copy import deepcopy, copy
from random import choices, randint, choice
# from pydantic.utils import deep_update

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
                 # faction_allegiance: tuple,
                 item_drops: dict,
                 weapons: dict,
                 bodyarmour: dict,
                 helmet: dict,
                 spawn_group_amount: int,
                 unarmed_ap_cost: int = 100,
                 move_ap_cost: int = 100,
                 ap: int = 100,
                 ap_per_turn: int = 100,
                 melee_accuracy: float = 0.5,  # more = more accurate
                 ranged_accuracy: float = 8.0,  # less = more accurate
                 move_success_chance: float = 1.0,
                 responds_to_sound: bool = True,
                 fears_death=True,
                 description: str = '',
                 active: bool = False
                 ):

        self.target_actor = None

        self.previous_target_actor = None
        self.previously_targeted_part = None

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

        # whether entity paths towards gunshot sounds
        self.responds_to_sound = responds_to_sound

        self.active = active
        self.item_drops = item_drops
        self.weapons = weapons
        self.bodyarmour = bodyarmour
        self.helmet = helmet
        self.spawn_group_amount = spawn_group_amount
        self.fears_death = fears_death
        self.fleeing_turns = 0
        self.has_fled_death = False
        self.description = description
        self.turns_attack_inactive = 0
        self.turns_move_inactive = 0

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
        return self._action_ap_modifier

    @ranged_accuracy.setter
    def ranged_accuracy(self, value: float) -> None:
        self._ranged_accuracy = value

    @action_ap_modifier.setter
    def action_ap_modifier(self, value: float) -> None:
        self._action_ap_modifier = value

    @ap.setter
    def ap(self, value: int) -> None:
        self._ap = min(value, self.max_ap)

    def give_weapon(self, current_level: int):

        # equips fighter with weapons
        try:

            if len(self.weapons[current_level].keys()) > 0:
                gun = deepcopy(choices(population=list(self.weapons[current_level].keys()),
                                       weights=list(self.weapons[current_level].values()),
                                       k=1)[0])
                held_weapon = deepcopy(gun)

                if self.parent.player:
                    held_weapon = held_weapon.update_properties(current_level, random_condition=False)
                else:
                    held_weapon = held_weapon.update_properties(current_level)

                weapon_properties = held_weapon.usable_properties

                if weapon_properties.chambered_bullet is None:
                    if hasattr(weapon_properties, 'compatible_magazine_type'):
                        bullets = copy(weapon_properties.loaded_magazine.magazine[0].parent)
                    else:
                        bullets = copy(weapon_properties.magazine[0].parent)
                else:
                    bullets = copy(weapon_properties.chambered_bullet.parent)

                amount = randint(10, 20)
                if amount > 0:
                    bullets.stacking.stack_size = amount
                    self.parent.inventory.add_to_inventory(item=bullets, item_container=None, amount=amount)

                # adds clips to inventory and loads them
                if hasattr(weapon_properties, 'compatible_clip'):
                    compatible_clip_type = weapon_properties.compatible_clip
                    compatible_clips = copy(gun.clip)
                    if compatible_clips is not None:
                        if isinstance(gun.clip, dict):

                            for clip in gun.clip.keys():
                                if clip.magazine_type != compatible_clip_type:
                                    compatible_clips.update({clip: gun.magazine[clip]})
                                    del compatible_clips[clip]

                            # randomly selects clip
                            clip = choices(population=list(compatible_clips.keys()),
                                           weights=list(compatible_clips.values()), k=1)[0]

                            for y in range(randint(0, 2)):
                                clip_copy = deepcopy(clip.parent)
                                clip_copy.load_magazine(entity=self.parent, ammo=weapon_properties.chambered_bullet,
                                                        load_amount=(randint(1, clip.mag_capacity)))
                                self.parent.inventory.add_to_inventory(item=clip_copy.parent,
                                                                       item_container=None, amount=1)
                        else:
                            clip = gun.clip
                            for y in range(randint(0, 2)):
                                clip_copy = deepcopy(clip)
                                clip_copy.usable_properties.load_magazine(entity=self.parent,
                                                                          ammo=weapon_properties.chambered_bullet,
                                                                          load_amount=(
                                                                              randint(
                                                                                  1,
                                                                                  clip_copy.usable_properties.
                                                                                  mag_capacity)))
                                self.parent.inventory.add_to_inventory(item=clip_copy, item_container=None, amount=1)

                # adds magazines to inventory and loads them

                if hasattr(weapon_properties, 'compatible_magazine_type'):

                    # if weapon can take multiple types of magazines, selects one
                    if len(weapon_properties.compatible_magazine_type) > 0:
                        compatible_magazine_type = choice(weapon_properties.compatible_magazine_type)
                    else:
                        compatible_magazine_type = weapon_properties.compatible_magazine_type[0]

                    compatible_magazines = copy(gun.magazine)
                    if compatible_magazines is not None:
                        if isinstance(gun.magazine, dict):
                            for magazine in gun.magazine.keys():
                                if magazine.usable_properties.magazine_type != compatible_magazine_type:
                                    compatible_magazines.update({magazine: gun.magazine[magazine]})

                                    del compatible_magazines[magazine]

                            # randomly selects magazine
                            if isinstance(list(compatible_magazines.values())[0], tuple):
                                magazine_weights = []
                                for value in compatible_magazines.values():
                                    try:
                                        magazine_weights.append(value[current_level])
                                    except IndexError:
                                        magazine_weights.append(value[int(len(value) - 1)])

                                magazine = choices(population=list(compatible_magazines.keys()),
                                                   weights=magazine_weights, k=1)[0]

                            else:
                                magazine = choices(population=list(compatible_magazines.keys()),
                                                   weights=list(compatible_magazines.values()), k=1)[0]

                            for y in range(randint(0, 2)):
                                mag_copy = deepcopy(magazine)
                                (mag_copy.usable_properties.
                                 load_magazine(entity=self.parent,
                                               ammo=weapon_properties.chambered_bullet,
                                               load_amount=(randint(1, mag_copy.usable_properties.mag_capacity))))
                                self.parent.inventory.add_to_inventory(item=mag_copy, item_container=None, amount=1)
                        else:
                            magazine = gun.magazine
                            for y in range(randint(0, 2)):
                                mag_copy = deepcopy(magazine)
                                (mag_copy.usable_properties.
                                 load_magazine(entity=self.parent, ammo=weapon_properties.chambered_bullet,
                                               load_amount=(randint(1, mag_copy.
                                                                    usable_properties.mag_capacity))))
                                self.parent.inventory.add_to_inventory(item=mag_copy, item_container=None, amount=1)

                self.parent.inventory.held = held_weapon
                self.parent.inventory.primary_weapon = held_weapon
                self.parent.inventory.held.usable_properties.parent = self.parent.inventory.held
                self.parent.inventory.held.parent = self.parent.inventory

        except KeyError:
            return

    def give_armour(self, current_level: int):

        helmet = None
        bodyarmour = None

        try:
            if len(self.helmet[current_level].keys()) > 0:
                helmet = deepcopy(choices(population=list(self.helmet[current_level].keys()),
                                          weights=list(self.helmet[current_level].values()),
                                          k=1)[0])

            if len(self.bodyarmour[current_level].keys()) > 0:
                bodyarmour = deepcopy(choices(population=list(self.bodyarmour[current_level].keys()),
                                              weights=list(self.bodyarmour[current_level].values()),
                                              k=1)[0])

            if bodyarmour is not None:
                self.parent.inventory.small_mag_capacity += bodyarmour.usable_properties.small_mag_slots
                self.parent.inventory.medium_mag_capacity += bodyarmour.usable_properties.medium_mag_slots
                self.parent.inventory.large_mag_capacity += bodyarmour.usable_properties.large_mag_slots

            for armour in (helmet, bodyarmour):
                if armour is not None:
                    for bodypart in self.parent.bodyparts:
                        if bodypart.part_type == armour.usable_properties.fits_bodypart:
                            bodypart.equipped = armour.usable_properties
        except KeyError:
            return

class MeleeFighter(Fighter):
    def __init__(self,
                 unarmed_meat_damage,
                 unarmed_armour_damage,
                 # faction_allegiance: tuple,
                 item_drops: dict,
                 weapons: dict,
                 bodyarmour: dict,
                 helmet: dict,
                 spawn_group_amount: int,
                 unarmed_ap_cost: int = 100,
                 move_ap_cost: int = 100,
                 ap: int = 100,
                 ap_per_turn: int = 100,
                 melee_accuracy: float = 0.5,  # more = more accurate
                 ranged_accuracy: float = 8.0,  # less = more accurate
                 move_success_chance: float = 1.0,
                 responds_to_sound: bool = True,
                 fears_death=True,
                 description: str = '',
                 active: bool = False
                 ):
        super().__init__(unarmed_meat_damage, unarmed_armour_damage, item_drops, weapons, bodyarmour, helmet,
                         spawn_group_amount, unarmed_ap_cost, move_ap_cost, ap, ap_per_turn, melee_accuracy,
                         ranged_accuracy, move_success_chance, responds_to_sound, fears_death, description, active)

    def give_weapon(self, current_level: int):

        try:

            if len(self.weapons[current_level].keys()) > 0:
                weapon = deepcopy(choices(population=list(self.weapons[current_level].keys()),
                                       weights=list(self.weapons[current_level].values()),
                                       k=1)[0])
                held_weapon = deepcopy(weapon)

                self.parent.inventory.held = held_weapon
                self.parent.inventory.primary_weapon = held_weapon
                self.parent.inventory.held.usable_properties.parent = self.parent.inventory.held
                self.parent.inventory.held.parent = self.parent.inventory

        except KeyError:
            return
class GunFighter(Fighter):
    def __init__(self,
                 unarmed_meat_damage,
                 unarmed_armour_damage,
                 item_drops: dict,
                 weapons: dict,
                 bodyarmour: dict,
                 helmet: dict,
                 spawn_group_amount: int,
                 unarmed_ap_cost: int = 100,
                 move_ap_cost: int = 100,
                 ap: int = 100,
                 ap_per_turn: int = 100,
                 melee_accuracy: float = 0.5,
                 ranged_accuracy: float = 10.0,
                 move_success_chance: float = 1.0,
                 responds_to_sound: bool = True,
                 automatic_fire_duration: float = 0.5,
                 felt_recoil: float = 1.0,
                 target_acquisition_ap: float = 2.0,
                 firing_ap_cost: float = 1.0,
                 ap_distance_cost_modifier: float = 1.5,
                 fears_death=True,
                 description: str = '',
                 active=False
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
        self.attack_style = ''

        super().__init__(unarmed_meat_damage, unarmed_armour_damage, item_drops, weapons, bodyarmour, helmet,
                         spawn_group_amount, unarmed_ap_cost, move_ap_cost, ap, ap_per_turn, melee_accuracy,
                         ranged_accuracy, move_success_chance, responds_to_sound, fears_death, description, active)

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
        self.attack_style = 'PRECISION'
        self.style_range_accuracy = 0.5
        self.automatic_fire_duration = 0.2

    def attack_style_cqc(self):
        self.attack_style = 'CLOSE QUARTERS'
        self.style_range_accuracy = 1.3
        self.automatic_fire_duration = 0.5

    def attack_style_measured(self):
        self.attack_style = 'MEASURED'
        self.style_range_accuracy = 1.0
        self.automatic_fire_duration = 0.35


class PlayerFighter(GunFighter):
    def __init__(self,
                 unarmed_meat_damage,
                 unarmed_armour_damage,
                 item_drops: dict,
                 weapons: dict,
                 bodyarmour: dict,
                 helmet: dict,
                 spawn_group_amount: int,
                 unarmed_ap_cost: int = 100,
                 move_ap_cost: int = 100,
                 ap: int = 100,
                 ap_per_turn: int = 100,
                 melee_accuracy: float = 0.5,
                 ranged_accuracy: float = 8.0,
                 move_success_chance: float = 1.0,
                 responds_to_sound: bool = True,
                 automatic_fire_duration: float = 0.5,
                 felt_recoil: float = 1.0,
                 target_acquisition_ap: float = 2.0,
                 firing_ap_cost: float = 1.0,
                 ap_distance_cost_modifier: float = 1.5,
                 skill_recoil_control: int = 0,
                 skill_marksmanship: int = 0,
                 skill_pistol_proficiency: int = 0,
                 skill_smg_proficiency: int = 0,
                 skill_rifle_proficiency: int = 0,
                 skill_revolver_proficiency: int = 0,
                 skill_sa_rifle_proficiency: int = 0,
                 skill_sa_pistol_proficiency: int = 0,
                 skill_pumpaction_proficiency: int = 0,
                 skill_breakaction_proficiency: int = 0,
                 skill_bolt_action_proficiency: int = 0,
                 skill_belt_fed_proficiency: int = 0,
                 fears_death=True,
                 description: str = '',
                 active=True
                 ):
        self._skill_recoil_control = skill_recoil_control
        self._skill_marksmanship = skill_marksmanship
        self._skill_pistol_proficiency = skill_pistol_proficiency
        self._skill_smg_proficiency = skill_smg_proficiency
        self._skill_rifle_proficiency = skill_rifle_proficiency
        self._skill_revolver_proficiency = skill_revolver_proficiency
        self._skill_sa_rifle_proficiency = skill_sa_rifle_proficiency
        self._skill_sa_pistol_proficiency = skill_sa_pistol_proficiency
        self._skill_pumpaction_proficiency = skill_pumpaction_proficiency
        self._skill_breakaction_proficiency = skill_breakaction_proficiency
        self._skill_bolt_action_proficiency = skill_bolt_action_proficiency
        self._skill_belt_fed_proficiency = skill_belt_fed_proficiency
        self.visible_tiles = None

        super().__init__(unarmed_meat_damage, unarmed_armour_damage, item_drops, weapons, bodyarmour, helmet,
                         spawn_group_amount, unarmed_ap_cost, move_ap_cost, ap, ap_per_turn, melee_accuracy,
                         ranged_accuracy, move_success_chance, responds_to_sound, automatic_fire_duration, felt_recoil,
                         target_acquisition_ap, firing_ap_cost, ap_distance_cost_modifier, fears_death, description,
                         active)

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
    def skill_recoil_control(self):
        return self._skill_recoil_control

    @skill_recoil_control.setter
    def skill_recoil_control(self, value):
        self._skill_recoil_control = min(value, 1000)

    @property
    def skill_revolver_proficiency(self):
        return self._skill_recoil_control

    @skill_revolver_proficiency.setter
    def skill_revolver_proficiency(self, value):
        self._skill_revolver_proficiency = min(value, 1000)

    @property
    def skill_bolt_action_proficiency(self):
        return self._skill_bolt_action_proficiency

    @skill_bolt_action_proficiency.setter
    def skill_bolt_action_proficiency(self, value):
        self._skill_bolt_action_proficiency = min(value, 1000)

    @property
    def skill_belt_fed_proficiency(self):
        return self._skill_belt_fed_proficiency

    @skill_belt_fed_proficiency.setter
    def skill_belt_fed_proficiency(self, value):
        self._skill_belt_fed_proficiency = min(value, 1000)

    @property
    def skill_sa_rifle_proficiency(self):
        return self._skill_sa_rifle_proficiency

    @skill_sa_rifle_proficiency.setter
    def skill_sa_rifle_proficiency(self, value):
        self._skill_sa_rifle_proficiency = min(value, 1000)

    @property
    def skill_sa_pistol_proficiency(self):
        return self._skill_sa_pistol_proficiency

    @skill_sa_pistol_proficiency.setter
    def skill_sa_pistol_proficiency(self, value):
        self._skill_sa_pistol_proficiency = min(value, 1000)

    @property
    def skill_pumpaction_proficiency(self):
        return self._skill_pumpaction_proficiency

    @skill_pumpaction_proficiency.setter
    def skill_pumpaction_proficiency(self, value):
        self._skill_pumpaction_proficiency = min(value, 1000)

    @property
    def skill_breakaction_proficiency(self):
        return self._skill_breakaction_proficiency

    @skill_breakaction_proficiency.setter
    def skill_breakaction_proficiency(self, value):
        self._skill_breakaction_proficiency = min(value, 1000)

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
