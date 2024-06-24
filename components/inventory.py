from __future__ import annotations

from typing import List, TYPE_CHECKING, Union
from colour import WHITE

from components.npc_templates import BaseComponent

if TYPE_CHECKING:
    from components.consumables import DetachableMagazine, Clip
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: float = 30.0):
        self.capacity = capacity
        self.items: List[Item] = []
        self.held = None

        self.primary_weapon = None
        self.secondary_weapon = None

        self.small_mag_capacity = 4
        self.medium_mag_capacity = 4
        self.large_mag_capacity = 2

        # self.ammopouch_capacity_shot = 18
        # self.ammopouch_capacity_rifle = 14
        # self.ammopouch_capacity_pistol = 25
        #
        # self.ammo_pouch_shot = []
        # self.ammo_pouch_rifle = []
        # self.ammo_pouch_pistol = []
        self.small_magazines = []
        self.medium_magazines = []
        self.large_magazines = []

    def add_to_inventory(self, item: Item, amount: int):

        if self.current_item_weight() + item.weight * amount > self.capacity:
            self.engine.message_log.add_message("Inventory full.", WHITE)

        else:
            item.parent = self

            if item.stacking:
                repeat_found = False
                # if item of this type already in inventory, tries to add it to existing stack
                for i in self.items:
                    if i.name == item.name:
                        repeat_item_index = self.items.index(i)
                        self.items[repeat_item_index].stacking.stack_size += amount
                        repeat_found = True

                # item of this type not already present in inventory
                if not repeat_found:
                    self.items.append(item)

    def current_item_weight(self) -> float:
        loadout = self.small_magazines + self.medium_magazines + self.large_magazines
        #  returns current combined weight of items in inventory
        current_weight = 0
        for item in self.items + loadout:
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
            current_weight += equipment.parent.weight

        return current_weight

    def add_to_magazines(self, magazine: Union[Clip, DetachableMagazine]):

        self.items.remove(magazine.parent)

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

    # def add_to_pouch(self, bullet: Bullet):
    #     if bullet.round_type == 'pistol':
    #         if bullet not in self.ammo_pouch_pistol:
    #             if len(self.ammo_pouch_pistol) < self.ammopouch_capacity_pistol:
    #                 self.ammo_pouch_pistol.append(bullet.parent)
    #
    #     elif bullet.round_type == 'rifle':
    #         if bullet not in self.ammo_pouch_rifle:
    #             if len(self.ammo_pouch_rifle) < self.ammopouch_capacity_rifle:
    #                 self.ammo_pouch_rifle.append(bullet.parent)
    #
    #     elif bullet.round_type == 'shot shell':
    #         if bullet not in self.ammo_pouch_shot:
    #             if len(self.ammo_pouch_shot) < self.ammopouch_capacity_shot:
    #                 self.ammo_pouch_shot.append(bullet.parent)
    #
    # def remove_from_pouch(self, bullet: Bullet):
    #     if bullet.parent in self.ammo_pouch_pistol:
    #         self.ammo_pouch_pistol.remove(bullet.parent)
    #
    #     elif bullet.parent in self.ammo_pouch_rifle:
    #         self.ammo_pouch_rifle.remove(bullet.parent)
    #
    #     elif bullet.parent in self.ammo_pouch_shot:
    #         self.ammo_pouch_shot.remove(bullet.parent)
    #
    def remove_from_magazines(self, magazine: Union[Clip, DetachableMagazine]):

        if magazine.parent in self.small_magazines:
            self.small_magazines.remove(magazine.parent)

        elif magazine.parent in self.medium_magazines:
            self.medium_magazines.remove(magazine.parent)

        elif magazine.parent in self.large_magazines:
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
