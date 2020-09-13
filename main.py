import tcod

from engine import Engine
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

from components.npc_templates import Fighter, Humanoid
from entity import Entity

from procgen import generate_dungeon


def main():

    # initialises values for screen width and height used when rendering the root console, placing player
    screen_width = 80
    screen_height = 50

    # width and height of the map
    map_width = 80
    map_height = 50

    # room variables, going to want to replace this with a class that detects lvl at some point
    room_max_size = 9
    room_min_size = 4
    max_rooms = 40
    max_overlapping_rooms = 2

    # fov settings
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    # defines what level of the dungeon the player is currently on
    current_level = 0

    """
    # making the player character
    fighter_component = Fighter(1, 100, 100, 100, 100)
    player = Humanoid(5, 10, 5, 0, 0, 0, 0, 0, 0, '@', tcod.white, tcod.BKGND_NONE,
                      'Player', blocks=True, fighter=fighter_component)
    entities = [player]

    # holds keyboard and mouse input
    key = tcod.Key()
    mouse = tcod.Mouse()

    # sets the turn to the players turn
    game_state = GameStates.PLAYERS_TURN

    # initialises root console
    con = tcod.console_new(screen_width, screen_height)

    # initialises game map
    max_monsters_per_room = 3
    game_map.make_map(max_rooms, player, entities, max_monsters_per_room, current_level, max_overlapping_rooms)

    fov_recompute = True

    fov_map = initialise_fov(game_map)

    camera = Camera(
        x=0,
        y=0,
        width=screen_width,
        height=screen_height,
        map_width=map_width,
        map_height=map_height,
    )
    camera.update(player)
    """

    # tells root console what font to use, initialisation of the root console
    tileset = tcod.tileset.load_tilesheet("cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    event_handler = EventHandler()

    fighter_component = Fighter(1, 100, 100, 100, 100)
    player = Humanoid(5, 10, 5, 0, 0, 0, 0, int(screen_width / 2), int(screen_height / 2), '@',
                      tcod.white, None, 'Player', blocks=True, fighter=fighter_component)
    entities = {player}

    game_map = generate_dungeon(map_width, map_height, current_level)

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
