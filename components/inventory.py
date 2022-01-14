from __future__ import annotations

from typing import List, TYPE_CHECKING

from components.npc_templates import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: float):
        self.capacity = capacity
        self.items: List[Item] = []
        self.held = None

    def current_item_weight(self) -> float:
        #  returns current combined weight of items in inventory
        current_weight = 0
        for item in self.items:
            if item.stacking:
                current_weight += item.weight * item.stacking.stack_size
            else:
                current_weight += item.weight

        # adds held item weight
        if self.held is not None:
            current_weight += self.held.weight

        # adds equipment weight
        equipment_list = []
        for part in self.parent.bodyparts:
            if part.equipped is not None:
                if part.equipped not in equipment_list:
                    equipment_list.append(part.equipped)

        for equipment in equipment_list:
            current_weight += equipment.weight

        return current_weight
