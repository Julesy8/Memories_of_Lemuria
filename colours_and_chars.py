import level_importer
import colour

class MapColoursChars:
    def __init__(self, level: int):
        self.level = level

        cols_chars = level_importer.level_dependent_import(level)

        # floor colours
        self.floor_fg_dark_param = cols_chars[2][0]
        self.floor_bg_dark_param = cols_chars[2][1]
        self.floor_fg_light_param = cols_chars[2][2]
        self.floor_bg_light_param = cols_chars[2][3]
        self.floor_tile_param = cols_chars[4]

        # wall colours
        self.wall_fg_dark_param = cols_chars[1][0]
        self.wall_bg_dark_param = cols_chars[1][1]
        self.wall_fg_light_param = cols_chars[1][2]
        self.wall_bg_light_param = cols_chars[1][3]
        self.wall_tile_param = cols_chars[3][0]

    def floor_fg_light(self):
        return self.floor_fg_light_param

    def floor_bg_light(self):
        return self.floor_bg_light_param

    def floor_fg_dark(self):
        return self.floor_fg_dark_param

    def floor_bg_dark(self):
        return self.floor_bg_dark_param

    def floor_tile(self):
        return self.floor_tile_param

    def wall_fg_light(self):
        return self.wall_fg_light_param

    def wall_bg_light(self):
        return self.wall_bg_light_param

    def wall_fg_dark(self):
        return self.wall_fg_dark_param

    def wall_bg_dark(self):
        return self.wall_bg_dark_param

    def wall_tile(self):
        return self.wall_tile_param


# level 0
level_0 = {
    1:  # wall colour
        # foreground, background
        (colour.DARK_GRAY, colour.BLACK,   # dark
         colour.LIGHT_BROWN, colour.BROWN),  # light

    2:  # floor colour
        # foreground, background
        (colour.DARK_GRAY, colour.BLACK,   # dark
         colour.LIGHT_GREY, colour.DARK_GRAY),  # light

    3: [35],  # wall tile

    4: [46, 96, 44]  # floor tile, to weight this add multiple of the same value
}