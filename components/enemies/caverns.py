from components.npc_templates import Fighter
from entity import Actor, Item, Stacking
from components.ai import HostileEnemy
from components.bodyparts import Arm, Leg, Head, Body
from components import consumables
from components.inventory import Inventory
import colour

import components.weapons.glock17


def placeholder_fighter():
    return Fighter(unarmed_meat_damage=10, unarmed_armour_damage=5)


Head_part = Head(hp=10, defence=5)
Body_part = Body(hp=10, defence=5)
R_Arm = Arm(hp=10, defence=5, name='right arm')
L_Arm = Arm(hp=10, defence=5, name='left arm')
R_Leg = Leg(hp=10, defence=5, name='right leg')
L_Leg = Leg(hp=10, defence=5, name='left leg')

body_parts = (Body_part, Head_part, R_Arm, L_Arm, R_Leg, L_Leg)

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
    can_spawn_armed=True,
)

placeholder_uncommon = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.GREEN,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
    can_spawn_armed=True,
)

caverns_enemies = {
    'Placeholder': {
        'weapons': [None, components.weapons.glock17.glock_17],
        'weapon weight': [2, 1],
        'armour': [],
        'armour weight': [],
        'drops': [],
        'drop weight': [],
    }
}

placeholder_item = Item(
    x=0, y=0,
    char="?",
    fg_colour=colour.MAGENTA,
    bg_colour=None,
    name="Placeholder Item",
    weight=1,
    stacking=None,
    usable_properties=None,
)

helmet = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Helmet",
    weight=1,
    stacking=None,
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Head',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
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
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Arms',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
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
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Legs',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
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
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Body',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
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
    usable_properties=consumables.HealingConsumable(amount=20),
)

