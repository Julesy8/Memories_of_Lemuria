from __future__ import annotations

from typing import List, Tuple, Optional

from random import randint, choice
import numpy as np  # type: ignore
import tcod

from components.consumables import GunMagFed, GunIntegratedMag, Gun, Weapon, MeleeWeapon, Bullet
from actions import Action, MovementAction, WaitAction, UnarmedAttackAction, AttackAction, \
    ReloadMagFed, LoadBulletsIntoMagazine, MeleeAttackAction, GunAttackAction
from entity import Actor

# TODO - make this more modular and clean

class BaseAI(Action):

    def __init__(self,entity: Actor,):
        self.queued_action: Optional[Action] = None
        self.turns_until_action: int = 0
        super().__init__(entity)

    def perform(self) -> None:
        raise NotImplementedError()

    def get_path_to(self, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
        """
        Compute and return a path to the target position.

        If there is no valid path then returns an empty list.
        """
        # Copy the walkable array.
        cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)

        for entity in self.entity.gamemap.entities:
            # Check that an entity blocks movement and the cost isn't zero (blocking.)
            if entity.blocks_movement and cost[entity.x, entity.y]:
                # Add to the cost of a blocked position.
                # A lower number means more enemies will crowd behind each other in
                # hallways.  A higher number means enemies will take longer paths in
                # order to surround the player.
                cost[entity.x, entity.y] += 10

        # Create a graph from the cost array and pass that graph to a new pathfinder.
        graph = tcod.path.SimpleGraph(cost=cost, cardinal=2, diagonal=3)
        pathfinder = tcod.path.Pathfinder(graph)

        pathfinder.add_root((self.entity.x, self.entity.y))  # Start position.

        # Compute the path to the destination and remove the starting point.
        path: List[List[int]] = pathfinder.path_to((dest_x, dest_y))[1:].tolist()

        # Convert from List[List[int]] to List[Tuple[int, int]].
        return [(index[0], index[1]) for index in path]


