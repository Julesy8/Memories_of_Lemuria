from components.consumables import MeleeWeapon
from entity import Item
import colour

# todo - add more melee weapons
knife = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Kitchen Knife",
    weight=0.22,
    stacking=None,
    description='An old kitchen knife. The edge is dull, but the point is still sharp enough to inflict serious '
                'damage.',
    usable_properties=MeleeWeapon(
        base_meat_damage=20,
        base_armour_damage=5,
        base_accuracy=1.0,
        ap_to_equip=100,
        base_ap_cost=100,
    )
)
