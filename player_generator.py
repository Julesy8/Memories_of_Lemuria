from __future__ import annotations

from typing import TYPE_CHECKING

import colour
from components.weapons.gun_maker import (g_17, g_40sw, g_10mm, ar15_weapon_300, ar10_weapon,
                                          ar15_weapon, ar_9mm, ar_40sw, ak47_weapon, ak74_weapon, ak556_weapon,
                                          m1045_weapon, m109_weapon, sks_weapon, mosin_weapon, m1911_45, m1911_9mm,
                                          m1911_10mm, m1911_40sw, m1_carbine_gun, m2_carbine_gun, m14_gun, r870_gun,
                                          supershorty_gun, m629_gun, m610_gun, tt33_gun, h015_gun, m3_gun,
                                          ppsh_gun, svt40_gun)

from components.armour import (helmet_ech, helmet_pasgt, helmet_m1,
                               helmet_ssh68, bodyarmour_pasgt, bodyarmour_improved, bodyarmour_interceptor,
                               platecarrier_3, platecarrier_4, platecarrier_3a)

from entity import Actor
from components.inventory import Inventory
from components.ai import PlayerCharacter
from random import choice
from components.npc_templates import PlayerFighter
from components.bodyparts import Body, Arm, Leg, Head
from copy import copy

if TYPE_CHECKING:
    from engine import Engine

weapons_levelled = {
    0: {
        m610_gun: 40,
        tt33_gun: 50,
        m1_carbine_gun: 40,
        mosin_weapon: 60,
        sks_weapon: 100,
        m629_gun: 15,
        g_17: 5,
        m1911_9mm: 30,
        m1911_45: 5,
        h015_gun: 20,
        m3_gun: 3,
        ar15_weapon: 1,
        ak47_weapon: 1,
        svt40_gun: 4,
        g_40sw: 1,
        ak556_weapon: 1,
        ak74_weapon: 1,
        m1911_40sw: 1,
        m2_carbine_gun: 2,
        m1045_weapon: 2,
        m109_weapon: 2,
        m14_gun: 2,
        ppsh_gun: 2,
        m1911_10mm: 1,
},

    1: {
        sks_weapon: 100,
        svt40_gun: 40,
        g_17: 5,
        g_40sw: 3,
        g_10mm: 1,
        m1911_45: 3,
        m1911_9mm: 5,
        m1911_10mm: 1,
        m1911_40sw: 2,
        m1_carbine_gun: 20,
        m629_gun: 10,
        h015_gun: 20,
        m610_gun: 4,
        tt33_gun: 15,
        m3_gun: 8,
        m14_gun: 3,
        ar15_weapon: 5,
        ar15_weapon_300: 1,
        ar_9mm: 1,
        ar_40sw: 1,
        ak47_weapon: 5,
        ak556_weapon: 1,
        ak74_weapon: 1,
        mosin_weapon: 30,
        m1045_weapon: 1,
        m109_weapon: 3,
        ppsh_gun: 2,
        m2_carbine_gun: 3,
        r870_gun: 2,
    },

    2: {
        sks_weapon: 120,
        ar15_weapon: 60,
        ar15_weapon_300: 3,
        ar_9mm: 2,
        ar_40sw: 2,
        ak47_weapon: 28,
        ak556_weapon: 5,
        ak74_weapon: 15,
        svt40_gun: 15,
        g_17: 5,
        g_40sw: 3,
        g_10mm: 1,
        m1911_45: 3,
        m1911_9mm: 5,
        m1911_10mm: 1,
        m1911_40sw: 2,
        mosin_weapon: 30,
        m1_carbine_gun: 20,
        m14_gun: 6,
        m3_gun: 10,
        m629_gun: 5,
        h015_gun: 6,
        tt33_gun: 4,
        m1045_weapon: 2,
        m109_weapon: 6,
        ppsh_gun: 2,
        m2_carbine_gun: 4,
        r870_gun: 4,
    },

    3: {
        sks_weapon: 40,
        ar15_weapon: 65,
        ar15_weapon_300: 5,
        ar_9mm: 4,
        ar_40sw: 4,
        ak47_weapon: 40,
        ak556_weapon: 10,
        ak74_weapon: 20,
        svt40_gun: 10,
        g_17: 5,
        g_40sw: 3,
        g_10mm: 1,
        m1911_45: 3,
        m1911_9mm: 5,
        m1911_10mm: 1,
        m1911_40sw: 2,
        mosin_weapon: 20,
        m1_carbine_gun: 15,
        m14_gun: 12,
        m3_gun: 12,
        m629_gun: 6,
        h015_gun: 2,
        tt33_gun: 3,
        m1045_weapon: 4,
        m109_weapon: 8,\

        ppsh_gun: 3,
        m2_carbine_gun: 5,
        r870_gun: 6,
        supershorty_gun: 1,
        ar10_weapon: 5,
    },

    4: {
        sks_weapon: 20,
        ar15_weapon: 75,
        ar15_weapon_300: 10,
        ar_9mm: 7,
        ar_40sw: 7,
        ak47_weapon: 50,
        ak556_weapon: 20,
        ak74_weapon: 30,
        svt40_gun: 6,
        g_17: 3,
        g_40sw: 1,
        g_10mm: 1,
        m1911_45: 1,
        m1911_9mm: 1,
        m1911_10mm: 1,
        m1911_40sw: 1,
        mosin_weapon: 8,
        m1_carbine_gun: 6,
        m14_gun: 16,
        m3_gun: 10,
        m1045_weapon: 4,
        m109_weapon: 8,
        ppsh_gun: 5,
        m2_carbine_gun: 9,
        r870_gun: 10,
        supershorty_gun: 2,
        ar10_weapon: 6,
    },

    5: {
        sks_weapon: 15,
        ar15_weapon: 75,
        ar15_weapon_300: 16,
        ar_9mm: 13,
        ar_40sw: 13,
        ak47_weapon: 56,
        ak556_weapon: 26,
        ak74_weapon: 36,
        g_17: 3,
        g_40sw: 1,
        g_10mm: 1,
        m1911_45: 1,
        m1911_9mm: 1,
        m1911_10mm: 1,
        m1911_40sw: 1,
        mosin_weapon: 4,
        m1_carbine_gun: 5,
        m14_gun: 20,
        m3_gun: 4,
        m1045_weapon: 14,
        m109_weapon: 18,
        ppsh_gun: 6,
        m2_carbine_gun: 7,
        r870_gun: 14,
        supershorty_gun: 3,
        ar10_weapon: 6,
    },
}

