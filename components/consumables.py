from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
import colour
import components.inventory
from components.npc_templates import BaseComponent
from input_handlers import ActionOrHandler
if TYPE_CHECKING:
    from entity import Actor, Item


class Usable(BaseComponent):

    parent: Item

    def __init__(self, usable_type: str):
        self.usable_type = usable_type

    def get_action(self, user: Actor) -> Optional[ActionOrHandler]:
        """Try to return the action for this item."""
        return actions.ItemAction(user, self.parent)

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


class HealingConsumable(Usable):
    def __init__(self, amount: int):
        self.amount = amount

        super().__init__(usable_type='consumable')

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


class Weapon(Usable):

    def __init__(self,
                 base_meat_damage: int,
                 base_armour_damage: int,
                 maximum_range: int,
                 base_accuracy: float,
                 range_accuracy_dropoff: Optional[int],
                 two_handed: bool = False,
                 ranged: bool = False,
                 cutting: bool = False
                 ):

        super().__init__(usable_type='weapon')

        self.base_meat_damage = base_meat_damage
        self.base_armour_damage = base_armour_damage
        self.ranged = ranged  # if true, weapon has range (non-melee)
        self.maximum_range = maximum_range  # determines how far away the weapon can deal damage
        self.base_accuracy = base_accuracy  # decimal value, modifies base_chance_to_hit for a limb
        self.range_accuracy_dropoff = range_accuracy_dropoff  # the range up to which the weapon is accurate
        self.two_handed = two_handed  # the amount of hands used to hold this weapon
        self.cutting = cutting # whether the weapon can cleanly remove limbs

        if not self.ranged:
            self.maximum_range = 1

    def activate(self, action: actions.ItemAction):
        return NotImplementedError


class Bullet(Usable):

    def __init__(self,
                 bullet_type: str,
                 meat_damage_factor: float,
                 armour_damage_factor: float,
                 accuracy_factor: float,
                 ):

        super().__init__(usable_type='ammunition')

        self.bullet_type = bullet_type
        self.meat_damage_factor = meat_damage_factor
        self.armour_damage_factor = armour_damage_factor
        self.accuracy_factor = accuracy_factor

    def activate(self, action: actions.ItemAction):
        return NotImplementedError


class Magazine(Usable):

    def __init__(self,
                 compatible_bullet_type,
                 mag_capacity,
                 ):
        self.compatible_bullet_type = compatible_bullet_type
        self.mag_capacity = mag_capacity

        super().__init__(usable_type='magazine')

    def activate(self, action: actions.ItemAction):
        return NotImplementedError


class Gun(Weapon):

    def __init__(self,
                 compatible_magazine_type: str,
                 chambered_bullet: Optional[Bullet],
                 loaded_magazine: Optional[Magazine],
                 base_meat_damage: int,
                 base_armour_damage: int,
                 base_accuracy: int,
                 range_accuracy_dropoff: int,
                 two_handed: bool,
                 ):

        self.compatible_magazine_type = compatible_magazine_type
        self.chambered_bullet = chambered_bullet
        self.loaded_magazine = loaded_magazine

        super().__init__(
            base_meat_damage=base_meat_damage,
            base_armour_damage=base_armour_damage,
            maximum_range=100,
            base_accuracy=base_accuracy,
            ranged=True,
            range_accuracy_dropoff=range_accuracy_dropoff,
            two_handed=two_handed,
        )


class Wearable(Usable):  # in future add different types of protection i.e. projectile + melee
    def __init__(self, protection: int, fits_bodypart_type: str):
        self.protection = protection
        self.fits_bodypart = fits_bodypart_type  # bodypart types able to equip the item

        super().__init__(usable_type='wearable')

    def activate(self, action: actions.ItemAction):
        return NotImplementedError
