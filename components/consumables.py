from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
import colour
import components.inventory
from components.npc_templates import BaseComponent
from exceptions import Impossible

if TYPE_CHECKING:
    from entity import Actor, Item


class Consumable(BaseComponent):

    parent: Item

    def get_action(self, consumer: Actor) -> Optional[actions.Action]:
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
        amount_recovered = consumer.fighter.heal(self.amount)

        if amount_recovered > 0:
            self.engine.message_log.add_message(
                f"You consume the {self.parent.name}, and recover {amount_recovered} HP!",
                colour.GREEN,
            )
            self.consume()
        else:
            raise Impossible(f"Your health is already full.")


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
        consumer = action.entity
        target = None
        closest_distance = self.maximum_range + 1.0
        distance = 0

        for actor in self.engine.game_map.actors:
            if actor is not consumer and self.parent.gamemap.visible[actor.x, actor.y]:
                distance = consumer.distance(actor.x, actor.y)

                if distance < closest_distance:
                    target = actor
                    closest_distance = distance

        if target:
            return actions.WeaponAttackAction(distance=distance, item=self.parent, entity=consumer,
                                              targeted_actor=target).attack()

        else:
            raise Impossible("No enemy is close enough to strike.")
