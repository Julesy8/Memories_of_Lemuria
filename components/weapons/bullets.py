import colour
from entity import Item, Stacking
from components.consumables import Bullet

bullet_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Bullet',
    weight=1,
    stacking=Stacking(stack_size=1),
    usable_properties=Bullet(
        bullet_type='9mm',
        meat_damage_factor=1.0,
        armour_damage_factor=1.0,
        accuracy_factor=1.0,
        recoil_modifier=4,
    )
)

bullet_dict = {
    "9mm": {
        "bullet_items": [bullet_9mm],
        "bullet_weight": [1]
    }
}