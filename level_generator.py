import copy

from random import random, randint, choice, choices

from level_gen_tools import generate_char_arrays, select_random_tile, Rect
from colours_and_chars import MapColoursChars
from game_map import GameMap
from level_parameters import Enemies_by_level, Items_by_level
from tile_types import down_stairs

from components.consumables import Gun, GunIntegratedMag, GunMagFed
from components.weapons.bullets import bullet_dict
from components.weapons.magazines import magazine_dict
from components.enemies.caverns import caverns_enemies

class MessyBSPTree:
    """
    A Binary Space Partition connected by a severely weighted
    drunkards walk algorithm.
    """

    def __init__(self, messy_tunnels, map_width, map_height, max_leaf_size, room_max_size,
                 room_min_size, max_monsters_per_room, max_items_per_room, engine, current_level):
        self.messy_tunnels = messy_tunnels
        self.map_width = map_width
        self.map_height = map_height
        self.current_level = current_level
        self.room = None
        self.max_leaf_size = max_leaf_size
        self.room_max_size = room_max_size
        self.room_min_size = room_min_size
        self.max_monsters_per_room = max_monsters_per_room
        self.max_items_per_room = max_items_per_room
        self.player = engine.player
        self._rooms = []

        # makes tuple of possible combinations of tile colours and characters
        self.colours_chars_tuple = MapColoursChars(current_level)

        # makes tuple of colours and characters into an array usable by new_tile
        self.colours_chars_array = generate_char_arrays(self.colours_chars_tuple.floor_fg_dark(),
                                                        self.colours_chars_tuple.floor_bg_dark(),
                                                        self.colours_chars_tuple.floor_fg_light(),
                                                        self.colours_chars_tuple.floor_bg_light(),
                                                        self.colours_chars_tuple.floor_tile()
                                                        )

        # change debug_fov to True to disable fov, False to enable
        self.dungeon = GameMap(engine, map_width, map_height, current_level, debug_fov=True, entities=[self.player])

    def generateLevel(self):
        # Creates an empty 2D array or clears existing array
        self._leafs = []

        rootLeaf = Leaf(0, 0, self.map_width, self.map_height - 4, self.messy_tunnels)
        self._leafs.append(rootLeaf)

        splitSuccessfully = True
        # loop through all leaves until they can no longer split successfully
        while splitSuccessfully:
            splitSuccessfully = False
            for l in self._leafs:
                if (l.child_1 is None) and (l.child_2 is None):
                    if ((l.width > self.max_leaf_size) or
                            (l.height > self.max_leaf_size) or
                            (random() > 0.8)):
                        if l.splitLeaf():  # try to split the leaf
                            self._leafs.append(l.child_1)
                            self._leafs.append(l.child_2)
                            splitSuccessfully = True

        rootLeaf.createRooms(self)

        # generates a room number for player and stairs to spawn in
        player_spawn_room = randint(0, len(self._rooms) - 1)
        stair_room = randint(0, len(self._rooms) - 1)

        # if player and stairs meant to spawn in the same room, regenerates stair room until it is not
        while stair_room == player_spawn_room:
            stair_room = randint(0, len(self._rooms) - 1)

        for room in self._rooms:
            if room == self._rooms[player_spawn_room]:
                room_centre_x, room_centre_y = room.centre()
                self.player.place(room_centre_x, room_centre_y, self.dungeon)

            else:
                place_entities(room, self.dungeon, self.max_monsters_per_room,
                               self.max_items_per_room, self.current_level)

            if room == self._rooms[stair_room]:
                room_centre_x, room_centre_y = room.centre()
                self.dungeon.tiles[room_centre_x, room_centre_y] = down_stairs
                self.dungeon.downstairs_location = room_centre_x, room_centre_y

        return self.dungeon

    def createRoom(self, room):
        # set all tiles within a rectangle to be floors
        self._rooms.append(room)
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.dungeon.tiles[x, y] = select_random_tile(self.colours_chars_array)

    def createHall(self, room1, room2):

        if self.messy_tunnels:
            # drunkards walk from room 1 to room 2
            drunkardX, drunkardY = room2.centre()
            goalX, goalY = room1.centre()
            while not (room1.x1 <= drunkardX <= room1.x2) or not (room1.y1 < drunkardY < room1.y2):
                # chooses direction
                north = 1.0
                south = 1.0
                east = 1.0
                west = 1.0

                weight = 1

                # weight the random walk against edges
                if drunkardX < goalX:  # drunkard left of point1
                    east += weight
                elif drunkardX > goalX:  # drunkard right of point1
                    west += weight
                if drunkardY < goalY:  # drunkard above point1
                    south += weight
                elif drunkardY > goalY:  # drunkard below point1
                    north += weight

                # normalize probabilities so they form a range from 0 to 1
                total = north + south + east + west
                north /= total
                south /= total
                east /= total
                west /= total

                # choose direction
                choice = random()
                if 0 <= choice < north:
                    dx = 0
                    dy = -1
                elif north <= choice < (north + south):
                    dx = 0
                    dy = 1
                elif (north + south) <= choice < (north + south + east):
                    dx = 1
                    dy = 0
                else:
                    dx = -1
                    dy = 0

                # check collision at edges
                if (0 < drunkardX + dx < self.map_width - 1) and (0 < drunkardY + dy < self.map_height - 5):
                    drunkardX += dx
                    drunkardY += dy
                    drunkardX = int(drunkardX)
                    drunkardY = int(drunkardY)
                    if not self.dungeon.tiles[drunkardX, drunkardY][0]:
                        self.dungeon.tiles[drunkardX, drunkardY] = select_random_tile(self.colours_chars_array)
        else:
            # connect two rooms by straight hallways
            x1, y1 = room1.centre()
            x2, y2 = room2.centre()
            # 50% chance that a tunnel will start horizontally
            if randint(0, 1) == 1:
                self.createHorTunnel(x1, x2, y1)
                self.createVirTunnel(y1, y2, x2)

            else:  # else it starts vertically
                self.createVirTunnel(y1, y2, x1)
                self.createHorTunnel(x1, x2, y2)

    def createHorTunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.dungeon.tiles[x, y] = select_random_tile(self.colours_chars_array)

    def createVirTunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.dungeon.tiles[x, y] = select_random_tile(self.colours_chars_array)


