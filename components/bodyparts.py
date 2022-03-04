from __future__ import annotations

from random import randint
from math import floor
from typing import Optional, TYPE_CHECKING
from copy import deepcopy
from random import choices

from components.consumables import RecipeUnlock
from components.datapacks import datapackdict
from entity import Actor, Entity, Item
from components.enemies.equipment import enemy_equipment
import colour

if TYPE_CHECKING:
    from engine import Engine


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
            self.engine.game_map.tiles[self.parent.x, self.parent.y][3][2] = colour.RED

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

        self.parent.ai = None

        entity = Entity(x=0, y=0, char=self.parent.char, fg_colour=colour.WHITE, bg_colour=None,
                        name=f"{self.parent.name} remains", blocks_movement=False, parent=self.engine.game_map)

        entity.place(x=self.parent.x, y=self.parent.y, gamemap=self.engine.game_map)

        item_pop = []
        item_weight = []

        # puts items in enemy inventory
        if self.parent.drops_items:
            for item in enemy_equipment[self.parent.name]["dropped items"]:
                item_pop.append(item[0])
                item_weight.append(item[1])

            # places random item in inventory
            item_drop = deepcopy(choices(population=item_pop, weights=item_weight, k=1)[0])

            if isinstance(item_drop, Item):

                # gives PDA datapack properties
                if item_drop.name == 'PDA':

                    data_pack_pop = []
                    data_pack_weight = []

                    for i in datapackdict[self.engine.current_level]:
                        data_pack_pop.append(i[0])
                        data_pack_weight.append(i[1])

                    item_drop.usable_properties = RecipeUnlock(choices(population=data_pack_pop,
                                                                       weights=data_pack_weight, k=1)[0])

                item_drop.usable_properties.parent = item_drop

                item_drop.place(x=self.parent.x, y=self.parent.y, gamemap=self.engine.game_map)

        if self.parent.inventory.held is not None:
            self.parent.inventory.held.place(x=self.parent.x, y=self.parent.y, gamemap=self.engine.game_map)

        if self.parent.player:
            self.engine.message_log.add_message("You died.", colour.LIGHT_MAGENTA)

        self.engine.game_map.entities.remove(self.parent)

    def deal_damage(self, meat_damage: int, armour_damage: int, attacker: Actor, item: Optional[Item] = None):

        fail_colour = colour.LIGHT_BLUE

        if attacker == self.engine.player:
            fail_colour = colour.YELLOW

        armour_protection = 0
        if self.equipped:
            armour_protection = self.equipped.usable_properties.protection

        if armour_damage < self.defence + armour_protection:
            damage = 0
        elif self.defence + armour_protection == 0:
            damage = meat_damage
        else:
            damage = floor(((armour_protection + self.defence)/armour_damage)) * meat_damage

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
