from components.consumables import MeleeWeapon
from entity import Item
import colour

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

axe = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Hatchet",
    weight=0.45,
    stacking=None,
    description='A rusty old hatchet.',
    usable_properties=MeleeWeapon(
        base_meat_damage=35,
        base_armour_damage=7,
        base_accuracy=0.9,
        ap_to_equip=150,
        base_ap_cost=200,
    )
)

hammer = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Claw Hammer",
    weight=0.51,
    stacking=None,
    description='A claw hammer.',
    usable_properties=MeleeWeapon(
        base_meat_damage=40,
        base_armour_damage=2,
        base_accuracy=0.8,
        ap_to_equip=130,
        base_ap_cost=220,
    )
)

ice_pick = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Ice Pick",
    weight=0.31,
    stacking=None,
    description='An ice pick. Its a mystery how this object came to be in the depths originally.',
    usable_properties=MeleeWeapon(
        base_meat_damage=25,
        base_armour_damage=4,
        base_accuracy=0.95,
        ap_to_equip=110,
        base_ap_cost=180,
    )
)

