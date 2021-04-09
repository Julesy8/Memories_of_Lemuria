from components.npc_templates import Fighter
from entity import Actor
from components.ai import HostileEnemy
from components.bodyparts import Bodypart
from components.inventory import Inventory
import colour


def placeholder_fighter():
    return Fighter(power = 10)


Head = Bodypart(None, 10, 5, True, False, False, False, 'Head', 'Head', base_chance_to_hit=80)
Body = Bodypart(None, 10, 5, True, False, False, False, 'Body', 'Body', base_chance_to_hit=90)
R_Arm =  Bodypart(None, 10, 5, False, False, False, True, 'Right Arm', 'Arms', base_chance_to_hit=80)
L_Arm = Bodypart(None, 10, 5, False, False, False, True, 'Left Arm', 'Arms', base_chance_to_hit=80)
R_Leg = Bodypart(None, 10, 5, False, False, True, False, 'Right Leg', 'Legs', base_chance_to_hit=80)
L_Leg = Bodypart(None, 10, 5, False, False, True, False, 'Left Leg', 'Legs', base_chance_to_hit=80)

body_parts = (Head, Body, R_Arm, L_Arm, R_Leg, L_Leg)

placeholder_common = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.WHITE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    inventory=Inventory(capacity=0),
    bodyparts=body_parts,
    move_cost=50
)

placeholder_uncommon = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.JADE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    inventory=Inventory(capacity=0),
    bodyparts=body_parts,
    energy_regain = 50,
    attack_cost = 50,
)

placeholder_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.BLUE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    inventory=Inventory(capacity=0),
    bodyparts=body_parts,
)

placeholder_v_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.PURPLE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    inventory=Inventory(capacity=0),
    bodyparts=body_parts,
)

placeholder_legendary = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.ORANGE,
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai = HostileEnemy,
    inventory=Inventory(capacity=0),
    bodyparts = body_parts,
)
