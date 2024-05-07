from components.npc_templates import Fighter, GunFighter, MeleeFighter
from entity import Actor
from components.commonitems import bandages, medkit, repair_kit
from components.weapons.melee import knife, hammer
from components.ai import HostileEnemy, HostileAnimal, HostileEnemyArmed, DeadAI
from components.bodyparts import Arm, Leg, Head, Body
from components.inventory import Inventory
import colour

from components.weapons.gun_maker import (g_17, g_40sw, g_10mm, ar15_weapon_300, ar10_weapon, mcr_weapon,
                                          ar15_weapon, ar_9mm, ar_40sw, ak47_weapon, ak74_weapon, ak556_weapon,
                                          m1045_weapon, m109_weapon, sks_weapon, mosin_weapon, m1911_45, m1911_9mm,
                                          m1911_10mm, m1911_40sw, m1_carbine_gun, m2_carbine_gun, m14_gun, r870_gun,
                                          supershorty_gun, m629_gun, m610_gun, dexix_gun, tt33_gun, h015_gun, m3_gun,
                                          ppsh_gun, svt40_gun)
from components.armour import (helmet_riot, helmet_ech, helmet_altyn, helmet_pasgt, helmet_ronin, helmet_m1,
                               helmet_ssh68, bodyarmour_pasgt, bodyarmour_improved, bodyarmour_interceptor,
                               platecarrier_3, platecarrier_4, platecarrier_3a)

# weapons_levelled_low = {
#
#     0: {
#         # low tier
#         m610_gun: 40,},
#
#     1: {
#         # low tier
#         sks_weapon: 100,
#     },
#
#     2: {
#         # low tier
#         sks_weapon: 120,
#     },
#
#     3: {
#         sks_weapon: 40,
#     },
#
#     4: {
#         sks_weapon: 20,
#     },
#
#     5: {
#         sks_weapon: 15,
#     },
# }

weapons_levelled_low = {

    0: {
        # low tier
        m610_gun: 40,
        tt33_gun: 50,
        m1_carbine_gun: 80,
        mosin_weapon: 60,
        sks_weapon: 100,
        m629_gun: 15,
        g_17: 5,
        m1911_9mm: 30,
        m1911_45: 5,
        h015_gun: 20,
        m1911_40sw: 1,
        g_40sw: 1, },

    1: {
        # low tier
        sks_weapon: 100,
        svt40_gun: 40,
        g_17: 5,
        g_40sw: 3,
        g_10mm: 1,
        m1911_45: 3,
        m1911_9mm: 5,
        m1911_10mm: 1,
        m1911_40sw: 2,
        m1_carbine_gun: 20,
        m629_gun: 10,
        h015_gun: 20,
        m610_gun: 4,
        tt33_gun: 15,
        mosin_weapon: 30,
    },

    2: {
        # low tier
        sks_weapon: 120,
        svt40_gun: 15,
        g_17: 5,
        g_40sw: 3,
        g_10mm: 1,
        m1911_45: 3,
        m1911_9mm: 5,
        m1911_10mm: 1,
        m1911_40sw: 2,
        mosin_weapon: 30,
        m1_carbine_gun: 20,
        m3_gun: 10,
        m629_gun: 5,
        h015_gun: 5,
        tt33_gun: 4,
    },

    3: {
        sks_weapon: 40,
        ar15_weapon: 65,
        ar15_weapon_300: 5,
        ar_9mm: 4,
        ar_40sw: 4,
        ak47_weapon: 40,
        ak556_weapon: 10,
        ak74_weapon: 20,
        svt40_gun: 10,
        g_17: 5,
        g_40sw: 3,
        g_10mm: 1,
        m1911_45: 3,
        m1911_9mm: 5,
        m1911_10mm: 1,
        m1911_40sw: 2,
        mosin_weapon: 20,
        m1_carbine_gun: 15,
        m14_gun: 12,
        m3_gun: 12,
        m629_gun: 6,
    },

    4: {
        sks_weapon: 20,
        ar15_weapon: 75,
        ar15_weapon_300: 10,
        ar_9mm: 7,
        ar_40sw: 7,
        ak47_weapon: 50,
        ak556_weapon: 20,
        ak74_weapon: 30,
        svt40_gun: 6,
        g_17: 15,
        g_40sw: 1,
        g_10mm: 1,
        m1911_45: 1,
        m1911_9mm: 1,
        m1911_10mm: 1,
        m1911_40sw: 1,
        m1_carbine_gun: 6,
        m3_gun: 10,
        m2_carbine_gun: 9,
    },

    5: {
        sks_weapon: 15,
        ar15_weapon: 75,
        ar15_weapon_300: 16,
        ar_9mm: 13,
        ar_40sw: 13,
        ak47_weapon: 56,
        ak556_weapon: 26,
        ak74_weapon: 36,
        g_10mm: 1,
        m1911_45: 1,
        m1911_10mm: 1,
        m14_gun: 20,
        m3_gun: 4,
        ppsh_gun: 6,
        m2_carbine_gun: 7,
        r870_gun: 14,
    },
}

