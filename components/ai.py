from __future__ import annotations

from typing import List, Tuple, Optional, TYPE_CHECKING

from random import randint, choice
import numpy as np  # type: ignore
import tcod

from components.consumables import GunMagFed, GunIntegratedMag, Gun, Weapon, Bullet, MeleeWeapon
from actions import Action, MovementAction, WaitAction, UnarmedAttackAction, \
    ReloadMagFed, LoadBulletsIntoMagazine, ReloadFromClip
from entity import Actor

if TYPE_CHECKING:
    from level_gen_tools import Rect


class BaseAI(Action):

    def __init__(self, entity: Actor, ):
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

    def execute_queued_action(self):
        if self.queued_action is not None:
            self.queued_action.handle_action()


class DeadAI(BaseAI):
    def __init__(self, entity: Actor):
        super().__init__(entity)

    def perform(self) -> None:
        pass


class PlayerCharacter(BaseAI):
    def __init__(self, entity: Actor):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []

    def perform(self) -> None:

        fighter = self.entity.fighter

        # AP regeneration
        fighter.ap += round(fighter.ap_per_turn * fighter.ap_per_turn_modifier)

        if self.entity.fighter.turns_attack_inactive >= 1:
            self.entity.fighter.turns_attack_inactive -= 1
        if self.entity.fighter.turns_move_inactive >= 1:
            self.entity.fighter.turns_move_inactive -= 1

        if self.entity.fighter.turns_move_inactive >= 1 and self.entity.fighter.turns_attack_inactive >= 1:
            return

        if self.entity.fighter.previous_target_actor is not None:
            # checks if previous target is still visible, if not resets to None
            if not self.engine.game_map.check_los(start_x=self.entity.fighter.previous_target_actor.x,
                                                  start_y=self.entity.fighter.previous_target_actor.y,
                                                  end_x=self.entity.x, end_y=self.entity.y):
                self.entity.previous_target_actor = None
                self.entity.previously_targeted_part = None

        if self.queued_action is not None:
            self.queued_action.handle_action()

        else:

            # any kind of movement action occurring
            if fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:

                if self.path:
                    dest_x, dest_y = self.path.pop(0)
                    MovementAction(
                        self.entity, dest_x - self.entity.x, dest_y - self.entity.y, handle_now=True
                    ).handle_action()


class HostileEnemy(BaseAI):
    def __init__(self, entity: Actor):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []
        self.attacking_target = True
        self.random_walk = False
        self.attack_radius = 1
        self.weapons_user = False
        self.roams = False

    def perform(self) -> None:

        target = self.entity.fighter.target_actor
        fighter = self.entity.fighter

        # AP regeneration
        fighter.ap += round(fighter.ap_per_turn * fighter.ap_per_turn_modifier)

        self.execute_queued_action()

        # if move or attack inactive, ticks down
        if self.entity.fighter.turns_attack_inactive >= 1:
            self.entity.fighter.turns_attack_inactive -= 1
        if self.entity.fighter.turns_move_inactive >= 1:
            self.entity.fighter.turns_move_inactive -= 1

        # cannot move or attack, returns
        if self.entity.fighter.turns_attack_inactive > 0 and self.entity.fighter.turns_move_inactive > 0:
            return

        distance = 1

        # target ai is none (target dead), resets to None
        if self.entity.fighter.target_actor is not None:
            if self.entity.fighter.target_actor.ai is None:
                self.entity.fighter.target_actor = None
            else:
                dx = target.x - self.entity.x
                dy = target.y - self.entity.y
                distance = max(abs(dx), abs(dy))  # Chebyshev distance.

            if self.random_walk and self.entity.fighter.target_actor is not None:
                if distance <= self.attack_radius:
                    self.attacking_target = True

        # checks if previous target is still visible, if not resets to None
        if self.entity.fighter.previous_target_actor is not None:
            if not self.engine.game_map.check_los(start_x=self.entity.fighter.previous_target_actor.x,
                                                  start_y=self.entity.fighter.previous_target_actor.y,
                                                  end_x=self.entity.x, end_y=self.entity.y):
                self.entity.previous_target_actor = None
                self.entity.previously_targeted_part = None

        # if no target, no current path and AI roams, paths to centre of a random room
        if self.entity.fighter.target_actor is None and self.roams and not self.path:
            random_room: Rect = choice(self.engine.game_map.rooms)
            if fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:
                self.path = self.get_path_to(random_room.centre()[0], random_room.centre()[1])

        attack_range = 1

        # if not attacking target and random_walk, moves in random directions until coming into attack radius of player
        if not self.attacking_target:
            if fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:
                if choice((True, False)):
                    MovementAction(
                        self.entity, randint(-1, 1), randint(-1, 1),
                    ).handle_action()
            return

        while fighter.ap > 0:

            # perform attack action
            if target is not None:
                if self.attack(attack_range=attack_range, distance=distance, target=target):
                    continue

            # any kind of movement action occurring
            if fighter.move_ap_cost <= fighter.ap and self.entity.fighter.turns_move_inactive <= 0:

                if target is not None:
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
                    continue

                else:
                    break

            break

        return WaitAction(self.entity).perform()

    def execute_queued_action(self):
        if self.queued_action is not None:
            self.queued_action.handle_action()

    def attack(self, distance, target, attack_range) -> bool:

        if target is None:
            return False

        if self.entity.fighter.ap > 0 >= self.entity.fighter.turns_attack_inactive and distance <= attack_range \
                and self.entity.fighter.fleeing_turns <= 0:

            UnarmedAttackAction(distance=distance, entity=self.entity, targeted_actor=target,
                                targeted_bodypart=None).handle_action()

            return True

        return False


