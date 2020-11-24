import numpy as np
import random
from typing import List

import level_gen_tools as tools
from colours_and_chars import MapColoursChars
from game_map import GameMap

level_params = {
    0: np.array([80,  # map width
                 50,  # map height
                 50,  # max rooms
                 40,  # min rooms
                 2,  # max overlapping rooms
                 6,  # max room size
                 4  # min room size
                 ])
}


def generate_dungeon(algorithm, current_level, player):
    game_map = 0
    if algorithm == "square_rooms":
        game_map = generate_square_rooms(level_params[current_level][0],
                                         level_params[current_level][1],
                                         current_level,
                                         level_params[current_level][2],
                                         level_params[current_level][3],
                                         level_params[current_level][4],
                                         level_params[current_level][5],
                                         level_params[current_level][6],
                                         player)
    return game_map


def generate_square_rooms(map_width,
                          map_height,
                          current_level,
                          max_rooms,
                          min_rooms,
                          max_overlapping_rooms,
                          room_max_size,
                          room_min_size,
                          player) -> GameMap:
    dungeon = GameMap(map_width, map_height, current_level)

    # makes tuple of possible combinations of tile colours and characters
    colours_chars_tuple = MapColoursChars(current_level)

    # makes tuple of colours and characters into an array usable by new_tile
    colours_chars_array = tools.generate_char_arrays(colours_chars_tuple.floor_fg_dark(),
                                                     colours_chars_tuple.floor_bg_dark(),
                                                     colours_chars_tuple.floor_tile()
                                                     )

    rooms: List[tools.RectangularRoom] = []

    for r in range(max_rooms):

        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        new_room = tools.RectangularRoom(x, y, room_width, room_height)

        (room_centre_x, room_centre_y) = new_room.center

        # Run through the other rooms and see if they intersect with this one.
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue  # This room intersects, so go to the next attempt.
        # If there are no intersections then the room is valid.

        # loops through all tiles in the room and assigns them a random tile based on the array of colours and chars
        for x in range(int(new_room.x1) + 1, int(new_room.x2)):
            for y in range(int(new_room.y1) + 1, int(new_room.y2)):
                dungeon.tiles[x, y] = tools.select_random_tile(colours_chars_array)

        """
        Fast method for making floors that can be used where the floor is just one colour and character throughout:
        dungeon.tiles[room_1.inner] = dungeon.floor
        """

        if len(rooms) == 0:
            # The first room, where the player starts.
            player.x, player.y = new_room.center
        else:  # All rooms after the first.
            # Dig out a tunnel between this room and the previous one.
            for x, y in tools.make_tunnel_right_angle(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tools.select_random_tile(colours_chars_array)

        for r in range(max_overlapping_rooms):

            overlapping_room_width = random.randint(room_min_size, room_max_size)
            overlapping_room_height = random.randint(room_min_size, room_max_size)

            overlapping_room_x = room_centre_x + random.randint(tools.round_up(-room_width / 2),
                                                                tools.round_up(room_width / 2))
            if overlapping_room_width + overlapping_room_x >= dungeon.width - 1 or \
                    overlapping_room_x - overlapping_room_width <= 1:
                continue

            overlapping_room_y = room_centre_y + random.randint(tools.round_up(-room_height / 2),
                                                                tools.round_up(room_height / 2))
            if overlapping_room_height + overlapping_room_y >= dungeon.height - 1 or \
                    overlapping_room_y - overlapping_room_height <= 1:
                continue

            # creates and generates overlapping room
            overlapping_room = tools.RectangularRoom(overlapping_room_x, overlapping_room_y,
                                                     overlapping_room_width, overlapping_room_height)

            if any(overlapping_room.intersects(other_room) for other_room in rooms):
                continue

            for x in range(int(overlapping_room.x1), int(overlapping_room.x2)):
                for y in range(int(overlapping_room.y1), int(overlapping_room.y2)):
                    dungeon.tiles[x, y] = tools.select_random_tile(colours_chars_array)

        # Finally, append the new room to the list.
        rooms.append(new_room)
        if len(rooms) < min_rooms:
            continue
    return dungeon


class MessyBSPTree:
    """
    A Binary Space Partition connected by a severely weighted
    drunkards walk algorithm.
    Requires Leaf and Rect classes.
     """

    def __init__(self, map_width, map_height, current_level, MAX_LEAF_SIZE, ROOM_MAX_SIZE,
                 ROOM_MIN_SIZE, smoothEdges, smoothing, filling, player):

        """
        DEFAULTS
        self.level = []
        self.room = None
        self.MAX_LEAF_SIZE = 24
        self.ROOM_MAX_SIZE = 15
        self.ROOM_MIN_SIZE = 6
        self.smoothEdges = True
        self.smoothing = 1
        self.filling = 3
        """
        self.map_width = map_width
        self.map_height = map_height
        self.current_level = current_level
        self.room = None
        self.MAX_LEAF_SIZE = MAX_LEAF_SIZE
        self.ROOM_MAX_SIZE = ROOM_MAX_SIZE
        self.ROOM_MIN_SIZE = ROOM_MIN_SIZE
        self.smoothEdges = smoothEdges
        self.smoothing = smoothing
        self.filling = filling
        self.player = player
        self._rooms = []

        # makes tuple of possible combinations of tile colours and characters
        self.colours_chars_tuple = MapColoursChars(current_level)

        # makes tuple of colours and characters into an array usable by new_tile
        self.colours_chars_array = tools.generate_char_arrays(self.colours_chars_tuple.floor_fg_dark(),
                                                              self.colours_chars_tuple.floor_bg_dark(),
                                                              self.colours_chars_tuple.floor_tile()
                                                              )

        self.dungeon = GameMap(map_width, map_height, current_level)

    def generateLevel(self):
        # Creates an empty 2D array or clears existing array
        self._leafs = []

        rootLeaf = Leaf(0, 0, self.map_width, self.map_height)
        self._leafs.append(rootLeaf)

        splitSuccessfully = True
        # loop through all leaves until they can no longer split successfully
        while splitSuccessfully:
            splitSuccessfully = False
            for l in self._leafs:
                if (l.child_1 is None) and (l.child_2 is None):
                    if ((l.width > self.MAX_LEAF_SIZE) or
                            (l.height > self.MAX_LEAF_SIZE) or
                            (random.random() > 0.8)):
                        if l.splitLeaf():  # try to split the leaf
                            self._leafs.append(l.child_1)
                            self._leafs.append(l.child_2)
                            splitSuccessfully = True

        rootLeaf.createRooms(self)
        self.cleanUpMap(self.map_width, self.map_height)

        return self.dungeon

    def createRoom(self, room):
        # set all tiles within a rectangle to be floors
        if len(self._rooms) == 0:
            # The first room, where the player starts.
            self.player.x, self.player.y = room.centre()
        self._rooms.append(room)
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.dungeon.tiles[x, y] = tools.select_random_tile(self.colours_chars_array)


    def createHall(self, room1, room2):
        # run a heavily weighted random Walk
        # from point2 to point1
        drunkardX, drunkardY = room2.centre()
        goalX, goalY = room1.centre()
        while not (room1.x1 <= drunkardX <= room1.x2) or not (room1.y1 < drunkardY < room1.y2):  #
            # ==== Choose Direction ====
            north = 1.0
            south = 1.0
            east = 1.0
            west = 1.0

            weight = 1

            # weight the random walk against edges
            if drunkardX < goalX:  # drunkard is left of point1
                east += weight
            elif drunkardX > goalX:  # drunkard is right of point1
                west += weight
            if drunkardY < goalY:  # drunkard is above point1
                south += weight
            elif drunkardY > goalY:  # drunkard is below point1
                north += weight

            # normalize probabilities so they form a range from 0 to 1
            total = north + south + east + west
            north /= total
            south /= total
            east /= total
            west /= total

            # choose the direction
            choice = random.random()
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

            # ==== Walk ====
            # check collision at edges
            if (0 < drunkardX + dx < self.map_width - 1) and (0 < drunkardY + dy < self.map_height - 1):
                drunkardX += dx
                drunkardY += dy
                drunkardX = int(drunkardX)
                drunkardY = int(drunkardY)
                if self.dungeon.tiles[drunkardX, drunkardY] == self.dungeon.wall:
                    self.dungeon.tiles[drunkardX, drunkardY] = tools.select_random_tile(self.colours_chars_array)

    def cleanUpMap(self, mapWidth, mapHeight):
        if self.smoothEdges:
            for i in range(3):
                # Look at each cell individually and check for smoothness
                for x in range(1, mapWidth - 1):
                    for y in range(1, mapHeight - 1):
                        if (self.dungeon.tiles[x, y] == self.dungeon.wall) and (self.getAdjacentWallsSimple(x, y)
                                                                        <= self.smoothing):
                            self.dungeon.tiles[x, y] = tools.select_random_tile(self.colours_chars_array)

                        if (self.dungeon.tiles[x, y]) and (self.getAdjacentWallsSimple(x, y) >= self.filling):
                            self.dungeon.tiles[x, y] = self.dungeon.wall

    def getAdjacentWallsSimple(self, x, y):  # finds the walls in four directions
        wallCounter = 0
        if self.dungeon.tiles[x, y - 1] == self.dungeon.wall:  # Check north
            wallCounter += 1
        if self.dungeon.tiles[x, y + 1] == self.dungeon.wall:  # Check south
            wallCounter += 1
        if self.dungeon.tiles[x - 1, y] == self.dungeon.wall:  # Check west
            wallCounter += 1
        if self.dungeon.tiles[x + 1, y] == self.dungeon.wall:  # Check east
            wallCounter += 1

        return wallCounter


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
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
        ==== Determine the direction of the split ====
        If the width of the leaf is >25% larger than the height,
        split the leaf vertically.
        If the height of the leaf is >25 larger than the width,
        split the leaf horizontally.
        Otherwise, choose the direction at random.
        '''

        splitHorizontally = random.choice([True, False])
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

        split = random.randint(self.MIN_LEAF_SIZE, max)  # determine where to split the leaf

        if splitHorizontally:
            self.child_1 = Leaf(self.x, self.y, self.width, split)
            self.child_2 = Leaf(self.x, self.y + split, self.width, self.height - split)
        else:
            self.child_1 = Leaf(self.x, self.y, split, self.height)
            self.child_2 = Leaf(self.x + split, self.y, self.width - split, self.height)

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
            w = random.randint(bspTree.ROOM_MIN_SIZE, min(bspTree.ROOM_MAX_SIZE, self.width - 1))
            h = random.randint(bspTree.ROOM_MIN_SIZE, min(bspTree.ROOM_MAX_SIZE, self.height - 1))
            x = random.randint(self.x, self.x + (self.width - 1) - w)
            y = random.randint(self.y, self.y + (self.height - 1) - h)
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
            elif random.random() < 0.5:
                return self.room_1
            else:
                return self.room_2
