import tcod as libtcod
from input_handlers import handle_keys
from entity import Entity, get_blocking_entities_at_location
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap
from fov_functions import initialise_fov, recompute_fov
from game_states import GameStates
from components.npc_templates import Fighter, Humanoid


def main():

    # limits FPS
    libtcod.sys_set_fps(30)

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

    # sets the value for where the player will be at game start to be the middle of the screen
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)
    #     def __init__(self, power, volume_blood, energy, move_cost, attack_cost, bleeds=True, alive=True):
    # making the player character
    fighter_component = Fighter(1, 100, 100, 100, 100)
    player = Humanoid(5, 10, 5, 0, 0, 0, 0, 0, 0, '@', libtcod.white, libtcod.BKGND_NONE,
                      'Player', blocks=True, fighter=fighter_component)
    entities = [player]

    # tells root console what font to use, initialisation of the root console
    libtcod.console_set_custom_font('cp437_10x10.png', flags=libtcod.FONT_LAYOUT_ASCII_INROW, nb_char_horiz=16,
                                    nb_char_vertic=16)
    libtcod.console_init_root(screen_width, screen_height, 'Age of Aquarius', fullscreen=False)

    # holds keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # sets the turn to the players turn
    game_state = GameStates.PLAYERS_TURN

    # initialises root console
    con = libtcod.console_new(screen_width, screen_height)

    # initialises game map
    max_monsters_per_room = 3
    game_map = GameMap(map_width, map_height, current_level, room_min_size, room_max_size)
    game_map.make_map(max_rooms, player, entities, max_monsters_per_room, current_level, max_overlapping_rooms)

    fov_recompute = True

    fov_map = initialise_fov(game_map)

    while not libtcod.console_is_window_closed():  # main game loop
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)  # capture new user inputs

        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius, fov_light_walls, fov_algorithm)

        render_all(con, entities, fov_map, fov_recompute,  game_map, screen_width, screen_height)
        libtcod.console_set_default_foreground(0, libtcod.white)  # sets console 0 foreground to white
        # player character placed on console 0
        libtcod.console_put_char(0, player.x, player.y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush()  # applies changes to console

        render_all(con, entities, fov_map, fov_recompute,  game_map, screen_width, screen_height)
        libtcod.console_put_char(0, player.x, player.y, ' ', libtcod.BKGND_NONE)

        # key handling
        action = handle_keys(key)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move and game_state == GameStates.PLAYERS_TURN:  # handles player movement
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy

            if not game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)

                if target:
                    print('Melee attack on ' + target.name + '!')
                else:
                    player.move(dx, dy)

                    fov_recompute = True

                game_state = GameStates.ENEMY_TURN

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity.ai:
                    entity.ai.take_turn(player, fov_map, game_map, entities)

            game_state = GameStates.PLAYERS_TURN


if __name__ == '__main__':
    main()
