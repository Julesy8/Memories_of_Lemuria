import tcod

from engine import Engine
from components.npc_templates import Fighter
from entity import Actor
from components.bodyparts import Bodypart
from level_parameters import level_params
from level_generator import MessyBSPTree
from components.ai import HostileEnemy

def main():

    """
    Main:
    -handles main game loop through engine
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
    fighter_component = Fighter(power=20, hp=10, defence=5)

    head = Bodypart(None, 50, 5, True, False, False, False, 'Head', 'Head')
    body = Bodypart(None, 50, 5, True, False, False, False, 'Body', 'Body')
    r_arm = Bodypart(None, 50, 5, False, False, False, True, 'Right Arm', 'Arms')
    l_arm = Bodypart(None, 50, 5,False, False, False, True, 'Left Arm', 'Arms')
    r_leg = Bodypart(None, 50, 5, False, False, True, False, 'Right Leg', 'Legs')
    l_leg = Bodypart(None, 50, 5, False, False, True, False, 'Left Leg', 'Legs')

    body_parts = [head, body, r_arm, l_arm, r_leg, l_leg]

    player = Actor(0,0,'@', [255,255,255], None, 'Player', ai=HostileEnemy, fighter=fighter_component,
                   bodyparts = body_parts, player=True)

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
