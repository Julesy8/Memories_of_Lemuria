from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
import colour
import components.inventory
from components.npc_templates import BaseComponent
from input_handlers import ActionOrHandler
if TYPE_CHECKING:
    from entity import Actor, Item


class Consumable(BaseComponent):

    parent: Item

    def get_action(self, consumer: Actor) -> Optional[ActionOrHandler]:
        """Try to return the action for this item."""
        return actions.ItemAction(consumer, self.parent)

    def activate(self, action: actions.ItemAction) -> None:
        """Invoke this items ability.

        `action` is the context for this activation.
        """
        raise NotImplementedError()

    def consume(self) -> None:
        """Remove the consumed item from its containing inventory."""
        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.remove(entity)


class HealingConsumable(Consumable):
    def __init__(self, amount: int):
        self.amount = amount

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity

        for bodypart in consumer.bodyparts:
            bodypart.heal(self.amount)

        self.engine.message_log.add_message(
            f"You use the {self.parent.name}",
            colour.GREEN,
        )
        self.parent.stacking.stack_size -= 1
        if self.parent.stacking.stack_size <= 0:
            self.consume()


class Weapon(Consumable):

    def __init__(self, damage: int, ranged: bool, maximum_range: int, base_accuracy: float, ranged_accuracy: int):
        self.power = damage
        self.ranged = ranged  # if true, weapon has range (non-melee)
        self.maximum_range = maximum_range  # determines how far away the weapon can deal damage
        self.base_accuracy = base_accuracy  # decimal value, modifies base_chance_to_hit for a limb
        self.ranged_accuracy = ranged_accuracy  # the range up to which the weapon is accurate

        if not self.ranged:
            self.maximum_range = 1

    def activate(self, action: actions.ItemAction):
        return NotImplementedError


class Wearable(Consumable):  # in future add different types of protection i.e. projectile + melee
    def __init__(self, protection: int, fits_bodypart_type: str):
        self.protection = protection
        self.fits_bodypart = fits_bodypart_type  # bodypart types able to equip the item

    def activate(self, action: actions.ItemAction):
        pass