class HostileEnemy(BaseAI):
    def __init__(self,entity: Actor,):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []

    def perform(self) -> None:
        target = self.entity.fighter.target_actor
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        distance = max(abs(dx), abs(dy))  # Chebyshev distance.

        fighter = self.entity.fighter

        # AP regeneration
        fighter.ap += round(fighter.ap_per_turn * fighter.ap_per_turn_modifier)

        if self.entity.fighter.turns_attack_inactive >= 1:
            self.entity.fighter.turns_attack_inactive -= 1
        if self.entity.fighter.turns_move_inactive >= 1:
            self.entity.fighter.turns_move_inactive -= 1

        attack_range = 1

        self.execute_queued_action(distance, target)

        # checks if previous target actor is still visible, if not resets to None
        if self.entity.fighter.previous_target_actor is not None:
            if not target.fighter.visible_tiles[self.entity.fighter.previous_target_actor.x,
            self.entity.fighter.previous_target_actor.y]:
                self.engine.player.fighter.previous_target_actor = None
                self.engine.player.fighter.previously_targeted_part = None

        while fighter.ap > 0:
            # skips turn if both attack and move actions inactive for this turn
            if self.entity.fighter.turns_attack_inactive > 0 and self.entity.fighter.turns_move_inactive > 0:
                break

            # perform attack action
            if fighter.ap > 0 >= self.entity.fighter.turns_attack_inactive and distance <= attack_range \
                    and self.entity.fighter.fleeing_turns <= 0 and \
                    target.fighter.visible_tiles[self.entity.x, self.entity.y]:

                if attack_range == 1:
                    UnarmedAttackAction(distance=distance, entity=self.entity, targeted_actor=target,
                                        targeted_bodypart=None).handle_action()

            # any kind of movement action occurring
            elif fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:

                # entity fleeing from target
                if self.entity.fighter.fleeing_turns > 0:

                    cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)
                    distance_dijkstra = tcod.path.maxarray((self.entity.gamemap.width,
                                                            self.entity.gamemap.height), order="F")
                    distance_dijkstra[target.x, target.y] = 0
                    tcod.path.dijkstra2d(distance_dijkstra, cost, cardinal=2, diagonal=3)
                    max_int = np.iinfo(distance_dijkstra.dtype).max
                    touched = (distance_dijkstra != max_int)
                    distance_dijkstra[touched] *= -6
                    distance_dijkstra[touched] //= 5
                    tcod.path.dijkstra2d(distance_dijkstra, cost, cardinal=2, diagonal=3)
                    self.path = tcod.path.hillclimb2d(distance_dijkstra, (self.entity.x, self.entity.y),
                                                      cardinal=True, diagonal=True)[1:].tolist()
                    self.entity.fighter.fleeing_turns -= 1

                # entity not fleeing and can see target, sets path to them
                elif target.fighter.visible_tiles[self.entity.x, self.entity.y] and \
                        self.entity.fighter.fleeing_turns == 0:
                    self.path = self.get_path_to(target.x, target.y)

                if self.path:
                    dest_x, dest_y = self.path.pop(0)
                    MovementAction(
                        self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                    ).handle_action()

                else:
                    break

            else:
                break

        return WaitAction(self.entity).perform()

    def execute_queued_action(self, distance, target):
        # checks if the queued action can still be performed
        if self.queued_action is not None:  # and self.entity.turns_attack_inactive == 0

            action_viable = True

            # for attack actions
            if isinstance(self.queued_action, AttackAction):

                # target still visible
                if target.fighter.visible_tiles[self.entity.x, self.entity.y]:

                    # updates distance
                    self.queued_action.distance = distance

                    if not distance == 1:
                        action_viable = False

                    # attack still viable
                    if action_viable:

                        self.turns_until_action -= 1

                        # no more wait turns
                        if self.turns_until_action == 0:
                            self.queued_action.handle_action()
                            self.queued_action = None

                    # attack not viable, cancels queued attack
                    else:
                        self.queued_action = None
                        # gives back the AP that would have been used for the remaining segment of the attack
                        self.entity.fighter.ap += round(self.turns_until_action * self.entity.fighter.ap_per_turn)
                        self.turns_until_action = 0

                # entity no longer visible, cancels queued attack
                else:
                    self.queued_action = None
                    self.turns_until_action = 0


