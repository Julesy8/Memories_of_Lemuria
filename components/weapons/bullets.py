import colour
from entity import Item, Stacking
from components.consumables import Bullet, ComponentPart
from components.gunparts import Parts
from components.commonitems import brass, lead

propellant = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='Smokeless Powder',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='Smokeless Powder',
    usable_properties=ComponentPart(part_type="propellant", disassemblable=False)
)

"""
9MM
"""

round_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Round',
    weight=0.0,
    stacking=Stacking(stack_size=10),
    description='A standard pressure 9mm round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='9mm',
        meat_damage=20,
        armour_damage=14,
        accuracy_factor=1.0,
        recoil_modifier=3,
        sound_modifier=8,
    )
)

round_9mm_plusp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Round +P',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='Overpressure 9mm round designed to deliver additional velocity',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='9mm',
        meat_damage=24,
        armour_damage=15,
        accuracy_factor=1.0,
        recoil_modifier=3.3,
        sound_modifier=9,
    )
)

round_9mm_subsonic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Round Subsonic',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='Subsonic 9mm ammunition designed to provide better suppressed functionality',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='9mm',
        meat_damage=18,
        armour_damage=13,
        accuracy_factor=1.0,
        recoil_modifier=2.7,
        sound_modifier=6,
    )
)

brass_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='9mm Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='9mm bullet casing',
    usable_properties=ComponentPart(part_type="brass_9mm", material={brass: 1})
)

bullet_9mm_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='9mm FMJ',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='9mm full metal jacket bullet',
    usable_properties=ComponentPart(part_type="bullet_9mm", suffix='FMJ', material={lead: 1})
)

bullet_9mm_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='9mm JHP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='9mm jacketed hollow point bullet',
    usable_properties=ComponentPart(part_type="bullet_9mm", suffix='JHP', material={lead: 1},
                                    meat_damage=1.2,
                                    armour_damage=0.8,
                                    )
)

bullet_9mm_ap = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='9mm AP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='9mm armour piercing bullet',
    usable_properties=ComponentPart(part_type="bullet_9mm", suffix='AP', material={lead: 1},
                                    meat_damage=0.9,
                                    armour_damage=1.3,
                                    )
)

"""
45
"""

round_45 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='45 ACP Round',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='A standard pressure 45 ACP round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='45',
        meat_damage=22,
        armour_damage=13,
        accuracy_factor=1.0,
        recoil_modifier=4,
        sound_modifier=9,
    )
)

round_45_plusp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='45 ACP Round +P',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='Overpressure 45 ACP round designed to deliver additional velocity',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='45',
        meat_damage=26,
        armour_damage=14,
        accuracy_factor=1.0,
        recoil_modifier=4.4,
        sound_modifier=9.9,
    )
)

round_45_subsonic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='45 ACP Round Subsonic',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='Subsonic 45 ACP ammunition designed to provide better suppressed functionality',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='45',
        meat_damage=20,
        armour_damage=11,
        accuracy_factor=1.0,
        recoil_modifier=3.4,
        sound_modifier=7,
    )
)

brass_45 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='45 ACP Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='45 ACP bullet casing',
    usable_properties=ComponentPart(part_type="brass_45", material={brass: 1})
)

bullet_45_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='45 ACP FMJ',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='45 ACP full metal jacket bullet',
    usable_properties=ComponentPart(part_type="bullet_45", suffix='FMJ', material={lead: 1})
)

bullet_45_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='45 ACP JHP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='45 ACP jacketed hollow point bullet',
    usable_properties=ComponentPart(part_type="bullet_45", suffix='JHP', material={lead: 1},
                                    meat_damage=1.2,
                                    armour_damage=0.8,
                                    )
)

bullet_45_ap = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='45 ACP AP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='45 ACP armour piercing bullet',
    usable_properties=ComponentPart(part_type="bullet_45", suffix='AP', material={lead: 1},
                                    meat_damage=0.9,
                                    armour_damage=1.3,
                                    )
)


"""
7.62 x 39
"""

round_762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='7.62x39 Round',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='A 7.62x39 round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='762',
        meat_damage=30,
        armour_damage=25,
        accuracy_factor=1.0,
        recoil_modifier=6,
        sound_modifier=15,
    )
)

brass_762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x39 Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x39 bullet casing',
    usable_properties=ComponentPart(part_type="brass_762", material={brass: 1})
)

bullet_762_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x39 FMJ',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x39 full metal jacket bullet',
    usable_properties=ComponentPart(part_type="bullet_762", suffix='FMJ', material={lead: 1})
)

bullet_762_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x39 JHP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x39 jacketed hollow point bullet',
    usable_properties=ComponentPart(part_type="bullet_762", suffix='JHP', material={lead: 1},
                                    meat_damage=1.2,
                                    armour_damage=0.8,
                                    )
)

bullet_762_ap = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x39 AP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x39 armour piercing bullet',
    usable_properties=ComponentPart(part_type="bullet_762", suffix='AP', material={lead: 1},
                                    meat_damage=0.9,
                                    armour_damage=1.3,
                                    )
)


"""
5.56 
"""

round_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='5.56x45 Round',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='A 5.56x45 round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='556',
        meat_damage=25,
        armour_damage=20,
        accuracy_factor=1.0,
        recoil_modifier=5,
        sound_modifier=13,
    )
)

brass_556 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.56x45 Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.56x45 bullet casing',
    usable_properties=ComponentPart(part_type="brass_556", material={brass: 1})
)

bullet_556_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.56x45 FMJ',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.56x45 full metal jacket bullet',
    usable_properties=ComponentPart(part_type="bullet_556", suffix='FMJ', material={lead: 1})
)

