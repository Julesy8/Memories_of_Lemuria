from components.npc_templates import Fighter, Humanoid
from components.ai import Melee
import tcod as libtcod
# going to want to import from ai also at some point

x = 1
y = 1


def placeholder_fighter():
    return Fighter(1, 100, 100, 100, 100, True, True)


placeholder_common = Humanoid(5, 10, 5, 0, 0, 0, 0,
                              x, y, 'N',
                              libtcod.white,
                              libtcod.BKGND_NONE,
                              'Placeholder',
                              fighter=placeholder_fighter(),
                              ai=Melee(5))


placeholder_uncommon = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                x, y, 'N',
                                libtcod.green,
                                libtcod.BKGND_NONE,
                                'Placeholder',
                                fighter=placeholder_fighter(),
                                ai=Melee(5))

placeholder_rare = Humanoid(5, 10, 5, 0, 0, 0, 0,
                            x, y, 'N',
                            libtcod.blue,
                            libtcod.BKGND_NONE,
                            'Placeholder',
                            fighter=placeholder_fighter(),
                            ai=Melee(5))

placeholder_v_rare = Humanoid(5, 10, 5, 0, 0, 0, 0,
                              x, y, 'N',
                              libtcod.purple,
                              libtcod.BKGND_NONE,
                              'Placeholder',
                              fighter=placeholder_fighter(),
                              ai=Melee(5))


placeholder_legendary = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                 x, y, 'N',
                                 libtcod.orange,
                                 libtcod.BKGND_NONE,
                                 'Placeholder',
                                 fighter=placeholder_fighter(),
                                 ai=Melee(5))

placeholder_common_alt = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                  x, y, 'N',
                                  libtcod.cyan,
                                  libtcod.BKGND_NONE,
                                  'Placeholder',
                                  fighter=placeholder_fighter(),
                                  ai=Melee(5))

placeholder_uncommon_alt = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                    x, y, 'N',
                                    libtcod.red,
                                    libtcod.BKGND_NONE,
                                    'Placeholder',
                                    fighter=placeholder_fighter(),
                                    ai=Melee(5))

placeholder_rare_alt = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                x, y, 'N',
                                libtcod.pink,
                                libtcod.BKGND_NONE,
                                'Placeholder',
                                fighter=placeholder_fighter(),
                                ai=Melee(5))

placeholder_v_rare_alt = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                  x, y, 'N',
                                  libtcod.violet,
                                  libtcod.BKGND_NONE,
                                  'Placeholder',
                                  fighter=placeholder_fighter(),
                                  ai=Melee(5))

placeholder_legendary_alt = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                     x, y, 'N',
                                     libtcod.yellow,
                                     libtcod.BKGND_NONE,
                                     'Placeholder',
                                     fighter=placeholder_fighter(),
                                     ai=Melee(5))
