from components.npc_templates import Fighter, GunFighter
from entity import Actor
from components.ai import HostileEnemy
from components.bodyparts import Arm, Leg, Head, Body
from components.inventory import Inventory
import colour

"""
-----
Sewers
-----

Giant Snake
Large Rat
Alligator
Outlaw
Peace Keeper
Maniac

-----
Caverns
-----

Troglodyte 
Soldier
Wyrm
Chimera
Dogman
Sasquatch

-----
The Nexion
-----

Cultists
Chimera
Reptilian Workers

-----
D.U.M.B
-----

Chimera
Reptilian Workers
Super Soldiers
Grey Workers

-----
Reptilian Hive
-----

Reptilian Workers
Reptilian Soldiers
Reptilian Captains
Grey Workers
Grey Telepaths
Insectoid
Hive Mother

"""


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

"""
Sewers
"""

giant_snake = Actor(
    x=0, y=0,
    char='S',
    fg_colour=colour.JADE,
    name='Snake',
    fighter=Fighter(unarmed_meat_damage=10, unarmed_armour_damage=2),
    ai=HostileEnemy,
    bodyparts=(Body(hp=45, protection_ballistic=0, protection_physical=0, depth=15, width=120, height=15),
               Head(hp=10, protection_ballistic=0, protection_physical=0, depth=15, width=15, height=15)),
    inventory=Inventory(capacity=0),
    fears_death=False,
    item_drops={},
    weapons={},
    spawn_group_amount=2
)

large_rat = Actor(
    x=0, y=0,
    char='r',
    fg_colour=colour.BROWN,
    name='Large Rat',
    fighter=Fighter(unarmed_meat_damage=6, unarmed_armour_damage=0),
    ai=HostileEnemy,
    bodyparts=(Body(hp=20, protection_ballistic=0, protection_physical=0, depth=15, width=20, height=15),),
    inventory=Inventory(capacity=0),
    fears_death=False,
    item_drops={},
    weapons={},
    spawn_group_amount=4
)

aligator = Actor(
    x=0, y=0,
    char='A',
    fg_colour=colour.GREEN,
    name='Aligator',
    fighter=Fighter(unarmed_meat_damage=30, unarmed_armour_damage=15, ap_per_turn=50),
    ai=HostileEnemy,
    bodyparts=(Body(hp=250, protection_ballistic=0, protection_physical=3, depth=50, width=250, height=50),
               Head(hp=150, protection_ballistic=0, protection_physical=3, depth=50, width=250, height=50),
               Leg(hp=35, protection_ballistic=0, name='right fore leg', protection_physical=4, depth=11, width=11,
                   height=15),
               Leg(hp=35, protection_ballistic=0, name='left fore leg', protection_physical=4, depth=11, width=11,
                   height=15),
               Leg(hp=35, protection_ballistic=0, name='right hind leg', protection_physical=4, depth=11, width=11,
                   height=15),
               Leg(hp=35, protection_ballistic=0, name='left hind leg', protection_physical=4, depth=11, width=11,
                   height=15),
               ),
    inventory=Inventory(capacity=0),
    fears_death=False,
    item_drops={},
    weapons={},
    spawn_group_amount=1
)

outlaw = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BROWN,
    name='Outlaw',
    fighter=GunFighter(unarmed_meat_damage=10, unarmed_armour_damage=3, ranged_accuracy=1.4),
    ai=HostileEnemy,
    bodyparts=(Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26),
               Body(hp=100, protection_ballistic=0, protection_physical=1, depth=20, width=35, height=56),
               Arm(hp=70, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=70, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=75, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=75, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(capacity=0),
    fears_death=True,
    item_drops={},
    weapons={},
    spawn_group_amount=1
)

