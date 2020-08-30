import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main():

    # initialises values for screen width and height used when rendering the root console, placing player
    screen_width = 80
    screen_height = 50

    # width and height of the map
    map_width = 80
    map_height = 80

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
    #     def __init__(self, power, volume_blood, energy, move_cost, attack_cost, bleeds=True, alive=True):
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
    game_map = GameMap(map_width, map_height, current_level, room_min_size, room_max_size)
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

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # tells root console what font to use, initialisation of the root console
    tileset = tcod.tileset.load_tilesheet("cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    event_handler = EventHandler()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Age of Aquarius",
        vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
