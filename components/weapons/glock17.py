from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import GunParts
import colour

glock_17 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17",
    weight=1,
    stacking=None,
    usable_properties=GunMagFed(
        compatible_magazine_type='glock9mm',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'automatic': 1200},
        current_fire_mode='single shot',
        base_meat_damage=10,
        base_armour_damage=10,
        base_accuracy=1.0,
        range_accuracy_dropoff=40,
        parts=GunParts(),
        enemy_attack_range=5
    )
)

glock17_frame = Item(
    x=0, y=0,
    char="f",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Frame",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='glock17_frame')
)

glock17_slide = Item(
    x=0, y=0,
    char="s",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Slide",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='glock17_slide')
)

glock17_barrel = Item(
    x=0, y=0,
    char="b",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Barrel",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='glock17_barrel')
)

glock_stock = Item(
    x=0, y=0,
    char="b",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='glock_stock')
)