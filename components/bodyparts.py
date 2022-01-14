from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from entity import Actor, Entity
from render_order import RenderOrder
import colour

if TYPE_CHECKING:
    from entity import Item
    from engine import Engine

blood = Entity(x=0, y=0, char=' ', fg_colour=colour.RED, bg_colour=colour.RED, name='Blood')


class Bodypart:

    parent: Actor

    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 base_chance_to_hit: int,  # base modifier of how likely the body part is to be hit when attacked
                 part_type: Optional[str],  # string associated with the type of bodypart it is, i.e. 'Head', 'Arm'
                 vital: bool = False,  # whether when the body part gets destroyed, the entity should die
                 destroyable: bool = True  # whether or not the body part should be able to be destroyed i.e. cut off, explode
                 ):

        self.max_hp = hp
        self.hp_last_turn = hp
        self._hp = hp
        self._defence = defence
        self.vital = vital
        self.equipped = None
        self.name = name
        self.base_chance_to_hit = base_chance_to_hit
        self.destroyable = destroyable

        self.part_type = part_type  # only required for player character

        self.functional = True  # whether or not bodypart is crippled

    @property
    def engine(self) -> Engine:
        return self.parent.gamemap.engine

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def defence(self) -> int:
        return self._defence

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))

        if self._hp == 0 and self.parent.ai:

            if self.vital:
                self.die()

            elif self.functional:
                self.cripple()

                if self.parent.player:
                    self.engine.message_log.add_message(f"Your {self.name} is crippled", fg=colour.RED)

                else:
                    self.engine.message_log.add_message(f"The {self.parent.name}'s {self.name} is crippled!",
                                                        fg=colour.GREEN)

    @defence.setter
    def defence(self, value):
        self._defence = value

    def die(self) -> None:

        self.parent.fg_colour = colour.WHITE
        self.parent.bg_colour = colour.LIGHT_RED
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE

        if self.parent.player:
            self.engine.message_log.add_message("You died.", colour.LIGHT_MAGENTA)

    def deal_damage(self, meat_damage: int, armour_damage: int, attacker: Actor, item: Optional[Item] = None):

        damage = meat_damage

        fail_colour = colour.LIGHT_BLUE

        if attacker == self.engine.player:
            fail_colour = colour.YELLOW

        armour_protection = 0
        if self.equipped:
            armour_protection = self.equipped.usable_properties.protection

        if armour_damage < self.defence + armour_protection:
            damage = 0

        # attack w/ weapon
        if item:
            if damage > 0:

                if damage >= self.max_hp * 0.45 and self.hp - damage <= 0 and self.functional and self.destroyable:
                    self.destroy(item)

                self.hp -= damage

            # hit, no damage dealt
            else:
                self.engine.message_log.add_message(f"The attack deals no damage.", fail_colour)

        # unarmed attack
        else:
            if damage > 0:
                self.hp -= damage

            # hit, no damage dealt
            else:
                self.engine.message_log.add_message(f"The attack deals no damage.", fail_colour)

    def cripple(self) -> None:
        self.functional = False

    def destroy(self, item: Optional[Item]):

        if item:
            if item.usable_properties.cutting:
                self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} flys off in an arc!",
                                                    colour.GREEN)

                #blood_entity = deepcopy(blood)  # TODO: bleeding here, place limb object onto map

            else:
                self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} explodes into pieces!",
                                                    colour.GREEN)

        self.cripple()

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value
        self.restore()

        return amount_recovered

    def restore(self):

        """
        this is only intended to be used on the player since they can't have their limbs destroyed
        if this needs to be used for other entities, need to implement a system not restoring limb functionality
        while having limbs destroyed
        """

        for bodypart in self.parent.bodyparts:
            bodypart.functional = True

        # restores original attack and movement stats
        self.parent.attack_interval = self.parent.attack_interval_original
        self.parent.attacks_per_turn = self.parent.attacks_per_turn_original
        self.parent.move_interval = self.parent.move_interval_original
        self.parent.moves_per_turn = self.parent.moves_per_turn_original

    def bodypart_to_entity(self,):
        return Entity(x=0, y=0, char=',', name=f"{self.parent.name} {self.name}", bg_colour=None,
                      fg_colour=colour.LIGHT_RED)


class Arm(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 base_chance_to_hit: int,
                 part_type: Optional[str] = 'Arms',
                 ):

        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            base_chance_to_hit=base_chance_to_hit,
            part_type=part_type
        )

    def cripple(self) -> None:

        self.functional = False

        if self.parent.inventory.held is not None:

            self.parent.inventory.held.place(self.parent.x, self.parent.y, self.engine.game_map)
            self.parent.inventory.held = None

            if self.parent == self.engine.player:
                self.engine.message_log.add_message(f"The {self.parent.inventory.held.name} slips from your grasp",
                                                    colour.RED)


class Leg(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 base_chance_to_hit: int,
                 part_type: Optional[str] = 'Legs',
                 ):

        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            base_chance_to_hit=base_chance_to_hit,
            part_type=part_type
        )

    def cripple(self) -> None:

        self.functional = False

        functional_legs = 0

        for parts in self.parent.bodyparts:
            if parts.part_type == 'Legs':
                if parts.functional:
                    functional_legs += 1

        if functional_legs > 0:

            if self.parent.moves_per_turn > 1:
                self.parent.moves_per_turn = 1

            else:
                self.parent.move_interval = self.parent.move_interval_original + 1

        else:
            self.parent.move_interval = 2 * self.parent.move_interval
