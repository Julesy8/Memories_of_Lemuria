from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING
from math import ceil, atan2, sin, cos
from random import randint
from copy import deepcopy, copy

import colour
import exceptions
from random import choices
from exceptions import Impossible

if TYPE_CHECKING:
    from engine import Engine
    from entity import Actor, Entity, Item
    from components.consumables import Gun, GunMagFed, Magazine, Bullet, GunIntegratedMag, Weapon, MeleeWeapon, \
        DetachableMagazine, Clip, Wearable
    from components.bodyparts import Bodypart


class Action:
    def __init__(self, entity: Actor, handle_now: bool = False) -> None:
        self.handle_now = handle_now
        self.action_str = ''
        self.entity = entity
        self.queued = False

    @property
    def engine(self) -> Engine:
        """Return the engine this action belongs to."""
        return self.entity.gamemap.engine

    def action_viable(self) -> bool:
        return True

    def handle_action(self) -> None:
        ap_cost = self.calculate_ap_cost()

        action_viable = self.action_viable()

        if self.entity.ai is None:
            return

        if self.handle_now and action_viable:
            return self.perform()

        # checks if action is viable
        if not action_viable:
            self.entity.ai.queued_action = None
            if self.queued:
                # gives back remaining AP
                turns_remaining = ceil(abs(self.entity.fighter.ap / self.entity.fighter.ap_per_turn *
                                           self.entity.fighter.ap_per_turn_modifier))
                self.entity.fighter.ap += turns_remaining * self.entity.fighter.ap_per_turn * self.entity.fighter.ap_per_turn_modifier
            if self.entity.player:
                return self.engine.message_log.add_message(f"{self.entity.name}: action failed", colour.RED)

        # if entity has no AP, returns
        if not self.queued and self.entity.fighter.ap < 0:
            if self.entity.player:
                self.engine.message_log.add_message(f"Cannot perform action: no AP", colour.RED)
            return

        # queued and has AP, performs action
        elif self.queued and self.entity.fighter.ap > 0:
            self.entity.ai.queued_action = None
            return self.perform()

        # if not in squad mode and aciton queued, handles turns so the action can be completed instantly in real time
        # (still takes turns in game time)
        elif self.queued and self.entity.fighter.ap <= 0 and not self.engine.squad_mode and self.entity.player:
            self.engine.handle_turns()

        # entity has enough AP, performs action
        elif self.entity.fighter.ap >= ap_cost:
            self.entity.fighter.ap -= ap_cost
            if self == self.entity.ai.queued_action:
                self.entity.ai.queued_action = None
            self.perform()

        # entity does not have enough AP to perform action
        elif not self.queued:
            # sets action to queued
            self.entity.fighter.ap -= ap_cost
            self.queued = True
            self.entity.ai.queued_action = self

            # if not in squad mode, handles turns so the action can be completed instantly in real time
            # (still takes turns in game time)
            if not self.engine.squad_mode and self.entity.player:
                self.engine.handle_turns()

    def calculate_ap_cost(self) -> int:
        return 0

    def perform(self) -> None:
        """Perform this action with the objects needed to determine its scope.

        `self.engine` is the scope this action is being performed in.

        `self.entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()


class WaitAction(Action):
    def perform(self) -> None:
        pass


class TakeStairsAction(Action):
    def __init__(self, entity: Actor, handle_now: bool = False) -> None:
        super().__init__(entity, handle_now)
        self.action_str = 'taking stairs'

    def perform(self) -> None:
        """
        Take the stairs, if any exist at the entity's location.
        """
        if (self.entity.x, self.entity.y) == self.engine.game_map.downstairs_location:
            for player in self.engine.players:
                if self.entity.distance_to(player) > 10:
                    raise exceptions.Impossible("Cannot move down stairs: players too far away")

            self.engine.game_map.generate_level()
            self.engine.game_map.camera_xy = (self.engine.player.x, self.engine.player.y)
            self.engine.update_floor_str()
        else:
            raise exceptions.Impossible("There is no way down from here")


class ActionWithDirection(Action):
    def __init__(self, entity: Actor, dx: int, dy: int, handle_now: bool = False):
        super().__init__(entity, handle_now)

        # positon_str_x = ''
        # position_str_y = ''
        #
        # if dy == 1:
        #     position_str_y = 'north'
        # elif dy == -1:
        #     position_str_y = 'south'
        #
        # if dx == 1:
        #     positon_str_x = 'east'
        # elif dx == -1:
        #     positon_str_x = 'west'
        #
        # self.action_str = f'moving {position_str_y} {positon_str_x}'

        self.dx = dx
        self.dy = dy

        if self.entity.fighter.target_actor is None:
            orientation = 0

            # tcod.event.K_UP: (0, -1),
            # tcod.event.K_DOWN: (0, 1),
            # tcod.event.K_LEFT: (-1, 0),
            # tcod.event.K_RIGHT: (1, 0),
            # tcod.event.K_HOME: (-1, -1),
            # tcod.event.K_END: (-1, 1),
            # tcod.event.K_PAGEUP: (1, -1),
            # tcod.event.K_PAGEDOWN: (1, 1),

            # north
            if self.dx == 0 and self.dy == -1:
                orientation = 1.57
            # south
            elif self.dx == 0 and self.dy == 1:
                orientation = -1.57
            # east
            elif self.dx == 1 and self.dy == 0:
                orientation = 3.141
            # north west
            elif self.dx == -1 and self.dy == -1:
                orientation = 0.785
            # south west
            elif self.dx == -1 and self.dy == 1:
                orientation = - 0.785
            # north east
            elif self.dx == 1 and self.dy == -1:
                orientation = -2.356
            # south east
            elif self.dx == 1 and self.dy == 1:
                orientation = 2.356

            self.entity.orientation = orientation

    @property
    def dest_xy(self) -> Tuple[int, int]:
        """Returns this actions destination."""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self) -> Optional[Entity]:
        """Return the blocking entity at this actions destination.."""
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination."""
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)

    def perform(self) -> None:
        raise NotImplementedError()


