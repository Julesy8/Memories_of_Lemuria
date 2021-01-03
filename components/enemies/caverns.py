from components.npc_templates import Fighter
from entity import Actor
from components.ai import HostileEnemy
from components.bodyparts import Bodypart

def placeholder_fighter():
    return Fighter(power = 10, bleeds = True)

Head = Bodypart(None, 10, 5, True, False, False, False, 'Head', 'Head')

Body = Bodypart(None, 10, 5, True, False, False, False, 'Body', 'Body')

R_Arm =  Bodypart(None, 10, 5, False, False, False, True, 'Right Arm', 'Arms')

L_Arm = Bodypart(None, 10, 5, False, False, False, True, 'Left Arm', 'Arms')

R_Leg = Bodypart(None, 10, 5, False, False, True, False, 'Right Leg', 'Legs')

L_Leg = Bodypart(None, 10, 5, False, False, True, False, 'Left Leg', 'Legs')

body_parts = (Head, Body, R_Arm, L_Arm, R_Leg, L_Leg)

placeholder_common = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = (255, 255, 255),
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    energy=100,
    attack_cost=100,
    move_cost=50
)

placeholder_uncommon = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = (0, 255, 0),
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    energy=100,
    attack_cost=100,
    move_cost=100

)

placeholder_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = (0, 0, 255),
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    energy=100,
    attack_cost=100,
    move_cost=100
)

placeholder_v_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = (255,0,255),
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    energy=100,
    attack_cost=100,
    move_cost=100
)

placeholder_legendary = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = (255, 128, 0),
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai = HostileEnemy,
    bodyparts = body_parts,
    energy=100,
    attack_cost=100,
    move_cost=100
)
