import colour


class MapColoursChars:
    def __init__(self, level: int):
        self.level = level

        level_colours_tiles = {

            # The Tunnels
            0: {
                "wall fg dark": colour.DARK_GRAY,
                "wall bg dark": colour.BLACK,
                "wall fg light": colour.LIGHT_GRAY,
                "wall bg light": colour.BLACK,

                "floor fg dark": colour.GUNMETAL,
                "floor bg dark": colour.BLACK,
                "floor fg light": colour.LIGHT_GRAY,
                "floor bg light": colour.BLACK,

                # "wall tile": 35,
                "wall tile": 9619,
                "floor tile": [46]
            },

            # Caverns
            1: {
                "wall fg dark": colour.DARK_GRAY,
                "wall bg dark": colour.BLACK,
                "wall fg light": colour.BROWN,
                "wall bg light": colour.LIGHT_BROWN,

                "floor fg dark": colour.DARK_GRAY,
                "floor bg dark": colour.BLACK,
                "floor fg light": colour.LIGHT_GRAY,
                "floor bg light": colour.BLACK,

                "wall tile": 35,
                "floor tile": [46, 46, 44]
            },

            # The Temple
            2: {
                "wall fg dark": colour.DARK_GRAY,
                "wall bg dark": colour.BLACK,
                "wall fg light": colour.RED,
                "wall bg light": colour.BLACK,

                "floor fg dark": colour.GUNMETAL,
                "floor bg dark": colour.BLACK,
                "floor fg light": colour.DARK_GRAY,
                "floor bg light": colour.BLACK,

                "wall tile": 9619,
                "floor tile": [43]
            },

            # the base
            3: {
                "wall fg dark": colour.DARK_GRAY,
                "wall bg dark": colour.BLACK,
                "wall fg light": colour.LIGHT_GUNMETAL,
                "wall bg light": colour.LIGHT_GRAY,

                "floor fg dark": colour.DARK_GRAY,
                "floor bg dark": colour.BLACK,
                "floor fg light": colour.LIGHT_GRAY,
                "floor bg light": colour.BLACK,

                "wall tile": 9617,
                "floor tile": [43]
            },

            # the labs
            4: {
                "wall fg dark": colour.DARK_GRAY,
                "wall bg dark": colour.BLACK,
                "wall fg light": colour.WHITE,
                "wall bg light": colour.BLACK,

                "floor fg dark": colour.DARK_GRAY,
                "floor bg dark": colour.BLACK,
                "floor fg light": colour.LIGHT_GRAY,
                "floor bg light": colour.BLACK,

                "wall tile": 9617,
                "floor tile": [46]
            },

            # Reptilian Hive
            5: {
                "wall fg dark": colour.DARK_GRAY,
                "wall bg dark": colour.BLACK,
                "wall fg light": colour.JADE,
                "wall bg light": colour.LIGHT_GUNMETAL,

                "floor fg dark": colour.LIGHT_GUNMETAL,
                "floor bg dark": colour.BLACK,
                "floor fg light": colour.DARK_GRAY,
                "floor bg light": colour.BLACK,

                "wall tile": 35,
                "floor tile": [46, 44, 44]
            },

        }

        # floor colours
        self.floor_fg_dark = level_colours_tiles[level]["floor fg dark"]
        self.floor_bg_dark = level_colours_tiles[level]["floor bg dark"]
        self.floor_fg_light = level_colours_tiles[level]["floor fg light"]
        self.floor_bg_light = level_colours_tiles[level]["floor bg light"]
        self.floor_tile = level_colours_tiles[level]["floor tile"]

        # wall colours
        self.wall_fg_dark = level_colours_tiles[level]["wall fg dark"]
        self.wall_bg_dark = level_colours_tiles[level]["wall bg dark"]
        self.wall_fg_light = level_colours_tiles[level]["wall fg light"]
        self.wall_bg_light = level_colours_tiles[level]["wall bg light"]
        self.wall_tile = level_colours_tiles[level]["wall tile"]