class AttackAction(Action):
    def __init__(self, distance: int, entity: Actor, targeted_actor: Actor, targeted_bodypart: Optional[Bodypart],
                 handle_now: bool = False):
        super().__init__(entity=entity, handle_now=handle_now)

        targeted_actor.active = True

        self.targeted_actor = targeted_actor
        self.targeted_bodypart = targeted_bodypart
        self.distance = distance
        self.attack_colour = colour.LIGHT_RED

        if self.targeted_bodypart:
            self.part_index = self.targeted_actor.bodyparts.index(self.targeted_bodypart)

        else:  # if no bodypart selected (should only be when entity is not player), sets value later
            self.part_index = None

        entity.previous_target_actor = targeted_actor

    def get_target(self) -> None:
        target = self.targeted_actor
        if not target:
            raise exceptions.Impossible("Nothing to attack.")

        if self.entity.player:
            self.attack_colour = colour.LIGHT_GREEN

        # selects random body part to target
        if not self.targeted_bodypart:
            no_parts = len(target.bodyparts)
            indices = list(range(0, no_parts))
            # first body part in part list weighted higher - should be main body part i.e. torso
            weights = [no_parts * 5]
            weights.extend([1 for i in range(no_parts - 1)])
            self.part_index = choices(indices, weights)[0]
            self.targeted_bodypart = target.bodyparts[self.part_index]


class UnarmedAttackAction(AttackAction):  # entity attacking without a weapon

    def __init__(self, distance: int, entity: Actor, targeted_actor: Actor, targeted_bodypart: Optional[Bodypart],
                 handle_now: bool = False):
        super().__init__(distance, entity, targeted_actor, targeted_bodypart, handle_now=handle_now)
        if targeted_bodypart is not None:
            self.action_str = f'unarmed attack on {targeted_actor.name}'
        else:
            self.action_str = ''

    def action_viable(self) -> bool:
        dx = self.targeted_actor.x - self.entity.x
        dy = self.targeted_actor.y - self.entity.y
        distance = max(abs(dx), abs(dy))  # Chebyshev distance.

        if self.engine.game_map.visible[self.targeted_actor.x, self.targeted_actor.y] \
                and distance == 1:
            return True
        else:
            return False

    def calculate_ap_cost(self) -> int:

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        fighter = self.entity.fighter
        ap_cost = round(fighter.unarmed_ap_cost * fighter.attack_ap_modifier * armour_ap_multiplier)
        return ap_cost

    def perform(self) -> None:

        self.get_target()

        # chance to hit calculation
        part_area = \
            self.targeted_actor.bodyparts[self.part_index].width * \
            self.targeted_actor.bodyparts[self.part_index].height

        hit_chance = part_area / 200 * 100 * self.entity.fighter.melee_accuracy

        # hit
        if randint(0, 100) < hit_chance:
            self.targeted_actor.bodyparts[self.part_index].deal_damage_melee(
                meat_damage=self.entity.fighter.unarmed_meat_damage,
                armour_damage=self.entity.fighter.unarmed_armour_damage,
                attacker=self.entity)

        # miss
        else:
            if self.entity.player:
                return self.engine.message_log.add_message(f"{self.entity.name}'s attack misses", colour.LIGHT_BLUE)

            else:
                return self.engine.message_log.add_message(f"{self.entity.name}'s attack misses", colour.LIGHT_BLUE)


class MeleeAttackAction(AttackAction):
    def __init__(self, distance: int, weapon: MeleeWeapon, entity: Actor, targeted_actor: Actor,
                 targeted_bodypart: Optional[Bodypart], handle_now: bool = False):
        super().__init__(distance=distance, entity=entity, targeted_actor=targeted_actor,
                         targeted_bodypart=targeted_bodypart, handle_now=handle_now)

        if targeted_bodypart is not None:
            self.action_str = f'attack on {targeted_actor.name}'
        else:
            self.action_str = ''

        self.weapon = weapon

    def action_viable(self) -> bool:
        dx = self.targeted_actor.x - self.entity.x
        dy = self.targeted_actor.y - self.entity.y
        distance = max(abs(dx), abs(dy))  # Chebyshev distance.

        if self.engine.game_map.visible[self.targeted_actor.x, self.targeted_actor.y] \
                and distance == 1:
            return True
        else:
            return False

    def calculate_ap_cost(self) -> int:

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        fighter = self.entity.fighter
        ap_cost = round(self.weapon.base_ap_cost * fighter.attack_ap_modifier * armour_ap_multiplier)
        return ap_cost

    def perform(self) -> None:
        self.get_target()

        part_area = self.targeted_actor.bodyparts[self.part_index].width * \
                    self.targeted_actor.bodyparts[self.part_index].height
        hit_chance = part_area / 200 * 100 * self.entity.fighter.melee_accuracy

        self.weapon.attack_melee(target=self.targeted_actor, attacker=self.entity,
                                 part_index=self.part_index, hitchance=hit_chance)


