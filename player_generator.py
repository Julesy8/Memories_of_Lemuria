from __future__ import annotations

from typing import TYPE_CHECKING

import colour
from components.weapons.gun_maker import g_17
from entity import Actor
from components.inventory import Inventory
from components.ai import PlayerCharacter
from random import choice
from components.npc_templates import PlayerFighter
from components.bodyparts import Body, Arm, Leg, Head
from copy import copy

if TYPE_CHECKING:
    from engine import Engine


def generate_player(current_level: int, players: list):

    player_colours = [colour.BLUE, colour.GREEN, colour.RED, colour.MAGENTA, colour.ORANGE, colour.YELLOW,
                      colour.PURPLE,
                      colour.CYAN, colour.LIGHT_BLUE, colour.LIGHT_GREEN, colour.LIGHT_RED, colour.LIGHT_MAGENTA]

    first_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles',
                   'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew',
                   'Kenneth',
                   'George', 'Joshua', 'Kevin', 'Brian', 'Edward', 'William', 'Nicholas', 'Tyler', 'Brandon', 'Jacob',
                   'Ryan', 'Justin', 'Jonathan', 'Austin', 'Cody', 'Eric', 'Benjamin', 'Adam', 'Samuel', 'Jeremy',
                   'Patrick', 'Alexander', 'Jesse', 'Zachary', 'Dylan', 'Nathan', 'Scott', 'Kyle', 'Jeffrey', 'Sean',
                   'Travis', 'Bryan', 'Ethan', 'Luke', 'Carlos', 'Ian', 'Peter', 'Christian', 'Cameron', 'Shawn',
                   'Luis',
                   'Jared', 'Juan', 'Caleb', 'Evan', 'Gabriel', 'Chase', 'Antonio', 'Cory', 'Curtis', 'Seth', 'Adrian',
                   'Jorge', 'Trevor', 'Dustin', 'Mario', 'Derek', 'Devin', 'Javier', 'Miguel', 'Julian', 'Oscar',
                   'Blake', 'Cole', 'Joel', 'Ronald', 'Francisco', 'Bradley', 'Eduardo', 'Devon', 'Maxwell', 'Ruben',
                   'Ricardo', 'Derrick', 'Tanner', 'Angel', 'Brett', 'Martin', 'Spencer', 'Gavin', 'Henry', 'Troy',
                   'Victor', 'Darius', 'Drew', ]

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
                  'Mcdonald', 'Cruz', 'Marshall', 'Ortiz', 'Gomez', 'Murray', 'Freeman']

    weapons_leveled = {
        0: {g_17: 5},
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
                                      spawn_group_amount=1, weapons=weapons_leveled[current_level])

    head_part = Head(hp=60, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26)
    body_part = Body(hp=100, protection_ballistic=0, protection_physical=0, depth=20, width=35, height=56)
    r_arm = Arm(hp=70, protection_ballistic=0, protection_physical=0, name='right arm', depth=10, width=10,
                height=78)
    l_arm = Arm(hp=70, protection_ballistic=0, protection_physical=0, name='left arm', depth=10, width=10,
                height=78)
    r_leg = Leg(hp=75, protection_ballistic=0, protection_physical=0, name='right leg', depth=12, width=15,
                height=100)
    l_leg = Leg(hp=75, protection_ballistic=0, protection_physical=0, name='left leg', depth=12, width=15,
                height=100)

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

    player.fighter.give_weapon()

    return player


def add_player(engine: Engine, player: Actor):
    engine.players.append(player)
    engine.message_log.add_message(f"New squad member: {player.name}", colour.MAGENTA)
    return True
