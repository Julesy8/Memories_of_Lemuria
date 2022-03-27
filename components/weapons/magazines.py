import colour
from entity import Item
from components.consumables import Magazine

glock_mag_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Magazine 9mm - Standard Capacity",
    weight=0.2,
    stacking=None,
    description='9mm Glock magazine - 17 round capacity',
    usable_properties=Magazine(
        magazine_type='glock9mm',
        compatible_bullet_type='9mm',
        mag_capacity=17,
        turns_to_load=1,
        magazine_size='small',
    )
)

glock_mag_9mm_33 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Magazine 9mm - Extended",
    weight=0.2,
    stacking=None,
    description='extended 9mm Glock magazine - 33 round capacity',
    usable_properties=Magazine(
        magazine_type='glock9mm',
        compatible_bullet_type='9mm',
        mag_capacity=33,
        turns_to_load=1,
        magazine_size='medium',
        base_accuracy=0.96,
    )
)

glock_mag_9mm_50 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Drum 9mm - 50 Rounds",
    weight=0.7,
    stacking=None,
    description='9mm Glock drum - 50 round capacity',
    usable_properties=Magazine(
        magazine_type='glock9mm',
        compatible_bullet_type='9mm',
        mag_capacity=50,
        turns_to_load=2,
        magazine_size='large',
        base_accuracy=0.90,
    )
)

glock_mag_9mm_100 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Beta Mag 9mm - 100 Rounds",
    weight=1,
    stacking=None,
    description='9mm Glock Beta Mag - 100 round capacity',
    usable_properties=Magazine(
        magazine_type='glock9mm',
        compatible_bullet_type='9mm',
        mag_capacity=100,
        turns_to_load=3,
        magazine_size='large',
        base_accuracy=0.85,
    )
)

magazine_dict = {
    "glock9mm": ([glock_mag_9mm, 2], [glock_mag_9mm_33, 1])
}

magazine_crafting_dict = {
    "Glock Magazine 9mm - 17 Round": {
        "required parts": {
            "polymer": 1,
            "steel": 1,
            },
        "compatible parts": {},
        "parts names": ["Material", "Material"],
        "item": glock_mag_9mm
    },
    "Glock Magazine 9mm - 33 Round": {
        "required parts": {
            "polymer": 2,
            "steel": 1,
        },
        "compatible parts": {},
        "parts names": ["Material", "Material"],
        "item": glock_mag_9mm_33
    },
    "Glock Drum 9mm - 50 Rounds": {
        "required parts": {
            "polymer": 3,
            "steel": 2,
        },
        "compatible parts": {},
        "parts names": ["Material", "Material"],
        "item": glock_mag_9mm_50
    },
    "Glock Beta Mag 9mm - 100 Rounds": {
        "required parts": {
            "polymer": 3,
            "steel": 3,
        },
        "compatible parts": {},
        "parts names": ["Material", "Material"],
        "item": glock_mag_9mm_100
    },
}
