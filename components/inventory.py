from __future__ import annotations

from typing import List, TYPE_CHECKING

from exceptions import Impossible
from components.npc_templates import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: float):
        self.capacity = capacity
        self.items: List[Item] = []
        self.held = None

    # TODO: take into account worn and equipped item weight + loaded magazines etc
    def current_item_weight(self) -> float:
        #  returns current combined weight of items in inventory
        current_weight = 0
        for item in self.items:
            if item.stacking:
                current_weight += item.weight * item.stacking.stack_size
            else:
                current_weight += item.weight
        return current_weight

    def equip_weapon(self, item):

        self.items.remove(item)
        self.held = item

    def unequip_weapon(self):

        self.items.append(self.parent.inventory.held)
        self.parent.inventory.held = None

    def equip_armour(self, item):  # TODO: frankly tf even is this

        item_removed = False

        for bodypart in self.parent.bodyparts:
            if item.usable_properties.usable_type == 'wearable':
                if bodypart.part_type == item.usable_properties.fits_bodypart:

                    if bodypart.equipped is not None:
                        raise Impossible(f"You are already wearing something there.")

                    else:
                        if not item_removed:
                            self.items.remove(item)
                            item_removed = True
                        bodypart.equipped = item

    def unequip_armour(self, item):

        for bodypart in self.parent.bodyparts:
            if bodypart.part_type == item.usable_properties.fits_bodypart:
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

    def load_magazine_into_gun(self, gun, magazine):
        if gun.loaded_magazine is not None:
            self.parent.inventory.items.append(gun.loaded_magazine)
            gun.parent.loaded_magazine = magazine

        else:
            gun.loaded_magazine = magazine

        self.items.remove(magazine)

    def unload_magazine_from_gun(self, gun):
        if gun.loaded_magazine is not None:
            self.parent.inventory.items.append(gun.loaded_magazine)
            gun.loaded_magazine = None
        else:
            raise Impossible(f"{gun.name} has no magazine loaded")

    def unload_bullets_from_magazine(self, magazine: Item):
        bullets_unloaded = []

        if len(magazine.usable_properties.magazine) > 0:
            for bullet in magazine.usable_properties.magazine:
                if bullet in bullets_unloaded:
                    pass
                else:
                    bullets_unloaded.append(bullet)
                    bullet_counter = 0
                    for i in magazine.usable_properties.magazine:
                        if i.name == bullet.name:
                            bullet_counter += 1
                    bullet.stacking.stack_size = bullet_counter

                    # if bullet of same type already in inventory, adds unloaded bullets to stack
                    bullet_type_in_inventory = False

                    for item in self.items:
                        if item.name == bullet.name:
                            item.stacking.stack_size += bullet.stacking.stack_size
                            bullet_type_in_inventory = True

                    # if no bullets of same type in inventory, adds to inventory
                    if not bullet_type_in_inventory:
                        self.parent.inventory.items.append(bullet)

            magazine.usable_properties.magazine = []

        else:
            raise Impossible(f"{magazine.name} is already empty")