class GunAttackAction(AttackAction):
    def __init__(self, distance: int, gun: Gun, entity: Actor, targeted_actor: Actor,
                 targeted_bodypart: Optional[Bodypart], handle_now: bool = False):
        super().__init__(distance=distance, entity=entity, targeted_actor=targeted_actor,
                         targeted_bodypart=targeted_bodypart, handle_now=handle_now)

        if targeted_bodypart is not None:
            self.action_str = f'shooting {targeted_actor.name}'
        else:
            self.action_str = ''

        self.weapon = gun
        self.total_weight = self.weapon.parent.weight
        self.guntype_proficiency = 1.0
        self.action_proficiency = 1.0
        self.marksmanship = 1.0
        self.rounds_in_mag = 0

        x = atan2(targeted_actor.y - self.entity.y,
                  targeted_actor.x - self.entity.x)

        self.target_acquisition_ap = ((self.weapon.target_acquisition_ap * self.entity.fighter.target_acquisition_ap) *
                                      (abs(atan2(sin(x - entity.orientation), cos(x - entity.orientation))) / 4.711))

        self.ap_distance_cost_modifier = (self.weapon.ap_distance_cost_modifier *
                                          self.entity.fighter.ap_distance_cost_modifier)

    def action_viable(self) -> bool:
        return self.engine.game_map.check_los(start_x=self.entity.x, start_y=self.entity.y,
                                              end_x=self.targeted_actor.x, end_y=self.targeted_actor.y)

    def get_mag_weight(self) -> None:
        return

    def additional_ap_cost(self) -> int:
        return 0

    def calculate_ap_cost(self) -> int:

        self.get_mag_weight()

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        self.give_proficiency()

        if self.queued:
            dx = self.targeted_actor.x - self.entity.x
            dy = self.targeted_actor.y - self.entity.y
            distance = max(abs(dx), abs(dy))  # Chebyshev distance.

            self.distance = distance

        self.additional_ap_cost()

        firing_ap_cost = 0
        ap_cost = 0

        # calculates AP modifier based on weight and weapon type
        if self.weapon.gun_type == 'pistol':
            weight_handling_modifier = 0.75 + 0.25 * self.total_weight
        elif self.weapon.gun_type != 'pistol' and not self.weapon.has_stock:
            weight_handling_modifier = 0.85 + 0.15 * (self.total_weight / 2)
        else:
            weight_handling_modifier = 0.85 + 0.15 * (self.total_weight / 3)

        # adds cost of firing (pulling trigger)
        ap_cost += self.weapon.firing_ap_cost * self.entity.fighter.firing_ap_cost * self.guntype_proficiency

        # ap cost for the given distance to the target
        ap_cost += self.ap_distance_cost_modifier * self.distance * self.guntype_proficiency * self.marksmanship * \
                   weight_handling_modifier * (2.0 - self.entity.fighter.style_range_accuracy)

        # if previous actor is different from the current target, adds cost of acquiring new target
        if self.entity.fighter.previous_target_actor != self.targeted_actor:
            ap_cost += self.target_acquisition_ap * self.guntype_proficiency * weight_handling_modifier

        # if previously targeted limb is different from currently targeted limb, adds cost of changing target
        elif self.entity.fighter.previously_targeted_part != self.targeted_bodypart:
            ap_cost += 0.5 * self.target_acquisition_ap * self.guntype_proficiency * weight_handling_modifier

        # adds AP cost of manually cycling action e.g. for bolt action
        if self.weapon.manual_action:
            if self.rounds_in_mag >= 1:
                ap_cost += self.weapon.action_cycle_ap_cost * self.action_proficiency

        # AP cost for the duration of fully automatic fire
        if self.weapon.fire_modes[self.weapon.current_fire_mode]['automatic']:
            rounds_to_fire = round(self.weapon.fire_modes[self.weapon.current_fire_mode]['fire rate'] / 60
                                   * self.weapon.fire_rate_modifier * self.entity.fighter.automatic_fire_duration)

            # if less rounds in magazine than rounds fired in the given duration of automatic fire, AP cost of
            # firing adjusted to amount of time it takes to fire remaining rounds in magazine
            if rounds_to_fire > self.rounds_in_mag:
                # time (and therefore AP) it takes to fire the given amount of rounds
                time_to_fire = self.entity.fighter.automatic_fire_duration
            else:
                time_to_fire = self.rounds_in_mag / round(
                    (self.weapon.fire_modes[self.weapon.current_fire_mode]['fire rate']
                     / 60 * self.weapon.fire_rate_modifier))

            firing_ap_cost += round(time_to_fire * 100)

        ap_cost *= self.entity.fighter.attack_ap_modifier * armour_ap_multiplier
        ap_cost += firing_ap_cost

        return ap_cost

    # gives XP and calculates proficiency multiplier based on gun type
    def give_proficiency(self) -> None:

        fighter = self.entity.fighter

        proficiency_actiontype = 1.0
        proficiency_guntype = 1.0

        if self.entity.player:
            if self.weapon.gun_type == 'pistol':
                proficiency_guntype = fighter.skill_pistol_proficiency
                proficiency_guntype += 1
            elif self.weapon.gun_type == 'pdw':
                proficiency_guntype = fighter.skill_smg_proficiency
                proficiency_guntype += 1
            elif self.weapon.gun_type == 'rifle':
                proficiency_guntype = fighter.skill_rifle_proficiency
                proficiency_guntype += 1

            if self.weapon.action_type == 'bolt action':
                proficiency_actiontype = fighter.skill_bolt_action_proficiency
                proficiency_actiontype += 1
            elif self.weapon.action_type == 'revolver':
                proficiency_actiontype = fighter.skill_revolver_proficiency
                proficiency_actiontype += 1
            elif self.weapon.action_type == 'semi-auto rifle':
                proficiency_actiontype = fighter.skill_sa_rifle_proficiency
                proficiency_actiontype += 1
            elif self.weapon.action_type == 'semi-auto pistol':
                proficiency_actiontype = fighter.skill_sa_pistol_proficiency
                proficiency_actiontype += 1
            elif self.weapon.action_type == 'pump action':
                proficiency_actiontype = fighter.skill_pumpaction_proficiency
                proficiency_actiontype += 1
            elif self.weapon.action_type == 'break action':
                proficiency_actiontype = fighter.skill_breakaction_proficiency
                proficiency_actiontype += 1

            self.guntype_proficiency = 1 - (proficiency_guntype / 4000)
            self.action_proficiency = 1 - (proficiency_actiontype / 4000)

            if self.distance > 7:
                self.marksmanship = 1 - (fighter.skill_marksmanship / 4000)
                fighter.skill_marksmanship += (self.distance // 7)

    def perform(self) -> None:

        self.get_target()

        self.weapon.attack_ranged(target=self.targeted_actor, attacker=self.entity,
                                  part_index=self.part_index, distance=self.distance,
                                  proficiency=self.guntype_proficiency, skill_range_modifier=self.marksmanship)

        # prints splatter message
        if self.targeted_bodypart.show_splatter_message:
            self.engine.message_log.add_message(self.targeted_bodypart.splatter_message, colour.GREEN)

            self.targeted_bodypart.show_splatter_message = False
            self.targeted_bodypart.splatter_message_shown = True

        self.entity.fighter.previously_targeted_part = self.targeted_bodypart
        self.entity.fighter.previous_target_actor = self.targeted_actor


class GunMagFedAttack(GunAttackAction):
    def __init__(self, distance: int, gun: GunMagFed, entity: Actor, targeted_actor: Actor,
                 targeted_bodypart: Optional[Bodypart], handle_now: bool = False):
        super().__init__(distance, gun, entity, targeted_actor, targeted_bodypart, handle_now=handle_now)
        self.weapon = gun
        self.total_weight = self.weapon.parent.weight

    def get_mag_weight(self) -> None:

        # adds weight of the magazine and loaded bullets to total weight for recoil calculations
        if self.weapon.loaded_magazine is not None:
            magazine = self.weapon.loaded_magazine.magazine
            mag_weight = self.weapon.loaded_magazine.parent.weight
            try:
                ammo_weight = len(magazine) * self.weapon.chambered_bullet.parent.weight
            except AttributeError:
                ammo_weight = 0
            self.total_weight += mag_weight + ammo_weight

    def additional_ap_cost(self) -> None:

        # alters attributes according to magazine properties
        if self.weapon.loaded_magazine is not None:
            rounds_in_mag = len(self.weapon.loaded_magazine.magazine)
            magazine = self.weapon.loaded_magazine.magazine

            self.target_acquisition_ap *= self.weapon.loaded_magazine.target_acquisition_ap_mod

            self.ap_distance_cost_modifier *= self.weapon.loaded_magazine.ap_distance_cost_mod

            # adds weight of magazine to total weight
            self.total_weight += self.weapon.loaded_magazine.parent.weight

            # adds weight of rounds in magazine to total weight
            if rounds_in_mag >= 1:
                self.total_weight += (len(magazine) * magazine[0].parent.weight)


class GunIntegratedMagAttack(GunAttackAction):

    def __init__(self, distance: int, gun: GunIntegratedMag, entity: Actor, targeted_actor: Actor,
                 targeted_bodypart: Optional[Bodypart], handle_now: bool = False):
        super().__init__(distance, gun, entity, targeted_actor, targeted_bodypart, handle_now=handle_now)
        self.weapon = gun

    def get_mag_weight(self) -> None:

        magazine = self.weapon.magazine
        try:
            self.total_weight += len(magazine) * self.weapon.chambered_bullet.parent.weight
        except AttributeError:
            return

    def additional_ap_cost(self) -> None:
        rounds_in_mag = len(self.weapon.magazine)
        magazine = self.weapon.magazine

        # adds weight of rounds in magazine to total weight
        if rounds_in_mag >= 1:
            self.total_weight += (len(magazine) * magazine[0].parent.weight)


class ClearJam(Action):

    def __init__(self, entity: Actor, gun: Gun):
        self.gun = gun
        super().__init__(entity)
        self.action_str = f'clearing jam'

    def calculate_ap_cost(self):

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        proficiency = 1.0

        if self.entity.player:

            if self.gun.action_type == 'bolt action':
                proficiency = copy(self.entity.fighter.skill_bolt_action_proficiency)
            elif self.gun.action_type == 'revolver':
                proficiency = copy(self.entity.fighter.skill_revolver_proficiency)
            elif self.gun.action_type == 'semi-auto rifle':
                proficiency = copy(self.entity.fighter.skill_sa_rifle_proficiency)
            elif self.gun.action_type == 'semi-auto pistol':
                proficiency = copy(self.entity.fighter.skill_sa_pistol_proficiency)
            elif self.gun.action_type == 'pump action':
                proficiency = copy(self.entity.fighter.skill_pumpaction_proficiency)
            elif self.gun.action_type == 'break action':
                proficiency = copy(self.entity.fighter.skill_breakaction_proficiency)

            proficiency = 1 - (proficiency / 4000)

        # jam takes between 2 and 5 seconds to clear
        return randint(2, 5) * 100 * self.entity.fighter.action_ap_modifier * proficiency * armour_ap_multiplier

    def perform(self) -> None:
        self.gun.jammed = False
        self.engine.message_log.add_message(f"{self.entity.name} cleared jam", colour.GREEN)


class ReloadMagFed(Action):
    def __init__(self, entity: Actor, gun: GunMagFed, magazine_to_load: DetachableMagazine):
        super().__init__(entity)
        self.action_str = f'reloading'
        self.gun = gun
        self.magazine_to_load = magazine_to_load

    def calculate_ap_cost(self):

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        ap_cost = 0

        proficiency = 1.0

        if self.entity.player:

            if self.gun.action_type == 'bolt action':
                proficiency = copy(self.entity.fighter.skill_bolt_action_proficiency)
            elif self.gun.action_type == 'revolver':
                proficiency = copy(self.entity.fighter.skill_revolver_proficiency)
            elif self.gun.action_type == 'semi-auto rifle':
                proficiency = copy(self.entity.fighter.skill_sa_rifle_proficiency)
            elif self.gun.action_type == 'semi-auto pistol':
                proficiency = copy(self.entity.fighter.skill_sa_pistol_proficiency)
            elif self.gun.action_type == 'pump action':
                proficiency = copy(self.entity.fighter.skill_pumpaction_proficiency)
            elif self.gun.action_type == 'break action':
                proficiency = copy(self.entity.fighter.skill_breakaction_proficiency)

            proficiency = 1 - (proficiency / 4000)

        # AP cost calculated
        ap_cost += \
            self.entity.fighter.action_ap_modifier * self.gun.load_time_modifier * self.magazine_to_load.ap_to_load

        # adds cost of cycling manual action
        if self.gun.manual_action:
            ap_cost += self.gun.action_cycle_ap_cost

        ap_cost *= proficiency * armour_ap_multiplier
        return ap_cost

    def perform(self) -> None:

        # loads magazine into gun
        if self.gun.loaded_magazine is not None:

            if not self.gun.keep_round_chambered:
                self.gun.loaded_magazine.magazine.append(self.gun.chambered_bullet)
                self.gun.chambered_bullet = None

            if self.entity.player:
                self.entity.inventory.items.append(self.gun.loaded_magazine.parent)
                self.entity.inventory.items.remove(self.magazine_to_load.parent)

        self.gun.loaded_magazine = deepcopy(self.magazine_to_load)

        if len(self.gun.loaded_magazine.magazine) > 0:
            if self.gun.chambered_bullet is None:
                self.gun.chambered_bullet = self.gun.loaded_magazine.magazine.pop()


class ReloadFromClip(Action):
    def __init__(self, entity: Actor, gun: Gun, clip: Clip):
        super().__init__(entity)
        self.action_str = f'reloading'
        self.gun = gun
        self.clip = clip

    def action_viable(self) -> bool:
        if self.gun.clip_reload_check_viable(clip=self.clip):
            return True

        elif self.entity.inventory.held != self.gun:
            return False

    def calculate_ap_cost(self):

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        ap_cost = 0

        proficiency = 1.0

        if self.entity.player:
            if self.gun.action_type == 'bolt action':
                proficiency = copy(self.entity.fighter.skill_bolt_action_proficiency)
            elif self.gun.action_type == 'revolver':
                proficiency = copy(self.entity.fighter.skill_revolver_proficiency)
            elif self.gun.action_type == 'semi-auto rifle':
                proficiency = copy(self.entity.fighter.skill_sa_rifle_proficiency)
            elif self.gun.action_type == 'semi-auto pistol':
                proficiency = copy(self.entity.fighter.skill_sa_pistol_proficiency)
            elif self.gun.action_type == 'pump action':
                proficiency = copy(self.entity.fighter.skill_pumpaction_proficiency)
            elif self.gun.action_type == 'break action':
                proficiency = copy(self.entity.fighter.skill_breakaction_proficiency)

            proficiency = 1 - (proficiency / 4000)

        # AP cost calculated
        ap_cost += \
            self.entity.fighter.action_ap_modifier * self.gun.load_time_modifier * self.clip.ap_to_load

        # adds cost of cycling manual action
        if self.gun.manual_action:
            ap_cost += self.gun.action_cycle_ap_cost

        ap_cost *= proficiency * armour_ap_multiplier
        return ap_cost

    def perform(self) -> None:
        self.gun.load_from_clip(clip=self.clip)

        if self.entity.player:

            if self.gun.clip_stays_in_gun:
                self.gun.clip_in_gun = self.clip

                if self.gun.clip_in_gun is not None:
                    self.entity.inventory.items.append(self.gun.clip_in_gun.parent)

                self.entity.inventory.items.remove(self.clip.parent)


class LoadBulletsIntoMagazine(Action):
    def __init__(self, entity: Actor, magazine: Magazine, bullets_to_load: int, bullet_type: Bullet):
        super().__init__(entity)
        self.action_str = f'loading magazine'

        self.magazine = magazine

        self.bullets_to_load = bullets_to_load
        self.bullet_type = bullet_type

        inventory = entity.inventory

        if bullets_to_load > bullet_type.parent.stacking.stack_size or bullets_to_load < 1:
            raise Impossible("Invalid entry.")

        # amount to be loaded is greater than no. of rounds available
        if bullets_to_load > bullet_type.parent.stacking.stack_size:
            bullets_to_load = bullet_type.parent.stacking.stack_size

        # amount to be loaded is greater than the magazine capacity
        if bullets_to_load > self.magazine.mag_capacity - len(self.magazine.magazine):
            bullets_to_load = self.magazine.mag_capacity - len(self.magazine.magazine)

        # 1 or more stack left in inventory after loading
        if bullet_type.parent.stacking.stack_size - bullets_to_load > 1:
            bullet_type.parent.stacking.stack_size -= bullets_to_load

        # no stacks left after loading
        elif bullet_type.parent.stacking.stack_size - bullets_to_load <= 0:
            if entity.player:
                inventory.items.remove(bullet_type.parent)

    def calculate_ap_cost(self):

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        ap_cost_modifier = self.entity.fighter.action_ap_modifier * self.bullet_type.load_time_modifier

        # loading ap calculated
        ap_cost, mag_load_time_modifier, proficiency = self.magazine.loading_ap()
        ap_cost_modifier *= mag_load_time_modifier

        # adds cost of loading each bullet
        ap_cost += proficiency * self.bullets_to_load * ap_cost_modifier * armour_ap_multiplier
        return ap_cost

    def perform(self) -> None:

        # loads bullets into gun
        self.magazine.load_magazine(entity=self.entity, ammo=self.bullet_type, load_amount=self.bullets_to_load)


class MovementAction(ActionWithDirection):

    def calculate_ap_cost(self):
        return self.entity.fighter.move_ap_cost

    def action_viable(self) -> bool:

        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            # Destination is out of bounds.
            raise exceptions.Impossible("Silent")

        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # Destination is blocked by a tile.
            raise exceptions.Impossible("Silent")

        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            # Destination is blocked by an entity.
            raise exceptions.Impossible("Silent")

        if self.blocking_entity:
            if self.entity.player:
                self.engine.message_log.add_message(
                    f"{self.entity.name}'s movement was interrupted - an enemy is in the "
                    f"way", colour.RED)
            return False
        else:
            return True

    def perform(self) -> None:

        self.entity.move(self.dx, self.dy)

        if self.entity.player:
            self.engine.game_map.camera_xy = (self.engine.player.x, self.engine.player.y)

        # if chance for move action to fail
        """
        if fighter.move_success_chance != 1.0:
            if random.uniform(0, 1) < fighter.move_success_chance:
                self.entity.move(self.dx, self.dy)
            elif self.entity.player:
                self.engine.message_log.add_message(f"{self.entity.name} tries to move but stumbles", colour.RED)
                trying_to_move = True
                while trying_to_move:  # TODO - this needs to be redone for squad system
                    if random.uniform(0, 1) < fighter.move_success_chance:
                        self.entity.move(self.dx, self.dy)
                        TryToMove(self.entity, self.dx, self.dy).perform()
                        trying_to_move = False
                    else:
                        self.engine.handle_enemy_turns()
        """


class BumpAction(ActionWithDirection):

    def perform(self) -> None:

        if self.target_actor and not self.target_actor.player:

            try:

                item_held = self.entity.inventory.held

                if item_held is not None:
                    self.entity.fighter.previous_target_actor = self.target_actor
                    return item_held.usable_properties.get_attack_action(distance=1, entity=self.entity,
                                                                         targeted_actor=self.target_actor,
                                                                         targeted_bodypart=self.target_actor.bodyparts[
                                                                             0]).handle_action()

                else:
                    self.entity.fighter.previous_target_actor = self.target_actor
                    return UnarmedAttackAction(distance=1, entity=self.entity, targeted_actor=self.target_actor,
                                               targeted_bodypart=self.target_actor.bodyparts[0]).handle_action()

            except AttributeError:
                pass

        else:
            return MovementAction(entity=self.entity, dx=self.dx, dy=self.dy, handle_now=True).handle_action()


class AddToInventory(Action):

    def __init__(self, entity: Actor, item: Item, amount: int):
        super().__init__(entity)
        self.item = item
        self.amount = amount
        self.action_str = f'adding item to inventory'
        self.item_copy = deepcopy(self.item)

    def calculate_ap_cost(self) -> int:
        return 0

    def action_viable(self) -> bool:

        stack_size = 1

        if self.item.stacking:
            stack_size = self.item.stacking.stack_size

        # checks if there is enough capacity for the item
        if self.entity.inventory.current_item_weight() + self.item.weight * stack_size > \
                self.entity.inventory.capacity:
            self.engine.message_log.add_message(f"{self.entity.name} - inventory full.", colour.RED)
            return False

        return True

    def perform(self) -> None:

        if self.item.stacking:

            if self.item.stacking.stack_size >= self.amount > 0:
                stack_amount = self.amount
            else:
                stack_amount = self.item.stacking.stack_size

            self.item_copy.stacking.stack_size = stack_amount
            self.item.stacking.stack_size -= self.item_copy.stacking.stack_size
            self.entity.inventory.add_to_inventory(item=self.item_copy, item_container=None, amount=self.amount)

            if self.item.stacking.stack_size <= 0:
                self.remove_from_container()

        else:

            self.entity.inventory.items.append(self.item_copy)
            self.remove_from_container()

        self.item_copy.parent = self.entity.inventory

    def remove_from_container(self):
        pass


class PickupAction(AddToInventory):
    def __init__(self, entity: Actor, item: Item, amount: int):
        super().__init__(entity, item, amount)
        self.action_str = f'picking up item'
        entity.previous_target_actor = None

    def calculate_ap_cost(self) -> int:
        return 300

    def action_viable(self) -> bool:
        if self.entity.x == self.item.x and self.entity.y == self.item.y:
            return True
        else:
            return False

    def remove_from_container(self):
        self.engine.game_map.entities.remove(self.item)


class DropAction(Action):

    def __init__(self, entity: Actor, item: Item, drop_amount: int):
        super().__init__(entity)
        self.action_str = f'dropping item'
        self.item = item
        self.drop_amount = drop_amount

        entity.previous_target_actor = None

    def calculate_ap_cost(self) -> int:
        return 300

    def perform(self) -> None:
        if self.item.stacking:
            if self.item.stacking.stack_size > 1:

                try:

                    # copy of the item to be dropped
                    dropped_item = deepcopy(self.item)

                    # sets dropped item to have correct stack size
                    dropped_item.stacking.stack_size = self.drop_amount

                    if self.drop_amount > 0:

                        # more than 1 stack left in after drop
                        if self.item.stacking.stack_size - self.drop_amount > 1:
                            self.item.stacking.stack_size -= self.drop_amount
                            dropped_item.place(self.entity.x, self.entity.y,
                                               self.engine.game_map)

                        # no stacks left after drop
                        elif self.item.stacking.stack_size - self.drop_amount <= 0:
                            self.entity.inventory.items.remove(self.item)

                            self.item.place(self.entity.x, self.entity.y, self.engine.game_map)

                except ValueError:
                    self.engine.message_log.add_message("Invalid entry", colour.RED)

            else:  # item stacking, stack size = 1
                self.entity.inventory.items.remove(self.item)
                self.item.place(self.entity.x, self.entity.y, self.engine.game_map)

        else:  # item not stacking
            self.entity.inventory.items.remove(self.item)
            self.item.place(self.entity.x, self.entity.y, self.engine.game_map)


class ItemAction(Action):
    def __init__(
            self, entity: Actor, item: Item, target_xy: Optional[Tuple[int, int]] = None
    ):
        super().__init__(entity)
        self.item = item
        if not target_xy:
            target_xy = entity.x, entity.y
        self.target_xy = target_xy

    @property
    def target_actor(self) -> Optional[Actor]:
        """Return the actor at this actions destination."""
        return self.engine.game_map.get_actor_at_location(*self.target_xy)

    def perform(self) -> None:
        """Invoke the items ability, this action will be given to provide context."""
        # if self.item.usable_properties:  # test
        try:
            self.item.usable_properties.activate(self)
        except NotImplementedError:
            pass


class RepairItem(Action):
    def __init__(self, entity: Actor, item_to_repair: Item, repair_kit_item: Item) -> None:
        super().__init__(entity)
        self.item_to_repair = item_to_repair
        self.repair_kit_item = repair_kit_item
        self.action_str = f'repairing item'

    def calculate_ap_cost(self) -> int:
        return 500

    def perform(self) -> None:
        self.repair_kit_item.usable_properties.activate(self)


class HealPart(Action):
    def __init__(self, entity: Actor, part_to_heal: Bodypart, healing_item: Item) -> None:
        super().__init__(entity)
        self.part_to_heal = part_to_heal
        self.healing_item = healing_item
        self.action_str = f'healing {part_to_heal.name}'

    def calculate_ap_cost(self) -> int:

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        return round(1000 * armour_ap_multiplier)

    def perform(self) -> None:
        self.healing_item.usable_properties.activate(self)


class EquipWeapon(Action):
    def __init__(self, entity: Actor, weapon: Weapon):
        super().__init__(entity)
        self.action_str = f'equipping {weapon.parent.name}'
        self.weapon = weapon

    def calculate_ap_cost(self) -> int:
        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        return round(self.weapon.get_equip_ap() * armour_ap_multiplier)

    def perform(self) -> None:
        self.entity.inventory.held = self.weapon.parent


class EquipWeaponToPrimary(EquipWeapon):
    def __init__(self, entity: Actor, weapon: Weapon):
        super().__init__(entity, weapon)
        self.action_str = f'equipping {weapon.parent.name}'

    def perform(self) -> None:
        self.entity.inventory.items.remove(self.weapon.parent)
        if self.entity.inventory.primary_weapon:
            if self.entity.inventory.held == self.entity.inventory.primary_weapon:
                self.entity.inventory.held = None

            self.entity.inventory.add_to_inventory(item=self.entity.inventory.primary_weapon,
                                                   item_container=None, amount=1)

        self.entity.inventory.primary_weapon = self.weapon.parent


class EquipWeaponToSecondary(EquipWeapon):
    def __init__(self, entity: Actor, weapon: Weapon):
        super().__init__(entity, weapon)
        self.action_str = f'equipping {weapon.parent.name}'

    def perform(self) -> None:
        self.entity.inventory.items.remove(self.weapon.parent)
        if self.entity.inventory.secondary_weapon:

            if self.entity.inventory.held == self.entity.inventory.secondary_weapon:
                self.entity.inventory.held = None

            self.entity.inventory.add_to_inventory(item=self.entity.inventory.secondary_weapon,
                                                   item_container=None, amount=1)

        self.entity.inventory.secondary_weapon = self.weapon.parent


class UnequipWeapon(EquipWeapon):

    def __init__(self, entity: Actor, weapon: Weapon):
        super().__init__(entity, weapon)
        self.action_str = f'unequipping {weapon.parent.name}'

    def perform(self) -> None:

        inventory = self.entity.inventory

        inventory.items.append(self.weapon.parent)

        if inventory.held == self.weapon.parent:
            inventory.held = None
        if inventory.primary_weapon == self.weapon.parent:
            inventory.primary_weapon = None
        elif inventory.secondary_weapon == self.weapon.parent:
            inventory.secondary_weapon = None


class CheckRoundsInMag(Action):
    def __init__(self, entity: Actor, weapon: GunMagFed):
        super().__init__(entity)
        self.action_str = f'checking rounds in mag'
        self.weapon = weapon

    def calculate_ap_cost(self) -> int:

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        proficiency_actiontype = 1.0

        if self.entity.player:

            if self.weapon.action_type == 'bolt action':
                proficiency_actiontype = copy(self.entity.fighter.skill_bolt_action_proficiency)
            elif self.weapon.action_type == 'revolver':
                proficiency_actiontype = copy(self.entity.fighter.skill_revolver_proficiency)
            elif self.weapon.action_type == 'semi-auto rifle':
                proficiency_actiontype = copy(self.entity.fighter.skill_sa_rifle_proficiency)
            elif self.weapon.action_type == 'semi-auto pistol':
                proficiency_actiontype = copy(self.entity.fighter.skill_sa_pistol_proficiency)
            elif self.weapon.action_type == 'pump action':
                proficiency_actiontype = copy(self.entity.fighter.skill_pumpaction_proficiency)
            elif self.weapon.action_type == 'break action':
                proficiency_actiontype = copy(self.entity.fighter.skill_breakaction_proficiency)

            proficiency_actiontype = 1 - (proficiency_actiontype / 4000)

        # AP cost calculated
        ap_cost = \
            (self.entity.fighter.action_ap_modifier *
             self.weapon.load_time_modifier * self.weapon.loaded_magazine.witness_check_ap * proficiency_actiontype)

        return round(ap_cost * armour_ap_multiplier)

    def action_viable(self) -> bool:

        if hasattr(self.weapon.loaded_magazine, 'witness_check_ap'):
            return True

        else:
            return False

    def perform(self) -> None:
        message = self.weapon.loaded_magazine.check_rounds_in_mag()
        self.engine.message_log.add_message(message, colour.WHITE)


class EquipWearable(Action):

    def __init__(self, entity: Actor, wearable: Wearable):
        super().__init__(entity)
        self.action_str = f'equipping {wearable.parent.name}'
        self.wearable = wearable

    def calculate_ap_cost(self) -> int:

        armour_ap_multiplier = 1.0

        for part in self.entity.bodyparts:
            if part.equipped is not None:
                armour_ap_multiplier *= part.equipped.ap_penalty

        return round(self.wearable.equip_ap_cost * armour_ap_multiplier)

    def perform(self) -> None:

        item_removed = False

        self.entity.inventory.small_mag_capacity += self.wearable.small_mag_slots
        self.entity.inventory.medium_mag_capacity += self.wearable.medium_mag_slots
        self.entity.inventory.large_mag_capacity += self.wearable.large_mag_slots

        for bodypart in self.entity.bodyparts:
            if bodypart.part_type == self.wearable.fits_bodypart:

                if bodypart.equipped:
                    self.engine.message_log.add_message(f"Already wearing something there.", colour.RED)

                else:
                    if not item_removed:
                        self.entity.inventory.items.remove(self.wearable.parent)
                        item_removed = True
                    bodypart.equipped = self.wearable


class UnequipWearable(EquipWearable):
    def __init__(self, entity: Actor, wearable: Wearable):
        super().__init__(entity, wearable)
        self.action_str = f'uneuipping {wearable.parent.name}'

    def perform(self) -> None:

        self.entity.inventory.small_mag_capacity -= self.wearable.small_mag_slots
        self.entity.inventory.medium_mag_capacity -= self.wearable.medium_mag_slots
        self.entity.inventory.large_mag_capacity -= self.wearable.large_mag_slots

        self.entity.inventory.update_magazines()

        for bodypart in self.entity.bodyparts:
            if bodypart.part_type == self.wearable.fits_bodypart:
                bodypart.equipped = None

        self.entity.inventory.items.append(self.wearable.parent)
