from entity import Item, Stacking
from components import consumables
import colour

steel = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.WHITE,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Steel",
    weight=1,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='steel', incompatible_parts=[])
)

polymer = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Polymer",
    weight=1,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='polymer', incompatible_parts=[])
)

aluminium = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.WHITE,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Aluminum",
    weight=1,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='aluminium', incompatible_parts=[])
)
