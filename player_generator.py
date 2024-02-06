from __future__ import annotations

from typing import TYPE_CHECKING

import colour
from components.weapons.gun_maker import (ar15_weapon, ar10_weapon, ak47_weapon, ak74_weapon, ak556_weapon,
                                          m1045_weapon, m109_weapon, sks_weapon, mosin_weapon, m1911_45, m1911_9mm,
                                          m1911_10mm, m1911_40sw, m1_carbine_gun, m2_carbine_gun, m14_gun, m1a_gun,
                                          r870_gun, supershorty_gun, g_17)

from components.armour import (helmet_riot, helmet_ssh68, helmet_m1, helmet_pasgt, helmet_ech, helmet_ronin,
                               helmet_altyn, bodyarmour_pasgt, bodyarmour_interceptor, bodyarmour_improved,
                               platecarrier_3a, platecarrier_3, platecarrier_4)

from entity import Actor
from components.inventory import Inventory
from components.ai import PlayerCharacter
from random import choice, randint, choices
from components.npc_templates import PlayerFighter
from components.bodyparts import Body, Arm, Leg, Head
from copy import copy, deepcopy

if TYPE_CHECKING:
    from engine import Engine

helmets_leveled = {0: {None: 1, helmet_riot: 20, helmet_ssh68: 4, helmet_m1: 4, helmet_pasgt: 2}}

bodyarmour_leveled = {0: {None: 50, bodyarmour_pasgt: 1}}


def generate_player(current_level: int, players: list):
    player_colours = [colour.BLUE, colour.JADE, colour.MAGENTA, colour.ORANGE, colour.YELLOW,
                      colour.PURPLE, colour.CYAN, colour.LIGHT_BLUE, colour.LIGHT_GREEN,
                      colour.LIGHT_MAGENTA, colour.LIGHT_YELLOW]

    first_names = ['James', 'John', 'Robert', 'Michael', 'Will', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles',
                   'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew',
                   'Kenneth', 'George', 'Joshua', 'Kevin', 'Brian', 'Edward', 'Nicholas', 'Tyler', 'Brandon',
                   'Jacob', 'Ryan', 'Justin', 'Jonathan', 'Austin', 'Cody', 'Eric', 'Benjamin', 'Adam', 'Samuel',
                   'Jeremy', 'Patrick', 'Alexander', 'Jesse', 'Zachary', 'Dylan', 'Nathan', 'Scott', 'Kyle', 'Jeffrey',
                   'Sean', 'Travis', 'Bryan', 'Ethan', 'Luke', 'Carlos', 'Ian', 'Peter', 'Christian', 'Cameron',
                   'Shawn', 'Luis', 'Jared', 'Juan', 'Caleb', 'Evan', 'Gabriel', 'Chase', 'Antonio', 'Cory', 'Curtis',
                   'Seth', 'Adrian', 'Jorge', 'Trevor', 'Dustin', 'Mario', 'Derek', 'Devin', 'Javier', 'Miguel',
                   'Julian', 'Oscar', 'Blake', 'Cole', 'Joel', 'Ronald', 'Francisco', 'Bradley', 'Eduardo', 'Devon',
                   'Maxwell', 'Ruben', 'Ricardo', 'Derrick', 'Tanner', 'Angel', 'Brett', 'Martin', 'Spencer', 'Gavin',
                   'Henry', 'Troy', 'Victor', 'Darius', 'Drew', 'Jack', 'Beau', 'Liam', 'Oliver', 'Max', 'Angus',
                   'Ryley', 'Carl', 'Hamish', 'Mitch', 'Ben', 'Xavier', 'Stanley', 'Sigfried', 'Kenny', 'Hans']

    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Martinez',
                  'Taylor', 'Anderson', 'Wilson', 'Jackson', 'Wright',
                  'Perez', 'Walker', 'Hall', 'Young', 'Allen', 'King', 'Scott', 'Green', 'Baker', 'Adams',
                  'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker',
                  'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan',
                  'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres',
                  'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett',
                  'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson',
                  'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander',
                  'Russell', 'Griffin', 'Diaz', 'Hayes', 'Myers', 'Ford', 'Hamilton', 'Graham', 'Sullivan', 'Wallace',
                  'Woods', 'Cole', 'West', 'Jordan', 'Owens', 'Reynolds', 'Fisher', 'Ellis', 'Harrison', 'Gibson',
                  'Mcdonald', 'Cruz', 'Marshall', 'Ortiz', 'Gomez', 'Murray', 'Freeman', 'Nobel']

    weapons_leveled = {
        0: {ar15_weapon: 1, ar10_weapon: 1, ak47_weapon: 1, ak74_weapon: 1, ak556_weapon: 1, m1045_weapon: 1,
            m109_weapon: 1, sks_weapon: 1, g_17: 1, mosin_weapon: 1, m1911_45: 1, m1911_9mm: 1, m1911_10mm: 1,
            m1911_40sw: 1, m1_carbine_gun: 1, m2_carbine_gun: 1, m14_gun: 1, m1a_gun: 1, r870_gun: 1,
            supershorty_gun: 1},
        1: {g_17: 5},
        2: {g_17: 5},
        3: {g_17: 5},
        4: {g_17: 5},
    }

    # randomly generates player name
    first_name = choice(first_names)
    last_name = choice(last_names)
    name = f"{first_name} {last_name}"

    colours = copy(player_colours)

    # prevents duplicate player colours
    if len(players) > 0:
        for player in players:
            if player.fg_colour in colours:
                colours.remove(player.fg_colour)

    # randomly selects player colour
    player_colour = choice(colours)

    fighter_component = PlayerFighter(unarmed_meat_damage=10, unarmed_armour_damage=5, item_drops={},
                                      spawn_group_amount=1, weapons=weapons_leveled,
                                      helmet=helmets_leveled,
                                      bodyarmour=bodyarmour_leveled,
                                      )

    head_part = Head(hp=60, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                     connected_to={'body': (0, -41)})
    body_part = Body(hp=20, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                     connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                   'right leg': (3, -78), 'left leg': (-3, -78)})
    r_arm = Arm(hp=30, protection_ballistic=0, protection_physical=1,
                name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)})
    l_arm = Arm(hp=30, protection_ballistic=0, protection_physical=1,
                name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)})
    r_leg = Leg(hp=40, protection_ballistic=0, protection_physical=1,
                name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)})
    l_leg = Leg(hp=40, protection_ballistic=0, protection_physical=1,
                name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})

    body_parts = (body_part, head_part, r_arm, l_arm, r_leg, l_leg)

    player = Actor(0,
                   0,
                   '@',
                   player_colour,
                   name,
                   ai=PlayerCharacter,
                   fighter=fighter_component,
                   bodyparts=body_parts,
                   player=True,
                   inventory=Inventory(capacity=15),
                   )

    player.fighter.give_weapon(current_level)
    player.fighter.give_armour(current_level)

    player.fighter.attack_style_measured()

    return player


def add_player(engine: Engine, player: Actor):
    engine.players.append(player)
    engine.message_log.add_message(f"New squad member: {player.name}", colour.MAGENTA)
    return True
