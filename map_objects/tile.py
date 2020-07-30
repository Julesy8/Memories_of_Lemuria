from random import randint


class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight. Level determines what char is
    displayed and foreground and background colours.
    """
    def __init__(self, blocked, level, block_sight=None):
        self.blocked = blocked
        self.level = level
        self.explored = False

        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight
        """
        Wall and floor colours determined by tile_colours dictionary. If the tile is a floor, and the dictionary
        corresponding for tile_char to the current level has 3 values rather than 1, generates a number between 1 and 3.
        Assigns tile a character from the dictionary based on this value.
        """
        if not block_sight:  # floor
            fg_colour = tile_colour[level][0]
            bg_colour = tile_colour[level][1]
            fg_colour_dark = tile_colour[level][4]
            bg_colour_dark = tile_colour[level][5]
            if tile_character[level][1]:
                char = tile_character[level][2]
            else:
                rand_tile = randint(1, 3)
                if rand_tile == 1:
                    char = tile_character[level][2]
                elif rand_tile == 2:
                    char = tile_character[level][3]
                else:
                    char = tile_character[level][4]

        else:  # wall
            fg_colour = tile_colour[level][2]
            bg_colour = tile_colour[level][3]
            fg_colour_dark = tile_colour[level][6]
            bg_colour_dark = tile_colour[level][7]
            char = tile_character[level][0]

        self.char = char
        self.fg_colour = fg_colour
        self.bg_colour = bg_colour
        self.fg_colour_dark = fg_colour_dark
        self.bg_colour_dark = bg_colour_dark


"""
The following dictionaries determine tile foreground and background colour and character. Dependent on what floor
the player is on, i.e. "caverns". For first dict, integers are colour values in order:
floor foreground, floor background, wall foreground, wall background.
Second dict represents hex character values in the order 
wall, multiple floor tiles or single, floor, floor, floor, where values after the second are the floor tiles
"""
tile_colour = {
    0: [[63, 63, 63], [31, 31, 31], [45, 45, 45], [63, 63, 63],  # light
                [32, 32, 32], [16, 16, 16], [23, 23, 23], [32, 32, 32]]  # dark
}

tile_character = {
    # 0 = #, 2 = dot, 3 = `, 4 = ,
    0: [35, False, 250, 96, 44]
}
