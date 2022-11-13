from entity import Item, Stacking
from components import consumables
import colour

pda = Item(
    x=0, y=0,
    char="{",
    fg_colour=colour.JADE,
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
    name="Medkit",
    weight=1,
    stacking=Stacking(stack_size=1),
    description='Heals you',
    usable_properties=consumables.HealingConsumable(amount=20),
)