class Leaf:  # used for the BSP tree algorithm
    def __init__(self, x, y, width, height, messy_tunnels):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.messy_tunnels = messy_tunnels
        self.min_leaf_size = 10
        self.child_1 = None
        self.child_2 = None
        self.room = None
        self.hall = None

    def splitLeaf(self):
        # begin splitting the leaf into two children
        if (self.child_1 is not None) or (self.child_2 is not None):
            return False  # This leaf has already been split

        '''
        Determines the direction of the split
        If the width of the leaf is >25% larger than the height,
        split the leaf vertically.
        If the height of the leaf is >25 larger than the width,
        split the leaf horizontally.
        Otherwise, choose the direction at random.
        '''

        splitHorizontally = choice([True, False])
        if self.width / self.height >= 1.25:
            splitHorizontally = False
        elif self.height / self.width >= 1.25:
            splitHorizontally = True

        if splitHorizontally:
            max = self.height - self.min_leaf_size
        else:
            max = self.width - self.min_leaf_size

        if max <= self.min_leaf_size:
            return False  # the leaf is too small to split further

        split = randint(self.min_leaf_size, max)  # determine where to split the leaf

        if splitHorizontally:
            self.child_1 = Leaf(self.x, self.y, self.width, split, self.messy_tunnels)
            self.child_2 = Leaf(self.x, self.y + split, self.width, self.height - split, self.messy_tunnels)
        else:
            self.child_1 = Leaf(self.x, self.y, split, self.height, self.messy_tunnels)
            self.child_2 = Leaf(self.x + split, self.y, self.width - split, self.height, self.messy_tunnels)

        return True

    def createRooms(self, bspTree):
        if self.child_1 or self.child_2:
            # recursively search for children until you hit the end of the branch
            if self.child_1:
                self.child_1.createRooms(bspTree)
            if self.child_2:
                self.child_2.createRooms(bspTree)

            if self.child_1 and self.child_2:
                bspTree.createHall(self.child_1.getRoom(),
                                self.child_2.getRoom())

        else:
            # Create rooms in the end branches of the bsp tree
            w = randint(bspTree.room_min_size, min(bspTree.room_max_size, self.width - 1))
            h = randint(bspTree.room_min_size, min(bspTree.room_max_size, self.height - 1))
            x = randint(self.x, self.x + (self.width - 1) - w)
            y = randint(self.y, self.y + (self.height - 1) - h)
            self.room = Rect(x, y, w, h)
            bspTree.createRoom(self.room)

    def getRoom(self):
        if self.room:
            return self.room

        else:
            if self.child_1:
                self.room_1 = self.child_1.getRoom()
            if self.child_2:
                self.room_2 = self.child_2.getRoom()

            if not self.child_1 and not self.child_2:
                # neither room_1 nor room_2
                return None

            elif not self.room_2:
                # room_1 and !room_2
                return self.room_1

            elif not self.room_1:
                # room_2 and !room_1
                return self.room_2

            # If both room_1 and room_2 exist, pick one
            elif random() < 0.5:
                return self.room_1
            else:
                return self.room_2