class HostileAnimal(HostileEnemy):
    def __init__(self, entity: Actor,):
        super().__init__(entity)
        self.attack_radius = 5
        self.attacking_target = False

    def perform(self) -> None:
        target = self.entity.fighter.target_actor
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        distance = max(abs(dx), abs(dy))  # Chebyshev distance.

        fighter = self.entity.fighter

        if distance <= self.attack_radius:
            self.attacking_target = True

        # AP regeneration
        fighter.ap += round(fighter.ap_per_turn * fighter.ap_per_turn_modifier)

        # if not attacking target, moves in random directions until coming into attack radius of player
        if not self.attacking_target:
            if fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:
                if choice((True, False)):
                    MovementAction(
                        self.entity, randint(-1, 1), randint(-1, 1),
                    ).handle_action()
            return

        if self.entity.fighter.turns_attack_inactive >= 1:
            self.entity.fighter.turns_attack_inactive -= 1
        if self.entity.fighter.turns_move_inactive >= 1:
            self.entity.fighter.turns_move_inactive -= 1

        attack_range = 1

        self.execute_queued_action(distance, target)

        # checks if previous target actor is still visible, if not resets to None
        if self.entity.fighter.previous_target_actor is not None:
            if not target.fighter.visible_tiles[self.entity.fighter.previous_target_actor.x,
            self.entity.fighter.previous_target_actor.y]:
                self.engine.player.fighter.previous_target_actor = None
                self.engine.player.fighter.previously_targeted_part = None

        while fighter.ap > 0:

            # skips turn if both attack and move actions inactive for this turn
            if self.entity.fighter.turns_attack_inactive > 0 and self.entity.fighter.turns_move_inactive > 0:
                break

            # perform attack action
            if fighter.ap > 0 and self.entity.fighter.turns_attack_inactive <= 0 and distance <= attack_range \
                    and self.entity.fighter.fleeing_turns <= 0 and \
                    target.fighter.visible_tiles[self.entity.x, self.entity.y]:

                UnarmedAttackAction(distance=distance, entity=self.entity, targeted_actor=target,
                                    targeted_bodypart=None).handle_action()

            # any kind of movement action occurring
            elif fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:

                # entity fleeing from target
                if self.entity.fighter.fleeing_turns > 0:

                    cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)
                    distance_dijkstra = tcod.path.maxarray((self.entity.gamemap.width,
                                                            self.entity.gamemap.height), order="F")
                    distance_dijkstra[target.x, target.y] = 0
                    tcod.path.dijkstra2d(distance_dijkstra, cost, cardinal=2, diagonal=3)
                    max_int = np.iinfo(distance_dijkstra.dtype).max
                    touched = (distance_dijkstra != max_int)
                    distance_dijkstra[touched] *= -6
                    distance_dijkstra[touched] //= 5
                    tcod.path.dijkstra2d(distance_dijkstra, cost, cardinal=2, diagonal=3)
                    self.path = tcod.path.hillclimb2d(distance_dijkstra, (self.entity.x, self.entity.y),
                                                      cardinal=True, diagonal=True)[1:].tolist()
                    self.entity.fighter.fleeing_turns -= 1

                # entity not fleeing and can see target, sets path to them
                elif target.fighter.visible_tiles[self.entity.x, self.entity.y] and \
                        self.entity.fighter.fleeing_turns == 0:
                    self.path = self.get_path_to(target.x, target.y)

                if self.path:
                    dest_x, dest_y = self.path.pop(0)
                    MovementAction(
                        self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                    ).handle_action()

                else:
                    break

            else:
                break

        return WaitAction(self.entity).perform()


