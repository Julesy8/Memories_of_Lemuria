import tcod

import traceback

from engine import Engine
from components.npc_templates import Fighter
from entity import Actor, Item # item is possibly temp
from components.bodyparts import Bodypart
from level_parameters import level_params
from level_generator import MessyBSPTree
from components.ai import HostileEnemy
from scrolling_map import Camera
from components.inventory import Inventory
import colour


def main():

    # initialises values for screen width and height used when rendering the root console, placing player
    screen_width = 80
    screen_height = 50

    # defines what level of the dungeon the player is currently on
    current_level = 0

    # tells root console what font to use, initialisation of the root console
    tileset = tcod.tileset.load_tilesheet("Md_curses_16x16.png", 16, 16, tcod.tileset.CHARMAP_CP437)

    # initialises player entity
    fighter_component = Fighter(power=6)

    head = Bodypart(hp=100, defence=20, vital=True, walking=False, grasping=False,
                    connected_to=[], equipped=None, name='Head', part_type='Head', base_chance_to_hit=80)
    body = Bodypart(hp=100, defence=20, vital=True, walking=False, grasping=False,
                    connected_to=[], equipped=None, name='Body', part_type='Body', base_chance_to_hit=90)
    r_arm = Bodypart(hp=100, defence=20, vital=False, walking=False, grasping=True,
                     connected_to=[], equipped=None, name='Right Arm', part_type='Arms', base_chance_to_hit=80)
    l_arm = Bodypart(hp=100, defence=20, vital=False, walking=False, grasping=True,
                     connected_to=[], equipped=None, name='Left Arm', part_type='Arms', base_chance_to_hit=80)
    r_leg = Bodypart(hp=100, defence=20, vital=False, walking=False, grasping=False,
                     connected_to=[], equipped=None, name='Right Leg', part_type='Legs', base_chance_to_hit=80)
    l_leg = Bodypart(hp=100, defence=20, vital=False, walking=False, grasping=False,
                     connected_to=[], equipped=None, name='Left Leg', part_type='Legs', base_chance_to_hit=80)

    body_parts = [head, body, r_arm, l_arm, r_leg, l_leg]

    player = Actor(0, 0,
                   '@',
                   colour.WHITE,
                   None,
                   'Player',
                   ai=HostileEnemy,
                   fighter=fighter_component,
                   bodyparts=body_parts,
                   attack_interval=0,
                   attacks_per_turn=1,
                   move_interval=0,
                   moves_per_turn=1,
                   player=True,
                   inventory=Inventory(capacity=26, held=None)
                   )

    engine = Engine(player=player)

    # initialises map
    map_class = MessyBSPTree(level_params[current_level][0],  # messy tunnels
                             level_params[current_level][1],  # map width
                             level_params[current_level][2],  # map height
                             level_params[current_level][3],  # max leaf size
                             level_params[current_level][4],  # max room size
                             level_params[current_level][5],  # room min size
                             level_params[current_level][6],  # max monsters per room
                             level_params[current_level][7],  # max items per room
                             engine,
                             current_level,
                             )

    engine.game_map = map_class.generateLevel()

    camera = Camera(
        camera_x=0,
        camera_y=0,
        screen_width=screen_width,
        screen_height=screen_height,
        map_width=level_params[current_level][1],
        map_height=level_params[current_level][2],
    )

    camera.update(player)

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
            root_console.clear()
            engine.event_handler.on_render(console=root_console, camera=camera)
            context.present(root_console)

            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:  # Handle exceptions in game.
                traceback.print_exc()  # Print error to stderr.
                # Then print the error to the message log.
                engine.message_log.add_message(traceback.format_exc(), colour.LIGHT_RED)
            camera.update(player)


if __name__ == "__main__":
    main()
