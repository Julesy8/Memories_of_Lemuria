from components.npc_templates import Fighter, GunFighter
from entity import Actor
from components.commonitems import pda
from components.ai import HostileEnemy, HostileAnimal, HostileEnemyArmed
from components.weapons.gun_maker import g_17, ak47_weapon, ar15_weapon
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

# health values scale with size of the animal roughly


def placeholder_fighter():
    return Fighter(unarmed_meat_damage=5, unarmed_armour_damage=5, item_drops={}, spawn_group_amount=1, weapons={})


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
    fg_colour=colour.YELLOW,
    name='Snake',
    fighter=Fighter(unarmed_meat_damage=10,
                    unarmed_armour_damage=2,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=2,
                    description='Large pythons lurk in the sewers, feeding on rodents and the occasional unfortunate '
                                'adventurer. The descendants of escaped pets, these are the least dangerous of the '
                                'reptilian creatures found in the depths.'
                    ),
    ai=HostileAnimal,
    bodyparts=(Body(hp=40, protection_ballistic=0, protection_physical=0, depth=15, width=120, height=15),
               Head(hp=5, protection_ballistic=0, protection_physical=0, depth=15, width=15, height=15)),
    inventory=Inventory(),

)

large_rat = Actor(
    x=0, y=0,
    char='r',
    fg_colour=colour.BROWN,
    name='Large Rat',
    fighter=Fighter(unarmed_meat_damage=6,
                    unarmed_armour_damage=0,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=4,
                    description='Rodents grown large from feeding on the detritus and death in the depths. While single '
                                'rats are little more than an annoyance for experienced adventurers, large groups may '
                                'serve a larger nuisance.'
                    ),
    ai=HostileAnimal,
    bodyparts=(Body(hp=10, protection_ballistic=0, protection_physical=0, depth=15, width=20, height=15),),
    inventory=Inventory(),

)

rat_king = Actor(
    x=0, y=0,
    char='R',
    fg_colour=colour.BROWN,
    name='Rat King',
    fighter=Fighter(unarmed_meat_damage=15,
                    unarmed_armour_damage=0,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=1,
                    description='A writhing mass of rodents, their tails intertwined. As dangerous as it is disgusting.'
                    ),
    ai=HostileAnimal,
    bodyparts=(Body(hp=200, protection_ballistic=0, protection_physical=0, depth=20, width=40, height=40,
                    name='Writhing Mass'),),
    inventory=Inventory(),
)

aligator = Actor(
    x=0, y=0,
    char='A',
    fg_colour=colour.GREEN,
    name='Aligator',
    fighter=Fighter(unarmed_meat_damage=30,
                    unarmed_armour_damage=4,
                    ap_per_turn=50,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=1,
                    description='A large reptile that has somehow found its way into the sewers.'
                    ),
    ai=HostileEnemy,
    bodyparts=(Body(hp=150, protection_ballistic=0, protection_physical=3, depth=50, width=250, height=50),
               Head(hp=30, protection_ballistic=0, protection_physical=3, depth=50, width=250, height=50),
               Leg(hp=35, protection_ballistic=0, name='right fore leg', protection_physical=4, depth=11, width=11,
                   height=15),
               Leg(hp=35, protection_ballistic=0, name='left fore leg', protection_physical=4, depth=11, width=11,
                   height=15),
               Leg(hp=35, protection_ballistic=0, name='right hind leg', protection_physical=4, depth=11, width=11,
                   height=15),
               Leg(hp=35, protection_ballistic=0, name='left hind leg', protection_physical=4, depth=11, width=11,
                   height=15),
               ),
    inventory=Inventory(),
)

