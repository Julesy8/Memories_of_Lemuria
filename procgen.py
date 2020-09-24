from typing import Tuple

from game_map import GameMap


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
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


def generate_dungeon(map_width, map_height, level) -> GameMap:
    dungeon = GameMap(map_width, map_height, level)

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    for x in range(int(room_1.x1) + 1, int(room_1.x2)):
        for y in range(int(room_1.y1) + 1, int(room_1.y2)):
            [x,y]["dark"]["ch"] = dungeon.floor

    return dungeon
