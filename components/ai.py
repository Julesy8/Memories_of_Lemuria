import tcod as libtcod


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
        """
        elif self.active:
            # if the monster has been sighted before, checks if the player is within its 'sensing radius', if it is
            # then moves towards the target
        THIS IS SURPREMELY FUCKED
            if monster.distance_to(target) <= self.fov_radius:
                monster.move_astar(target, entities, game_map)
                monster.fighter.energy -= monster.fighter.move_cost
        """