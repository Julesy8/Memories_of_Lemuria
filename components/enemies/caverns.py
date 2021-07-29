from components.npc_templates import Fighter
from entity import Actor, Item
from components.ai import HostileEnemy
from components.bodyparts import Bodypart
from components.consumables import HealingConsumable, Weapon, Wearable
from components.inventory import Inventory
import colour


def placeholder_fighter():
    return Fighter(power=10)


Head = Bodypart(hp=10, defence=5, vital=True, walking=False, grasping=False,
                connected_to=[], equipped=None, name='Head', part_type='Head', base_chance_to_hit=80)
Body = Bodypart(hp=10, defence=5, vital=True, walking=False, grasping=False,
                connected_to=[], equipped=None, name='Body', part_type='Body', base_chance_to_hit=90)
R_Arm = Bodypart(hp=10, defence=5, vital=False, walking=False, grasping=True,
                 connected_to=[], equipped=None, name='Right Arm', part_type='Arms', base_chance_to_hit=80)
L_Arm = Bodypart(hp=10, defence=5, vital=False, walking=False, grasping=True,
                 connected_to=[], equipped=None, name='Left Arm', part_type='Arms', base_chance_to_hit=80)
R_Leg = Bodypart(hp=10, defence=5, vital=False, walking=False, grasping=False,
                 connected_to=[], equipped=None, name='Right Leg', part_type='Legs', base_chance_to_hit=80)
L_Leg = Bodypart(hp=10, defence=5, vital=False, walking=False, grasping=False,
                 connected_to=[], equipped=None, name='Left Leg', part_type='Legs', base_chance_to_hit=80)

body_parts = (Head, Body, R_Arm, L_Arm, R_Leg, L_Leg)

placeholder_common = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.WHITE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    attack_interval=0,
    attacks_per_turn=1,
    move_interval=0,
    moves_per_turn=2,
    inventory=Inventory(capacity=0, held=None),
)

placeholder_uncommon = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.JADE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    attack_interval=0,
    attacks_per_turn=1,
    move_interval=2,
    moves_per_turn=1,
    inventory=Inventory(capacity=0, held=None),
)

placeholder_rare = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.BLUE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0, held=None),
)

placeholder_v_rare = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.PURPLE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0, held=None),
)

placeholder_legendary = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.ORANGE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0, held=None),
)

health_potion = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GREEN,
    bg_colour=None,
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
    weapon=None,
    wearable=None
)

placeholder_item = Item(
    x=0, y=0,
    char="?",
    fg_colour=colour.MAGENTA,
    bg_colour=None,
    name="Placeholder Item",
    consumable=None,
    weapon=None,
    wearable=None
)

glock = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Fawty",
    consumable=None,
    weapon=Weapon(
        damage=50,
        ranged=True,
        maximum_range=100,
        base_accuracy=0.9,
        ranged_accuracy=10
    ),
    wearable=None
)

sword = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Sword",
    consumable=None,
    weapon=Weapon(
        damage=50,
        ranged=False,
        maximum_range=1,
        base_accuracy=0.9,
        ranged_accuracy=10
    ),
    wearable=None
)

helmet = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Helmet",
    consumable=None,
    weapon=None,
    wearable=(Wearable(
        protection=2,
        fits_bodypart_type='Head'
    ))
)

pauldron = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Pauldrons",
    consumable=None,
    weapon=None,
    wearable=(Wearable(
        protection=2,
        fits_bodypart_type='Arms'
    ))
)

greaves = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Greaves",
    consumable=None,
    weapon=None,
    wearable=(Wearable(
        protection=2,
        fits_bodypart_type='Legs'
    ))
)

chestplate = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Chestplate",
    consumable=None,
    weapon=None,
    wearable=(Wearable(
        protection=2,
        fits_bodypart_type='Body'
    ))
)