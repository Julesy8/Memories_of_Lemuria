import tcod

from engine import Engine
from components.npc_templates import Fighter, Humanoid
from level_parameters import level_params
from level_generator import MessyBSPTree

def main():

    """
    Main:
    - handles main game loop through engine
    -Initialises player
    -Initialises engine
    -Initialises gamemap
    -Initialises terminal

    GameMap:
    -gets information from engine
    -handles rendering
    -handles colour/s of walls
    -initialises game map as just walls
    -prints to terminal
    -handles FOV
    -handles entity blocking

    Engine
    -gets information from gamemap
    -handles enemy turns
    -updates FOV through GameMap
    -Renders through gamemap

    Level_generator
    -from gamemap generates level
    -places player + entities
    """

    # initialises values for screen width and height used when rendering the root console, placing player
    screen_width = 80
    screen_height = 50

    # defines what level of the dungeon the player is currently on
    current_level = 0

    # tells root console what font to use, initialisation of the root console
    tileset = tcod.tileset.load_tilesheet("cp437_10x10.png", 16, 16, tcod.tileset.CHARMAP_CP437)


    # initialises player entity
    fighter_component = Fighter(1, 100, 100, 100, 100)
    player = Humanoid(5, 10, 5, 0, 0, 0, 0, 0, 0, '@', [255,255,255], None,
                      'Player', blocks_movement=True, fighter=fighter_component)

    engine = Engine(player=player)

    # initialises map
    map_class = MessyBSPTree(level_params[current_level][0], level_params[current_level][1],
                             level_params[current_level][2], level_params[current_level][3],
                             level_params[current_level][4], level_params[current_level][5],
                             level_params[current_level][6],
                             engine, current_level)
    
    engine.game_map = map_class.generateLevel()

    engine.update_fov()

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

            engine.event_handler.handle_events()

if __name__ == "__main__":
    main()
