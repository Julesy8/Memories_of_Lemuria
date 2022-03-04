from entity import Item
from components import consumables
import colour


helmet = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Helmet",
    weight=1,
    stacking=None,
    description='goes on your head',
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Head',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

pauldron = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Pauldrons",
    weight=1,
    stacking=None,
    description='goes on your arms',
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Arms',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

greaves = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Greaves",
    weight=1,
    stacking=None,
    description='goes on your legs',
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Legs',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

chestplate = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Chestplate",
    weight=1,
    stacking=None,
    description='protects your chest',
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Body',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

armour_crafting_dict = {
    "Helmet": {
        "required parts": {
            "steel": 1,
            },
        "compatible parts": {},
        "parts names": ["Material"],
        "item": helmet
    },
}
