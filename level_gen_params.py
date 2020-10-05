import numpy as np
from random import randint
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

        room_width = randint(room_min_size, room_max_size)
        room_height = randint(room_min_size, room_max_size)

        x = randint(0, dungeon.width - room_width - 1)
        y = randint(0, dungeon.height - room_height - 1)

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

            overlapping_room_width = randint(room_min_size, room_max_size)
            overlapping_room_height = randint(room_min_size, room_max_size)

            overlapping_room_x = room_centre_x + randint(tools.round_up(-room_width / 2),
                                                         tools.round_up(room_width / 2))
            if overlapping_room_width + overlapping_room_x >= dungeon.width - 1 or \
                    overlapping_room_x - overlapping_room_width <= 1:
                continue

            overlapping_room_y = room_centre_y + randint(tools.round_up(-room_height / 2),
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
