from random import random, randint, choice, choices
from copy import deepcopy
import numpy as np  # type: ignore

from level_gen_tools import generate_char_arrays, select_random_tile, Rect
from colours_and_chars import MapColoursChars
from game_map import GameMap
from level_parameters import Enemies_by_level, Items_by_level
from tile_types import down_stairs, new_wall
from entity import Entity
import colour
from render_order import RenderOrder

stairs_entity = Entity(x=0, y=0, char='>', fg_colour=colour.LIGHT_GRAY, name='Stairs',
                       render_order=RenderOrder.ITEM)

class RoomPattern:
    def __init__(self,
                 file: str,
                 size_x: int,
                 size_y: int,
                 ):
        self.file = file
        self.size_x = size_x
        self.size_y = size_y
        self.rooms = open(file, 'r')

    def give_lines(self):
        return self.rooms.readlines()

class MessyBSPTree:
    """
    A Binary Space Partition connected by a severely weighted
    drunkards walk algorithm.
    """

    def __init__(self, messy_tunnels, map_width, map_height, max_leaf_size, room_max_size,
                 room_min_size, max_items_per_room, fov_radius, engine, current_level):
        self.messy_tunnels = messy_tunnels
        self.map_width = map_width
        self.map_height = map_height
        self.current_level = current_level
        self.room = None
        self.max_leaf_size = max_leaf_size
        self.room_max_size = room_max_size
        self.room_min_size = room_min_size
        self.max_items_per_room = max_items_per_room
        self.fov_radius = fov_radius
        self.player = engine.player
        self.engine = engine
        self._rooms = []
        self._leafs = []

        self.enemy_population = []
        self.enemy_weight = []

        self.item_population = []
        self.item_weight = []

        for i in Enemies_by_level[self.current_level]:
            self.enemy_population.append(i[0])
            self.enemy_weight.append(i[1])

        for i in Items_by_level[self.current_level]:
            self.item_population.append(i[0])
            self.item_weight.append(i[1])

        # makes tuple of possible combinations of tile colours and characters
        self.colours_chars_tuple = MapColoursChars(current_level)

        # makes tuple of colours and characters into an array usable by new_tile
        self.colours_chars_array = generate_char_arrays(self.colours_chars_tuple.floor_fg_dark,
                                                        self.colours_chars_tuple.floor_bg_dark,
                                                        self.colours_chars_tuple.floor_fg_light,
                                                        self.colours_chars_tuple.floor_bg_light,
                                                        self.colours_chars_tuple.floor_tile
                                                        )

        # room_7x7 = RoomPattern(file='room_7x7.txt', size_x=7, size_y=7)
        # room_7x14 = RoomPattern(file='room_7x14.txt', size_x=7, size_y=14)
        # room_14x7 = RoomPattern(file='room_14x7.txt', size_x=14, size_y=7)
        # room_14x14 = RoomPattern(file='room_14x14.txt', size_x=14, size_y=14)
        # room_7x21 = RoomPattern(file='room_7x21.txt', size_x=7, size_y=21)
        # room_21x7 = RoomPattern(file='room_21x7.txt', size_x=21, size_y=7)
        # room_14x21 = RoomPattern(file='room_14x21.txt', size_x=14, size_y=21)
        # room_21x14 = RoomPattern(file='room_21x14.txt', size_x=21, size_y=14)
        # room_21x21 = RoomPattern(file='room_21x21.txt', size_x=21, size_y=21)
        #
        # self.room_pattern_files = {
        #     (7, 7): room_7x7,
        #     (7, 14): room_7x14,
        #     (14, 7): room_14x7,
        #     (14, 14): room_14x14,
        #     (7, 21): room_7x21,
        #     (21, 7): room_21x7,
        #     (14, 21): room_14x21,
        #     (21, 14): room_21x14,
        #     (21, 21): room_21x21,
        # }
        #
        # room_patterns_list = (room_7x7, room_7x14, room_14x7, room_14x14, room_7x21, room_21x7, room_14x21, room_21x14,
        #                       room_21x21)
        #
        #
        # self.room_patterns_split = {}
        #
        # for pattern in room_patterns_list:
        #     pattern_index = 0
        #     rooms_split = []
        #     room_lines = pattern.give_lines()
        #
        #     for i in range(len(room_lines) // pattern.size_x):
        #         rooms_split.append(room_lines[pattern_index:pattern_index + pattern.size_x])
        #         pattern_index += pattern.size_x + 1
        #
        #     self.room_patterns_split[pattern.file] = rooms_split

        self.dungeon = GameMap(engine=engine, width=map_width, height=map_height, entities=[] + engine.players,
                               fov_radius=self.fov_radius)

    def generate_level(self):

        """
        generates caverns using random walk
        """

        number_of_caverns = 3
        cavern_size = 500

        for x in range(number_of_caverns):
            cave_x = randint(20, 80)
            cave_y = randint(20, 80)
            self.dungeon.tiles[cave_x, cave_y] = select_random_tile(self.colours_chars_array)

            cavern_tiles = 0

            while cavern_tiles < cavern_size:

                # moves in random direction
                movement = randint(1, 4)

                if movement == 1:  # up
                    if cave_y + 1 < self.map_height - 2:
                        cave_y += 1
                    else:
                        continue
                elif movement == 2:  # down
                    if cave_y - 1 > 2:
                        cave_y -= 1
                    else:
                        continue
                elif movement == 3:  # left
                    if cave_x - 1 > 2:
                        cave_x -= 1
                    else:
                        continue
                elif movement == 4:  # right
                    if cave_x + 1 < self.map_width - 2:
                        cave_x += 1
                    else:
                        continue

                if not self.dungeon.tiles["walkable"][cave_x, cave_y]:

                    remove_tiles = randint(1, 4)

                    if remove_tiles == 1:  # up right
                        self.dungeon.tiles[cave_x, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x + 1, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x, cave_y + 1] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x + 1, cave_y + 1] = select_random_tile(self.colours_chars_array)

                    if remove_tiles == 2:  # down right

                        self.dungeon.tiles[cave_x, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x + 1, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x, cave_y - 1] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x + 1, cave_y - 1] = select_random_tile(self.colours_chars_array)

                    if remove_tiles == 3:  # up left

                        self.dungeon.tiles[cave_x, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x - 1, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x, cave_y + 1] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x - 1, cave_y + 1] = select_random_tile(self.colours_chars_array)

                    if remove_tiles == 4:  # down left

                        self.dungeon.tiles[cave_x, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x - 1, cave_y] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x, cave_y - 1] = select_random_tile(self.colours_chars_array)
                        self.dungeon.tiles[cave_x - 1, cave_y - 1] = select_random_tile(self.colours_chars_array)

                    cavern_tiles += 1

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
                        if l.split_leaf():  # try to split the leaf
                            self._leafs.append(l.child_1)
                            self._leafs.append(l.child_2)
                            splitSuccessfully = True

        rootLeaf.create_rooms(self)

        # generates a room number for player and stairs to spawn in
        player_spawn_room = randint(0, len(self._rooms) - 1)
        stair_room = randint(0, len(self._rooms) - 1)

        # if player and stairs meant to spawn in the same room, regenerates stair room until it is not
        while stair_room == player_spawn_room:
            stair_room = randint(0, len(self._rooms) - 1)

        for room in self._rooms:
            if room == self._rooms[player_spawn_room]:
                for player in self.engine.players:
                    player_placed = False
                    while not player_placed:
                        x = randint(room.x1 + 1, room.x2 - 1)
                        y = randint(room.y1 + 1, room.y2 - 1)
                        if not any(entity.x == x and entity.y == y for entity in self.dungeon.entities):
                            player.place(x, y, self.dungeon)
                            player_placed = True

            else:
                self.place_entities(room)

            if room == self._rooms[stair_room]:
                room_centre_x, room_centre_y = room.centre()
                self.dungeon.tiles[room_centre_x, room_centre_y] = down_stairs
                stairs = deepcopy(stairs_entity)
                stairs.place(x=room_centre_x, y=room_centre_y, gamemap=self.dungeon)
                self.dungeon.downstairs_location = room_centre_x, room_centre_y

        self.dungeon.rooms = self._rooms

        return self.dungeon

    def create_room(self, room):
        # set all tiles within a rectangle to be floors
        self._rooms.append(room)

        enclose_room = choice((True, False, False, False))

        if enclose_room:
            for x in range(room.x1, room.x2 + 1):
                for y in range(room.y1, room.y2 + 1):
                    self.dungeon.tiles[x, y] = (
                                    new_wall(self.colours_chars_tuple.wall_fg_dark,
                                             self.colours_chars_tuple.wall_bg_dark,
                                             self.colours_chars_tuple.wall_fg_light,
                                             self.colours_chars_tuple.wall_bg_light,
                                             self.colours_chars_tuple.wall_tile
                                             ))

        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.dungeon.tiles[x, y] = select_random_tile(self.colours_chars_array)

    def create_prefab_room(self, room, prefab, x, y):

        self._rooms.append(room)

        line_index = 0
        for line in prefab:
            line = line.rstrip()
            char_index = 0
            for char in line:

                if not char == '.':
                    self.dungeon.tiles[char_index + x,  # TODO - will sometimes get index error here
                                       line_index + y] = (
                        new_wall(self.colours_chars_tuple.wall_fg_dark,
                                 self.colours_chars_tuple.wall_bg_dark,
                                 self.colours_chars_tuple.wall_fg_light,
                                 self.colours_chars_tuple.wall_bg_light,
                                 ord(char)
                                 ))
                else:
                    self.dungeon.tiles[char_index + x, line_index + y] = select_random_tile(self.colours_chars_array)

                char_index += 1
            line_index += 1

    def create_hall(self, room1, room2):

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
                direction_choice = random()
                if 0 <= direction_choice < north:
                    dx = 0
                    dy = -1
                elif north <= direction_choice < (north + south):
                    dx = 0
                    dy = 1
                elif (north + south) <= direction_choice < (north + south + east):
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
                self.create_tunnel_horizontal(x1, x2, y1)
                self.create_tunnel_vertical(y1, y2, x2)

            else:  # else it starts vertically
                self.create_tunnel_vertical(y1, y2, x1)
                self.create_tunnel_horizontal(x1, x2, y2)

    def create_tunnel_horizontal(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.dungeon.tiles[x, y] = select_random_tile(self.colours_chars_array)

    def create_tunnel_vertical(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.dungeon.tiles[x, y] = select_random_tile(self.colours_chars_array)

    def place_entities(self, room: Rect):

        enemy = deepcopy(choices(population=self.enemy_population, weights=self.enemy_weight,
                                 k=1)[0])

        number_of_monsters = randint(0, enemy.fighter.spawn_group_amount)
        number_of_items = randint(0, self.max_items_per_room)

        for i in range(number_of_monsters):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any(entity.x == x and entity.y == y for entity in self.dungeon.entities):
                # place enemy
                enemy.place(x, y, self.dungeon)
                enemy.fighter.give_weapon(self.current_level)
                enemy.fighter.give_armour(self.current_level)

        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any(entity.x == x and entity.y == y for entity in self.dungeon.entities) and \
                    self.dungeon.tiles[x, y] != down_stairs:
                item = deepcopy(choices(population=self.item_population, weights=self.item_weight, k=1)[0])
                item.place(x, y, self.dungeon)


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
        self.room_1 = None
        self.room_2 = None
        self.room = None
        self.hall = None

    def split_leaf(self):
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
            max_size = self.height - self.min_leaf_size
        else:
            max_size = self.width - self.min_leaf_size

        if max_size <= self.min_leaf_size:
            return False  # the leaf is too small to split further

        split = randint(self.min_leaf_size, max_size)  # determine where to split the leaf

        if splitHorizontally:
            self.child_1 = Leaf(self.x, self.y, self.width, split, self.messy_tunnels)
            self.child_2 = Leaf(self.x, self.y + split, self.width, self.height - split, self.messy_tunnels)
        else:
            self.child_1 = Leaf(self.x, self.y, split, self.height, self.messy_tunnels)
            self.child_2 = Leaf(self.x + split, self.y, self.width - split, self.height, self.messy_tunnels)

        return True

    def create_rooms(self, bsp_tree):
        if self.child_1 or self.child_2:
            # recursively search for children until you hit the end of the branch
            if self.child_1:
                self.child_1.create_rooms(bsp_tree)
            if self.child_2:
                self.child_2.create_rooms(bsp_tree)

            if self.child_1 and self.child_2:
                bsp_tree.create_hall(self.child_1.get_room(),
                                     self.child_2.get_room())

        else:
            # Create rooms in the end branches of the bsp tree
            # custom_room = choice((True, False, False, False, False))
            #
            # if custom_room:
            #     w = choices((7, 14, 21), (15, 10, 2))[0]
            #     h = choices((7, 14, 21), (15, 10, 2))[0]
            #
            #     if w >= self.width - 1 or h >= self.height - 1:
            #         pass
            #     else:
            #         x = randint(self.x, self.x + (self.width - 1) - w)
            #         y = randint(self.y, self.y + (self.height - 1) - h)
            #         print(w)
            #         print(h)
            #         room_pattern = bsp_tree.room_pattern_files[(h, w)]
            #         print(room_pattern.file)
            #         prefab = choice(bsp_tree.room_patterns_split[room_pattern.file])
            #         self.room = Rect(x + 1, y + 1, h - 1, w - 1)
            #         # self.room = Rect(x, y, w, h)
            #         return bsp_tree.create_prefab_room(prefab=prefab, room=self.room, x=x, y=y)

            max_w = min(bsp_tree.room_max_size, self.width - 1)
            max_h = min(bsp_tree.room_max_size, self.height - 1)
            w = randint(bsp_tree.room_min_size, max_w)
            h = randint(bsp_tree.room_min_size, max_h)
            x = randint(self.x, self.x + (self.width - 1) - w)
            y = randint(self.y, self.y + (self.height - 1) - h)
            self.room = Rect(x, y, w, h)
            bsp_tree.create_room(self.room)

    def get_room(self):
        if self.room:
            return self.room

        else:
            if self.child_1:
                self.room_1 = self.child_1.get_room()
            if self.child_2:
                self.room_2 = self.child_2.get_room()

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
