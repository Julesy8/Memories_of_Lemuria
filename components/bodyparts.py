from __future__ import annotations

from copy import deepcopy
from random import randint
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
                 base_chance_to_hit: int,
                 part_type: Optional[str],
                 vital: bool = False,
                 ):

        self.max_hp = hp
        self.hp_last_turn = hp
        self._hp = hp
        self._defence = defence
        self.vital = vital  # whether when the body part gets destroyed, the entity should die
        self.equipped = None  # equipped armour item
        self.name = name

        # base modifier of how likely the body part is to be hit when attacked between
        # 1 and 100. Higher = more likely to hit.
        self.base_chance_to_hit = base_chance_to_hit

        self.part_type = part_type  # string associated with the type of bodypart it is, i.e. 'Head', 'Arm'
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

        if self._hp <= self.max_hp * 0.70 and self.parent.bleeds:
            blood_copy = deepcopy(self.parent.blood_entity)
            blood_copy.place(x=self.parent.x, y=self.parent.y, gamemap=self.engine.game_map)

        if self._hp == 0 and self.parent.ai:

            if self.vital:
                self.die()

        elif self._hp <= self.max_hp * 1/3 and self.functional:
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
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE

        for item in self.parent.inventory.items:
            item.place(x=self.parent.x, y=self.parent.y, gamemap=self.engine.game_map)

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

        for bodypart in self.parent.bodyparts:
            bodypart.functional = True

        # restores original attack and movement stats
        self.parent.attack_interval = self.parent.attack_interval_original
        self.parent.attacks_per_turn = self.parent.attacks_per_turn_original
        self.parent.move_interval = self.parent.move_interval_original
        self.parent.moves_per_turn = self.parent.moves_per_turn_original

        # restores original entity base accuracy stats
        self.parent.fighter.ranged_accuracy = self.parent.fighter.ranged_accuracy_original
        self.parent.fighter.melee_accuracy = self.parent.fighter.melee_accuracy_original


class Arm(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 base_chance_to_hit: int = 90,
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

        self.parent.fighter.ranged_accuracy = self.parent.fighter.ranged_accuracy * 0.8
        self.parent.fighter.ranged_accuracy = self.parent.fighter.ranged_accuracy * 0.8


class Leg(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 base_chance_to_hit: int = 90,
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


class Head(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 base_chance_to_hit: int = 80,
                 name: str = 'head',
                 part_type: Optional[str] = 'Head',
                 ):

        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            base_chance_to_hit=base_chance_to_hit,
            part_type=part_type,
            vital=True
        )

    def cripple(self) -> None:

        # crippling the head 'knocks out' the entity for a random amount of turns

        if not self.parent == self.engine.player:

            self.functional = False

            turns_inactive = randint(3, 6)
            self.parent.turns_move_inactive = turns_inactive
            self.parent.turns_attack_inactive = turns_inactive


class Body(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 base_chance_to_hit: int = 100,
                 name: str = 'body',
                 part_type: Optional[str] = 'Body',
                 ):

        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            base_chance_to_hit=base_chance_to_hit,
            part_type=part_type,
            vital=True
        )
