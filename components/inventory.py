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

    def current_item_weight(self) -> int:
        #  returns current combined weight of items in inventory
        current_weight = 0
        for item in self.items:
            current_weight += item.weight
        return current_weight

    def equip_weapon(self, item):
        try:
            if item.usable_properties.usable_type == 'wearable':

                available_slots = []  # list of availbale grasping bodyparts

                for bodypart in self.parent.bodyparts:
                    if bodypart.arm and bodypart.functional and not bodypart.held:
                        available_slots.append(bodypart)

                # TODO: better way of handling held items
                if item.weapon.two_handed and len(available_slots) > 1:
                    part_index_1 = self.parent.bodyparts.index(available_slots[-1])
                    part_index_2 = self.parent.bodyparts.index(available_slots[-2])
                    self.parent.bodyparts[part_index_1].held = item
                    self.parent.bodyparts[part_index_2].held = item

                elif not item.weapon.two_handed and len(available_slots) >= 1:
                    part_index = self.parent.bodyparts.index(available_slots[-1])
                    self.parent.bodyparts[part_index].held = item

                else:
                    raise Impossible(f"You can't equip this item")

                self.items.remove(item)
                self.engine.message_log.add_message(f"You are holding the {item.name}.")

        except TypeError:
            raise Impossible(f"You can't equip this item")

    def unequip_weapon(self, item):

        for bodypart in self.parent.bodyparts:
            if bodypart.held == item:
                bodypart.held = None

        self.items.append(item)
        self.engine.message_log.add_message(f"You moved your held item to your inventory.")

    def equip_armour(self, item):

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
                        self.engine.message_log.add_message(f"You put on the {item.name}.")

    def unequip_armour(self, item):

        for bodypart in self.parent.bodyparts:
            if bodypart.part_type == item.wearable.fits_bodypart:
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
