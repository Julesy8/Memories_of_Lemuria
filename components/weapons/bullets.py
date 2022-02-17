import colour
from entity import Item, Stacking
from components.consumables import Bullet, ComponentPart
from components.gunparts import BulletParts

round_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Bullet',
    weight=1,
    stacking=Stacking(stack_size=1),
    description='9mm bullet',
    usable_properties=Bullet(
        parts=BulletParts(),
        bullet_type='9mm',
        meat_damage_factor=1.0,
        armour_damage_factor=1.0,
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
    weight=1,
    stacking=Stacking(stack_size=1),
    description='9mm bullet casing',
    usable_properties=ComponentPart(part_type="brass_9mm")
)

bullet_9mm = Item(
    x=0, y=0,
    char=".",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    name='9mm Bullet',
    weight=1,
    stacking=Stacking(stack_size=1),
    description='9mm bullet',
    usable_properties=ComponentPart(part_type="bullet_9mm")
)

bullet_dict = {
    "9mm": {
        "bullet_items": [round_9mm],
        "bullet_weight": [1]
    }
}

bullet_crafting_dict = {
    "9mm Bullet": {
        "required parts": ["brass_9mm", "bullet_9mm", "powder_charge"],
        "compatible parts": [],
        "parts names": ["Casing", "Bullet", "Propellant"],
        "item": bullet_9mm
    },
}