def place_entities(room: Rect, dungeon: GameMap, maximum_monsters: int, maximum_items: int, level: int):
    number_of_monsters = randint(0, maximum_monsters)
    number_of_items = randint(0, maximum_items)

    for i in range(number_of_monsters):
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            enemy = copy.deepcopy(choices(population=Enemies_by_level[level][0], weights=Enemies_by_level[level][1], k=1)[0])
            enemy.place(x, y, dungeon)

            if enemy.can_spawn_armed:
                enemy.inventory.held = copy.deepcopy(choices(population=caverns_enemies[enemy.name]["weapons"], weights=caverns_enemies[enemy.name]["weapon weight"], k=1)[0])

                # TODO: Make readable

                if enemy.inventory.held is not None:

                    enemy.inventory.held.parent = enemy.inventory

                    if isinstance(enemy.inventory.held.usable_properties, Gun):
                        gun_parts = []

                        for value in enemy.inventory.held.usable_properties.possible_parts.values():

                            part_selected = choices(population=value[0], weights=value[1])
                            part_selected.append(gun_parts)

                        for part in gun_parts:
                            setattr(enemy.inventory.held.usable_properties.parts, part.part_type, part)

                        enemy.inventory.held.usable_properties.parts.update_partlist()

                        # gives gun magazine
                        if isinstance(enemy.inventory.held.usable_properties, GunMagFed):
                            enemy.inventory.held.usable_properties.loaded_magazine = copy.deepcopy(choices(
                                population=magazine_dict[enemy.inventory.held.usable_properties.compatible_magazine_type]["mag_items"],
                                weights=magazine_dict[enemy.inventory.held.usable_properties.compatible_magazine_type]["mag_weight"],
                                k=1)[0])

                            enemy.inventory.held.usable_properties.loaded_magazine.parent = enemy.inventory

                            ammo = copy.deepcopy(choices(population=bullet_dict[enemy.inventory.held.usable_properties.loaded_magazine.usable_properties.compatible_bullet_type]["bullet_items"],
                                                         weights=bullet_dict[enemy.inventory.held.usable_properties.loaded_magazine.usable_properties.compatible_bullet_type]["bullet_weight"], k=1)[0])

                            ammo.stacking.stack_size = enemy.inventory.held.usable_properties.loaded_magazine.usable_properties.mag_capacity

                            enemy.inventory.held.usable_properties.loaded_magazine.usable_properties.load_magazine(ammo=ammo, load_amount=ammo.stacking.stack_size)

                            enemy.inventory.held.usable_properties.previously_loaded_magazine = \
                                copy.deepcopy(enemy.inventory.held.usable_properties.loaded_magazine)

                            enemy.inventory.held.usable_properties.chambered_bullet = \
                                copy.deepcopy(enemy.inventory.held.usable_properties.loaded_magazine.usable_properties.magazine[-1])



    for i in range(number_of_items):
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities) and dungeon.tiles[x, y] != down_stairs:
            item = copy.deepcopy(choices(population=Items_by_level[level][0], weights=Items_by_level[level][1], k=1)[0])
            item.place(x, y, dungeon)