helmets_levelled = {
    0: {helmet_m1: 1,
        helmet_ssh68: 1,
        None: 5
        },
    1: {helmet_m1: 3,
        helmet_ssh68: 1,
        helmet_pasgt: 1,
        None: 10
        },
    2: {helmet_m1: 4,
        helmet_ssh68: 2,
        helmet_pasgt: 2,
        None: 15
        },
    3: {
        helmet_pasgt: 4,
        helmet_ech: 2,
        None: 20
        },
    4: {
        helmet_pasgt: 6,
        helmet_ech: 3,
        None: 20
        },
    5: {
        helmet_pasgt: 6,
        helmet_ech: 3,
        None: 10
        },
}

bodyarmour_levelled = {
    0: {
        platecarrier_3a: 1,
        None: 10,
        },
    1: {bodyarmour_pasgt: 3,
        platecarrier_3a: 4,
        platecarrier_3: 1,
        None: 20,
        },
    2: {bodyarmour_pasgt: 1,
        platecarrier_3a: 2,
        platecarrier_3: 1,
        None: 10,
        },
    3: {bodyarmour_pasgt: 3,
        bodyarmour_improved: 1,
        platecarrier_3a: 5,
        platecarrier_3: 3,
        None: 20,
        },
    4: {bodyarmour_pasgt: 1,
        bodyarmour_improved: 2,
        platecarrier_3a: 3,
        platecarrier_3: 5,
        None: 20,
        },
    5: {bodyarmour_pasgt: 1,
        bodyarmour_improved: 3,
        bodyarmour_interceptor: 2,
        platecarrier_3a: 1,
        platecarrier_3: 4,
        platecarrier_4: 1,
        None: 20,
        },
}