class HostileAnimal(HostileEnemy):
    def __init__(self, entity: Actor):
        super().__init__(entity=entity)
        self.attacking_target = False
        self.attack_radius = 5
        self.random_walk = True
        self.weapons_user = False
        self.roams = False


class HostileEnemyArmed(HostileEnemy):
    def __init__(self, entity: Actor):
        super().__init__(entity=entity)
        self.attack_radius = 1
        self.attacking_target = True
        self.random_walk = False
        self.weapons_user = True
        self.roams = True

    def attack(self, distance: int, target, attack_range) -> bool:

        held_item = self.entity.inventory.held
        has_weapon = False

        # check held weapon type
        if held_item is not None:
            if isinstance(held_item.usable_properties, Weapon):
                has_weapon = True
                if isinstance(held_item.usable_properties, Gun):
                    attack_range = held_item.usable_properties.zero_range

        if target is None:
            return False

        self.path = self.get_path_to(target.x, target.y)

        if self.entity.fighter.ap > 0 >= self.entity.fighter.turns_attack_inactive and distance <= attack_range \
                and self.entity.fighter.fleeing_turns <= 0 and \
                target.fighter.visible_tiles[self.entity.x, self.entity.y] and self.queued_action is None:

            if attack_range == 1:

                # melee weapon attack
                if has_weapon:
                    if isinstance(held_item.usable_properties, MeleeWeapon):
                        held_item.usable_properties.get_attack_action(distance=distance,
                                                                      entity=self.entity,
                                                                      targeted_actor=target,
                                                                      targeted_bodypart=None).handle_action()
                        return True

                # unarmed attack
                UnarmedAttackAction(distance=distance, entity=self.entity, targeted_actor=target,
                                    targeted_bodypart=None).handle_action()

            # has gun equipped
            else:
                # mag fed gun
                if isinstance(held_item.usable_properties, GunMagFed):

                    # reload weapon
                    if held_item.usable_properties.chambered_bullet is None:
                        ReloadMagFed(entity=self.entity, gun=held_item.usable_properties,
                                     magazine_to_load=held_item.usable_properties.previously_loaded_magazine). \
                            handle_action()
                        self.entity.fighter.fleeing_turns = (
                            round(held_item.usable_properties.previously_loaded_magazine.ap_to_load
                                  / self.entity.fighter.ap_per_turn))

                    # round in chamber, attacks
                    else:
                        held_item.usable_properties.get_attack_action(distance=distance, entity=self.entity,
                                                                      targeted_actor=target,
                                                                      targeted_bodypart=None).handle_action()
                    return True

                # gun integrated mag
                elif isinstance(held_item.usable_properties, GunIntegratedMag):

                    # reload weapon
                    if held_item.usable_properties.chambered_bullet is None and isinstance(
                            held_item.usable_properties.previously_loaded_round.usable_properties, Bullet):

                        if held_item.usable_properties.previously_loaded_clip is not None:
                            # reload from clip
                            ReloadFromClip(entity=self.entity,
                                           clip=held_item.usable_properties.previously_loaded_clip,
                                           gun=held_item.usable_properties).handle_action()
                            self.entity.fighter.fleeing_turns = (
                                round(held_item.usable_properties.previously_loaded_clip.ap_to_load
                                      / self.entity.fighter.ap_per_turn))

                        else:
                            no_bullets_to_load = held_item.usable_properties.mag_capacity - \
                                                 len(held_item.usable_properties.magazine)
                            LoadBulletsIntoMagazine(entity=self.entity, magazine=held_item,
                                                    bullet_type=held_item.usable_properties.previously_loaded_round.usable_properties,
                                                    bullets_to_load=no_bullets_to_load).handle_action()

                    # round in chamber, attacks
                    else:
                        held_item.usable_properties.get_attack_action(distance=distance,
                                                                      entity=self.entity,
                                                                      targeted_actor=target,
                                                                      targeted_bodypart=None).handle_action()
                    return True

        # reload if magazine below half capacity and player not visible, reloads
        elif not target.fighter.visible_tiles[self.entity.x, self.entity.y] and has_weapon:

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
                            self.entity.fighter.fleeing_turns = (no_bullets_to_load * 2)
                            return True

                # magazine fed gun
                elif isinstance(held_item.usable_properties, GunMagFed):
                    loaded_magazine = getattr(held_item.usable_properties, 'loaded_magazine')
                    mag_capacity = getattr(loaded_magazine, 'mag_capacity')
                    mag_round_count = len(getattr(loaded_magazine, 'magazine'))

                    if mag_capacity < mag_round_count / 2:
                        if not isinstance(self.queued_action, ReloadMagFed):
                            (ReloadMagFed(entity=self.entity, gun=held_item,
                                          magazine_to_load=held_item.usable_properties.previously_loaded_magazine).
                             handle_action())
                            self.entity.fighter.fleeing_turns = (
                                round(held_item.usable_properties.previously_loaded_magazine.ap_to_load
                                      / self.entity.fighter.ap_per_turn))
                            return True
        return False
