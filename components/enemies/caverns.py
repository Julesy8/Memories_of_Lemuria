from components.npc_templates import Fighter
from entity import Actor, Item, Stacking
from components.ai import HostileEnemy
from components.bodyparts import Bodypart
from components import consumables
from components.inventory import Inventory
from components.level import Level
import colour


def placeholder_fighter():
    return Fighter(unarmed_damage=10)


Head = Bodypart(hp=10, defence=5, head=True, vital=True, name='head', part_type='Head', base_chance_to_hit=80)
Body = Bodypart(hp=10, defence=5, body=True, vital=True, name='body', part_type='Body', base_chance_to_hit=90)
R_Arm = Bodypart(hp=10, defence=5, arm=True, name='right arm', part_type='Arms', base_chance_to_hit=80)
L_Arm = Bodypart(hp=10, defence=5, arm=True, name='left arm', part_type='Arms', base_chance_to_hit=80)
R_Leg = Bodypart(hp=10, defence=5, leg=True, name='right leg', part_type='Legs', base_chance_to_hit=80)
L_Leg = Bodypart(hp=10, defence=5, leg=True, name='left leg', part_type='Legs', base_chance_to_hit=80)

body_parts = (Body, Head, R_Arm, L_Arm, R_Leg, L_Leg)  # TODO: Make array instead of tuple

placeholder_common = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.WHITE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50)
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
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50)
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
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50)
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
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50)
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
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50)
)

health_potion = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GREEN,
    bg_colour=None,
    name="Health Potion",
    weight=1,
    stacking=None,
    consumable=consumables.HealingConsumable(amount=4),
    weapon=None,
    wearable=None
)

placeholder_item = Item(
    x=0, y=0,
    char="?",
    fg_colour=colour.MAGENTA,
    bg_colour=None,
    name="Placeholder Item",
    weight=1,
    stacking=None,
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
    weight=1,
    stacking=None,
    consumable=None,
    weapon=consumables.Weapon(
        damage=50,
        maximum_range=100,
        base_accuracy=0.9,
        ranged_accuracy=10,
        ranged=True,
        projectile_type=True
    ),
    wearable=None
)

sword = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.RED,
    bg_colour=None,
    name="Sword",
    weight=1,
    stacking=None,
    consumable=None,
    weapon=consumables.Weapon(
        damage=1000,
        maximum_range=1,
        base_accuracy=0.9,
        ranged_accuracy=10,
        two_handed=True,
        cutting_type=True
    ),
    wearable=None
)

helmet = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Helmet",
    weight=1,
    stacking=None,
    consumable=None,
    weapon=None,
    wearable=(consumables.Wearable(
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
    weight=1,
    stacking=None,
    consumable=None,
    weapon=None,
    wearable=(consumables.Wearable(
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
    weight=1,
    stacking=None,
    consumable=None,
    weapon=None,
    wearable=(consumables.Wearable(
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
    weight=1,
    stacking=None,
    consumable=None,
    weapon=None,
    wearable=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Body'
    ))
)

medkit = Item(
    x=0, y=0,
    char="+",
    fg_colour=colour.GREEN,
    bg_colour=None,
    name="Medkit",
    weight=1,
    stacking=Stacking(stack_size=1),
    consumable=consumables.HealingConsumable(amount=20),
    weapon=None,
    wearable=None
)
