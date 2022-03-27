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

round_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Round',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='A standard pressure 9mm round',
    usable_properties=Bullet(
        parts=Parts(),
        bullet_type='9mm',
        meat_damage=20,
        armour_damage=10,
        accuracy_factor=1.0,
        recoil_modifier=1.0,
        sound_modifier=1.0,
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
        armour_damage=12,
        accuracy_factor=1.0,
        recoil_modifier=1.1,
        sound_modifier=1.1,
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
        armour_damage=8,
        accuracy_factor=1.0,
        recoil_modifier=0.90,
        sound_modifier=0.8,
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

bullet_dict = {
    "9mm": ([round_9mm, 1], [round_9mm, 1])
}

bullet_crafting_dict = {
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
}

bullet_part_crafting_dict = {
    "9mm": {
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
