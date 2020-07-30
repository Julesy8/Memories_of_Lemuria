from map_objects.tile import Tile
from map_objects.shapes import Rect
from random import randint
from entity import Entity
import tcod as libtcod
from components.enemies.enemies_by_level import Enemies_by_level  # temporary until switchcase implementation for import


class GameMap:
    def __init__(self, width, height, level, room_min_size, room_max_size):
        self.width = width
        self.height = height
        self.level = level
        self.room_min_size = room_min_size
        self.room_max_size = room_max_size
        self.tiles = self.initialize_tiles()

        """
        def level_zero():
            from components.enemies.enemies_by_level import Enemies_by_level

        import_switcher = {
            0: level_zero
        }
        import_function = import_switcher.get(level)
        import_function()
        """

    def initialize_tiles(self):
        tiles = [[Tile(True, self.level) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, player, entities, max_monsters_per_room, level, max_overlapping_rooms):
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            room_dimensions = self.generate_room()

            # "Rect" class makes rectangles easier to work with
            new_room = Rect(room_dimensions[0], room_dimensions[1], room_dimensions[2], room_dimensions[3])

            # run through the other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid

                # "paint" it to the map's tiles
                self.create_room(new_room)

                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()

                overlapping_rooms = 0
                while overlapping_rooms <= max_overlapping_rooms:
                    # the following prevents overlapping rooms from going over the map boundary, created with help from
                    # odd
                    room_width = randint(self.room_min_size, self.room_max_size)
                    room_height = randint(self.room_min_size, self.room_max_size)

                    # creates x value for overlapping room
                    # room_dimensions[2] = room width
                    overlapping_room_x = new_x - (room_dimensions[2] / 2) + randint(1, room_dimensions[2])

                    # calculates distance between the width of the map and the overlapping room x value
                    dist = self.width - overlapping_room_x

                    # determines what the width of the overlapping room should be based on whether the
                    # dist is greater than x for the overlapping room and less than the max room size
                    # or whether dist is less than the overlapping room size and the max room size
                    if dist > overlapping_room_x and overlapping_room_x < self.room_max_size:
                        room_width = int(randint(self.room_min_size, self.room_max_size)) - 1

                    if dist < overlapping_room_x and dist < self.room_max_size:
                        room_width = int(randint(self.room_min_size, self.room_max_size) % int(dist))

                    # creates y value for overlapping room
                    # room_dimensions[3] = room height
                    overlapping_room_y = new_y - (room_dimensions[3] / 2) + randint(1, room_dimensions[3])

                    dist = self.height - overlapping_room_y
                    if dist > overlapping_room_y and overlapping_room_y < self.room_max_size:
                        room_height = int(randint(self.room_min_size, self.room_max_size)) - 1

                    if dist < overlapping_room_y and dist < self.room_max_size:
                        room_height = int(randint(self.room_min_size, self.room_max_size) % int(dist))

                    # creates the overlapping room
                    overlapping_room = Rect(overlapping_room_x, overlapping_room_y, room_width, room_height)

                    # if this is the first room, i.e. the player's starting room, don't spawn any enemies.
                    self.create_room(overlapping_room)
                    if num_rooms == 0:
                        pass
                    else:
                        self.place_entities(overlapping_room, entities, max_monsters_per_room, level)
                    overlapping_rooms += 1

                if num_rooms == 0:
                    # this is the first room, where the player starts at
                    player.x = new_x
                    player.y = new_y
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel

                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    # flip a coin (random number that is either 0 or 1)
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                        # finally, append the new room to the list
                    # once again prevents npcs from spawning in players starting room
                    self.place_entities(new_room, entities, max_monsters_per_room, level)
                rooms.append(new_room)
                num_rooms += 1

        # for safety's sake, once all the rooms are generated creates a box of walls around the map perimeter to
        # ensure that there are no holes
        self.create_h_wall(0, 79, 0)
        self.create_h_wall(0, 79, 49)
        self.create_v_wall(0, 49, 0)
        self.create_v_wall(0, 49, 79)

    def place_entities(self, room, entities, max_monsters_per_room, level):
        num_monsters = randint(0, max_monsters_per_room)
        # creates random x and y values for the entity
        for i in range(num_monsters):
            if room.x2 - 1 < room.x1 + 1 or room.y2 - 1 < room.y1 + 1:
                break
            else:
                x = randint(int(room.x1) + 1, int(room.x2) - 1)
                y = randint(int(room.y1) + 1, int(room.y2) - 1)
            """
            places entity at x and y if there is not already an entity at x and y. Generates a random rarity valuable
            and based on that searches the corresponding dictionary for the given level for that rarity and based on 
            that places an entity.
            """
            if not any([entity for entity in entities if entity.x == x and entity.y == y]) and x and y != 0:
                entity_rarity = randint(1, 100)
                if entity_rarity <= 60:          # common
                    enemy = Enemies_by_level[level][0][randint(0, len(Enemies_by_level[level][0]) - 1)]

                elif 60 <= entity_rarity <= 80:  # uncommon
                    enemy = Enemies_by_level[level][1][randint(0, len(Enemies_by_level[level][0]) - 1)]

                elif 80 <= entity_rarity <= 95:  # rare
                    enemy = Enemies_by_level[level][2][randint(0, len(Enemies_by_level[level][0]) - 1)]

                elif 95 <= entity_rarity <= 99:  # very rare
                    enemy = Enemies_by_level[level][3][randint(0, len(Enemies_by_level[level][0]) - 1)]

                else:                            # ultra rare
                    enemy = Enemies_by_level[level][4][randint(0, len(Enemies_by_level[level][0]) - 1)]
                enemy.spawn(entities, x, y)

    def generate_room(self):
        w = randint(self.room_min_size, self.room_max_size)
        h = randint(self.room_min_size, self.room_max_size)
        # random position without going out of the boundaries of the map
        x = randint(0, self.width - w - 1)
        y = randint(0, self.height - h - 1)
        return x, y, w, h

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(int(room.x1) + 1, int(room.x2)):
            for y in range(int(room.y1) + 1, int(room.y2)):
                self.tiles[x][y] = Tile(False, self.level)

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y] = Tile(False, self.level)

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y] = Tile(False, self.level)

    def create_h_wall(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y] = Tile(True, self.level)

    def create_v_wall(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y] = Tile(True, self.level)

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False


    ''' going to need to work on this later
    # level: [min room size (int), max room size (int), max_rooms (int), overlapping_rooms (int), enemies (dict),
    # items (dict),
    level_generator = {
        "Caverns": []
    }
    '''
