from __future__ import annotations

from typing import List, TYPE_CHECKING, Union
from copy import deepcopy
from colour import RED

from components.npc_templates import BaseComponent

if TYPE_CHECKING:
    from components.consumables import DetachableMagazine, Clip
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: float):
        self.capacity = capacity
        self.items: List[Item] = []
        self.held = None

        self.primary_weapon = None
        self.secondary_weapon = None

        self.small_mag_capacity = 3
        self.medium_mag_capacity = 3
        self.large_mag_capacity = 3

        self.small_magazines = []
        self.medium_magazines = []
        self.large_magazines = []

    def add_to_inventory(self, item: Item, item_container, amount: int):

        item_copy = deepcopy(item)
        stack_amount = 1

        if self.current_item_weight() + item.weight * stack_amount > self.capacity:
            self.engine.message_log.add_message("Inventory full.", RED)

        else:
            item_copy.parent = self

            if item.stacking:

                if 0 < amount <= item.stacking.stack_size:
                    stack_amount = amount
                else:
                    stack_amount = item.stacking.stack_size

                item_copy.stacking.stack_size = stack_amount

                # if item of this type already in inventory, tries to add it to existing stack
                repeat_found = False
                for i in self.items:
                    if i.name == item.name:
                        repeat_item_index = self.items.index(i)
                        self.items[repeat_item_index].stacking.stack_size += item_copy.stacking.stack_size
                        repeat_found = True
                if repeat_found:
                    item.stacking.stack_size -= item_copy.stacking.stack_size
                else:
                    # item of this type not already present in inventory
                    self.items.append(item_copy)

            else:
                self.items.append(item_copy)
                if item_container is not None:
                    item_container.remove(item)

    def current_item_weight(self) -> float:
        #  returns current combined weight of items in inventory
        current_weight = 0
        for item in self.items:
            if item.stacking:
                current_weight += item.weight * item.stacking.stack_size
            else:
                current_weight += item.weight

        # adds held item weight
        # if self.held is not None:
        #     current_weight += self.held.weight

        # adds equipment weight
        equipment_list = []
        for part in self.parent.bodyparts:
            if part.equipped is not None:
                if part.equipped not in equipment_list:
                    equipment_list.append(part.equipped)

        for equipment in equipment_list:
            current_weight += equipment.weight

        return current_weight

    def add_to_magazines(self, magazine: Union[Clip, DetachableMagazine]):

        if magazine.magazine_size == 'small':
            if magazine not in self.small_magazines:
                if len(self.small_magazines) < self.small_mag_capacity:
                    self.small_magazines.append(magazine.parent)

        elif magazine.magazine_size == 'medium':
            if magazine not in self.medium_magazines:
                if len(self.medium_magazines) < self.medium_mag_capacity:
                    self.medium_magazines.append(magazine.parent)

        elif magazine.magazine_size == 'large':
            if magazine not in self.large_magazines:
                if len(self.large_magazines) < self.large_mag_capacity:
                    self.large_magazines.append(magazine.parent)

    def remove_from_magazines(self, magazine: Union[Clip, DetachableMagazine]):

        if magazine in self.small_magazines:
            self.small_magazines.remove(magazine.parent)

        elif magazine in self.medium_magazines:
            self.medium_magazines.remove(magazine.parent)

        elif magazine in self.large_magazines:
            self.large_magazines.remove(magazine.parent)

    def update_magazines(self):

        if len(self.small_magazines) > self.small_mag_capacity:
            while len(self.small_magazines) > self.small_mag_capacity:
                self.small_magazines.pop()

        if len(self.medium_magazines) > self.medium_mag_capacity:
            while len(self.medium_magazines) > self.medium_mag_capacity:
                self.medium_magazines.pop()

        if len(self.large_magazines) > self.large_mag_capacity:
            while len(self.large_magazines) > self.large_mag_capacity:
                self.large_magazines.pop()
