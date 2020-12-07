import copy

from random import random, randint, choice

import level_gen_tools as tools
from colours_and_chars import MapColoursChars
from game_map import GameMap
from level_parameters import Enemies_by_level


#if TYPE_CHECKING:
#    from engine import Engine

class MessyBSPTree:
    """
    A Binary Space Partition connected by a severely weighted
    drunkards walk algorithm.
    """

    def __init__(self, tunnel_type, map_width, map_height, MAX_LEAF_SIZE, ROOM_MAX_SIZE,
                 ROOM_MIN_SIZE, max_monsters_per_room, engine, current_level):
        self.tunnel_type = tunnel_type
        self.map_width = map_width
        self.map_height = map_height
        self.current_level = current_level
        self.room = None
        self.MAX_LEAF_SIZE = MAX_LEAF_SIZE
        self.ROOM_MAX_SIZE = ROOM_MAX_SIZE
        self.ROOM_MIN_SIZE = ROOM_MIN_SIZE
        self.max_monsters_per_room = max_monsters_per_room
        self.player = engine.player
        self._rooms = []

        # makes tuple of possible combinations of tile colours and characters
        self.colours_chars_tuple = MapColoursChars(current_level)

        # makes tuple of colours and characters into an array usable by new_tile
        self.colours_chars_array = tools.generate_char_arrays(self.colours_chars_tuple.floor_fg_dark(),
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

        rootLeaf = Leaf(0, 0, self.map_width, self.map_height, self.tunnel_type)
        self._leafs.append(rootLeaf)

        splitSuccessfully = True
        # loop through all leaves until they can no longer split successfully
        while splitSuccessfully:
            splitSuccessfully = False
            for l in self._leafs:
                if (l.child_1 is None) and (l.child_2 is None):
                    if ((l.width > self.MAX_LEAF_SIZE) or
                            (l.height > self.MAX_LEAF_SIZE) or
                            (random() > 0.8)):
                        if l.splitLeaf():  # try to split the leaf
                            self._leafs.append(l.child_1)
                            self._leafs.append(l.child_2)
                            splitSuccessfully = True

        rootLeaf.createRooms(self)
        return self.dungeon

    def createRoom(self, room):
        # set all tiles within a rectangle to be floors
        if len(self._rooms) == 0:
            # The first room, where the player starts.
            room_centre = room.centre()
            self.player.place(*room_centre, self.dungeon)

        else:
            place_entities(room, self.dungeon, self.max_monsters_per_room, self.current_level)
        self._rooms.append(room)
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.dungeon.tiles[x, y] = tools.select_random_tile(self.colours_chars_array)

    def createHall(self, room1, room2, tunnel_type):
        if tunnel_type == 0:
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
                if (0 < drunkardX + dx < self.map_width - 1) and (0 < drunkardY + dy < self.map_height - 1):
                    drunkardX += dx
                    drunkardY += dy
                    drunkardX = int(drunkardX)
                    drunkardY = int(drunkardY)
                    if self.dungeon.tiles[drunkardX, drunkardY] == self.dungeon.wall:
                        self.dungeon.tiles[drunkardX, drunkardY] = tools.select_random_tile(self.colours_chars_array)
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
            self.dungeon.tiles[x, y] = tools.select_random_tile(self.colours_chars_array)

    def createVirTunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.dungeon.tiles[x, y] = tools.select_random_tile(self.colours_chars_array)


class Rect:  # used for the tunneling algorithm
    def __init__(self, x, y, w, h):
        self.x1 = int(x)
        self.y1 = int(y)
        self.x2 = int(x) + int(w)
        self.y2 = int(y) + int(h)

    def centre(self):
        centerX = (self.x1 + self.x2) / 2
        centerY = (self.y1 + self.y2) / 2
        centerX = int(centerX)
        centerY = int(centerY)
        return centerX, centerY

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


class Leaf:  # used for the BSP tree algorithm
    def __init__(self, x, y, width, height, tunnel_type):  # as in MessyBSPTree, tunnel type 0 = drunkard, 1 = straight
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tunnel_type = tunnel_type
        self.MIN_LEAF_SIZE = 10
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
            max = self.height - self.MIN_LEAF_SIZE
        else:
            max = self.width - self.MIN_LEAF_SIZE

        if max <= self.MIN_LEAF_SIZE:
            return False  # the leaf is too small to split further

        split = randint(self.MIN_LEAF_SIZE, max)  # determine where to split the leaf

        if splitHorizontally:
            self.child_1 = Leaf(self.x, self.y, self.width, split, self.tunnel_type)
            self.child_2 = Leaf(self.x, self.y + split, self.width, self.height - split, self.tunnel_type)
        else:
            self.child_1 = Leaf(self.x, self.y, split, self.height, self.tunnel_type)
            self.child_2 = Leaf(self.x + split, self.y, self.width - split, self.height, self.tunnel_type)

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
                                self.child_2.getRoom(), self.tunnel_type)

        else:
            # Create rooms in the end branches of the bsp tree
            w = randint(bspTree.ROOM_MIN_SIZE, min(bspTree.ROOM_MAX_SIZE, self.width - 1))
            h = randint(bspTree.ROOM_MIN_SIZE, min(bspTree.ROOM_MAX_SIZE, self.height - 1))
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

def place_entities(room: Rect, dungeon: GameMap, maximum_monsters: int, level: int):
    number_of_monsters = randint(0, maximum_monsters)

    for i in range(number_of_monsters):
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            entity_rarity = randint(1, 100)
            if entity_rarity <= 60:          # common
                enemy = copy.deepcopy(Enemies_by_level[level][0][randint(0, len(Enemies_by_level[level][0]) - 1)])

            elif 60 <= entity_rarity <= 80:  # uncommon
                enemy = copy.deepcopy(Enemies_by_level[level][1][randint(0, len(Enemies_by_level[level][0]) - 1)])

            elif 80 <= entity_rarity <= 95:  # rare
                enemy = copy.deepcopy(Enemies_by_level[level][2][randint(0, len(Enemies_by_level[level][0]) - 1)])

            elif 95 <= entity_rarity <= 99:  # very rare
                enemy = copy.deepcopy(Enemies_by_level[level][3][randint(0, len(Enemies_by_level[level][0]) - 1)])

            else:                            # ultra rare
                enemy = copy.deepcopy(Enemies_by_level[level][4][randint(0, len(Enemies_by_level[level][0]) - 1)])

            enemy.place(x, y, dungeon)