outlaw = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BROWN,
    name='Outlaw',
    fighter=GunFighter(unarmed_meat_damage=10,
                       unarmed_armour_damage=1,
                       ranged_accuracy=1.4,
                       fears_death=True,
                       item_drops={None: 500, pda: 100, },
                       weapons={ak47_weapon: 5, },
                       spawn_group_amount=1,
                       description="Many criminals and deviants have retreated into the depths in hopes of evading the "
                                   "detection by the tyrannical surface world forces. Often carrying knives and "
                                   "pistols, they won't hesitate to attack lone adventurers."
                       ),
    ai=HostileEnemyArmed,
    bodyparts=(Body(hp=60, protection_ballistic=0, protection_physical=1, depth=20, width=35, height=56),
               Head(hp=20, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26),
               Arm(hp=30, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=30, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=40, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=40, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(),
)

peacekeeper = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BLUE,
    name='Peace Keeper',
    fighter=GunFighter(unarmed_meat_damage=10,
                       unarmed_armour_damage=1,
                       ranged_accuracy=1.4,
                       fears_death=True,
                       item_drops={},
                       weapons={},
                       spawn_group_amount=1,
                       description="With surface world police and military forces struggling to maintain order, peace "
                                   "keepers have been deployed to quell rebellion and anarchy. These blue-helmeted "
                                   "foreign soldiers often be seen in the caverns in pursuit of outlaws and anti-"
                                   "government elements."
                       ),
    ai=HostileEnemyArmed,
    bodyparts=(Body(hp=60, protection_ballistic=0.2, protection_physical=2, depth=20, width=35, height=56),
               Head(hp=20, protection_ballistic=0.16, protection_physical=2, depth=20, width=20, height=26),
               Arm(hp=30, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=30, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=40, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=40, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(),
)


maniac = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_RED,
    name='Maniac',
    fighter=GunFighter(unarmed_meat_damage=10,
                       unarmed_armour_damage=1,
                       ranged_accuracy=1.4,
                       fears_death=False,
                       item_drops={},
                       weapons={},
                       spawn_group_amount=2,
                       description="Under the pressure of the oppressive darkness and savagery of the depths, many "
                                   "individuals fleeing the tyrannical surface government have fallen to violent "
                                   "insanity. Often carrying knives, they are deadly to the inexperienced adventurer."
                       ),
    ai=HostileEnemy,
    bodyparts=(
               Body(hp=60, protection_ballistic=0, protection_physical=0, depth=20, width=35, height=56),
               Head(hp=20, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26),
               Arm(hp=30, protection_ballistic=0, protection_physical=0,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=30, protection_ballistic=0, protection_physical=0,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=40, protection_ballistic=0, protection_physical=0,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=40, protection_ballistic=0, protection_physical=0,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(),
)

"""
Caverns
"""

troglodyte = Actor(
    x=0, y=0,
    char='t',
    fg_colour=colour.WHITE,
    name='Troglodyte',
    fighter=Fighter(unarmed_meat_damage=16,
                    unarmed_armour_damage=1,
                    responds_to_sound=False,
                    fears_death=True,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=4,
                    description="Humans degenerated by hundreds of generations of exposure to the depths, and recently "
                                "exposed to humanity again due to recent incursions into the depths. Crawling on all "
                                "fours, they have a pale and ghoulish appearance."
                    ),
    ai=HostileEnemy,
    bodyparts=(
               Body(hp=60, protection_ballistic=0, protection_physical=0, depth=17, width=30, height=40),
               Head(hp=10, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=18),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='right arm', depth=8, width=8, height=55),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='left arm', depth=8, width=8, height=55),
               Leg(hp=40, protection_ballistic=0, protection_physical=0,
                   name='right leg', depth=10, width=12, height=70),
               Leg(hp=40, protection_ballistic=0, protection_physical=0,
                   name='left leg', depth=10, width=12, height=70)
               ),
    inventory=Inventory(),
)

soldier = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BLUE,
    name='Soldier',
    fighter=GunFighter(unarmed_meat_damage=20,
                       unarmed_armour_damage=4,
                       ranged_accuracy=1.2,
                       fears_death=True,
                       item_drops={},
                       weapons={},
                       spawn_group_amount=2,
                       description="Soldiers tasked with protecting deep underground military bases from civilians, "
                                   "armed with heavy weaponry and permitted to use lethal force at their discretion."
                       ),
    ai=HostileEnemyArmed,
    bodyparts=(
               Body(hp=60, protection_ballistic=0.28, protection_physical=3, depth=20, width=35, height=56),
               Head(hp=20, protection_ballistic=0.2, protection_physical=3, depth=20, width=20, height=26),
               Arm(hp=30, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78),
               Arm(hp=30, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78),
               Leg(hp=40, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100),
               Leg(hp=40, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100)
               ),
    inventory=Inventory(),
)

wyrm = Actor(
    x=0, y=0,
    char='W',
    fg_colour=colour.JADE,
    name='Wyrm',
    fighter=Fighter(unarmed_meat_damage=25,
                    unarmed_armour_damage=3,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=1,
                    description="A large serpentine reptilian creature of Draconian origins. It burrows deep into the "
                                "earth and ambushes unsuspecting prey."
                    ),
    ai=HostileEnemy,
    bodyparts=(Body(hp=100, protection_ballistic=0, protection_physical=0, depth=30, width=300, height=30),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=30, width=30, height=35)),
    inventory=Inventory(),
)

chimera = Actor(
    x=0, y=0,
    char='C',
    fg_colour=colour.LIGHT_YELLOW,
    name='Chimera',
    fighter=Fighter(unarmed_meat_damage=21,
                    unarmed_armour_damage=3,
                    move_ap_cost=75,
                    fears_death=True,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=2,
                    description='A quadrupedal genetically modified abomination escaped from the labs of the deep '
                                'underground military base. It is hairless with sharp teeth and claws.'
                    ),
    ai=HostileEnemy,
    bodyparts=(Body(hp=80, protection_ballistic=0, protection_physical=0, depth=17, width=25, height=50),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=18),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='right arm', depth=8, width=8, height=35),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='left arm', depth=8, width=8, height=35),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='right leg', depth=10, width=12, height=35),
               Leg(hp=30, protection_ballistic=0, protection_physical=0,
                   name='left leg', depth=10, width=12, height=35)
               ),
    inventory=Inventory(),
)

dogman = Actor(
    x=0, y=0,
    char='D',
    fg_colour=colour.LIGHT_GRAY,
    name='Dogman',
    fighter=Fighter(unarmed_meat_damage=33,
                    unarmed_armour_damage=3,
                    move_ap_cost=50,
                    responds_to_sound=False,
                    fears_death=True,
                    item_drops={},
                    weapons={},
                    spawn_group_amount=1,
                    description="A very large canine-like humanoid biped of unknown origins. Some say they are another "
                                "genetically modified abomination created in the underground labs, however, "
                                "hundreds of reports of these werewolf like creatures stalking the forests for "
                                "centuries seems to point to a more mysterious origin."
                    ),
    ai=HostileEnemy,
    bodyparts=(Body(hp=200, protection_ballistic=0.2, protection_physical=2, depth=35, width=50, height=75),
               Head(hp=100, protection_ballistic=0.16, protection_physical=2, depth=50, width=40, height=45),
               Arm(hp=140, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=18, width=18, height=104),
               Arm(hp=140, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=18, width=18, height=104),
               Leg(hp=150, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=23, width=23, height=133),
               Leg(hp=150, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=23, width=23, height=133)
               ),
    inventory=Inventory(),
)

"""
Nexion
"""