class HostileEnemyArmed(BaseAI):
    def __init__(self, entity: Actor,):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []

    def perform(self) -> None:

        # print('performing AI method')

        target = self.entity.fighter.target_actor
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        distance = max(abs(dx), abs(dy))  # Chebyshev distance.

        fighter = self.entity.fighter

        # AP regeneration
        fighter.ap += round(fighter.ap_per_turn * fighter.ap_per_turn_modifier)

        if self.entity.fighter.turns_attack_inactive >= 1:
            self.entity.fighter.turns_attack_inactive -= 1
        if self.entity.fighter.turns_move_inactive >= 1:
            self.entity.fighter.turns_move_inactive -= 1

        # check if holding weapon
        held_item = self.entity.inventory.held
        attack_range = 1
        has_weapon = False
        reload_check = True

        # check held weapon type
        if held_item is not None:
            if isinstance(held_item.usable_properties, Weapon):
                has_weapon = True
                if isinstance(held_item.usable_properties, Gun):
                    attack_range = held_item.usable_properties.zero_range

        self.execute_queued_action(distance, target)

        # checks if previous target actor is still visible, if not resets to None
        if self.entity.fighter.previous_target_actor is not None:
            if not target.fighter.visible_tiles[self.entity.fighter.previous_target_actor.x,
            self.entity.fighter.previous_target_actor.y]:
                self.engine.player.fighter.previous_target_actor = None
                self.engine.player.fighter.previously_targeted_part = None

        while fighter.ap > 0:
            # print('entered loop')
            # skips turn if both attack and move actions inactive for this turn
            if self.entity.fighter.turns_attack_inactive > 0 and self.entity.fighter.turns_move_inactive > 0:
                break

            # perform attack action
            if fighter.ap > 0 and self.entity.fighter.turns_attack_inactive <= 0 and distance <= attack_range \
                    and self.entity.fighter.fleeing_turns <= 0 and \
                    target.fighter.visible_tiles[self.entity.x, self.entity.y] and self.queued_action is None:

                self.path = self.get_path_to(target.x, target.y)

                if attack_range == 1:

                    # unarmed attack
                    if not has_weapon:
                        UnarmedAttackAction(distance=distance, entity=self.entity, targeted_actor=target,
                                            targeted_bodypart=None).handle_action()

                    # melee weapon attack
                    else:
                        if isinstance(held_item.usable_properties, Weapon):
                            held_item.usable_properties.get_attack_action(distance=distance, entity=self.entity,
                                                                          targeted_actor=target, targeted_bodypart=None)

                # has gun equipped
                else:
                    # mag fed gun
                    if isinstance(held_item.usable_properties, GunMagFed):

                        # reload weapon
                        if held_item.usable_properties.chambered_bullet is None:
                            # print('reloading')
                            ReloadMagFed(entity=self.entity, gun=held_item.usable_properties,
                                         magazine_to_load=held_item.usable_properties.previously_loaded_magazine). \
                                handle_action()

                        # round in chamber, attacks
                        else:
                            # print('shooting')
                            held_item.usable_properties.get_attack_action(distance=distance, entity=self.entity,
                                                                          targeted_actor=target, targeted_bodypart=None)

                    # gun integrated mag
                    elif isinstance(held_item.usable_properties, GunIntegratedMag):

                        no_bullets_to_load = held_item.usable_properties.mag_capacity - \
                                             len(held_item.usable_properties.magazine)

                        # reload weapon
                        if held_item.usable_properties.chambered_bullet is None and isinstance(
                                held_item.usable_properties.previously_loaded_round.usable_properties, Bullet):
                            LoadBulletsIntoMagazine(entity=self.entity, magazine=held_item,
                                                    bullet_type=held_item.usable_properties.previously_loaded_round.usable_properties,
                                                    bullets_to_load=no_bullets_to_load).handle_action()

                        # round in chamber, attacks
                        else:
                            held_item.usable_properties.get_attack_action(distance=distance, entity=self.entity,
                                                                          targeted_actor=target, targeted_bodypart=None)

            # reload if magazine below half capacity and player not visible, reloads
            elif not target.fighter.visible_tiles[self.entity.x, self.entity.y] and has_weapon and reload_check:

                # print('reload check')

                reload_check = False

                if isinstance(held_item.usable_properties, Gun):

                    # integrated magazine gun
                    if isinstance(held_item.usable_properties, GunIntegratedMag):
                        mag_capacity = getattr(held_item.usable_properties, 'mag_capacity')
                        mag_round_count = len(getattr(held_item.usable_properties, 'magazine'))
                        no_bullets_to_load = mag_capacity - mag_round_count

                        if mag_capacity < mag_round_count / 2:
                            if not isinstance(self.queued_action, LoadBulletsIntoMagazine) and isinstance(
                                held_item.usable_properties.previously_loaded_round.usable_properties, Bullet):
                                LoadBulletsIntoMagazine(entity=self.entity, magazine=held_item,
                                                        bullet_type=held_item.usable_properties.previously_loaded_round.usable_properties,
                                                        bullets_to_load=no_bullets_to_load).handle_action()
                                pass

                    # magazine fed gun
                    elif isinstance(held_item.usable_properties, GunMagFed):
                        loaded_magazine = getattr(held_item.usable_properties, 'loaded_magazine')
                        mag_capacity = getattr(loaded_magazine, 'mag_capacity')
                        mag_round_count = len(getattr(loaded_magazine, 'magazine'))

                        if mag_capacity < mag_round_count / 2:
                            if not isinstance(self.queued_action, ReloadMagFed):
                                ReloadMagFed(entity=self.entity, gun=held_item,
                                             magazine_to_load=held_item.usable_properties.previously_loaded_magazine). \
                                    perform()
                                pass

            # any kind of movement action occurring
            elif fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:

                # print('moving')

                # entity fleeing from target
                if self.entity.fighter.fleeing_turns > 0:

                    cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)
                    distance_dijkstra = tcod.path.maxarray((self.entity.gamemap.width,
                                                            self.entity.gamemap.height), order="F")
                    distance_dijkstra[target.x, target.y] = 0
                    tcod.path.dijkstra2d(distance_dijkstra, cost, cardinal=2, diagonal=3)
                    max_int = np.iinfo(distance_dijkstra.dtype).max
                    touched = (distance_dijkstra != max_int)
                    distance_dijkstra[touched] *= -6
                    distance_dijkstra[touched] //= 5
                    tcod.path.dijkstra2d(distance_dijkstra, cost, cardinal=2, diagonal=3)
                    self.path = tcod.path.hillclimb2d(distance_dijkstra, (self.entity.x, self.entity.y),
                                                      cardinal=True, diagonal=True)[1:].tolist()
                    self.entity.fighter.fleeing_turns -= 1

                # entity not fleeing and can see target, sets path to them
                elif target.fighter.visible_tiles[self.entity.x, self.entity.y] and \
                        self.entity.fighter.fleeing_turns == 0:
                    # print('set path')
                    self.path = self.get_path_to(target.x, target.y)

                if self.path:
                    # print('pathing towards')
                    dest_x, dest_y = self.path.pop(0)
                    MovementAction(
                        self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                    ).handle_action()

                else:
                    break

            else:
                break

        return WaitAction(self.entity).perform()

    def execute_queued_action(self, distance, target):

        # checks if the queued action can still be performed
        if self.queued_action is not None:  # and self.entity.turns_attack_inactive == 0

            # print('executing queued action: ', self.queued_action)

            held_item = self.entity.inventory.held
            action_viable = True

            # for attack actions
            if isinstance(self.queued_action, AttackAction):

                # target still visible
                if target.fighter.visible_tiles[self.entity.x, self.entity.y]:

                    # updates distance
                    self.queued_action.distance = distance

                    # attack with a weapon
                    if isinstance(self.queued_action, MeleeAttackAction) or isinstance(self.queued_action, GunAttackAction):
                        # check if still holding weapon
                        if not self.queued_action.weapon == held_item:
                            action_viable = False

                        # if melee weapon checks if in range
                        if isinstance(held_item.usable_properties, MeleeWeapon):
                            if not distance == 1:
                                action_viable = False

                    # unarmed attack
                    else:
                        # checks if in range for unarmed attack
                        if not distance == 1:
                            action_viable = False

                    # attack still viable
                    if action_viable:

                        # print('passed action viable check')

                        self.turns_until_action -= 1

                        # no more wait turns
                        if self.turns_until_action <= 0:
                            self.queued_action.handle_action()
                            self.queued_action = None

                    # attack not viable, cancels queued attack
                    else:
                        self.queued_action = None
                        # gives back the AP that would have been used for the remaining segment of the attack
                        self.entity.fighter.ap += round(self.turns_until_action * self.entity.fighter.ap_per_turn)
                        self.turns_until_action = 0

                # entity no longer visible, cancels queued attack
                else:
                    self.queued_action = None
                    self.turns_until_action = 0

            # reload action
            if isinstance(self.queued_action, LoadBulletsIntoMagazine) or isinstance(self.queued_action, ReloadMagFed):

                # check if gun still held
                if not self.queued_action.gun == held_item.usable_properties:
                    action_viable = False

                if action_viable:

                    self.turns_until_action -= 1

                    # no more wait turns
                    if self.turns_until_action <= 0:
                        self.queued_action.handle_action()
                        self.queued_action = None

                # reload not viable, cancels queued reload
                else:
                    self.queued_action = None
                    # gives back the AP that would have been used for the reload
                    self.entity.fighter.ap += round(self.turns_until_action * self.entity.fighter.ap_per_turn)
                    self.turns_until_action = 0