bullet_556_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.56x45 JHP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.56x45 jacketed hollow point bullet',
    usable_properties=ComponentPart(part_type="bullet_556", suffix='JHP', material={lead: 1},
                                    meat_damage=1.2,
                                    armour_damage=0.8,
                                    )
)

bullet_556_ap = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.56x45 AP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.56x45 armour piercing bullet',
    usable_properties=ComponentPart(part_type="bullet_556", suffix='AP', material={lead: 1},
                                    meat_damage=0.9,
                                    armour_damage=1.3,
                                    )
)

"""
300 blackout
"""

round_300blk = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='.300 BLK Round',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='A .300 BLK round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='300blk',
        meat_damage=28,
        armour_damage=17,
        accuracy_factor=1.0,
        recoil_modifier=5.5,
        sound_modifier=14,
    )
)

brass_300blk = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='.300 BLK Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='.300 BLK bullet casing',
    usable_properties=ComponentPart(part_type="brass_300blk", material={brass: 1})
)

bullet_300blk_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='.300 BLK FMJ',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='.300 BLK full metal jacket bullet',
    usable_properties=ComponentPart(part_type="bullet_300blk", suffix='FMJ', material={lead: 1})
)

bullet_300blk_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='.300 BLK JHP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='.300 BLK jacketed hollow point bullet',
    usable_properties=ComponentPart(part_type="bullet_300blk", suffix='JHP', material={lead: 1},
                                    meat_damage=1.2,
                                    armour_damage=0.8,
                                    )
)

bullet_300blk_ap = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='.300 BLK AP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='.300 BLK armour piercing bullet',
    usable_properties=ComponentPart(part_type="bullet_300blk", suffix='AP', material={lead: 1},
                                    meat_damage=0.9,
                                    armour_damage=1.3,
                                    )
)


"""
5.45
"""

round_545 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='5.45x39 Round',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='A 5.45x39 round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='545',
        meat_damage=24,
        armour_damage=23,
        accuracy_factor=1.0,
        recoil_modifier=4.7,
        sound_modifier=14,
    )
)

brass_545 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.45x39 Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.45x39 bullet casing',
    usable_properties=ComponentPart(part_type="brass_545", material={brass: 1})
)

bullet_545_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.45x39 FMJ',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.45x39 full metal jacket bullet',
    usable_properties=ComponentPart(part_type="bullet_545", suffix='FMJ', material={lead: 1})
)

bullet_545_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.45x39 JHP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.45x39 jacketed hollow point bullet',
    usable_properties=ComponentPart(part_type="bullet_545", suffix='JHP', material={lead: 1},
                                    meat_damage=1.2,
                                    armour_damage=0.8,
                                    )
)

bullet_545_ap = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='5.45x39 AP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='5.45x39 armour piercing bullet',
    usable_properties=ComponentPart(part_type="bullet_545", suffix='AP', material={lead: 1},
                                    meat_damage=0.9,
                                    armour_damage=1.3,
                                    )
)

"""
7.62x51 
"""

round_308 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='7.62x51 Round',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='A 7.62x51 round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='308',
        meat_damage=35,
        armour_damage=20,
        accuracy_factor=1.0,
        recoil_modifier=8,
        sound_modifier=18,
    )
)

brass_308 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x51 Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x51 bullet casing',
    usable_properties=ComponentPart(part_type="brass_308", material={brass: 1})
)

bullet_308_fmj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x51 FMJ',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x51 full metal jacket bullet',
    usable_properties=ComponentPart(part_type="bullet_308", suffix='FMJ', material={lead: 1})
)

bullet_308_jhp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x51 JHP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x51 jacketed hollow point bullet',
    usable_properties=ComponentPart(part_type="bullet_308", suffix='JHP', material={lead: 1},
                                    meat_damage=1.2,
                                    armour_damage=0.8,
                                    )
)

bullet_308_ap = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='7.62x51 AP',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='7.62x51 armour piercing bullet',
    usable_properties=ComponentPart(part_type="bullet_308", suffix='AP', material={lead: 1},
                                    meat_damage=0.9,
                                    armour_damage=1.3,
                                    )
)

bullet_dict = {
    "9mm": ([round_9mm, 1], [round_9mm, 1])
}

bullet_crafting_dict = {
    "9mm": {
        "9mm Round": {
            "required parts": {
                "brass_9mm": 1,
                "bullet_9mm": 1,
                "propellant": 2,
                },
            "compatible parts": {},
            "parts names": ["Casing", "Bullet", "Propellant"],
            "item": round_9mm
        },
        "9mm Round +P": {
            "required parts": {
                "brass_9mm": 1,
                "bullet_9mm": 1,
                "propellant": 3,
            },
            "compatible parts": {},
            "parts names": ["Casing", "Bullet", "Propellant"],
            "item": round_9mm_plusp
        },
        "9mm Round Subsonic": {
            "required parts": {
                "brass_9mm": 1,
                "bullet_9mm": 1,
                "propellant": 1,
            },
            "compatible parts": {},
            "parts names": ["Casing", "Bullet", "Propellant"],
            "item": round_9mm_plusp
        },
        "9mm FMJ Bullet": {
            "required parts": {
                "lead": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": bullet_9mm_fmj
        },
        "9mm JHP Bullet": {
            "required parts": {
                "lead": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": bullet_9mm_jhp
        },
        "9mm AP Bullet": {
            "required parts": {
                "lead": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": bullet_9mm_ap
        },
        "9mm Brass": {
            "required parts": {
                "brass": 1,
            },
            "compatible parts": {},
            "parts names": ["Material"],
            "item": brass_9mm
        },
    }
}


