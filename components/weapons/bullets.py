import colour
from entity import Item, Stacking
from components.consumables import Bullet, ComponentPart
from components.gunparts import Parts
from components.commonitems import brass, lead

propellant = Item(
    x=0, y=0,
    char="'",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='Smokeless Powder',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='Smokeless Powder',
    usable_properties=ComponentPart(part_type="propellant", incompatible_parts=[], disassemblable=False)
)


round_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Bullet',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='9mm bullet',
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

brass_9mm = Item(
    x=0, y=0,
    char="'",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='9mm Casing',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='9mm bullet casing',
    usable_properties=ComponentPart(part_type="brass_9mm", incompatible_parts=[], material={brass: 1})
)

bullet_9mm = Item(
    x=0, y=0,
    char=".",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='9mm Bullet',
    weight=0.0,
    stacking=Stacking(stack_size=1),
    description='9mm bullet',
    usable_properties=ComponentPart(part_type="bullet_9mm", incompatible_parts=[], material={lead: 1})
)

bullet_dict = {
    "9mm": ([round_9mm, 1], [round_9mm, 1])
}

bullet_crafting_dict = {
    "9mm Round": {
        "required parts": {
            "brass_9mm": 1,
            "bullet_9mm": 1,
            "propellant": 1,
            },
        "compatible parts": {},
        "parts names": ["Casing", "Bullet", "Propellant"],
        "item": round_9mm
    },
}

bullet_part_crafting_dict = {
    "9mm Bullet": {
        "required parts": {
            "lead": 1,
            },
        "compatible parts": {},
        "parts names": ["Material"],
        "item": bullet_9mm
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
