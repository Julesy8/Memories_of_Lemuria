from __future__ import annotations

from typing import List, Tuple, TYPE_CHECKING

import numpy as np  # type: ignore
import tcod

from actions import Action, MeleeAction, MovementAction, WaitAction

if TYPE_CHECKING:
    from entity import Actor


class BaseAI(Action):
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
        self.entity.energy += self.entity.energy_regain

        while self.entity.energy > 0:

            entity_fleeing = False

            # checks if entity should be fleeing
            if self.entity.fears_death:
                for bodypart in self.entity.bodyparts:
                    if bodypart.vital and bodypart.hp < bodypart.max_hp/3:
                        entity_fleeing = True
                        break

            # perform melee action
            if distance <= 1 and self.entity.energy >= self.entity.attack_cost and not entity_fleeing:
                MeleeAction(self.entity, dx, dy).perform()
                self.entity.energy -= self.entity.attack_cost

            # any kind of move action occurring
            elif self.entity.energy >= self.entity.move_cost:

                # entity fleeing from target
                """
                if entity_fleeing and self.entity.active:
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
                    path_xy = tcod.path.hillclimb2d(distance_dijkstra, (self.entity.x, self.entity.y),
                                                    cardinal=True, diagonal=True)[1:].tolist()
                    if path_xy:
                        dest_x, dest_y = path_xy.pop(0)
                        self.entity.energy -= self.entity.move_cost
                        MovementAction(self.entity, dest_x - self.entity.x, dest_y - self.entity.y, ).perform()
                    else:
                        break
                """

                # path towards player given player is visible and entity is not fleeing
                # make elif if fleeing enabled
                if self.path and self.engine.game_map.visible[self.entity.x, self.entity.y] \
                        and self.entity.energy >= self.entity.move_cost:
                    dest_x, dest_y = self.path.pop(0)
                    self.entity.energy -= self.entity.move_cost
                    MovementAction(
                        self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                    ).perform()

                else:
                    # move towards the target if not too far away and entity is active
                    if self.entity.active and distance < self.entity.active_radius:
                        self.path = self.get_path_to(target.x, target.y)
                        if self.path:
                            dest_x, dest_y = self.path.pop(0)
                            self.entity.energy -= self.entity.move_cost
                            MovementAction(
                                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                            ).perform()
                        else:
                            break
                    else:
                        break

            # if target too far away, become inactive (stop following)
            elif self.entity.active and distance > 10:
                self.entity.active = False

            else:
                break

        return WaitAction(self.entity).perform()

    def move_towards(self):
        if self.path:
            dest_x, dest_y = self.path.pop(0)
            self.entity.energy -= self.entity.move_cost
            MovementAction(
                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
            ).perform()
        else:
            return
