from __future__ import annotations

from typing import List, TYPE_CHECKING

from exceptions import Impossible
from components.npc_templates import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: List[Item] = []
        self.held: List[Item] = []

    def drop(self, item: Item) -> None:
        """
        Removes an item from the inventory and restores it to the game map, at the player's current location.
        """
        self.items.remove(item)
        item.place(self.parent.x, self.parent.y, self.gamemap)

        self.engine.message_log.add_message(f"You dropped the {item.name}.")

    def equip_weapon(self, item):
        self.items.remove(item)

        if len(self.held) > 0:
            raise Impossible(f"you are already holding an item")
        else:
            self.held.append(item)
            self.engine.message_log.add_message(f"You are holding the {item.name}.")

    def unequip_weapon(self, item):
        self.held.remove(item)

        if len(self.items) + 1 > self.capacity:
            raise Impossible(f"your inventory is full")

        else:
            self.items.append(item)
            self.engine.message_log.add_message(f"You moved your held item to your inventory ")
