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

        self.small_mag_capacity = 3
        self.medium_mag_capacity = 3
        self.large_mag_capacity = 3

        self.small_magazines = []
        self.medium_magazines = []
        self.large_magazines = []

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

    def add_to_magazines(self, magazine: Item):

        if magazine.usable_properties.magazine_size == 'small':
            if magazine not in self.small_magazines:
                if len(self.small_magazines) < self.small_mag_capacity:
                    self.small_magazines.append(magazine)

        elif magazine.usable_properties.magazine_size == 'medium':
            if magazine not in self.medium_magazines:
                if len(self.medium_magazines) < self.medium_mag_capacity:
                    self.medium_magazines.append(magazine)

        elif magazine.usable_properties.magazine_size == 'large':
            if magazine not in self.large_magazines:
                if len(self.large_magazines) < self.large_mag_capacity:
                    self.large_magazines.append(magazine)

    def remove_from_magazines(self, magazine: Item):

        if magazine in self.small_magazines:
            self.small_magazines.remove(magazine)

        elif magazine in self.medium_magazines:
            self.medium_magazines.remove(magazine)

        elif magazine in self.large_magazines:
            self.large_magazines.remove(magazine)

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