from __future__ import annotations

from typing import List, Tuple

import numpy as np  # type: ignore
import tcod

from actions import Action, MeleeAction, MovementAction, WaitAction
from components.npc_templates import BaseComponent
from entity import Actor

class BaseAI(Action, BaseComponent):
    def perform(self) -> None:
        raise NotImplementedError()

    def get_path_to(self, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
        """Compute and return a path to the target position.

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

        if self.engine.game_map.visible[self.entity.x, self.entity.y]:
            if distance <= 1:
                return MeleeAction(self.entity, dx, dy).perform()

            self.path = self.get_path_to(target.x, target.y)

        if self.path:
            dest_x, dest_y = self.path.pop(0)
            return MovementAction(
                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
            ).perform()

        return WaitAction(self.entity).perform()

"""
class Melee:
    def __init__(self, fov_radius, active=False):
        self.fov_radius = fov_radius
        self.active = active

    def take_turn(self, target, fov_map, game_map, entities):
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            #turn_taken = True
            # if monster.active is false (first time seeing monster), sets it to true
            #if not self.active:
             #   self.active = True
            # adds 100 to monster.energy, this way monsters can deplete energy for multiple turns and
            # regain it over time
            monster.fighter.energy += 100

            while monster.fighter.energy > 0:
                # if distance to target >= 2 and the monster has enough energy to move, moves towards target,
                # subtracts move cost from monster.energy
                if monster.distance_to(target) >= 2 and monster.fighter.energy >= monster.fighter.move_cost:
                    monster.move_astar(target, entities, game_map)
                    monster.fighter.energy -= monster.fighter.move_cost

                # if the target is alive and monster has enough energy to attack, attacks
                elif target.fighter.alive and monster.fighter.energy >= monster.fighter.attack_cost:
                    print('Melee attack by {0}!'.format(monster.name))
                    monster.fighter.energy -= monster.fighter.attack_cost
        '''
        elif self.active:
            # if the monster has been sighted before, checks if the player is within its 'sensing radius', if it is
            # then moves towards the target
        THIS IS SURPREMELY FUCKED
            if monster.distance_to(target) <= self.fov_radius:
                monster.move_astar(target, entities, game_map)
                monster.fighter.energy -= monster.fighter.move_cost
        '''
"""