weapons_levelled_mid = {

    0: {
        sks_weapon: 100,
        m1_carbine_gun: 80,
        m3_gun: 3,
        m2_carbine_gun: 2,
        ppsh_gun: 2,
        svt40_gun: 4,
        m14_gun: 2
    },

    1: {
        # mid tier
        sks_weapon: 100,
        m1_carbine_gun: 80,
        svt40_gun: 4,
        ar15_weapon: 5,
        ar15_weapon_300: 1,
        ar_9mm: 1,
        ar_40sw: 1,
        ak47_weapon: 5,
        ak556_weapon: 1,
        ak74_weapon: 1,
        ppsh_gun: 2,
        m2_carbine_gun: 3,
    },

    2: {
        sks_weapon: 120,
        svt40_gun: 15,
        m14_gun: 6,
        ar15_weapon: 60,
        ar15_weapon_300: 3,
        ar_9mm: 2,
        ar_40sw: 2,
        ak47_weapon: 28,
        ak556_weapon: 5,
        ak74_weapon: 15,
        ppsh_gun: 2,
        m2_carbine_gun: 4,
        r870_gun: 4,
    },

    3: {
        ar15_weapon: 65,
        ar15_weapon_300: 5,
        ar_9mm: 4,
        ar_40sw: 4,
        ak47_weapon: 56,
        ak556_weapon: 10,
        ak74_weapon: 20,
        m14_gun: 12,
        ppsh_gun: 3,
        m2_carbine_gun: 5,
        r870_gun: 6,
        supershorty_gun: 1,
        ar10_weapon: 5,
    },

    4: {
        ar15_weapon: 75,
        ar15_weapon_300: 10,
        ar_9mm: 7,
        ar_40sw: 7,
        ak47_weapon: 50,
        ak556_weapon: 20,
        ak74_weapon: 30,
        m14_gun: 16,
        m1045_weapon: 4,
        m109_weapon: 8,
        ppsh_gun: 5,
        m2_carbine_gun: 9,
        r870_gun: 10,
        supershorty_gun: 2,
        dexix_gun: 1,
        ar10_weapon: 6,
    },

    5: {
        ar15_weapon: 375,
        ar15_weapon_300: 80,
        ar_9mm: 65,
        ar_40sw: 65,
        ak47_weapon: 280,
        ak556_weapon: 130,
        ak74_weapon: 180,
        m14_gun: 100,
        m1045_weapon: 70,
        m109_weapon: 90,
        ppsh_gun: 30,
        m2_carbine_gun: 35,
        r870_gun: 70,
        supershorty_gun: 15,
        dexix_gun: 5,
        ar10_weapon: 30,
    },
}

