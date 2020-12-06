from components.npc_templates import Fighter, Humanoid
from components.ai import Melee

x = 1
y = 1

def placeholder_fighter():
    return Fighter(1, 100, 100, 100, 100, True, True)


placeholder_common = Humanoid(5, 10, 5, 0, 0, 0, 0,
                              x, y, 'N',
                              [255,255,255],
                              None,
                              'Placeholder',
                              fighter=placeholder_fighter(),
                              ai=Melee(5))


placeholder_uncommon = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                x, y, 'N',
                                [0,255,0],
                                None,
                                'Placeholder',
                                fighter=placeholder_fighter(),
                                ai=Melee(5))

placeholder_rare = Humanoid(5, 10, 5, 0, 0, 0, 0,
                            x, y, 'N',
                            [0,0,255],
                            None,
                            'Placeholder',
                            fighter=placeholder_fighter(),
                            ai=Melee(5))

placeholder_v_rare = Humanoid(5, 10, 5, 0, 0, 0, 0,
                              x, y, 'N',
                              [255,0,255],
                              None,
                              'Placeholder',
                              fighter=placeholder_fighter(),
                              ai=Melee(5))


placeholder_legendary = Humanoid(5, 10, 5, 0, 0, 0, 0,
                                 x, y, 'N',
                                 [255,128,0],
                                 None,
                                 'Placeholder',
                                 fighter=placeholder_fighter(),
                                 ai=Melee(5))
