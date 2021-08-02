from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING
import tcod
from copy import deepcopy

from exceptions import Impossible
from components.npc_templates import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: int, held: Optional[Item]):
        self.capacity = capacity
        self.items: List[Item] = []
        self.held: Optional[Item] = held

    def current_item_weight(self):
        #  returns current combined weight of items in inventory
        current_weight = 0
        for item in self.items:
            current_weight += item.weight
        return current_weight

    def equip_weapon(self, item):
        if item.weapon:

            if self.held is not None:
                raise Impossible(f"you are already holding an item")

            else:
                self.items.remove(item)
                self.held = item
                self.engine.message_log.add_message(f"You are holding the {item.name}.")

    def unequip_weapon(self, item):
        self.held = None

        if self.current_item_weight() + item.weight > self.capacity:
            raise Impossible(f"Your inventory is full")

        else:
            if item.stacking:
                try:
                    repeat_item_index = self.parent.inventory.items.index(item)
                    self.parent.inventory.items[repeat_item_index].stacking.stack_size += item.stacking.stack_size

                except ValueError:
                    self.items.append(item)

            else:
                self.items.append(item)

            self.engine.message_log.add_message(f"You moved your held item to your inventory ")

    def equip_armour(self, item):

        item_removed = False

        for bodypart in self.parent.bodyparts:
            if bodypart.type == item.wearable.fits_bodypart:

                if bodypart.equipped is not None:
                    raise Impossible(f"You are already wearing something there")

                else:
                    if not item_removed:
                        self.items.remove(item)
                        item_removed = True
                    bodypart.equipped = item
                    self.engine.message_log.add_message(f"You put on the {item.name}.")

    def unequip_armour(self, item):

        for bodypart in self.parent.bodyparts:
            if bodypart.type == item.wearable.fits_bodypart:
                bodypart.equipped = None

        if self.current_item_weight() + item.weight > self.capacity:
            raise Impossible(f"Your inventory is full")

        else:
            if item.stacking:
                try:
                    repeat_item_index = self.parent.inventory.items.index(item)
                    self.parent.inventory.items[repeat_item_index].stacking.stack_size += item.stacking.stack_size

                except ValueError:
                    self.items.append(item)

            else:
                self.items.append(item)

            self.engine.message_log.add_message(f"You took off the {item.name}")