weapons_levelled_high = {

    0: {
        ak556_weapon: 2,
        ak74_weapon: 2,
        ar15_weapon: 2,
        ak47_weapon: 2,
        g_10mm: 3,
        ar15_weapon_300: 1,
        m1911_10mm: 3,
        ar_9mm: 1,
        ar_40sw: 1},

    1: {
        m14_gun: 3,
        ar15_weapon: 5,
        ar15_weapon_300: 1,
        ar_9mm: 1,
        ar_40sw: 1,
        ak47_weapon: 5,
        ak556_weapon: 1,
        ak74_weapon: 1,
        m1045_weapon: 1,
        m109_weapon: 3,
        ppsh_gun: 2,
        m2_carbine_gun: 3,
        r870_gun: 2,
        supershorty_gun: 1,
        dexix_gun: 1,
    },

    2: {
        ar15_weapon: 150,
        ar15_weapon_300: 7,
        ar_9mm: 5,
        ar_40sw: 5,
        ak47_weapon: 85,
        ak556_weapon: 13,
        ak74_weapon: 37,
        m14_gun: 15,
        m1045_weapon: 5,
        m109_weapon: 15,
        ppsh_gun: 5,
        m2_carbine_gun: 10,
        r870_gun: 10,
        supershorty_gun: 2,
        dexix_gun: 5,
        ar10_weapon: 7,
        mcr_weapon: 1,
    },

    3: {
        ar15_weapon: 65,
        ar15_weapon_300: 5,
        ar_9mm: 4,
        ar_40sw: 4,
        ak47_weapon: 80,
        ak556_weapon: 10,
        ak74_weapon: 20,
        m14_gun: 12,
        m1045_weapon: 4,
        m109_weapon: 8,
        ppsh_gun: 3,
        m2_carbine_gun: 5,
        r870_gun: 6,
        supershorty_gun: 2,
        dexix_gun: 2,
        ar10_weapon: 5,
        mcr_weapon: 1,
    },

    4: {
        ar15_weapon: 65,
        ar15_weapon_300: 10,
        ar_9mm: 7,
        ar_40sw: 7,
        ak47_weapon: 50,
        ak556_weapon: 20,
        ak74_weapon: 30,
        m14_gun: 16,
        m1045_weapon: 4,
        m109_weapon: 8,
        r870_gun: 10,
        supershorty_gun: 2,
        dexix_gun: 2,
        ar10_weapon: 6,
        mcr_weapon: 1,
    },

    5: {
        ar15_weapon: 75,
        ar15_weapon_300: 10,
        ar_9mm: 7,
        ar_40sw: 7,
        ak47_weapon: 50,
        ak556_weapon: 20,
        ak74_weapon: 30,
        m14_gun: 16,
        m1045_weapon: 4,
        m109_weapon: 8,
        r870_gun: 10,
        supershorty_gun: 2,
        dexix_gun: 1,
        ar10_weapon: 6,
        mcr_weapon: 2,
    },
}

# bodyarmour

bodyarmour_levelled_low = {
    0: {
        None: 1,
    },
    1: {bodyarmour_pasgt: 1,
        platecarrier_3a: 2,
        None: 10,
        },
    2: {bodyarmour_pasgt: 2,
        platecarrier_3a: 4,
        platecarrier_3: 2,
        None: 20,
        },
    3: {bodyarmour_pasgt: 2,
        bodyarmour_improved: 1,
        platecarrier_3a: 4,
        platecarrier_3: 2,
        None: 20,
        },
    4: {bodyarmour_pasgt: 2,
        bodyarmour_improved: 1,
        platecarrier_3a: 4,
        platecarrier_3: 2,
        None: 20,
        },
    5: {bodyarmour_pasgt: 2,
        bodyarmour_improved: 1,
        platecarrier_3a: 4,
        platecarrier_3: 2,
        None: 20,
        },
}

bodyarmour_levelled_mid = {
    0: {
        platecarrier_3a: 1,
        None: 10,
    },
    1: {bodyarmour_pasgt: 3,
        platecarrier_3a: 4,
        platecarrier_3: 1,
        None: 20,
        },
    2: {bodyarmour_pasgt: 1,
        platecarrier_3a: 2,
        platecarrier_3: 1,
        None: 10,
        },
    3: {bodyarmour_pasgt: 3,
        bodyarmour_improved: 1,
        platecarrier_3a: 5,
        platecarrier_3: 3,
        None: 20,
        },
    4: {bodyarmour_pasgt: 1,
        bodyarmour_improved: 2,
        platecarrier_3a: 3,
        platecarrier_3: 5,
        None: 20,
        },
    5: {bodyarmour_pasgt: 1,
        bodyarmour_improved: 3,
        bodyarmour_interceptor: 2,
        platecarrier_3a: 1,
        platecarrier_3: 4,
        platecarrier_4: 1,
        None: 20,
        },
}

