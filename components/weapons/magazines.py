import colour
from entity import Item
from components.consumables import Magazine


glock_mag_9mm = Item(
    x=0, y=0,
    char="m",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Magazine 9mm",
    weight=1,
    stacking=None,
    usable_properties=Magazine(
        magazine_type='glock9mm',
        compatible_bullet_type='9mm',
        mag_capacity=17,
        turns_to_load=1,
        magazine_size='small',
    )
)

magazine_dict = {
    "glock9mm": {
        "mag_items": [glock_mag_9mm],
        "mag_weight": [1]
    }
}