from components.consumable import HealingConsumable
from entity import Item
import colour

medkit = Item(
    char="+",
    fg_colour=colour.GREEN,
    bg_colour=None,
    name="MedKit",
    consumable=HealingConsumable(amount=4),
)