bodyarmour_levelled_high = {
    0: {bodyarmour_pasgt: 1,
        platecarrier_3a: 2,
        },
    1: {bodyarmour_pasgt: 3,
        platecarrier_3: 1,
        },
    2: {
        bodyarmour_improved: 1,
        platecarrier_3: 2,
    },
    3: {
        bodyarmour_improved: 2,
        bodyarmour_interceptor: 1,
        platecarrier_3: 6,
        platecarrier_4: 1,
    },
    4: {
        bodyarmour_improved: 6,
        bodyarmour_interceptor: 1,
        platecarrier_4: 2,
    },
    5: {
        bodyarmour_improved: 6,
        bodyarmour_interceptor: 2,
        platecarrier_4: 1,
    },
}

# helmets

helmets_levelled_low = {
    0: {helmet_riot: 3,
        None: 15
        },
    1: {helmet_riot: 3,
        helmet_m1: 3,
        helmet_ssh68: 1,
        None: 20
        },
    2: {
        helmet_m1: 1,
        helmet_ssh68: 1,
        helmet_pasgt: 2,
        None: 20
    },
    3: {helmet_m1: 2,
        helmet_ssh68: 2,
        helmet_pasgt: 3,
        None: 20
        },
    4: {helmet_m1: 3,
        helmet_ssh68: 3,
        helmet_pasgt: 3,
        None: 15
        },
    5: {helmet_m1: 5,
        helmet_ssh68: 5,
        helmet_pasgt: 6,
        helmet_ech: 2,
        None: 20
        },
}

helmets_levelled_mid = {
    0: {helmet_m1: 1,
        helmet_ssh68: 1,
        None: 5
        },
    1: {helmet_m1: 3,
        helmet_ssh68: 1,
        helmet_pasgt: 1,
        None: 10
        },
    2: {helmet_m1: 4,
        helmet_ssh68: 2,
        helmet_pasgt: 2,
        None: 15
        },
    3: {
        helmet_pasgt: 4,
        helmet_ech: 2,
        None: 20
    },
    4: {
        helmet_pasgt: 6,
        helmet_ech: 3,
        None: 20
    },
    5: {
        helmet_pasgt: 6,
        helmet_ech: 3,
        None: 10
    },
}

helmets_levelled_high = {
    0: {
        helmet_m1: 1,
        helmet_ssh68: 1,
    },
    1: {
        helmet_m1: 3,
        helmet_ssh68: 1,
        helmet_pasgt: 1,
    },
    2: {helmet_m1: 3,
        helmet_ssh68: 2,
        helmet_pasgt: 2,
        },
    3: {
        helmet_pasgt: 6,
        helmet_ech: 2,
        helmet_altyn: 1,
    },
    4: {
        helmet_ech: 20,
        helmet_ronin: 1,
        helmet_altyn: 2,
    },
    5: {
        helmet_ech: 15,
        helmet_ronin: 1,
        helmet_altyn: 2,
    },
}

"""
Tunnels
"""

giant_snake = Actor(
    x=0, y=0,
    char='S',
    fg_colour=colour.YELLOW,
    name='Snake',
    fighter=Fighter(unarmed_meat_damage=5,
                    unarmed_armour_damage=1,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=2,
                    description='Large pythons lurk in the tunnels, feeding on rodents and the occasional unfortunate '
                                'adventurer. The descendants of escaped pets, these are the least dangerous of the '
                                'reptilian creatures found in the depths.'
                    ),
    ai=DeadAI,
    bodyparts=(Body(hp=40, protection_ballistic=0, protection_physical=0, depth=16, width=120, height=16,
                    connected_to={'head': (68, 0)}),
               Head(hp=5, protection_ballistic=0, protection_physical=0, depth=16, width=16, height=16,
                    connected_to={'body': (-68, 0)})),
    inventory=Inventory(),
)

