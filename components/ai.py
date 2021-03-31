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
        self.entity.energy += self.entity.energy_regain

        while self.entity.energy > 0:

            if self.engine.game_map.visible[self.entity.x, self.entity.y]:

                if distance <= 1 and self.entity.energy >= self.entity.attack_cost:
                    MeleeAction(self.entity, dx, dy).perform()
                    self.entity.energy -= self.entity.attack_cost
                self.path = self.get_path_to(target.x, target.y)

                if self.path and self.entity.energy >= self.entity.move_cost:
                    dest_x, dest_y = self.path.pop(0)
                    self.entity.energy -= self.entity.move_cost
                    MovementAction(
                        self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                    ).perform()
                else:
                    break

            else:
                if self.entity.active and distance < 10:
                    self.path = self.get_path_to(target.x, target.y)

                    if self.path and self.entity.energy >= self.entity.move_cost:
                        dest_x, dest_y = self.path.pop(0)
                        self.entity.energy -= self.entity.move_cost
                        MovementAction(
                            self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                        ).perform()
                    else:
                        break

                elif self.entity.active and distance > 10:
                    self.entity.active = False

                else:
                    break

        return WaitAction(self.entity).perform()

    def path_to(self):
        if self.path and self.entity.energy >= self.entity.move_cost:
            dest_x, dest_y = self.path.pop(0)
            self.entity.energy -= self.entity.move_cost
            MovementAction(
                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
            ).perform()
        else:
            return

    def flee(self):
        # http://www.roguebasin.com/index.php?title=Dijkstra_Maps_Visualized#--_Fleeing_AI_--
        # makes the AI flee from the player
        if self.entity.energy >= self.entity.move_cost:
            cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)

            distance = tcod.path.maxarray((self.entity.gamemap.width, self.entity.gamemap.height), order="F")
            distance[self.engine.player.x, self.engine.player.y] = 0

            dijkstra_map = tcod.path.dijkstra2d(distance, cost, cardinal=2, diagonal=3)
            max_int = np.iinfo(dijkstra_map.dtype).max
            touched = (dijkstra_map != max_int)
            dijkstra_map[touched] *= -6
            dijkstra_map[touched] //= 5
            tcod.path.dijkstra2d(distance, cost, cardinal=2, diagonal=3)
            path_xy = tcod.path.hillclimb2d(distance, (self.entity.x, self.entity.y),
                                            cardinal=True, diagonal=True)[1:].tolist()
            if path_xy:
                dest_x, dest_y = path_xy.pop(0)
                self.entity.energy -= self.entity.move_cost
                MovementAction(self.entity, dest_x - self.entity.x, dest_y - self.entity.y,).perform()
            else:
                return

        else:
            return
