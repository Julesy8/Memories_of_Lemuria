from __future__ import annotations

import random
from typing import Optional, Tuple, TYPE_CHECKING
from math import ceil
from random import randint
from copy import deepcopy, copy
import numpy.random

import colour
import exceptions
from random import choices
from exceptions import Impossible

if TYPE_CHECKING:
    from engine import Engine
    from entity import Actor, Entity, Item
    from components.consumables import Gun, GunMagFed, Magazine, Bullet
    from components.bodyparts import Bodypart


class Action:
    def __init__(self, entity: Actor) -> None:
        super().__init__()
        self.entity = entity

    @property
    def engine(self) -> Engine:
        """Return the engine this action belongs to."""
        return self.entity.gamemap.engine

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
    def perform(self) -> None:
        """
        Take the stairs, if any exist at the entity's location.
        """
        if (self.entity.x, self.entity.y) == self.engine.game_map.downstairs_location:
            self.engine.game_map.generate_level()
            self.engine.game_map.camera_xy = (self.engine.player.x, self.engine.player.y)
            self.engine.update_floor_str()
        else:
            raise exceptions.Impossible("There is no way down from here")


class ActionWithDirection(Action):
    def __init__(self, entity: Actor, dx: int, dy: int):
        super().__init__(entity)

        self.dx = dx
        self.dy = dy

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
                 queued: Optional[bool] = False):
        super().__init__(entity)

        targeted_actor.active = True

        self.targeted_actor = targeted_actor
        self.targeted_bodypart = targeted_bodypart
        self.queued = queued
        self.distance = distance
        self.attack_colour = colour.LIGHT_RED

        if self.targeted_bodypart:
            self.part_index = self.targeted_actor.bodyparts.index(self.targeted_bodypart)

        else:  # if no bodypart selected (should only be when entity is not player), sets value later
            self.part_index = None

        entity.previous_target_actor = targeted_actor

    def perform(self) -> None:
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

    def attack(self) -> None:
        # attack method to be replaced by specific attack methods
        raise NotImplementedError()


class UnarmedAttackAction(AttackAction):  # entity attacking without a weapon

    def attack(self) -> None:

        # cant attack if outside range
        if self.distance > 1:
            return

        self.perform()

        fighter = self.entity.fighter
        ap_cost = round(fighter.unarmed_ap_cost * fighter.attack_ap_modifier)

        # check if adequate AP
        if fighter.ap >= ap_cost or self.queued:

            # subtracts AP cost
            if not self.queued:
                fighter.ap -= ap_cost

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
                    return self.engine.message_log.add_message("You miss the attack", colour.YELLOW)

                else:
                    return self.engine.message_log.add_message(f"{self.entity.name}'s attack misses", colour.LIGHT_BLUE)

            if self.entity.player:
                if fighter.ap <= 0:
                    return

        # insufficient AP for action - queues action for later turn
        elif self.entity.ai.queued_action is None:
            fighter.ap -= ap_cost

            turns_to_skip = ceil(abs(fighter.ap / (fighter.ap_per_turn * fighter.ap_per_turn_modifier)))

            # attacker is player
            if self.entity.player:
                attack_viable = True
                for i in range(turns_to_skip):
                    self.engine.handle_enemy_turns()

                    dx = self.targeted_actor.x - self.entity.x
                    dy = self.targeted_actor.y - self.entity.y
                    distance = max(abs(dx), abs(dy))  # Chebyshev distance.

                    # check if action can still be performed
                    if self.engine.game_map.visible[self.targeted_actor.x, self.targeted_actor.y] \
                            and distance == 1:
                        continue
                    else:
                        attack_viable = False
                        self.engine.message_log.add_message("Your attack was interrupted", colour.RED)
                        break

                if attack_viable:
                    self.queued = True
                    self.attack()

            # attacker is AI
            else:
                self.queued = True
                self.entity.ai.queued_action = self

                # how many turns entity has to wait until attack
                self.entity.ai.turns_until_action = turns_to_skip


