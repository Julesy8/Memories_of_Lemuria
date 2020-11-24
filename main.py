import tcod

from engine import Engine
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

from components.npc_templates import Fighter, Humanoid
from entity import Entity

import level_gen_params

def main():
    # initialises values for screen width and height used when rendering the root console, placing player
    screen_width = 80
    screen_height = 50

    # defines what level of the dungeon the player is currently on
    current_level = 0

    # tells root console what font to use, initialisation of the root console
    tileset = tcod.tileset.load_tilesheet("cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    event_handler = EventHandler()

    fighter_component = Fighter(1, 100, 100, 100, 100)
    player = Humanoid(5, 10, 5, 0, 0, 0, 0, int(screen_width / 2), int(screen_height / 2), '@',
                      tcod.white, None, 'Player', blocks=True, fighter=fighter_component)
    entities = {player}

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
            
             def __init__(self, map_width, map_height, current_level, MAX_LEAF_SIZE, ROOM_MAX_SIZE,
                 ROOM_MIN_SIZE, smoothEdges, smoothing, filling, player):
            
            """

    map_class = level_gen_params.MessyBSPTree(80, 50, 0, 24, 15, 6, True, 1, 3, player)
    game_map = map_class.generateLevel()

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Age of Aquarius",
            vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
