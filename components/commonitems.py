from entity import Item, Stacking
from components import consumables
import colour

pda = Item(
    x=0, y=0,
    char="{",
    fg_colour=colour.JADE,
    bg_colour=None,
    stacking=None,
    name="PDA",
    weight=1,
    description='contains data',
    usable_properties=consumables.Usable(),
)

medkit = Item(
    x=0, y=0,
    char="+",
    fg_colour=colour.GREEN,
    bg_colour=None,
    name="Medkit",
    weight=1,
    stacking=Stacking(stack_size=1),
    description='heals you',
    usable_properties=consumables.HealingConsumable(amount=20),
)

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