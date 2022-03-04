from entity import Item
from components.consumables import GunMagFed, ComponentPart
from components.gunparts import Parts
import colour
from components.commonitems import steel, polymer

glock17_frame = Item(
    x=0, y=0,
    char="f",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Frame",
    weight=0.2,
    stacking=None,
    usable_properties=ComponentPart(part_type='glock17_frame', incompatible_parts=[], material={polymer: 1}),
    description='glock barrel'
)

glock17_slide = Item(
    x=0, y=0,
    char="s",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Slide",
    weight=0.2,
    stacking=None,
    usable_properties=ComponentPart(part_type='glock17_slide', incompatible_parts=[], material={steel: 1}),
    description='glock slide'
)

glock17_barrel = Item(
    x=0, y=0,
    char="b",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17 Barrel",
    weight=0.2,
    stacking=None,
    usable_properties=ComponentPart(part_type='glock17_barrel', prefix='standard', incompatible_parts=[],
                                    material={steel: 1}),
    description='glock barrel'
)

glock_stock = Item(
    x=0, y=0,
    char="b",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Stock",
    weight=0.4,
    stacking=None,
    usable_properties=ComponentPart(part_type='glock_stock', incompatible_parts=[], material={polymer: 1}),
    description='glock stock'
)

glock_parts_dict = {
    "glock17_frame": ([glock17_frame, 1], [glock17_frame, 1]),
    "glock17_slide": ([glock17_slide, 1], [glock17_slide, 1]),
    "glock17_barrel": ([glock17_barrel, 1], [glock17_barrel, 1]),
    "glock_stock": ([None, 1], [glock_stock, 1]),
}

glock_17 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17",
    weight=0.7,
    stacking=None,
    description='glock 17 handgun',
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
        parts=Parts(),
        enemy_attack_range=5,
        possible_parts=glock_parts_dict,
        sound_radius=10,
        recoil=3,
        close_range_accuracy=1.0,
    )
)