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
    weight=0.5,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='steel', incompatible_parts=[], disassemblable=False)
)

polymer = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Polymer",
    weight=0.3,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='polymer', incompatible_parts=[], disassemblable=False)
)

aluminium = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.WHITE,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Aluminum",
    weight=0.5,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='aluminium', incompatible_parts=[], disassemblable=False)
)

brass = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Brass",
    weight=0.001,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='brass', incompatible_parts=[], disassemblable=False)
)

lead = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.DARK_GRAY,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Lead",
    weight=0.001,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='lead', incompatible_parts=[], disassemblable=False)
)