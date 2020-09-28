from typing import Iterator, Tuple, List, TYPE_CHECKING
import random
import numpy as np

import tcod

import tile_types
from game_map import GameMap
from colours_and_chars import MapColoursChars


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.width = width
        self.height = height
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    def intersects(self, other) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )


def generate_char_arrays(floor_fg_l, floor_bg_l, floor_chars):
    """
    From tuples representing the colours of the tiles and possible floor characters (from dictionary in
    colours_and_chars), generates a series of lists representing possible combinations of floor colours and characters,
    which are used to an array representing these tiles.

    !!! Can be expanded in future to use multiple possible colours for a single floor !!!
    """
    floor_list = []
    for x in floor_chars:
        floor_list.append(tile_types.new_floor(floor_fg_l, floor_bg_l, x))
    floor_arrays = np.array(floor_list)
    return floor_arrays


def select_random_tile(character_array):
    """
    Using an array of possible tiles from (from generate_char_arrays), selects a tile in the array at random

    !!! Possibilities can be weighted in future using multiple entries of the same tile !!!
    """
    character_index = random.randint(0, character_array.size - 1)
    character = character_array[character_index]
    return character


def make_tunnel_right_angle(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:  # 50% chance.
        # Move horizontally, then vertically.
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y


def generate_dungeon(
        map_width,
        map_height,
        current_level,
        max_rooms,
        max_overlapping_rooms,
        room_max_size,
        room_min_size,
        player
) -> GameMap:

    dungeon = GameMap(map_width, map_height, current_level)

    # makes tuple of possible combinations of tile colours and characters
    colours_chars_tuple = MapColoursChars(current_level)

    # makes tuple of colours and characters into an array usable by new_tile
    colours_chars_array = generate_char_arrays(colours_chars_tuple.floor_fg_dark(),
                                               colours_chars_tuple.floor_bg_dark(),
                                               colours_chars_tuple.floor_tile()
                                               )

    rooms: List[RectangularRoom] = []
    overlapping_rooms: List[RectangularRoom] = []

    for r in range(max_rooms):

        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        new_room = RectangularRoom(x, y, room_width, room_height)

        (room_centre_x, room_centre_y) = new_room.center

        # Run through the other rooms and see if they intersect with this one.
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue  # This room intersects, so go to the next attempt.
        # If there are no intersections then the room is valid.

        # loops through all tiles in the room and assigns them a random tile based on the array of colours and chars
        for x in range(int(new_room.x1) + 1, int(new_room.x2)):
            for y in range(int(new_room.y1) + 1, int(new_room.y2)):
                dungeon.tiles[x, y] = select_random_tile(colours_chars_array)

        """
        Fast method for making floors that can be used where the floor is just one colour and character throughout:
        dungeon.tiles[room_1.inner] = dungeon.floor
        """

        if len(rooms) == 0:
            # The first room, where the player starts.
            player.x, player.y = new_room.center
        else:  # All rooms after the first.
            # Dig out a tunnel between this room and the previous one.
            for x, y in make_tunnel_right_angle(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = select_random_tile(colours_chars_array)

        for r in range(max_overlapping_rooms):

            overlapping_room_width = random.randint(room_min_size, new_room.width)
            overlapping_room_height = random.randint(room_min_size, new_room.height)

            overlapping_room_x = room_centre_x + random.randint(-room_width + 1, room_width - 1)
            if overlapping_room_width + overlapping_room_x >= dungeon.width - 1 or \
                    overlapping_room_x - overlapping_room_width <= 1:
                continue

            overlapping_room_y = room_centre_y + random.randint(-room_height + 1, room_height - 1)
            if overlapping_room_height + overlapping_room_y >= dungeon.height - 1 or \
                    overlapping_room_y - overlapping_room_height <= 1:
                continue

            # creates and generates overlapping room
            overlapping_room = RectangularRoom(overlapping_room_x, overlapping_room_y,
                                               overlapping_room_width, overlapping_room_height)

            if any(overlapping_room.intersects(other_room) for other_room in rooms):
                continue

            for x in range(int(overlapping_room.x1), int(overlapping_room.x2)):
                for y in range(int(overlapping_room.y1), int(overlapping_room.y2)):
                    dungeon.tiles[x, y] = select_random_tile(colours_chars_array)

        # Finally, append the new room to the list.
        rooms.append(new_room)

    return dungeon
