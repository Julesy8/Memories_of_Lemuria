from components.npc_templates import Fighter
from entity import Actor, Item
from components.ai import HostileEnemy
from components.bodyparts import Bodypart
from components.consumables import HealingConsumable
from components.inventory import Inventory
import colour


def placeholder_fighter():
    return Fighter(power=10)


Head = Bodypart(10, 5, True, False, False, 'Head', 'Head', base_chance_to_hit=80)
Body = Bodypart(10, 5, True, False, False, 'Body', 'Body', base_chance_to_hit=90)
R_Arm =  Bodypart(10, 5, False, False, True, 'Right Arm', 'Arms', base_chance_to_hit=80)
L_Arm = Bodypart(10, 5, False, False, True, 'Left Arm', 'Arms', base_chance_to_hit=80)
R_Leg = Bodypart(10, 5, False, False, False, 'Right Leg', 'Legs', base_chance_to_hit=80)
L_Leg = Bodypart(10, 5, False, False, False, 'Left Leg', 'Legs', base_chance_to_hit=80)

body_parts = (Head, Body, R_Arm, L_Arm, R_Leg, L_Leg)

placeholder_common = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.WHITE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    attack_interval=0,
    attacks_per_turn=1,
    move_interval=0,
    moves_per_turn=2,
    inventory=Inventory(capacity=0),
)

placeholder_uncommon = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.JADE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    attack_interval=0,
    attacks_per_turn=1,
    move_interval=2,
    moves_per_turn=1,
    inventory=Inventory(capacity=0),
)

placeholder_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.BLUE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
)

placeholder_v_rare = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.PURPLE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
)

placeholder_legendary = Actor(
    x=0, y=0,
    char = 'N',
    fg_colour = colour.ORANGE,
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    ai = HostileEnemy,
    bodyparts = body_parts,
    inventory=Inventory(capacity=0),
)

health_potion = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GREEN,
    bg_colour=None,
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
)
