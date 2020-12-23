from components.npc_templates import Fighter
from entity import Actor
from components.ai import HostileEnemy
from components.bodyparts import Bodypart

def placeholder_fighter():
    return Fighter(power= 6, bleeds = True)

Head = Bodypart(5, 5, True, False, False, False, True, 'Head', 'Head')

Body = Bodypart(10, 5, True, False, False, False, True, 'Body', 'Body')

R_Arm =  Bodypart(5, 5, False, False, False, True, True, 'Right Arm', 'Arms')

L_Arm = Bodypart(5, 5, False, False, False, True, True, 'Left Arm', 'Arms')

R_Leg = Bodypart(5, 5, False, False, True, False, True, 'Right Leg', 'Legs')

L_Leg = Bodypart(5, 5, False, False, True, False, True, 'Left Leg', 'Legs')

body_parts = [Head, Body, R_Arm, L_Arm, R_Leg, L_Leg]

placeholder_common = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = [255, 255, 255],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts = body_parts
)

placeholder_uncommon = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = [0, 255, 0],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts = body_parts
)

placeholder_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = [0, 0, 255],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts = body_parts
)

placeholder_v_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = [255,0,255],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai = HostileEnemy,
    bodyparts = body_parts
)

placeholder_legendary = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = [255, 128, 0],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai = HostileEnemy,
    bodyparts = body_parts
)
