from entity import Item, Stacking
from components import consumables
import colour

# pda = Item(
#     x=0, y=0,
#     char="{",
#     fg_colour=colour.JADE,
#     stacking=None,
#     name="PDA",
#     weight=0.3,
#     description='Contains part schematics for assembling firearms from parts',
#     usable_properties=consumables.Usable(),
# )

medkit = Item(
    x=0, y=0,
    char="+",
    fg_colour=colour.GREEN,
    name="Medkit",
    weight=0.4,
    stacking=Stacking(stack_size=1),
    description='Effective for treating severe injuries.',
    usable_properties=consumables.HealingConsumable(amount=60),
)

bandages = Item(
    x=0, y=0,
    char="+",
    fg_colour=colour.RED,
    name="Bandages",
    weight=0.1,
    stacking=Stacking(stack_size=1),
    description='Effective for treating low-severity injuries.',
    usable_properties=consumables.HealingConsumable(amount=20),
)

repair_kit = Item(
    x=0, y=0,
    char="k",
    fg_colour=colour.GREEN,
    name="Repair Kit",
    weight=1,
    stacking=Stacking(stack_size=1),
    description='Used to repair weapon parts',
    usable_properties=consumables.RepairKit(),
)
