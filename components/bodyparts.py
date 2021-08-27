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
                 equipped: Optional[Item] = None,  # equipped item for the given body part
                 vital: bool = False,  # whether when the body part gets destroyed, the entity should die
                 body: bool = False,  # gives bodypart body functionality
                 head: bool = False,  # gives bodypart head functionality
                 leg: bool = False,  # gives bodypart leg functionality
                 arm: bool = False,  # gives bodypart arm functionality
                 ):

        self.max_hp = hp
        self.hp_last_turn = hp
        self._hp = hp
        self._defence = defence
        self.vital = vital
        self.equipped = equipped
        self.name = name
        self.base_chance_to_hit = base_chance_to_hit

        self.part_type = part_type  # only required for player character

        self.body = body
        self.head = head
        self.leg = leg
        self.arm = arm

        self.functional = True  # whether or not bodypart is crippled
        self.destroyed = False

        if self.arm:
            self.held = None

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

            elif self.functional and not self.destroyed:
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

    def deal_damage(self, damage: int, attacker: Actor, item: Optional[Item] = None):

        attack_colour = colour.RED
        fail_colour = colour.LIGHT_BLUE

        if attacker == self.engine.player:
            attack_colour = colour.GREEN
            fail_colour = colour.YELLOW

        if item:
            if damage > 0:
                if item.weapon.cutting_type:
                    self.engine.message_log.add_message(f"{attacker.name} slashes {self.parent.name} on the "
                                                        f"{self.name} with the {item.name}", attack_colour)

                elif item.weapon.projectile_type:
                    self.engine.message_log.add_message(f"{attacker.name} shoots the {self.parent.name} in the "
                                                        f"{self.name} with the {item.name}", attack_colour)

                else:
                    self.engine.message_log.add_message(f"{attacker.name} strikes {self.parent.name} on the "
                                                        f"{self.name} with the {item.name}", attack_colour)

                if damage >= self.max_hp * 0.45 and self.hp - damage <= 0 and self.functional and not self.body:
                    self.destroy(item)

                self.hp -= damage

            else:
                if item.weapon.cutting_type:
                    self.engine.message_log.add_message(f"{attacker.name} slashes {self.parent.name} with the"
                                                        f" {item.name} but the blow glances off", fail_colour)

                elif item.weapon.projectile_type:
                    self.engine.message_log.add_message(f"{attacker.name} shoots the {self.parent.name} in the "
                                                        f"{self.name} with the {item.name}, but the bullet does "
                                                        f"nothing", fail_colour)

                else:
                    self.engine.message_log.add_message(f"{attacker.name} tries to strike {self.parent.name} but the"
                                                        f" blow glances off", fail_colour)

        else:
            if damage > 0:
                self.engine.message_log.add_message(f"{attacker.name} strikes {self.parent.name} on the "
                                                    f"{self.name}", attack_colour)

                self.hp -= damage

            else:
                self.engine.message_log.add_message(f"{attacker.name} tries to strike {self.parent.name} but the blow"
                                                    f" glances off", fail_colour)

    def cripple(self) -> None:
        self.functional = False

        if self.leg:
            functional_legs = 0

            for parts in self.parent.bodyparts:
                if parts.leg:
                    if parts.functional:
                        functional_legs += 1

            if functional_legs > 0:

                if self.parent.moves_per_turn > 1:
                    self.parent.moves_per_turn = 1

                else:
                    self.parent.move_interval = self.parent.move_interval_original + 1

            else:
                self.parent.move_interval = 2 * self.parent.move_interval

        if self.arm:
            if self.held:

                for bodypart in self.parent.bodyparts:
                    if bodypart.arm:
                        if bodypart.held == self.held:
                            bodypart.held = None

                self.held.place(self.parent.x, self.parent.y, self.engine.game_map)

                if self.parent == self.engine.player:
                    self.engine.message_log.add_message(f"The {self.held.name} slips from your grasp", colour.RED)

                else:
                    self.engine.message_log.add_message(f"The {self.held.name} slips from {self.parent.name}'s grasp"
                                                        , colour.GREEN)

    def destroy(self, item: Optional[Item]):

        self.destroyed = True

        if item:
            if item.weapon.cutting_type:
                self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} flys off in an arc!",
                                                    colour.GREEN)

                #blood_entity = deepcopy(blood)  # TODO: bleeding here

            elif item.weapon.projectile_type:
                self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} explodes into pieces!",
                                                    colour.GREEN)

            else:
                self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} is crushed to a pulp!",
                                                    colour.GREEN)

        else:
            self.engine.message_log.add_message(f"{self.parent.name}'s {self.name} is crushed to a pulp!", colour.GREEN)

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