wyrm = Actor(
    x=0, y=0,
    char='W',
    fg_colour=colour.GREEN,
    name='Wyrm',
    fighter=Fighter(unarmed_meat_damage=30,
                    unarmed_armour_damage=5,
                    move_ap_cost=50,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=1,
                    description='An alien reptilian creature resemble a huge serpent, ten metres in length.'
                    ),
    ai=DeadAI,
    bodyparts=(Body(hp=400, protection_ballistic=0.15, protection_physical=0, depth=160, width=1200, height=160,
                    connected_to={'head': (680, 0)}),
               Head(hp=120, protection_ballistic=0.25, protection_physical=0, depth=160, width=160, height=160,
                    connected_to={'body': (-680, 0)})),
    inventory=Inventory(),
)

large_rat = Actor(
    x=0, y=0,
    char='r',
    fg_colour=colour.BROWN,
    name='Large Rat',
    fighter=Fighter(unarmed_meat_damage=3,
                    move_ap_cost=200,
                    unarmed_armour_damage=0,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=2,
                    description='Rodents grown large from feeding on the detritus and death in the depths. While single'
                                'rats are little more than an annoyance for experienced adventurers, large groups may '
                                'serve a larger nuisance.'
                    ),
    ai=DeadAI,
    bodyparts=(
        Body(hp=10, protection_ballistic=0, protection_physical=0, depth=15, width=20, height=15, connected_to={}),),
    inventory=Inventory(),

)

blob = Actor(
    x=0, y=0,
    char='O',
    fg_colour=colour.LIGHT_PURPLE,
    name='Blob',
    bleeds=False,
    fighter=Fighter(unarmed_meat_damage=6,
                    unarmed_armour_damage=7,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=10,
                    description='An experimental gelatinous self-replicating bioweapon. It attacks by trapping and '
                                'digesting its prey.'
                    ),
    ai=DeadAI,
    bodyparts=(
        Body(hp=30, protection_ballistic=0, protection_physical=0, depth=100, width=100, height=100, connected_to={}),),
    inventory=Inventory(),
)

rat_king = Actor(
    x=0, y=0,
    char='R',
    fg_colour=colour.BROWN,
    name='Rat King',
    fighter=Fighter(unarmed_meat_damage=6,
                    unarmed_armour_damage=0,
                    responds_to_sound=False,
                    fears_death=False,
                    item_drops={},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=1,
                    description='A writhing mass of rodents, their tails intertwined. As dangerous as it is disgusting.'
                    ),
    ai=DeadAI,
    bodyparts=(Body(hp=120, protection_ballistic=0, protection_physical=0, depth=20, width=40, height=40,
                    name='writhing mass', connected_to={}),),
    inventory=Inventory(),
)

