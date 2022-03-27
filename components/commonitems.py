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
    description='Contains data including weapon and parts schematics',
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
    description='Heals you',
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
    usable_properties=consumables.ComponentPart(part_type='steel', disassemblable=False)
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
    usable_properties=consumables.ComponentPart(part_type='polymer', disassemblable=False)
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
    usable_properties=consumables.ComponentPart(part_type='aluminium', disassemblable=False)
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
    usable_properties=consumables.ComponentPart(part_type='brass', disassemblable=False)
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
    usable_properties=consumables.ComponentPart(part_type='lead', disassemblable=False)
)

glass = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.WHITE,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Glass",
    weight=0.1,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='glass', disassemblable=False)
)

battery = Item(
    x=0, y=0,
    char="*",
    fg_colour=colour.YELLOW,
    bg_colour=None,
    stacking=Stacking(stack_size=1),
    name="Battery",
    weight=0.1,
    description='Raw crafting material',
    usable_properties=consumables.ComponentPart(part_type='battery', disassemblable=False)
)