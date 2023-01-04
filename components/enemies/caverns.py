from components.npc_templates import Fighter
from entity import Actor
from components.ai import HostileEnemy
from components.bodyparts import Arm, Leg, Head, Body
from components.inventory import Inventory
import colour


def placeholder_fighter():
    return Fighter(unarmed_meat_damage=5, unarmed_armour_damage=5)


# Head_part = Head(hp=10, protection_ballistic=5)
# Body_part = Body(hp=10, protection_ballistic=5)
# R_Arm = Arm(hp=10, protection_ballistic=5, name='right arm')
# L_Arm = Arm(hp=10, protection_ballistic=5, name='left arm')
# R_Leg = Leg(hp=10, protection_ballistic=5, name='right leg')
# L_Leg = Leg(hp=10, protection_ballistic=5, name='left leg')

# body_parts = (Body_part, Head_part, R_Arm, L_Arm, R_Leg, L_Leg)

# enemies - snake, rat, bandit, feral dog,

giant_snake = Actor(
    x=0, y=0,
    char='s',
    fg_colour=colour.JADE,
    name='Giant Snake',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=(Body(hp=45, protection_ballistic=0, protection_physical=0, depth=15, width=120, height=15),
               Head(hp=10, protection_ballistic=0, protection_physical=0, depth=15, width=15, height=15)),
    inventory=Inventory(capacity=0),
    fears_death=False,
    item_drops={},
    weapons={},
    spawn_group_amount=1
)

large_rat = Actor(
    x=0, y=0,
    char='r',
    fg_colour=colour.BROWN,
    name='Large Rat',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=(Body(hp=10, protection_ballistic=0, protection_physical=0, depth=10, width=15, height=35),),
    inventory=Inventory(capacity=0),
    fears_death=False,
    item_drops={},
    weapons={},
    spawn_group_amount=3
)