class WeaponAttackAction(AttackAction):
    # TODO - change item type to weapon
    def __init__(self, distance: int, item: Item, entity: Actor, targeted_actor: Actor,
                 targeted_bodypart: Optional[Bodypart]):
        super().__init__(distance, entity, targeted_actor, targeted_bodypart)
        self.item = item

    # TODO - separate action classes for integrated mag and mag fed and melee

    def attack(self) -> None:
        self.perform()

        fighter = self.entity.fighter

        weapon_type = type(self.item.usable_properties).__name__

        ap_cost = 0

        proficiency = 1.0
        marksmanship = 1.0

        # AP cost calculations
        if weapon_type == 'GunMagFed' or weapon_type == 'GunIntegratedMag':

            gun = self.item.usable_properties

            target_acquisition_ap = gun.target_acquisition_ap * self.entity.fighter.target_acquisition_ap
            ap_distance_cost_modifier = gun.ap_distance_cost_modifier * self.entity.fighter.ap_distance_cost_modifier

            total_weight = self.item.weight

            rounds_in_mag = 0

            # gives XP and calculates proficiency multiplier based on gun type
            if self.entity.player:
                if self.item.usable_properties.gun_type == 'pistol':
                    proficiency = copy(fighter.skill_pistol_proficiency)
                    fighter.skill_pistol_proficiency += 1
                elif self.item.usable_properties.gun_type == 'pdw':
                    proficiency = copy(fighter.skill_smg_proficiency)
                    fighter.skill_smg_proficiency += 1
                elif self.item.usable_properties.gun_type == 'rifle':
                    proficiency = copy(fighter.skill_rifle_proficiency)
                    fighter.skill_rifle_proficiency += 1
                elif self.item.usable_properties.gun_type == 'bolt action':
                    proficiency = copy(fighter.skill_bolt_action_proficiency)
                    fighter.skill_bolt_action_proficiency += 1

                proficiency = 1 - (proficiency / 4000)

                if self.distance > 15:
                    marksmanship = fighter.skill_marksmanship
                    fighter.skill_marksmanship += ((self.distance - 15) // 10) + 1

            # alters attributes according to magazine properties
            if weapon_type == 'GunMagFed':
                if hasattr(gun, 'loaded_magazine'):
                    rounds_in_mag = len(gun.loaded_magazine.magazine)
                    magazine = gun.loaded_magazine.magazine

                    target_acquisition_ap *= getattr(gun.loaded_magazine,
                                                     'target_acquisition_ap_mod')
                    ap_distance_cost_modifier *= getattr(gun.loaded_magazine,
                                                         'ap_distance_cost_mod')

                    # adds weight of magazine to total weight
                    total_weight += gun.loaded_magazine.parent.weight

            elif weapon_type == 'GunIntegratedMag':
                rounds_in_mag = len(gun.magazine)
                magazine = gun.magazine

            # adds weight of rounds in magazine to total weight
            if rounds_in_mag >= 1:
                total_weight += (len(magazine) * magazine[0].parent.weight)

            # calculates AP modifier based on weight and weapon type
            if gun.gun_type == 'pistol':
                weight_handling_modifier = 0.4 + 0.6 * total_weight

            else:
                weight_handling_modifier = 0.5 + 0.5 * (total_weight / 4)

            # adds cost of firing (pulling trigger)
            ap_cost += gun.firing_ap_cost * self.entity.fighter.firing_ap_cost * proficiency

            # ap cost for the given distance to the target
            ap_cost += ap_distance_cost_modifier * self.distance * proficiency * marksmanship * weight_handling_modifier

            # if previous actor is different from the current target, adds cost of acquiring new target
            if self.entity.fighter.previous_target_actor == self.entity.fighter.target_actor:
                ap_cost += target_acquisition_ap * proficiency * weight_handling_modifier

            # adds AP cost of manually cycling action e.g. for bolt action
            if gun.manual_action:
                if rounds_in_mag >= 1:
                    ap_cost += gun.action_cycle_ap_cost * proficiency

            # AP cost for the duration of fully automatic fire
            if gun.fire_modes[gun.current_fire_mode]['automatic']:
                rounds_to_fire = round(gun.fire_modes[gun.current_fire_mode]['fire rate'] / 60
                                       * gun.fire_rate_modifier * fighter.automatic_fire_duration)

                # if less rounds in magazine than rounds fired in the given duration of automatic fire, AP cost of
                # firing adjusted to amount of time it takes to fire remaining rounds in magazine
                if rounds_to_fire > rounds_in_mag:
                    # time (and therefore AP) it takes to fire the given amount of rounds
                    time_to_fire = fighter.automatic_fire_duration
                else:
                    time_to_fire = rounds_in_mag / round((gun.fire_modes[gun.current_fire_mode]['fire rate']
                                                          / 60 * gun.fire_rate_modifier))

                ap_cost += round(time_to_fire * 100)

        # melee weapon
        else:
            ap_cost += self.item.usable_properties.base_ap_cost

        ap_cost *= fighter.attack_ap_modifier

        if fighter.ap >= ap_cost or self.queued:

            if not self.queued:
                fighter.ap -= ap_cost

            # firearm attack
            if weapon_type == 'GunMagFed' or weapon_type == 'GunIntegratedMag':

                # calculate hit location on body
                standard_deviation = 0.1 * self.distance
                hit_location_x = numpy.random.normal(scale=standard_deviation, size=1)[0]
                hit_location_y = numpy.random.normal(scale=standard_deviation, size=1)[0]

                self.item.usable_properties.attack_ranged(target=self.targeted_actor, attacker=self.entity,
                                                          part_index=self.part_index, hit_location_x=hit_location_x,
                                                          hit_location_y=hit_location_y, distance=self.distance,
                                                          proficiency=proficiency, skill_range_modifier=marksmanship)

            # melee
            else:

                dx = self.targeted_actor.x - self.entity.x
                dy = self.targeted_actor.y - self.entity.y
                distance = max(abs(dx), abs(dy))  # Chebyshev distance.

                if distance == 1:
                    part_area = self.targeted_actor.bodyparts[self.part_index].width * \
                                self.targeted_actor.bodyparts[self.part_index].height
                    hit_chance = part_area / 200 * 100 * self.entity.fighter.melee_accuracy

                    self.item.usable_properties.attack_melee(target=self.targeted_actor, attacker=self.entity,
                                                             part_index=self.part_index, hit_chance=hit_chance)

        # insufficient AP for action - queues action for later turn
        elif not self.queued:
            fighter.ap -= ap_cost

            turns_to_skip = ceil(abs(fighter.ap / (fighter.ap_per_turn * fighter.ap_per_turn_modifier)))

            # attacker is player
            if self.entity.player:

                attack_viable = True
                for i in range(turns_to_skip):
                    self.engine.handle_enemy_turns()
                    # check if action can still be performed
                    if self.engine.game_map.visible[self.targeted_actor.x, self.targeted_actor.y] and \
                            self.item == self.entity.inventory.held:
                        continue
                    else:
                        attack_viable = False
                        self.engine.message_log.add_message("Your attack was interrupted", colour.RED)
                        break

                if attack_viable:
                    dx = self.targeted_actor.x - self.entity.x
                    dy = self.targeted_actor.y - self.entity.y
                    distance = max(abs(dx), abs(dy))  # Chebyshev distance.

                    self.queued = True
                    self.distance = distance
                    self.attack()

            # attacker is AI
            else:
                self.queued = True
                self.entity.ai.queued_action = self

                # how many turns entity has to wait until attack
                self.entity.ai.turns_until_action = turns_to_skip


class ClearJam(Action):

    def __init__(self, entity: Actor, gun: Gun):
        self.gun = gun
        super().__init__(entity)

    def perform(self):

        proficiency = 1.0

        self.gun.jammed = False

        if self.entity.player:
            if self.gun.gun_type == 'pistol':
                proficiency = copy(self.entity.fighter.skill_pistol_proficiency)
            elif self.gun.gun_type == 'pdw':
                proficiency = copy(self.entity.fighter.skill_smg_proficiency)
            elif self.gun.gun_type == 'rifle':
                proficiency = copy(self.entity.fighter.skill_rifle_proficiency)
            elif self.gun.gun_type == 'bolt action':
                proficiency = copy(self.entity.fighter.skill_bolt_action_proficiency)

            proficiency = 1 - (proficiency / 4000)

        # jam takes between 2 and 5 seconds to clear
        jam_ap = randint(2, 5) * 100 * self.entity.fighter.action_ap_modifier * proficiency

        # skips player turns while clearing jam
        # if self.entity.player:
        self.engine.message_log.add_message(f"Cleared jam", colour.GREEN)
        if jam_ap >= 100:
            for i in range(round(jam_ap / 100)):
                self.engine.handle_enemy_turns()
            self.entity.fighter.ap -= jam_ap % 100
        else:
            self.entity.fighter.ap -= jam_ap
        # else:
        #     turns_to_skip = ceil(abs(self.entity.fighter.ap / (self.entity.fighter.ap_per_turn *
        #                                                        self.entity.fighter.ap_per_turn_modifier)))
        #     self.entity.ai.turns_until_action = turns_to_skip


class ReloadMagFed(Action):
    def __init__(self, entity: Actor, gun: GunMagFed, magazine_to_load: Magazine):
        super().__init__(entity)
        self.gun = gun
        self.magazine_to_load = magazine_to_load
        self.queued = False

        # resets previous target actor since need to reacquire target after reloading
        entity.previous_target_actor = None

    def perform(self) -> None:

        ap_cost = 0

        proficiency = 1.0

        # TODO - proficiencies for non-player characters eventually
        if self.entity.player:
            if self.gun.gun_type == 'pistol':
                proficiency = copy(self.entity.fighter.skill_pistol_proficiency)
            elif self.gun.gun_type == 'pdw':
                proficiency = copy(self.entity.fighter.skill_smg_proficiency)
            elif self.gun.gun_type == 'rifle':
                proficiency = copy(self.entity.fighter.skill_rifle_proficiency)
            elif self.gun.gun_type == 'bolt action':
                proficiency = copy(self.entity.fighter.skill_bolt_action_proficiency)

            proficiency = 1 - (proficiency / 4000)

        # AP cost calculated
        ap_cost += \
            self.entity.fighter.action_ap_modifier * self.gun.load_time_modifier * self.magazine_to_load.ap_to_load

        # adds cost of cycling manual action
        if self.gun.manual_action:
            ap_cost += self.gun.action_cycle_ap_cost

        ap_cost *= proficiency

        # sufficient AP cost or action queued
        if self.entity.fighter.ap >= ap_cost or self.queued:

            if not self.queued:
                self.entity.fighter.ap -= ap_cost

            # loads magazine into gun
            self.gun.load_gun(magazine=self.magazine_to_load)

        # insufficient AP to reload and not queued
        elif not self.queued:

            self.entity.fighter.ap -= ap_cost

            # calculates turns needed to regain AP
            turns_cost = ceil(abs(self.entity.fighter.ap / (self.entity.fighter.ap_per_turn *
                                                            self.entity.fighter.ap_per_turn_modifier)))

            # player reloading, handles turns
            if self.entity.player:

                self.gun.load_gun(magazine=self.magazine_to_load)

                for i in range(turns_cost):
                    self.engine.handle_enemy_turns()

            # ai reloading
            else:
                self.queued = True
                self.entity.ai.queued_action = self
                self.entity.ai.turns_until_action = turns_cost
                self.entity.ai.fleeing_turns = turns_cost


class LoadBulletsIntoMagazine(Action):
    def __init__(self, entity: Actor, magazine: Magazine, bullets_to_load: int, bullet_type: Bullet):
        super().__init__(entity)

        self.magazine = magazine
        self.queued = False

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
            if self.engine.player == entity:
                inventory.items.remove(bullet_type.parent)

        # resets previous target actor since need to reacquire target after reloading
        entity.previous_target_actor = None

    def perform(self) -> None:

        mag_class_type = type(self.magazine).__name__

        ap_cost = 0

        proficiency = 1.0

        ap_cost_modifier = self.entity.fighter.action_ap_modifier * self.bullet_type.load_time_modifier

        # loading integrated magazine gun
        if mag_class_type == "GunIntegratedMag":

            # TODO this should probably be handled by the consumables class

            if not self.magazine.keep_round_chambered and self.magazine.chambered_bullet is not None:
                AddToInventory(item=self.magazine.chambered_bullet.parent, amount=1, entity=self.entity)

            if self.entity.player:
                if self.magazine.gun_type == 'pistol':
                    proficiency = copy(self.entity.fighter.skill_pistol_proficiency)
                elif self.magazine.gun_type == 'pdw':
                    proficiency = copy(self.entity.fighter.skill_smg_proficiency)
                elif self.magazine.gun_type == 'rifle':
                    proficiency = copy(self.entity.fighter.skill_rifle_proficiency)
                elif self.magazine.gun_type == 'bolt action':
                    proficiency = copy(self.entity.fighter.skill_bolt_action_proficiency)

                proficiency = 1 - (proficiency / 4000)

            # adds cost of cycling manual action
            if self.magazine.manual_action:
                ap_cost += proficiency * self.magazine.action_cycle_ap_cost

            ap_cost_modifier *= self.magazine.load_time_modifier

        # adds cost of loading each bullet
        ap_cost += proficiency * self.bullets_to_load * ap_cost_modifier

        # sufficient AP cost or action queued
        if self.entity.fighter.ap >= ap_cost or self.queued:

            if not self.queued:
                self.entity.fighter.ap -= ap_cost

            # loads bullets into gun
            self.magazine.load_magazine(ammo=self.bullet_type,
                                        load_amount=self.bullets_to_load)

        # insufficient AP to reload and not queued
        elif not self.queued:

            self.entity.fighter.ap -= ap_cost

            # calculates turns needed to regain AP
            turns_cost = ceil(abs(self.entity.fighter.ap / (self.entity.fighter.ap_per_turn *
                                                            self.entity.fighter.ap_per_turn_modifier)))

            # player reloading, handles turns
            if self.entity.player:
                for i in range(turns_cost):
                    self.engine.handle_enemy_turns()

                self.magazine.load_magazine(ammo=self.bullet_type,
                                            load_amount=self.bullets_to_load)

            # ai reloading
            else:
                self.queued = True
                self.entity.ai.queued_action = self
                self.entity.ai.turns_until_action = turns_cost
                self.entity.ai.fleeing_turns = turns_cost


class MovementAction(ActionWithDirection):
    def perform(self) -> None:

        fighter = self.entity.fighter

        if fighter.ap >= fighter.move_ap_cost:

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

            # if chance for move action to fail
            if fighter.move_success_chance != 1.0:
                if random.uniform(0, 1) < fighter.move_success_chance:
                    self.entity.move(self.dx, self.dy)
                elif self.entity.player:
                    self.engine.message_log.add_message("You try to move but you stumble", colour.RED)
                    trying_to_move = True
                    while trying_to_move:
                        if random.uniform(0, 1) < fighter.move_success_chance:
                            self.entity.move(self.dx, self.dy)
                            TryToMove(self.entity, self.dx, self.dy).perform()
                            trying_to_move = False
                        else:
                            self.engine.handle_enemy_turns()

                self.engine.game_map.camera_xy = (self.engine.player.x, self.engine.player.y)

            else:
                self.entity.move(self.dx, self.dy)
                if self.entity.player:
                    self.engine.game_map.camera_xy = (self.engine.player.x, self.engine.player.y)
            fighter.ap -= fighter.move_ap_cost

        else:
            if self.entity.player:
                fighter.ap -= fighter.move_ap_cost
                turns_to_wait = ceil(abs(fighter.ap / (fighter.ap_per_turn * fighter.ap_per_turn_modifier))) + 1
                for i in range(turns_to_wait):
                    self.engine.handle_enemy_turns()

                self.perform()


class TryToMove(ActionWithDirection):
    def perform(self) -> None:
        if self.blocking_entity:
            self.engine.message_log.add_message("Movement interrupted - an enemy is in the way", colour.RED)
        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()


class BumpAction(ActionWithDirection):
    def perform(self) -> None:

        if self.blocking_entity:

            try:

                item_held = self.engine.player.inventory.held

                if item_held is not None:
                    return WeaponAttackAction(distance=1, item=item_held, entity=self.entity,
                                              targeted_actor=self.blocking_entity,
                                              targeted_bodypart=self.target_actor.bodyparts[0]).attack()

                else:
                    return UnarmedAttackAction(distance=1, entity=self.entity, targeted_actor=self.blocking_entity,
                                               targeted_bodypart=self.target_actor.bodyparts[0]).attack()

            except AttributeError:
                pass

        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()


class AddToInventory(Action):

    def __init__(self, entity: Actor, item: Item, amount: int):
        super().__init__(entity)
        self.item = item
        self.amount = amount
        self.item_copy = deepcopy(self.item)

    def perform(self) -> None:

        if self.item.stacking:

            # checks if there is enough capacity for the item
            if self.entity.inventory.current_item_weight() + self.item.weight * self.item.stacking.stack_size > \
                    self.entity.inventory.capacity:
                self.engine.message_log.add_message("Inventory full.", colour.RED)
                return

            if self.item.stacking.stack_size >= self.amount > 0:
                stack_amount = self.amount
            else:
                stack_amount = self.item.stacking.stack_size

            self.item_copy.stacking.stack_size = stack_amount

            # if item of this type already in inventory, tries to add it to existing stack
            repeat_found = False
            for i in self.entity.inventory.items:
                if i.name == self.item.name:
                    repeat_item_index = self.entity.inventory.items.index(i)
                    self.entity.inventory.items[repeat_item_index].stacking.stack_size += \
                        self.item_copy.stacking.stack_size
                    repeat_found = True

            if not repeat_found:
                # item of this type not already present in inventory
                self.entity.inventory.items.append(self.item_copy)

            self.item.stacking.stack_size -= self.item_copy.stacking.stack_size

            if self.item.stacking.stack_size <= 0:
                self.remove_from_container()

        else:

            if self.entity.inventory.current_item_weight() + self.item.weight > self.entity.inventory.capacity:
                self.engine.message_log.add_message("Inventory full.", colour.RED)

            else:
                self.entity.inventory.items.append(self.item_copy)
                self.remove_from_container()

        self.item_copy.parent = self.entity.inventory

    def remove_from_container(self):
        pass


class PickupAction(AddToInventory):
    def __init__(self, entity: Actor, item: Item, amount: int):
        super().__init__(entity, item, amount)

        entity.previous_target_actor = None

    def remove_from_container(self):
        self.engine.game_map.entities.remove(self.item)


class DropAction(Action):

    def __init__(self, entity: Actor, item: Item, drop_amount: int):
        super().__init__(entity)
        self.item = item
        self.drop_amount = drop_amount

        entity.previous_target_actor = None

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
        self.item.usable_properties.activate(self)


class RepairItem(Action):
    def __init__(self, entity: Actor, item_to_repair: Item, repair_kit_item: Item) -> None:
        super().__init__(entity)
        self.item_to_repair = item_to_repair
        self.repair_kit_item = repair_kit_item

    def perform(self) -> None:
        self.repair_kit_item.usable_properties.activate(self)


class HealPart(Action):
    def __init__(self, entity: Actor, part_to_heal: Bodypart, healing_item: Item) -> None:
        super().__init__(entity)
        self.part_to_heal = part_to_heal
        self.healing_item = healing_item

    def perform(self) -> None:
        self.healing_item.usable_properties.activate(self)
