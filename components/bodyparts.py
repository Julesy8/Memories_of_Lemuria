from __future__ import annotations

from random import randint
from math import floor, sqrt, pi
from numpy import log
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
                 width: int,
                 height: int,
                 depth: int,  # tissue depth (cm)
                 part_type: Optional[str],
                 strength_tissue: int = 1000000,  # tissue tensile strength, newtons per square metre
                 density_tissue: int = 1040,  # density of tissue, kg/m^3
                 vital: bool = False,
                 ):

        self.max_hp = hp
        self.hp_last_turn = hp
        self._hp = hp
        self._defence = defence
        self.width = width
        self.height = height
        self.depth = depth
        self.vital = vital  # whether when the body part gets destroyed, the entity should die
        self.strength_tissue = strength_tissue
        self.density_tissue = density_tissue
        self.equipped = None  # equipped armour item
        self.name = name

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

        elif self._hp <= self.max_hp * (1 / 4) and self.functional:
            self.cripple()

            if self.parent.player:
                self.engine.message_log.add_message(f"Your {self.name} is crippled", fg=colour.RED)

            else:
                self.engine.message_log.add_message(f"The {self.parent.name}'s {self.name} is crippled!",
                                                    fg=colour.GREEN)

            # causes AI to flee
            if self.vital:
                if self.parent.fears_death and not self.parent.has_fled_death:
                    self.parent.fleeing_turns = 8
                    self.parent.has_fled_death = True

    @defence.setter
    def defence(self, value):
        self._defence = value

    def die(self) -> None:

        self.parent.ai = None

        entity = Entity(x=0, y=0, char=self.parent.char, fg_colour=colour.WHITE, name=f"{self.parent.name} remains",
                        blocks_movement=False, parent=self.engine.game_map)

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

    def deal_damage_melee(self, meat_damage: int, armour_damage: int, attacker: Actor):

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
            damage = meat_damage - floor(((armour_protection + self.defence) / armour_damage)) * meat_damage

        if damage > 0:
            self.hp -= damage

        # hit, no damage dealt
        else:
            self.engine.message_log.add_message(f"The attack deals no damage.", fail_colour)

    def deal_damage_gun(self, diameter_bullet: float, mass_bullet: int, velocity_bullet: int,
                        drag_bullet: float, config_bullet: float, attacker: Actor):

        diameter_bullet = diameter_bullet * 25.4  # millimitres
        mass_bullet = mass_bullet * 0.0647989  # grams
        velocity_bullet = velocity_bullet * 0.3048  # metres per second

        fail_colour = colour.LIGHT_BLUE

        if attacker == self.engine.player:
            fail_colour = colour.YELLOW

        if self.equipped:
            armour_protection = self.equipped.usable_properties.protection + self.defence
            ballistic_limit = sqrt(((diameter_bullet ** 3) / mass_bullet) *
                                   ((armour_protection / (9.35 * 10 ** -9 * diameter_bullet)) ** 1.25))
            residual_velocity = 0
            try:
                residual_velocity = sqrt((velocity_bullet ** 2) - (ballistic_limit ** 2))
            except ValueError:
                pass
            velocity_bullet = residual_velocity

        if velocity_bullet > 0:

            # uniaxial strain proportionality
            strain_prop = (diameter_bullet ** (1.0 / 3)) * sqrt(self.strength_tissue / self.density_tissue)

            pen_depth = log(((velocity_bullet / strain_prop) ** 2 + 1)) * \
                        (mass_bullet / (pi * ((0.5 * (diameter_bullet / 10)) ** 2)
                                        * (self.density_tissue / 1000) * drag_bullet))

            wound_mass = round(pi * (0.5 * ((diameter_bullet / 10) ** 2)) * pen_depth *
                               (self.density_tissue / 1000) * config_bullet)

            if wound_mass > 0:
                self.hp -= wound_mass

            # hit, no damage dealt
            else:
                self.engine.message_log.add_message(f"The attack deals no damage.", fail_colour)

        # failed to penetrate armour
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

        # restores original stats
        self.parent.fighter.ranged_accuracy = self.parent.fighter.ranged_accuracy_original
        self.parent.fighter.melee_accuracy = self.parent.fighter.melee_accuracy_original
        self.parent.fighter.action_ap_modifier = 1.0
        self.parent.fighter.move_success_chance = self.parent.fighter.move_success_original
        self.parent.fighter.move_ap_cost = self.parent.fighter.move_ap_original
        self.parent.fighter.self.ap_per_turn_modifier = 1.0


class Arm(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 width: int,
                 height: int,
                 depth: int,
                 strength_tissue: int = 1000000,
                 density_tissue: int = 1040,
                 part_type: Optional[str] = 'Arms',
                 ):

        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            width=width,
            height=height
        )

    def cripple(self) -> None:

        self.functional = False

        if isinstance(self.parent.inventory.held, Item):

            self.parent.inventory.held.place(self.parent.x, self.parent.y, self.engine.game_map)
            self.parent.inventory.held = None

            if self.parent == self.engine.player:
                self.engine.message_log.add_message(f"The {self.parent.inventory.held.name} slips from your grasp",
                                                    colour.RED)

        self.parent.fighter.ranged_accuracy *= 1.2
        self.parent.fighter.melee_accuracy *= 0.8
        self.parent.fighter.action_ap_modifier *= 1.3


class Leg(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 name: str,
                 width: int,
                 height: int,
                 depth: int,
                 strength_tissue: int = 1000000,
                 density_tissue: int = 1040,
                 part_type: Optional[str] = 'Legs',
                 ):

        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            width=width,
            height=height
        )

    def cripple(self) -> None:

        self.functional = False

        functional_legs = 0

        for parts in self.parent.bodyparts:
            if parts.part_type == 'Legs':
                if parts.functional:
                    functional_legs += 1

        if functional_legs > 0:

            if self.parent.fighter.move_ap_cost < self.parent.fighter.max_ap:
                self.parent.fighter.move_ap_cost = self.parent.fighter.max_ap

            else:
                self.parent.fighter.move_success_chance *= 0.7

        else:
            self.parent.fighter.move_success_chance *= 0.5


class Head(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 width: int,
                 height: int,
                 depth: int,
                 strength_tissue: int = 1000000,
                 density_tissue: int = 1040,
                 name: str = 'head',
                 part_type: Optional[str] = 'Head',
                 ):
        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            vital=True,
            width=width,
            height=height
        )

    def cripple(self) -> None:
        # crippling the head 'knocks out' the entity for a random amount of turns

        if not self.parent == self.engine.player:
            self.functional = False

            turns_inactive = randint(3, 6)
            self.parent.turns_move_inactive = turns_inactive
            self.parent.turns_attack_inactive = turns_inactive
            self.parent.fighter.self.ap_per_turn_modifier = 0.7


class Body(Bodypart):
    def __init__(self,
                 hp: int,
                 defence: int,
                 width: int,
                 height: int,
                 depth: int,
                 strength_tissue: int = 1000000,
                 density_tissue: int = 1040,
                 name: str = 'torso',
                 part_type: Optional[str] = 'Body',
                 ):
        super().__init__(
            hp=hp,
            defence=defence,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            vital=True,
            width=width,
            height=height
        )