def generate_player(current_level: int, players: list):
    player_colours = [colour.BLUE, colour.JADE, colour.MAGENTA, colour.ORANGE, colour.YELLOW,
                      colour.PURPLE, colour.CYAN, colour.LIGHT_BLUE, colour.LIGHT_GREEN,
                      colour.LIGHT_MAGENTA, colour.LIGHT_YELLOW]

    first_names = ['James', 'John', 'Robert', 'Michael', 'Will', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles',
                   'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew',
                   'Kenneth', 'George', 'Joshua', 'Kevin', 'Brian', 'Edward', 'Nicholas', 'Tyler', 'Brandon',
                   'Jacob', 'Ryan', 'Justin', 'Jonathan', 'Austin', 'Cody', 'Eric', 'Benjamin', 'Adam', 'Samuel',
                   'Jeremy', 'Patrick', 'Alexander', 'Jesse', 'Zachary', 'Dylan', 'Nathan', 'Scott', 'Kyle', 'Jeffrey',
                   'Sean', 'Travis', 'Bryan', 'Ethan', 'Carlos', 'Ian', 'Peter', 'Christian', 'Cameron',
                   'Shawn', 'Luis', 'Jared', 'Juan', 'Caleb', 'Evan', 'Gabriel', 'Chase', 'Antonio', 'Cory', 'Curtis',
                   'Seth', 'Adrian', 'Jorge', 'Trevor', 'Dustin', 'Mario', 'Derek', 'Devin', 'Javier', 'Miguel',
                   'Julian', 'Oscar', 'Blake', 'Cole', 'Joel', 'Ronald', 'Francisco', 'Bradley', 'Eduardo', 'Devon',
                   'Maxwell', 'Ruben', 'Ricardo', 'Derrick', 'Tanner', 'Angel', 'Brett', 'Martin', 'Spencer', 'Gavin',
                   'Henry', 'Troy', 'Victor', 'Darius', 'Drew', 'Jack', 'Beau', 'Liam', 'Oliver', 'Max', 'Angus',
                   'Ryley', 'Carl', 'Mitch', 'Ben', 'Xavier', 'Stanley', 'Sigfried', 'Kenny', 'Hans', 'Ronnie',
                   'Simon', 'Skinny', 'Nelson', 'Willy', 'Theron', 'Clifford', 'Trey', 'Bertie', 'Craig', 'Vance',
                   'Tyrone', 'Otis', 'Kris', 'Randall', 'Brendan', 'Phillip', 'Warren', 'Arnold', 'Dean', 'Daryl',
                   'Glen', 'Harry', 'Tommy', 'Ted', ' Tony', 'Elijah', 'Dennis', 'Kurt', 'Brent', 'Dominic', 'Gary',
                   'Leonard', 'Ramon', 'Mel', 'Marcos']

    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Martinez',
                  'Taylor', 'Anderson', 'Wilson', 'Jackson', 'Wright', 'Gates', 'Archer', 'Fleming', 'Grimes', 'Duran'
                  'Perez', 'Walker', 'Hall', 'Young', 'Allen', 'King', 'Scott', 'Green', 'Baker', 'Adams', 'House',
                  'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker',
                  'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan',
                  'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres',
                  'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett',
                  'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson',
                  'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander',
                  'Russell', 'Griffin', 'Diaz', 'Hayes', 'Myers', 'Ford', 'Hamilton', 'Graham', 'Sullivan', 'Wallace',
                  'Woods', 'Cole', 'West', 'Jordan', 'Owens', 'Reynolds', 'Fisher', 'Ellis', 'Harrison', 'Gibson',
                  'Mcdonald', 'Cruz', 'Marshall', 'Ortiz', 'Gomez', 'Murray', 'Freeman', 'Yates', 'Swanson', 'Moore',
                  'Flynn', 'Whitaker', 'Werner', 'Hurst', 'Bradford', 'Holt', 'Blair', 'Howell', 'Schmidt', 'Pratt',
                  'Nolan', 'Conley', 'Davidson', 'Hardy', 'Recard', 'Willis', 'Schaffer', 'Meyers', 'Carr', 'Mosley',
                  'Lane', 'Weaver', 'Callahan', 'Vaughn', 'Crowley', 'Elliott', 'Edwards', 'Preston', 'Khan', 'Reese']

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
                                      spawn_group_amount=1, weapons=weapons_levelled,
                                      helmet=helmets_levelled,
                                      bodyarmour=bodyarmour_levelled,
                                      )

    head_part = Head(hp=180, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                     connected_to={'body': (0, -41)})
    body_part = Body(hp=60, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                     connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                   'right leg': (3, -78), 'left leg': (-3, -78)})
    r_arm = Arm(hp=90, protection_ballistic=0, protection_physical=1,
                name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)})
    l_arm = Arm(hp=90, protection_ballistic=0, protection_physical=1,
                name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)})
    r_leg = Leg(hp=120, protection_ballistic=0, protection_physical=1,
                name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)})
    l_leg = Leg(hp=120, protection_ballistic=0, protection_physical=1,
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
    engine.message_log.add_message(f"Recruited new squad member: {player.name}", colour.MAGENTA)
    return True