zombie_soldier = Actor(
    x=0, y=0,
    char='Z',
    fg_colour=colour.LIGHT_BROWN,
    name='Undead Soldier',
    fighter=GunFighter(unarmed_meat_damage=10,
                       unarmed_armour_damage=1,
                       fears_death=False,
                       item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                       weapons=weapons_levelled_low,
                       helmet=helmets_levelled_low,
                       bodyarmour=bodyarmour_levelled_low,
                       spawn_group_amount=1,
                       ranged_accuracy=15.0,
                       automatic_fire_duration=0.5,
                       felt_recoil=5.0,
                       firing_ap_cost=3.0,
                       ap_distance_cost_modifier=1.0,
                       description="Corpses of soldiers reanimated by dark magic or alien technology. They retain "
                                   "some ability to use firearms."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=140, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=30, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

zombie = Actor(
    x=0, y=0,
    char='Z',
    fg_colour=colour.LIGHT_JADE,
    name='Undead Shambler',
    fighter=Fighter(unarmed_meat_damage=10,
                    unarmed_armour_damage=1,
                    fears_death=False,
                    item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=3,
                    description="A corpse reanimated by dark magic or alien technology."
                    ),
    ai=DeadAI,
    bodyparts=(Body(hp=140, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=30, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

fast_zombie = Actor(
    x=0, y=0,
    char='Z',
    fg_colour=colour.JADE,
    name='Undead Sprinter',
    fighter=Fighter(unarmed_meat_damage=10,
                    unarmed_armour_damage=1,
                    fears_death=False,
                    move_ap_cost=50,
                    item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=2,
                    description="A corpse reanimated by dark magic or alien technology. They're fast runners."
                    ),
    ai=DeadAI,
    bodyparts=(Body(hp=140, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=30, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

hulk_zombie = Actor(
    x=0, y=0,
    char='H',
    fg_colour=colour.JADE,
    name='Undead Hulk',
    fighter=Fighter(unarmed_meat_damage=20,
                    unarmed_armour_damage=1,
                    move_ap_cost=200,
                    fears_death=False,
                    item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                    weapons={},
                    helmet={},
                    bodyarmour={},
                    spawn_group_amount=1,
                    description="A corpse reanimated by dark magic or alien technology. A mutated hulking mass, "
                                "slow but terrifyingly strong."
                    ),
    ai=DeadAI,
    bodyparts=(Body(hp=360, protection_ballistic=0, protection_physical=1, depth=40, width=72, height=112,
                    connected_to={'head': (0, 82), 'right arm': (46, -22), 'left arm': (-46, -22),
                                  'right leg': (6, -156), 'left leg': (-6, -156)}, aim_location_offset=28),
               Head(hp=120, protection_ballistic=0, protection_physical=0, depth=40, width=40, height=52,
                    connected_to={'body': (0, -82)}),
               Arm(hp=180, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=20, width=20, height=156, connected_to={'body': (-46, 22)}),
               Arm(hp=180, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=20, width=20, height=156, connected_to={'left arm': (46, 22)}),
               Leg(hp=240, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=24, width=30, height=200, connected_to={'right leg': (-6, 156)}),
               Leg(hp=240, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=24, width=30, height=200, connected_to={'left leg': (6, 156)})
               ),
    inventory=Inventory(),
)

test_dummy = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BROWN,
    name='Test Dummy',
    fighter=GunFighter(unarmed_meat_damage=5,
                       unarmed_armour_damage=1,
                       fears_death=True,
                       item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                       weapons=weapons_levelled_low,
                       helmet=helmets_levelled_low,
                       bodyarmour=bodyarmour_levelled_low,
                       spawn_group_amount=1,
                       description="Footsoldier of the Luciferian Volunteer Army, motivated to maintain the current "
                                   "order. Not very well trained or equipped."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=120, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

grunt = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BROWN,
    name='LVA Grunt',
    fighter=GunFighter(unarmed_meat_damage=5,
                       unarmed_armour_damage=1,
                       fears_death=True,
                       item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                       weapons=weapons_levelled_low,
                       helmet=helmets_levelled_low,
                       bodyarmour=bodyarmour_levelled_low,
                       spawn_group_amount=1,
                       ranged_accuracy=11.0,
                       automatic_fire_duration=0.5,
                       felt_recoil=1.2,
                       firing_ap_cost=1.1,
                       ap_distance_cost_modifier=1.7,
                       description="Footsoldier of the Luciferian Volunteer Army, motivated to maintain the current "
                                   "order. Not very well trained or equipped."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=120, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

reptilian = Actor(
    x=0, y=0,
    char='R',
    fg_colour=colour.LIGHT_GREEN,
    name='Reptilian Worker',
    fighter=Fighter(unarmed_meat_damage=15,
                       unarmed_armour_damage=4,
                       fears_death=False,
                       item_drops={None: 100},
                       weapons={},
                       helmet={},
                       bodyarmour={},
                       spawn_group_amount=1,
                       description="A reptilian-type humanoid alien. They are tall and muscular."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=156, protection_ballistic=0.15, protection_physical=2, depth=26, width=46, height=72,
                    connected_to={'head': (0, 53), 'right arm': (29, -14), 'left arm': (-29, -14),
                                  'right leg': (3, -101), 'left leg': (-3, -101)}, aim_location_offset=18),
               Head(hp=52, protection_ballistic=0.15, protection_physical=0, depth=26, width=26, height=33,
                    connected_to={'body': (0, -68)}),
               Arm(hp=78, protection_ballistic=0.15, protection_physical=2,
                   name='right arm', depth=13, width=13, height=101, connected_to={'body': (-29, 14)}),
               Arm(hp=78, protection_ballistic=0.15, protection_physical=2,
                   name='left arm', depth=13, width=13, height=101, connected_to={'left arm': (29, 14)}),
               Leg(hp=104, protection_ballistic=0.15, protection_physical=2,
                   name='right leg', depth=15, width=19, height=130, connected_to={'right leg': (-3, 101)}),
               Leg(hp=104, protection_ballistic=0.15, protection_physical=2,
                   name='left leg', depth=15, width=19, height=130, connected_to={'left leg': (3, 101)})
               ),
    inventory=Inventory(),
)

reptilian_soldier = Actor(
    x=0, y=0,
    char='R',
    fg_colour=colour.GREEN,
    name='Reptilian Soldier',
    fighter=GunFighter(unarmed_meat_damage=15,
                       unarmed_armour_damage=4,
                       fears_death=False,
                       item_drops={None: 100},
                       weapons=weapons_levelled_high,
                       felt_recoil=0.7,
                       ranged_accuracy=7.0,
                       firing_ap_cost=0.8,
                       ap_distance_cost_modifier=1.1,
                       helmet={},
                       bodyarmour={},
                       spawn_group_amount=1,
                       description="A reptilian-type humanoid alien. They are tall and muscular."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=156, protection_ballistic=0.3, protection_physical=4, depth=26, width=46, height=72,
                    connected_to={'head': (0, 53), 'right arm': (29, -14), 'left arm': (-29, -14),
                                  'right leg': (3, -101), 'left leg': (-3, -101)}, aim_location_offset=18),
               Head(hp=52, protection_ballistic=0.2, protection_physical=4, depth=26, width=26, height=33,
                    connected_to={'body': (0, -68)}),
               Arm(hp=78, protection_ballistic=0.15, protection_physical=4,
                   name='right arm', depth=13, width=13, height=101, connected_to={'body': (-29, 14)}),
               Arm(hp=78, protection_ballistic=0.15, protection_physical=4,
                   name='left arm', depth=13, width=13, height=101, connected_to={'left arm': (29, 14)}),
               Leg(hp=104, protection_ballistic=0.15, protection_physical=4,
                   name='right leg', depth=15, width=19, height=130, connected_to={'right leg': (-3, 101)}),
               Leg(hp=104, protection_ballistic=0.15, protection_physical=4,
                   name='left leg', depth=15, width=19, height=130, connected_to={'left leg': (3, 101)})
               ),
    inventory=Inventory(),
)

soldier = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BROWN,
    name='LVA Soldier',
    fighter=GunFighter(unarmed_meat_damage=5,
                       unarmed_armour_damage=1,
                       fears_death=True,
                       item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                       weapons=weapons_levelled_mid,
                       helmet=helmets_levelled_mid,
                       bodyarmour=bodyarmour_levelled_mid,
                       spawn_group_amount=1,
                       description="Experienced soldier of the Luciferian Volunteer Army. Better trained and "
                                   "equipped than conscripts."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=120, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

soldier_gov = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_BLUE,
    name='Government Soldier',
    fighter=GunFighter(unarmed_meat_damage=5,
                       unarmed_armour_damage=1,
                       fears_death=True,
                       item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                       weapons={0: {ar15_weapon: 20, ar15_weapon_300: 2, r870_gun: 4, m14_gun: 2, ar_9mm: 1,
                                    ar_40sw: 1},
                                1: {ar15_weapon: 20, ar15_weapon_300: 2, r870_gun: 4, m14_gun: 2, ar_9mm: 1,
                                                                    ar_40sw: 1},
                                2: {ar15_weapon: 20, ar15_weapon_300: 2, r870_gun: 4, m14_gun: 2, ar_9mm: 1,
                                                                    ar_40sw: 1},
                                3: {ar15_weapon: 20, ar15_weapon_300: 2, r870_gun: 4, m14_gun: 2, ar_9mm: 1,
                                                                    ar_40sw: 1},
                                4: {ar15_weapon: 20, ar15_weapon_300: 2, r870_gun: 4, m14_gun: 2, ar_9mm: 1,
                                                                    ar_40sw: 1},
                                5: {ar15_weapon: 20, ar15_weapon_300: 2, r870_gun: 4, m14_gun: 2, ar_9mm: 1,
                                    ar_40sw: 1},
                                },
                       helmet={0: {None: 1, helmet_ech: 1}, 1: {None: 1, helmet_ech: 1}, 2: {None: 1, helmet_ech: 1},
                               3: {None: 1, helmet_ech: 1}, 4: {None: 1, helmet_ech: 1}, 5: {None: 1, helmet_ech: 1}},
                       bodyarmour={0: {None: 1, bodyarmour_interceptor: 1}, 1: {None: 1, bodyarmour_interceptor: 1},
                                   2: {None: 1, bodyarmour_interceptor: 1}, 3: {None: 1, bodyarmour_interceptor: 1},
                                   4: {None: 1, bodyarmour_interceptor: 1}, 5: {None: 1, bodyarmour_interceptor: 1}},
                       spawn_group_amount=1,
                       description="A professional soldier of the Government's forces."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=120, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

officer = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.GREEN,
    name='LVA Officer',
    fighter=GunFighter(unarmed_meat_damage=9,
                       unarmed_armour_damage=1,
                       fears_death=False,
                       item_drops={None: 100, medkit: 5, bandages: 10, repair_kit: 5},
                       weapons=weapons_levelled_high,
                       helmet=helmets_levelled_high,
                       bodyarmour=bodyarmour_levelled_high,
                       spawn_group_amount=1,
                       ranged_accuracy=8.0,
                       felt_recoil=0.8,
                       firing_ap_cost=0.9,
                       ap_distance_cost_modifier=1.2,
                       description="Veteran soldiers of the Luciferian Volunteer Army. Well trained, equipped and "
                                   "highly ideologically motivated. These soldiers will not retreat, even when facing "
                                   "imminent death."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=120, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)

maniac = Actor(
    x=0, y=0,
    char='☺',
    fg_colour=colour.LIGHT_RED,
    name='Maniac',
    fighter=MeleeFighter(unarmed_meat_damage=5,
                       unarmed_armour_damage=1,
                       fears_death=False,
                       item_drops={},
                       weapons={0: {knife: 2, hammer: 1}, 1: {knife: 2, hammer: 1}, 2: {knife: 2, hammer: 1},
                                3: {knife: 2, hammer: 1}, 4: {knife: 2, hammer: 1}, 5: {knife: 2, hammer: 1}},
                       helmet={},
                       bodyarmour={},
                       spawn_group_amount=2,
                       description="Under the pressure of the oppressive darkness and savagery of the depths, many "
                                   "individuals fleeing the tyrannical surface government have fallen to violent "
                                   "insanity. Often carrying knives, they are deadly to the inexperienced adventurer."
                       ),
    ai=DeadAI,
    bodyparts=(Body(hp=120, protection_ballistic=0, protection_physical=1, depth=20, width=36, height=56,
                    connected_to={'head': (0, 41), 'right arm': (23, -11), 'left arm': (-23, -11),
                                  'right leg': (3, -78), 'left leg': (-3, -78)}, aim_location_offset=14),
               Head(hp=40, protection_ballistic=0, protection_physical=0, depth=20, width=20, height=26,
                    connected_to={'body': (0, -41)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='right arm', depth=10, width=10, height=78, connected_to={'body': (-23, 11)}),
               Arm(hp=60, protection_ballistic=0, protection_physical=1,
                   name='left arm', depth=10, width=10, height=78, connected_to={'left arm': (23, 11)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='right leg', depth=12, width=15, height=100, connected_to={'right leg': (-3, 78)}),
               Leg(hp=80, protection_ballistic=0, protection_physical=1,
                   name='left leg', depth=12, width=15, height=100, connected_to={'left leg': (3, 78)})
               ),
    inventory=Inventory(),
)