peacekeeper = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BLUE,
    name='Peace Keeper',
    fighter=GunFighter(unarmed_meat_damage=10, unarmed_armour_damage=3, ranged_accuracy=1.3),
    ai=HostileEnemy,
    bodyparts=(Head(hp=40, protection_ballistic=0.16, protection_physical=2, depth=20, width=20, height=26),
               Body(hp=100, protection_ballistic=0.2, protection_physical=2, depth=20, width=35, height=56),
               Arm(hp=70, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=70, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=75, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=75, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(capacity=0),
    fears_death=True,
    item_drops={},
    weapons={},
    spawn_group_amount=1
)


maniac = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_RED,
    name='Maniac',
    fighter=Fighter(unarmed_meat_damage=20, unarmed_armour_damage=5),
    ai=HostileEnemy,
    bodyparts=(Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26),
               Body(hp=100, protection_ballistic=0, protection_physical=0, depth=20, width=35, height=56),
               Arm(hp=70, protection_ballistic=0, protection_physical=0,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=70, protection_ballistic=0, protection_physical=0,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=75, protection_ballistic=0, protection_physical=0,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=75, protection_ballistic=0, protection_physical=0,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(capacity=0),
    fears_death=False,
    item_drops={},
    weapons={},
    spawn_group_amount=1
)

"""
Caverns
"""

troglodyte = Actor(
    x=0, y=0,
    char='t',
    fg_colour=colour.WHITE,
    name='Troglodyte',
    fighter=Fighter(unarmed_meat_damage=16, unarmed_armour_damage=1),
    ai=HostileEnemy,
    bodyparts=(Head(hp=32, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=18),
               Body(hp=80, protection_ballistic=0, protection_physical=0, depth=17, width=30, height=40),
               Leg(hp=56, protection_ballistic=0, protection_physical=0,
                   name='right arm', depth=8, width=8, height=55),
               Leg(hp=56, protection_ballistic=0, protection_physical=0,
                   name='left arm', depth=8, width=8, height=55),
               Leg(hp=60, protection_ballistic=0, protection_physical=0,
                   name='right leg', depth=10, width=12, height=70),
               Leg(hp=60, protection_ballistic=0, protection_physical=0,
                   name='left leg', depth=10, width=12, height=70)
               ),
    inventory=Inventory(capacity=0),
    fears_death=True,
    item_drops={},
    weapons={},
    spawn_group_amount=4
)

soldier = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BLUE,
    name='Soldier',
    fighter=GunFighter(unarmed_meat_damage=20, unarmed_armour_damage=4, ranged_accuracy=1.2),
    ai=HostileEnemy,
    bodyparts=(Head(hp=40, protection_ballistic=0.2, protection_physical=3, depth=20, width=20, height=26),
               Body(hp=100, protection_ballistic=0.28, protection_physical=3, depth=20, width=35, height=56),
               Arm(hp=70, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=70, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=75, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=75, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(capacity=0),
    fears_death=True,
    item_drops={},
    weapons={},
    spawn_group_amount=2
)

wyrm = Actor(
    x=0, y=0,
    char='W',
    fg_colour=colour.JADE,
    name='Wyrm',
    fighter=Fighter(unarmed_meat_damage=25, unarmed_armour_damage=3),
    ai=HostileEnemy,
    bodyparts=(Body(hp=100, protection_ballistic=0, protection_physical=0, depth=30, width=300, height=30),
               Head(hp=80, protection_ballistic=0, protection_physical=0, depth=30, width=30, height=35)),
    inventory=Inventory(capacity=0),
    fears_death=False,
    item_drops={},
    weapons={},
    spawn_group_amount=1
)

chimera = Actor(
    x=0, y=0,
    char='C',
    fg_colour=colour.LIGHT_YELLOW,
    name='Chimera',
    fighter=Fighter(unarmed_meat_damage=21, unarmed_armour_damage=3, move_ap_cost=75),
    ai=HostileEnemy,
    bodyparts=(Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=18),
               Body(hp=80, protection_ballistic=0, protection_physical=0, depth=17, width=25, height=50),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='right arm', depth=8, width=8, height=35),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='left arm', depth=8, width=8, height=35),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='right leg', depth=10, width=12, height=35),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='left leg', depth=10, width=12, height=35)
               ),
    inventory=Inventory(capacity=0),
    fears_death=True,
    item_drops={},
    weapons={},
    spawn_group_amount=2
)

dogman = Actor(
    x=0, y=0,
    char='D',
    fg_colour=colour.LIGHT_GRAY,
    name='Dogman',
    fighter=Fighter(unarmed_meat_damage=33, unarmed_armour_damage=3, move_ap_cost=50),
    ai=HostileEnemy,
    bodyparts=(Head(hp=100, protection_ballistic=0.16, protection_physical=2, depth=50, width=40, height=45),
               Body(hp=200, protection_ballistic=0.2, protection_physical=2, depth=35, width=50, height=75),
               Arm(hp=140, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=18, width=18, height=104),
               Arm(hp=140, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=18, width=18, height=104),
               Leg(hp=150, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=23, width=23, height=133),
               Leg(hp=150, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=23, width=23, height=133)
               ),
    inventory=Inventory(capacity=0),
    fears_death=True,
    item_drops={},
    weapons={},
    spawn_group_amount=1
)

"""
Nexion
"""