from __future__ import annotations

from typing import List, Tuple, Optional

import numpy as np  # type: ignore
import tcod

from components.consumables import Gun, Weapon, MeleeWeapon
from actions import Action, WeaponAttackAction, MovementAction, WaitAction, UnarmedAttackAction, AttackAction, \
    ReloadAction
from entity import Actor


class BaseAI(Action):

    def __init__(self, entity: Actor):
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
            # Check that an enitiy blocks movement and the cost isn't zero (blocking.)
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
    def __init__(self, entity: Actor):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []

    def perform(self) -> None:
        target = self.engine.player
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        distance = max(abs(dx), abs(dy))  # Chebyshev distance.

        fighter = self.entity.fighter

        # AP regeneration
        fighter.ap += round(fighter.ap_per_turn * fighter.ap_per_turn_modifier)

        if self.entity.turns_attack_inactive >= 1:
            self.entity.turns_attack_inactive -= 1
        if self.entity.turns_move_inactive >= 1:
            self.entity.turns_move_inactive -= 1

        # check if holding weapon
        held_item = self.entity.inventory.held
        attack_range = 1
        has_weapon = False

        # check held weapon type
        if held_item is not None:
            if isinstance(held_item.usable_properties, Weapon):
                has_weapon = True
                if hasattr(held_item.usable_properties, 'enemy_attack_range'):
                    attack_range = held_item.usable_properties.enemy_attack_range

        self.execute_queued_action(distance, target)

        while fighter.ap > 0:
            # skips turn if both attack and move actions inactive for this turn
            if self.entity.turns_attack_inactive > 0 and self.entity.turns_move_inactive > 0:
                break

            # perform attack action
            if fighter.ap > 0 and self.entity.turns_attack_inactive <= 0 and distance <= attack_range \
                    and self.entity.fleeing_turns <= 0 and self.engine.game_map.visible[self.entity.x, self.entity.y]:

                if attack_range == 1:

                    # unarmed attack
                    if not has_weapon:
                        UnarmedAttackAction(distance=distance, entity=self.entity, targeted_actor=target,
                                            targeted_bodypart=None).attack()

                    # melee weapon attack
                    else:
                        WeaponAttackAction(distance=distance, item=held_item, entity=self.entity,
                                           targeted_actor=target, targeted_bodypart=None).attack()

                # has gun equipped
                else:
                    if isinstance(held_item.usable_properties, Gun):

                        # reload weapon
                        if held_item.usable_properties.chambered_bullet is None:

                            self.queued_action = ReloadAction(entity=self.entity, gun=held_item)

                        # round in chamber, attacks
                        else:
                            WeaponAttackAction(distance=distance, item=held_item, entity=self.entity,
                                               targeted_actor=target, targeted_bodypart=None).attack()

            # any kind of movement action occurring
            elif fighter.move_ap_cost <= fighter.ap and self.entity.turns_move_inactive <= 0:

                # entity fleeing from target
                if self.entity.fleeing_turns > 0:

                    print('yes')
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
                    self.entity.fleeing_turns -= 1

                # entity not fleeing
                else:
                    # move towards the target
                    self.path = self.get_path_to(target.x, target.y)

                if self.path:
                    dest_x, dest_y = self.path.pop(0)
                    MovementAction(
                        self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                    ).perform()

                else:
                    break

            else:
                break

        return WaitAction(self.entity).perform()

    def execute_queued_action(self, distance, target):
        # checks if the queued action can still be performed
        if self.queued_action is not None:  # and self.entity.turns_attack_inactive == 0

            held_item = self.entity.inventory.held
            action_viable = True

            # for attack actions
            if isinstance(self.queued_action, AttackAction):

                # target still visible
                if self.engine.game_map.visible[target.x, target.y]:

                    # updates distance
                    self.queued_action.distance = distance

                    # attack with a weapon
                    if isinstance(self.queued_action, WeaponAttackAction):
                        # check if still holding weapon
                        if not self.queued_action.item == held_item:
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

                        self.turns_until_action -= 1

                        # no more wait turns
                        if self.turns_until_action == 0:
                            self.queued_action.attack()
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
            if isinstance(self.queued_action, ReloadAction):

                # check if gun still held
                if not self.queued_action.gun == held_item:
                    action_viable = False

                if action_viable:
                    self.turns_until_action -= 1

                    # no more wait turns
                    if self.turns_until_action == 0:
                        self.queued_action.perform()
                        self.queued_action = None
