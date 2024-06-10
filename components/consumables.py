from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from exceptions import Impossible

from numpy import random
from math import sqrt, e, pi, cos, sin
from random import uniform, choices, choice
from copy import deepcopy
from pydantic.utils import deep_update

import actions
import colour
import components.inventory
from input_handlers import SelectPartToRepair, MainGameEventHandler, BaseEventHandler, SelectPartToHeal
from components.npc_templates import BaseComponent

if TYPE_CHECKING:
    from components.bodyparts import Bodypart
    from components.gunparts import Parts
    from entity import Item, Actor
    from input_handlers import ActionOrHandler


class Usable(BaseComponent):
    parent: Item

    def get_action(self, user: Actor) -> Optional[ActionOrHandler]:
        """Try to return the action for this item."""
        return actions.ItemAction(user, self.parent)

    def get_attack_action(self, distance: int, entity: Actor, targeted_actor: Actor,
                          targeted_bodypart: Optional[Bodypart]):
        raise NotImplementedError

    def activate(self, action: ActionOrHandler) -> None:
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
        self.heal_amount = amount

    def get_action(self, user: Actor) -> Optional[ActionOrHandler]:
        options = []
        # appends injured body parts to options
        for bodypart in user.bodyparts:
            if bodypart.hp < bodypart.max_hp:
                options.append(bodypart)

        # returns part selection menu
        return SelectPartToHeal(engine=self.engine,
                                options=options,
                                callback=lambda part_to_heal:
                                actions.HealPart(entity=user,
                                                 part_to_heal=part_to_heal,
                                                 healing_item=self.parent,),
                                parent_handler=MainGameEventHandler(self.engine)
                                )

    def activate(self, action: actions.HealPart) -> BaseEventHandler:
        bodypart = action.part_to_heal
        bodypart.heal(self.heal_amount)

        self.parent.stacking.stack_size -= 1

        self.engine.message_log.add_message(f"{self.parent.name}s remaining: {self.parent.stacking.stack_size}",
                                            colour.WHITE, )

        if self.parent.stacking.stack_size <= 0:
            self.consume()
            return MainGameEventHandler(self.engine)


class RepairKit(Usable):

    def get_action(self, user: Actor) -> SelectPartToRepair:

        options = []

        # appends repairable items to options list
        for item in self.engine.player.inventory.items:
            if isinstance(item.usable_properties, GunComponent):
                if hasattr(item.usable_properties, 'condition_accuracy'):
                    if item.usable_properties.condition_accuracy < 5:
                        options.append(item)
                        continue
                elif hasattr(item.usable_properties, 'condition_function'):
                    if item.usable_properties.condition_function < 5:
                        options.append(item)

        # returns part selection menu
        return SelectPartToRepair(engine=self.engine,
                                  options=options,
                                  callback=lambda item_to_repair:
                                  actions.RepairItem(entity=user,
                                                     item_to_repair=item_to_repair,
                                                     repair_kit_item=self.parent),
                                  parent_handler=MainGameEventHandler(self.engine))

    def activate(self, action: actions.RepairItem) -> BaseEventHandler:
        item = action.item_to_repair

        assert isinstance(item.usable_properties, GunComponent)

        # adds to part condition
        if item.usable_properties.accuracy_part:
            if item.usable_properties.condition_accuracy < 5:
                item.usable_properties.condition_accuracy += 1

        if item.usable_properties.functional_part:
            if item.usable_properties.condition_function < 5:
                item.usable_properties.condition_function += 1

        self.parent.stacking.stack_size -= 1

        self.engine.message_log.add_message(f"Repair kits remaining: {self.parent.stacking.stack_size}", colour.WHITE, )

        if self.parent.stacking.stack_size <= 0:
            self.consume()
            return MainGameEventHandler(self.engine)


class Weapon(Usable):

    def __init__(self,
                 ap_to_equip: int,
                 base_ap_cost: int = 100,
                 ranged: bool = False,
                 ):

        self.ranged = ranged  # if true, weapon has range (non-melee)
        self.ap_to_equip = ap_to_equip
        self.base_ap_cost = base_ap_cost

    def activate(self, action: actions.ItemAction):
        raise NotImplementedError

    def equip(self, user: Actor) -> None:
        actions.EquipWeapon(entity=user, weapon=self).handle_action()

    def equip_to_primary(self, user: Actor) -> None:
        actions.EquipWeaponToPrimary(entity=user, weapon=self).handle_action()

    def equip_to_secondary(self, user: Actor) -> None:
        actions.EquipWeaponToSecondary(entity=user, weapon=self).handle_action()

    def unequip(self, user: Actor) -> None:
        actions.UnequipWeapon(entity=user, weapon=self).handle_action()

    def get_equip_ap(self) -> int:

        entity = self.parent
        inventory = entity.parent

        weight_handling_modifier = 1.0

        if isinstance(self, Gun):

            total_weight = self.parent.weight

            # magazine fed gun
            if hasattr(self, 'loaded_magazine'):
                if self.loaded_magazine is not None:
                    magazine = self.loaded_magazine.magazine
                    total_weight += len(magazine) * magazine[0].parent.weight + self.loaded_magazine.parent.weight
            # integrated magazine gun
            elif isinstance(self, GunIntegratedMag):
                magazine = self.magazine
                total_weight += len(magazine) * magazine[0].parent.weight

            # calculates AP modifier based on weight and weapon type

            if self.gun_type == 'pistol':
                weight_handling_modifier = 0.75 + 0.25 * total_weight
            elif self.gun_type != 'pistol' and not self.has_stock:
                weight_handling_modifier = 0.85 + 0.15 * (total_weight / 2)
            else:
                weight_handling_modifier = 0.85 + 0.15 * (total_weight / 3)

        equip_time = self.ap_to_equip * inventory.parent.fighter.action_ap_modifier * weight_handling_modifier

        if hasattr(self, 'loaded_magazine'):
            if self.loaded_magazine is not None:
                equip_time *= self.loaded_magazine.equip_ap_mod

        return self.ap_to_equip


class MeleeWeapon(Weapon):

    def __init__(self,
                 base_meat_damage: int,
                 base_armour_damage: int,
                 base_accuracy: float,
                 ap_to_equip: int,
                 base_ap_cost: int = 100,
                 ):

        self.base_accuracy = base_accuracy
        self.base_meat_damage = base_meat_damage
        self.base_armour_damage = base_armour_damage
        self.base_ap_cost = base_ap_cost

        super().__init__(
            ranged=False,
            ap_to_equip=ap_to_equip
        )

    def get_attack_action(self, distance: int, entity: Actor, targeted_actor: Actor,
                          targeted_bodypart: Optional[Bodypart]):
        return actions.MeleeAttackAction(distance=distance, entity=entity, targeted_actor=targeted_actor,
                                         weapon=self, targeted_bodypart=targeted_bodypart)

    def attack_melee(self, target: Actor, attacker: Actor, part_index: int, hitchance: int):

        weapon_accuracy_type = attacker.fighter.melee_accuracy

        # successful hit
        if hitchance <= (float(target.bodyparts[part_index].base_chance_to_hit) * self.base_accuracy
                         * weapon_accuracy_type):

            # does damage to given bodypart
            target.bodyparts[part_index].deal_damage_melee(
                meat_damage=self.base_meat_damage,
                armour_damage=self.base_armour_damage,
                attacker=attacker)

        # miss
        else:
            if attacker.player:
                return self.engine.message_log.add_message("You miss", colour.YELLOW)

            else:
                return self.engine.message_log.add_message(f"{attacker.name} misses", colour.LIGHT_BLUE)


class Bullet(Usable):

    def __init__(self,
                 bullet_type: str,
                 round_type: str,
                 mass: int,  # bullet mass in grains
                 charge_mass: float,  # mass of propellant in grains
                 diameter: float,  # inches
                 velocity: int,  # feet per second
                 proj_config: float,  # corresponds to form factor, e.g. JHP, FMJ
                 drag_coefficient: float,  # drag coeficient in 10% ballistic gel for different projectil types
                 spread_modifier: float,  # range penalty per tile to account for spread
                 ballistic_coefficient: float,
                 bullet_length: float,  # inches
                 projectile_type: str = 'single projectile',  # e.g. buckshot, birdshot
                 max_expansion: float = 1.0,  # multiplier of diameter
                 max_expansion_velocity: int = 2000,  # velocity at which bullet expands to maximum diameter
                 bullet_expands=False,  # whether bullet expands (hollow point / soft point)
                 bullet_yaws=False,  # whether bullet tumbles
                 bullet_fragments=False,  # whether bullet fragments
                 load_time_modifier: int = 300,
                 projectile_no: int = 1,
                 ):
        self.bullet_type = bullet_type
        self.round_type = round_type
        self.projectile_type = projectile_type
        self.mass = mass
        self.charge_mass = charge_mass
        self.diameter = diameter
        self.velocity = velocity
        self.proj_config = proj_config
        self.drag_coefficient = drag_coefficient
        self.ballistic_coefficient = ballistic_coefficient
        self.bullet_length = bullet_length
        self.max_expansion = max_expansion
        self.max_expansion_velocity = max_expansion_velocity
        self.bullet_expands = bullet_expands
        self.bullet_yaws = bullet_yaws
        self.bullet_fragments = bullet_fragments
        self.load_time_modifier = load_time_modifier
        self.projectile_no = projectile_no
        self.spread_modifier = spread_modifier


class Magazine(Usable):

    def __init__(self,
                 compatible_bullet_type: tuple,  # compatible bullet i.e. 9mm
                 mag_capacity: int,
                 ):
        self.compatible_bullet_type = compatible_bullet_type
        self.mag_capacity = mag_capacity
        self.magazine: list[Item] = []

    def loading_ap(self):
        return 0, 1.0, 1.0

    def load_magazine(self, entity: Actor, ammo: Item, load_amount: int) -> None:

        # loads bullets into magazine
        single_round = deepcopy(ammo)

        for i in range(load_amount):
            self.magazine.append(single_round)
            if len(self.magazine) == \
                    self.mag_capacity:
                break

        if isinstance(self, GunIntegratedMag):
            self.chamber_round()

        if isinstance(self, Gun):
            if self.clip_stays_in_gun:

                if self.clip_in_gun is not None:
                    entity.inventory.items.append(self.clip_in_gun.parent)

    def unload_magazine(self, entity: Actor) -> None:
        # unloads bullets from magazine
        inventory = entity.inventory

        if isinstance(inventory, components.inventory.Inventory):

            if isinstance(self, GunIntegratedMag):
                if not self.keep_round_chambered:
                    self.magazine.append(self.chambered_bullet)
                    setattr(self, "chambered_bullet", None)

            if len(self.magazine) > 0:
                for bullet in self.magazine:
                    if bullet is not None:
                        actions.AddToInventory(item=bullet, amount=1,
                                               entity=inventory.parent).handle_action()

                self.magazine = []

            else:
                return self.engine.message_log.add_message(f"{self.parent.name} is already empty", colour.RED)


class DetachableMagazine(Magazine):
    def __init__(self,
                 magazine_type: str,  # type of weapon this magazine works with i.e. glock 9mm
                 compatible_bullet_type: tuple,  # compatible bullet i.e. 9mm
                 mag_capacity: int,
                 magazine_size: str,  # small, medium or large
                 ap_to_load: int,  # ap it takes to load magazine into gun
                 witness_check_ap: int,  # ap it takes to check roughly how many rounds in magazine
                 failure_chance: int = 0,  # % chance to cause a jam
                 target_acquisition_ap_mod: float = 1.0,
                 ap_distance_cost_mod: float = 1.0,
                 equip_ap_mod: float = 1.0,
                 witness: bool = False,
                 ):
        super().__init__(compatible_bullet_type=compatible_bullet_type, mag_capacity=mag_capacity)

        self.magazine_type = magazine_type
        self.magazine_size = magazine_size
        self.ap_to_load = ap_to_load
        self.failure_chance = failure_chance
        self.target_acquisition_ap_mod = target_acquisition_ap_mod
        self.ap_distance_cost_mod = ap_distance_cost_mod
        self.equip_ap_mod = equip_ap_mod
        self.witness = witness
        self.witness_check_ap = witness_check_ap

    def check_rounds_in_mag(self) -> str:
        rounds_in_mag = len(self.magazine)
        round_str = ''
        if rounds_in_mag == self.mag_capacity:
            round_str = f'magazine full (capacity: {self.mag_capacity} rounds)'
        elif rounds_in_mag >= 0.8 * self.mag_capacity:
            round_str = f'magazine almost full (capacity: {self.mag_capacity} rounds)'
        elif rounds_in_mag >= 0.55 * self.mag_capacity:
            round_str = f'magazine over half full (capacity: {self.mag_capacity} rounds)'
        elif rounds_in_mag >= 0.45 * self.mag_capacity:
            round_str = f'magazine about half full (capacity: {self.mag_capacity} rounds)'
        elif rounds_in_mag <= 0.45 * self.mag_capacity:
            round_str = f'magazine less than half full (capacity: {self.mag_capacity} rounds)'
        elif rounds_in_mag <= 0.25 * self.mag_capacity:
            round_str = f'magazine less than a quarter full (capacity: {self.mag_capacity}) rounds'
        elif rounds_in_mag <= 0.1 * self.mag_capacity:
            round_str = f'magazine almost empty (capacity: {self.mag_capacity} rounds)'

        return round_str


class Clip(Magazine):
    def __init__(self,
                 magazine_type: str,
                 compatible_bullet_type: tuple,
                 mag_capacity: int,
                 magazine_size: str,
                 ap_to_load: int,
                 requires_gun_empty: bool = False
                 ):
        super().__init__(compatible_bullet_type=compatible_bullet_type, mag_capacity=mag_capacity)

        self.magazine_type = magazine_type
        self.magazine_size = magazine_size
        self.ap_to_load = ap_to_load
        self.requires_gun_empty = requires_gun_empty


# y, x
recoil_patterns = ((1.0, 0.0), (0.9, 0.1), (0.9, 0.1), (0.8, 0.2), (0.8, 0.2), (0.7, 0.3), (0.6, 0.4), (0.5, 0.5),
                   (0.4, 0.6))


class Gun(Weapon):
    def __init__(self,
                 parts: Parts,
                 gun_type: str,
                 action_type: str,
                 compatible_bullet_type: tuple,
                 velocity_modifier: dict,
                 ap_to_equip: int,
                 fire_modes: dict,  # fire rates in rpm
                 current_fire_mode: str,
                 keep_round_chambered: bool,
                 sound_modifier: float,
                 felt_recoil: float,  # 1.0 = regular M4
                 zero_range: int,  # yards
                 barrel_length: float,  # inches
                 sight_height_above_bore: float,  # inches
                 receiver_height_above_bore: float,  # inches
                 target_acquisition_ap: int,  # ap cost for acquiring new target
                 ap_distance_cost_modifier: float,  # AP cost modifier for distance from target
                 sight_spread_modifier: float,  # accuracy of the weapon's sighting system (MoA / 100)
                 handling_spread_modifier: float,  # spread purely due to accuracy of the sights themselves (MoA / 100)
                 projectile_spread_modifier: dict,  # spread due to ballistic factors i.e. barrel length, choke
                 manual_action: bool = False,
                 action_cycle_ap_cost: int = 100,
                 condition_accuracy: int = 5,
                 condition_function: int = 5,
                 firing_ap_cost: int = 25,  # additional AP cost for firing
                 muzzle_break_efficiency: float = 0.0,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 clip_stays_in_gun: bool = False,
                 clip_in_gun: Optional[Clip] = None,
                 compatible_clip: str = None,
                 previously_loaded_clip: Optional[Clip] = None,
                 chambered_bullet: Optional[Item] = None,
                 pdw_stock: bool = False,
                 has_stock: bool = False,
                 short_barrel: bool = False,
                 ):

        """
        velocity_modifier - increased w/ barrel length
        ap_to_equip - increased w/ weight, barrel length
        sound_modifier - decreased by suppressor
        felt_recoil - decreased w/ increased ergonomics and muzzle devices
        zero_range - set by optic,
        target_acquisition_ap - increased w/ barrel length and optic zoom, decreased w/ increased ergonomics and
        decreased weight
        firing_ap_cost - depends on type of trigger
        ap_distance_cost_modifier - decreased w/ increased optic zoom, decreased weight, ergonomics
        load_time_modifier - decreased w/ increased ergonomics
        """
        self.parts = parts
        self.gun_type = gun_type
        self.action_type = action_type
        self.has_stock = has_stock
        self.short_barrel = short_barrel
        self.compatible_bullet_type = compatible_bullet_type
        self.parts.parent = self
        self.felt_recoil = felt_recoil
        self.velocity_modifier = velocity_modifier
        self.muzzle_break_efficiency = muzzle_break_efficiency
        self.zero_range = zero_range
        self.receiver_height_above_bore = receiver_height_above_bore
        self.sight_height_above_bore = sight_height_above_bore
        self.barrel_length = barrel_length
        self.sight_spread_modifier = sight_spread_modifier
        self.handling_spread_modifier = handling_spread_modifier
        self.projectile_spread_modifier = projectile_spread_modifier
        self.clip_stays_in_gun = clip_stays_in_gun
        self.clip_in_gun = clip_in_gun
        self.previously_loaded_clip = previously_loaded_clip
        self.chambered_bullet = chambered_bullet
        self.keep_round_chambered = keep_round_chambered
        self.fire_modes = fire_modes
        self.current_fire_mode = current_fire_mode
        self.sound_modifier = sound_modifier
        self.fire_rate_modifier = fire_rate_modifier
        self.load_time_modifier = load_time_modifier
        self.target_acquisition_ap = target_acquisition_ap
        self.firing_ap_cost = firing_ap_cost
        self.ap_distance_cost_modifier = ap_distance_cost_modifier
        self.condition_accuracy = condition_accuracy
        self.condition_function = condition_function
        self.compatible_clip = compatible_clip
        self.pdw_stock = pdw_stock
        self.jammed = False

        self.manual_action = manual_action
        if self.manual_action:
            self.action_cycle_ap_cost = action_cycle_ap_cost

        self.momentum_gun = 0
        self.time_in_barrel = 0

        super().__init__(
            ranged=True,
            ap_to_equip=ap_to_equip,
        )

    def get_attack_action(self, distance: int, entity: Actor, targeted_actor: Actor,
                          targeted_bodypart: Optional[Bodypart]):
        raise NotImplementedError

    def attack_ranged(self, distance: int, target: Actor, attacker: Actor, part_index: int,
                      proficiency: float, skill_range_modifier: float) -> None:

        if self.jammed:
            self.engine.message_log.add_message("Attack failed: gun jammed.", colour.RED)

        recoil_control = 1.0

        if attacker.player:
            recoil_control = 1.0 - (attacker.fighter.skill_recoil_control / 4000)

        self.momentum_gun = 0
        self.time_in_barrel = 0

        recoil_spread_list = []

        # number of rounds fired in a single second
        if self.fire_modes[self.current_fire_mode]['automatic']:
            rounds_to_fire = round(self.fire_modes[self.current_fire_mode]['fire rate'] / 60 * self.fire_rate_modifier
                                   * attacker.fighter.automatic_fire_duration)
        else:
            rounds_to_fire = self.fire_modes[self.current_fire_mode]['fire rate']

        rounds_fired = 0
        recoil_penalty = 0

        if distance < 1:
            distance = 1

        dist_yards = distance * 1.09361

        # list of the shot sound radius of each shot fired
        sound_radius_list: list[float] = [0, ]

        # previous round fired, recorded for purposes of recoil calculations
        previous_round_fired = None

        sight_height_above_bore_total = self.sight_height_above_bore + self.receiver_height_above_bore

        mag_weight = 0
        magazine = None

        # adds weight of the magazine and loaded bullets to total weight for recoil calculations
        if isinstance(self, GunMagFed):
            if self.loaded_magazine is not None:
                magazine = self.loaded_magazine.magazine
                mag_weight = self.loaded_magazine.parent.weight

        elif isinstance(self, GunIntegratedMag):
            magazine = self.magazine

        # fires rounds
        while rounds_to_fire > 0:

            if self.chambered_bullet is not None:

                velocity_modifier = (self.velocity_modifier[self.chambered_bullet.usable_properties.projectile_type] *
                                     self.velocity_modifier[self.chambered_bullet.usable_properties.bullet_type])

                ammo_weight = 0

                if magazine is not None:
                    ammo_weight = len(magazine) * self.chambered_bullet.weight

                total_weight = self.parent.weight + mag_weight + ammo_weight

                # if attacker is player, jams the gun depending on its functional condition
                if attacker.player:

                    mag_fail_chance = 0

                    if isinstance(self, GunMagFed):
                        if self.loaded_magazine:
                            if isinstance(self.loaded_magazine, DetachableMagazine):
                                mag_fail_chance = self.loaded_magazine.failure_chance

                    if choices(population=(True, False), weights=(round(10 - ((self.condition_function / 5) * 10) +
                                                                        mag_fail_chance), 100))[0]:
                        self.engine.message_log.add_message("Your gun is jammed!", colour.RED)
                        self.jammed = True
                        return

                muzzle_velocity = self.chambered_bullet.usable_properties.velocity * velocity_modifier

                # calculates 'sound radius' based on barrel pressure relative to that of a glock 17 firing 115 gr
                # bullets, which has an arbitrary sound radius of 20 when unsuppressed
                sound_radius = ((self.chambered_bullet.usable_properties.mass * muzzle_velocity ** 2) /
                                (2 * (pi * (self.chambered_bullet.usable_properties.diameter / 2) ** 2)
                                 * self.barrel_length) / 181039271) * 20 * self.sound_modifier

                # if the sound radius of the fired round is not already in the list, appends it to the list for
                sound_radius_list.append(sound_radius)

                # aim location coordinates (inches)
                standard_deviation_aim = (dist_yards * attacker.fighter.ranged_accuracy * proficiency *
                                      skill_range_modifier * (self.handling_spread_modifier * 0.01) * 1.047)

                aim_location_x = random.normal(scale=standard_deviation_aim, size=1)[0]
                aim_location_y = random.normal(scale=standard_deviation_aim, size=1)[0]

                standard_deviation_sight = dist_yards * self.sight_spread_modifier * 1.047

                hit_location_x = random.normal(scale=standard_deviation_sight, size=1)[0]
                hit_location_y = random.normal(scale=standard_deviation_sight, size=1)[0]

                hit_location_x += aim_location_x
                hit_location_y += aim_location_y

                # projectile hit locations from ballistic factors
                projectile_spread_modifier = (self.projectile_spread_modifier
                                              [self.chambered_bullet.usable_properties.projectile_type] *
                                              self.chambered_bullet.usable_properties.spread_modifier *
                                              min((5 / self.condition_accuracy), 2) * dist_yards) * 1.047

                # Pejsa's projectile drop formula
                retardation_coefficient = \
                    self.chambered_bullet.usable_properties.ballistic_coefficient * 246 * muzzle_velocity ** 0.45

                projectile_drop = ((41.68 / muzzle_velocity) / ((1 / dist_yards) -
                                                                (1 / (retardation_coefficient -
                                                                      (0.75 + 0.00006 * dist_yards)
                                                                      * 0.5 * dist_yards)))) ** 2

                drop_at_zero = ((41.68 / muzzle_velocity) / ((1 / self.zero_range) -
                                                             (1 / (retardation_coefficient -
                                                                   (0.75 + 0.00006 * self.zero_range)
                                                                   * 0.5 * self.zero_range)))) ** 2

                # inches
                projectile_path = abs((projectile_drop + sight_height_above_bore_total) +
                                      (drop_at_zero + sight_height_above_bore_total) * dist_yards / self.zero_range)

                velocity_at_distance = muzzle_velocity * (1 - 3 * 0.5 * dist_yards / retardation_coefficient) ** (
                        1 / 0.5)

                for i in range(self.chambered_bullet.usable_properties.projectile_no):
                    spread_angle = uniform(0, 1) * 2 * pi

                    radius_projectile = (projectile_spread_modifier * 0.5) * sqrt(uniform(0, 1))
                    spread_x_projectile = radius_projectile * cos(spread_angle)
                    spread_y_projectile = radius_projectile * sin(spread_angle)

                    recoil_pattern = choice(recoil_patterns)
                    recoil_x = recoil_pattern[1] * recoil_penalty
                    recoil_y = recoil_pattern[0] * recoil_penalty

                    # checks if hit
                    hit_location_x += (recoil_x * dist_yards) + spread_x_projectile
                    hit_location_y += (recoil_y * dist_yards) + projectile_path + spread_y_projectile

                    # does damage to given bodypart
                    target.bodyparts[part_index].deal_damage_gun(
                        diameter_bullet=self.chambered_bullet.usable_properties.diameter,
                        mass_bullet=self.chambered_bullet.usable_properties.mass,
                        velocity_bullet=velocity_at_distance,
                        drag_bullet=self.chambered_bullet.usable_properties.drag_coefficient,
                        config_bullet=self.chambered_bullet.usable_properties.proj_config,
                        bullet_length=self.chambered_bullet.usable_properties.bullet_length,
                        bullet_expands=self.chambered_bullet.usable_properties.bullet_expands,
                        bullet_yaws=self.chambered_bullet.usable_properties.bullet_yaws,
                        bullet_fragments=self.chambered_bullet.usable_properties.bullet_fragments,
                        bullet_max_expansion=self.chambered_bullet.usable_properties.max_expansion,
                        bullet_expansion_velocity=self.chambered_bullet.usable_properties.max_expansion_velocity,
                        attacker=attacker,
                        hit_location_x=hit_location_x,
                        hit_location_y=hit_location_y,
                    )

                self.chambered_bullet = None
                self.chamber_round()

                rounds_to_fire -= 1
                rounds_fired += 1

                if self.chambered_bullet is not None:

                    # prevents recalculating recoil multiple times if the same bullet
                    # is chambered as was previously fired
                    if previous_round_fired is None or previous_round_fired == self.chambered_bullet:

                        # calculates recoil amount
                        muzzle_break = 0
                        if self.muzzle_break_efficiency is not None:
                            muzzle_break = self.muzzle_break_efficiency

                        gas_velocity = muzzle_velocity * 1.7
                        bullet_momentum = \
                            self.chambered_bullet.usable_properties.mass * 0.000142857 * muzzle_velocity * \
                            self.chambered_bullet.usable_properties.projectile_no
                        gas_momentum = \
                            self.chambered_bullet.usable_properties.charge_mass * 0.000142857 * muzzle_velocity / 2
                        momentum_jet = \
                            self.chambered_bullet.usable_properties.charge_mass * 0.000142857 * gas_velocity * \
                            ((1 - muzzle_break) ** (1 / sqrt(e)))
                        self.momentum_gun = bullet_momentum + gas_momentum + momentum_jet

                    # potentailly better equation found in ADA561571 equation 7 - 8
                    velocity_gun = (self.momentum_gun / total_weight)
                    # recoil spread (MoA) based assuming M4 recoil spread is 2 MoA with stock, handguard,
                    # and pistol grip reducing felt recoil by 70% shooting 55gr bullets.
                    # arbitrary but almost impossible to calculate actual muzzle rise for all guns and conifgurations
                    recoil_spread = \
                        (velocity_gun * self.felt_recoil * attacker.fighter.felt_recoil * 0.008 * proficiency *
                         recoil_control)

                    recoil_spread_list.append(recoil_spread)

                    rounds_per_quarter_sec = \
                        round((self.fire_modes[self.current_fire_mode]['fire rate'] /
                               60 * self.fire_rate_modifier) * 0.25)

                    if rounds_fired > rounds_per_quarter_sec:
                        rounds = recoil_spread_list[-rounds_per_quarter_sec:]
                        recoil_penalty = sum(rounds)
                    else:
                        recoil_penalty = sum(recoil_spread_list)

                    if attacker.player:
                        attacker.fighter.skill_recoil_control += round((recoil_penalty * 50))

            else:
                self.shot_sound_activation(sound_radius=max(sound_radius_list), attacker=attacker)
                if attacker.player:
                    self.engine.message_log.add_message(f"Out of ammo.", colour.RED)
                break

        attacker.fighter.ap -= round(75 * recoil_penalty)

        self.shot_sound_activation(sound_radius=max(sound_radius_list), attacker=attacker)

    def shot_sound_activation(self, sound_radius: float, attacker: Actor) -> None:
        # shot sound alert enemies in the vicinity of where the shot was fired from
        # only needs to be computed once for the 'loudest' shot fired

        for x in set(self.gamemap.actors):

            if not attacker.fighter.responds_to_sound:
                continue

            dx = x.x - attacker.x
            dy = x.y - attacker.y
            distance = max(abs(dx), abs(dy))  # Chebyshev distance.

            # if entity in range of the gun shot sound, starts pathing towards source of sound
            if distance <= sound_radius:

                if not x.player:
                    try:
                        path = x.ai.get_path_to(attacker.x, attacker.y)
                    except AttributeError:
                        continue
                    # TODO - bandaid fix
                    except RecursionError:
                        continue
                    if len(path) <= sound_radius:
                        setattr(x.ai, 'path', path)
                        x.active = True

                # prints to console vaguely where gunshots are coming from for the player
                if not attacker.player and not self.gamemap.visible[attacker.x, attacker.y]:

                    position_str = 'north'

                    x_dist = abs(abs(self.engine.player.x) - (abs(attacker.x)))
                    y_dist = abs(abs(self.engine.player.y) - (abs(attacker.y)))

                    if x_dist > y_dist:
                        if self.engine.player.x < attacker.x:
                            position_str = 'east'
                        else:
                            position_str = 'west'

                    elif self.engine.player.y < attacker.y:
                        position_str = 'south'

                    self.engine.message_log.add_message(f"You hear gun shots coming from the {position_str}",
                                                        colour.WHITE)

    def load_from_clip(self, clip: Clip):

        entity = self.parent
        inventory = entity.parent

        magazine = self

        if isinstance(self, GunIntegratedMag):
            magazine = self

        if isinstance(self, GunMagFed):
            magazine = self.loaded_magazine

        if isinstance(inventory, components.inventory.Inventory) and len(clip.magazine) > 0 and magazine:

            if len(clip.magazine) <= magazine.mag_capacity - len(magazine.magazine):
                if self.chambered_bullet:
                    actions.AddToInventory(item=self.chambered_bullet, amount=1, entity=inventory.parent)
                magazine.magazine += clip.magazine
                clip.magazine = []
                self.chambered_bullet = magazine.magazine.pop()

    def clip_reload_check_viable(self, clip: Clip) -> bool:
        entity = self.parent
        inventory = entity.parent

        magazine = None

        if isinstance(self, GunIntegratedMag):
            magazine = self

        if isinstance(self, GunMagFed):
            if self.loaded_magazine:
                magazine = self.loaded_magazine
            else:
                if inventory.parent.player:
                    raise Impossible(f"{inventory.parent.name}: cannot reload from clip - no magazine")
                else:
                    return False

        if isinstance(inventory, components.inventory.Inventory) and len(clip.magazine) > 0 and magazine:
            if len(clip.magazine) <= magazine.mag_capacity - len(magazine.magazine):
                return True

            elif inventory.parent.player:
                self.engine.message_log.add_message(f"{inventory.parent.name}: cannot load from clip",
                                                    colour.RED)

        elif inventory.parent.player:
            self.engine.message_log.add_message(f"{inventory.parent.name}: cannot load from clip",
                                                colour.RED)

        if len(magazine.magazine) > 0 and clip.requires_gun_empty and inventory.parent.player:
            self.engine.message_log.add_message(f"{inventory.parent.name}: rounds still loaded",
                                                colour.RED)

        return False

    def chamber_round(self):
        return NotImplementedError


class Wearable(Usable):
    def __init__(self,
                 ballistic_protection_level: str,
                 protection_ballistic: float,  # equivalent to inches of mild steel
                 coverage_v: float,  # chance that when an attack occurs, the armour will be hit
                 coverage_d: float,
                 coverage_l: float,
                 coverage_r: float,
                 protection_physical: int,
                 fits_bodypart_type: str,
                 equip_ap_cost: int,
                 ap_penalty: float = 1.0,
                 small_mag_slots: int = 0,
                 medium_mag_slots: int = 0,
                 large_mag_slots: int = 0,
                 ):
        self.ap_penalty = ap_penalty
        self.ballistic_protection_level = ballistic_protection_level
        self.protection_ballistic = protection_ballistic
        self.coverage_v = coverage_v
        self.coverage_d = coverage_d
        self.coverage_l = coverage_l
        self.coverage_r = coverage_r
        self.protection_physical = protection_physical
        self.fits_bodypart = fits_bodypart_type  # bodypart types able to equip the item

        self.equip_ap_cost = equip_ap_cost

        # how much of an item type the armour can carry
        self.small_mag_slots = small_mag_slots
        self.medium_mag_slots = medium_mag_slots
        self.large_mag_slots = large_mag_slots

    def equip(self, user: Actor) -> None:
        actions.EquipWearable(entity=user, wearable=self).handle_action()

    def unequip(self, user: Actor) -> None:
        actions.UnequipWearable(entity=user, wearable=self).handle_action()


class GunMagFed(Gun):
    def __init__(self,
                 parts: Parts,
                 gun_type: str,
                 action_type: str,
                 compatible_magazine_type: tuple,
                 compatible_bullet_type: tuple,
                 velocity_modifier: dict,
                 ap_to_equip: int,
                 fire_modes: dict,
                 current_fire_mode: str,
                 keep_round_chambered: bool,
                 sound_modifier: float,
                 zero_range: int,
                 barrel_length: float,
                 sight_height_above_bore: float,
                 receiver_height_above_bore: float,
                 felt_recoil: float,
                 target_acquisition_ap: int,
                 ap_distance_cost_modifier: float,
                 sight_spread_modifier: float,
                 handling_spread_modifier: float,
                 projectile_spread_modifier: dict,
                 manual_action: bool = False,
                 action_cycle_ap_cost: int = 100,
                 condition_accuracy: int = 5,
                 condition_function: int = 5,
                 firing_ap_cost: int = 25,  # additional AP cost for firing
                 muzzle_break_efficiency: float = 0.0,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 chambered_bullet: Optional[Item] = None,
                 loaded_magazine: Optional[DetachableMagazine] = None,
                 clip_stays_in_gun: bool = False,
                 clip_in_gun: Optional[Clip] = None,
                 compatible_clip: str = None,
                 has_stock: bool = False,
                 pdw_stock: bool = False,
                 short_barrel: bool = False,
                 ):

        self.compatible_magazine_type = compatible_magazine_type
        self.loaded_magazine = loaded_magazine

        # for AIs to know what type of magazine to reload
        self.previously_loaded_magazine = loaded_magazine

        super().__init__(
            parts=parts,
            action_type=action_type,
            velocity_modifier=velocity_modifier,
            ap_to_equip=ap_to_equip,
            fire_modes=fire_modes,
            current_fire_mode=current_fire_mode,
            keep_round_chambered=keep_round_chambered,
            chambered_bullet=chambered_bullet,
            sound_modifier=sound_modifier,
            muzzle_break_efficiency=muzzle_break_efficiency,
            fire_rate_modifier=fire_rate_modifier,
            load_time_modifier=load_time_modifier,
            compatible_bullet_type=compatible_bullet_type,
            zero_range=zero_range,
            sight_spread_modifier=sight_spread_modifier,
            handling_spread_modifier=handling_spread_modifier,
            clip_stays_in_gun=clip_stays_in_gun,
            clip_in_gun=clip_in_gun,
            felt_recoil=felt_recoil,
            sight_height_above_bore=sight_height_above_bore,
            target_acquisition_ap=target_acquisition_ap,
            firing_ap_cost=firing_ap_cost,
            ap_distance_cost_modifier=ap_distance_cost_modifier,
            receiver_height_above_bore=receiver_height_above_bore,
            condition_accuracy=condition_accuracy,
            condition_function=condition_function,
            manual_action=manual_action,
            action_cycle_ap_cost=action_cycle_ap_cost,
            compatible_clip=compatible_clip,
            gun_type=gun_type,
            has_stock=has_stock,
            short_barrel=short_barrel,
            barrel_length=barrel_length,
            pdw_stock=pdw_stock,
            projectile_spread_modifier=projectile_spread_modifier
        )

    def load_gun(self, user: Actor, magazine: DetachableMagazine):
        actions.ReloadMagFed(entity=user, magazine_to_load=magazine, gun=self).handle_action()

    def unload_gun(self):

        entity = self.parent
        inventory = entity.parent

        if isinstance(inventory, components.inventory.Inventory):

            if self.loaded_magazine is not None:

                if not self.keep_round_chambered:
                    self.loaded_magazine.magazine.append(self.chambered_bullet)
                    self.chambered_bullet = None

                inventory.items.append(self.loaded_magazine.parent)
                self.loaded_magazine = None

            else:
                self.engine.message_log.add_message(f"{entity.name} has no magazine loaded", colour.RED)

    def chamber_round(self):

        entity = self.parent
        inventory = entity.parent

        if self.loaded_magazine is not None:
            if len(self.loaded_magazine.magazine) > 0:
                if self.loaded_magazine.magazine[-1].usable_properties.bullet_type in \
                        self.compatible_bullet_type:
                    self.chambered_bullet = self.loaded_magazine.magazine.pop()
                else:
                    self.engine.message_log.add_message(f"{inventory.parent.name} failed to chamber a new round",
                                                        colour.RED)

    def get_attack_action(self, distance: int, entity: Actor, targeted_actor: Actor,
                          targeted_bodypart: Optional[Bodypart]):
        return actions.GunMagFedAttack(distance=distance, entity=entity, targeted_actor=targeted_actor,
                                       gun=self, targeted_bodypart=targeted_bodypart)


class GunIntegratedMag(Gun, Magazine):
    def __init__(self,
                 parts: Parts,
                 gun_type: str,
                 action_type: str,
                 velocity_modifier: dict,
                 ap_to_equip: int,
                 fire_modes: dict,
                 current_fire_mode: str,
                 compatible_bullet_type: tuple,
                 mag_capacity: int,
                 keep_round_chambered: bool,  # if when unloading gun the chambered round should stay
                 sound_modifier: float,
                 felt_recoil: float,
                 zero_range: int,
                 barrel_length: float,
                 sight_height_above_bore: float,
                 receiver_height_above_bore: float,
                 target_acquisition_ap: int,
                 ap_distance_cost_modifier: float,
                 sight_spread_modifier: float,
                 handling_spread_modifier: float,
                 projectile_spread_modifier: dict,
                 manual_action: bool = False,
                 action_cycle_ap_cost: int = 100,
                 condition_accuracy: int = 5,
                 condition_function: int = 5,
                 firing_ap_cost: int = 25,  # additional AP cost for firing
                 muzzle_break_efficiency: float = 0.0,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 clip_stays_in_gun: bool = False,
                 clip_in_gun: Optional[Clip] = None,
                 compatible_clip: str = None,
                 chambered_bullet: Optional[Item] = None,
                 has_stock: bool = False,
                 pdw_stock: bool = False,
                 short_barrel: bool = False,
                 ):
        self.mag_capacity = mag_capacity

        # magazine = list[item]
        self.magazine = []

        self.previously_loaded_round = chambered_bullet

        super().__init__(
            parts=parts,
            action_type=action_type,
            velocity_modifier=velocity_modifier,
            ap_to_equip=ap_to_equip,
            fire_modes=fire_modes,
            current_fire_mode=current_fire_mode,
            keep_round_chambered=keep_round_chambered,
            chambered_bullet=chambered_bullet,
            sound_modifier=sound_modifier,
            muzzle_break_efficiency=muzzle_break_efficiency,
            fire_rate_modifier=fire_rate_modifier,
            load_time_modifier=load_time_modifier,
            compatible_bullet_type=compatible_bullet_type,
            zero_range=zero_range,
            sight_spread_modifier=sight_spread_modifier,
            handling_spread_modifier=handling_spread_modifier,
            felt_recoil=felt_recoil,
            sight_height_above_bore=sight_height_above_bore,
            target_acquisition_ap=target_acquisition_ap,
            firing_ap_cost=firing_ap_cost,
            ap_distance_cost_modifier=ap_distance_cost_modifier,
            receiver_height_above_bore=receiver_height_above_bore,
            condition_accuracy=condition_accuracy,
            condition_function=condition_function,
            manual_action=manual_action,
            action_cycle_ap_cost=action_cycle_ap_cost,
            clip_stays_in_gun=clip_stays_in_gun,
            clip_in_gun=clip_in_gun,
            compatible_clip=compatible_clip,
            gun_type=gun_type,
            has_stock=has_stock,
            short_barrel=short_barrel,
            barrel_length=barrel_length,
            pdw_stock=pdw_stock,
            projectile_spread_modifier=projectile_spread_modifier
        )

    def chamber_round(self):
        if len(self.magazine) > 0:
            self.chambered_bullet = self.magazine.pop()

    def get_attack_action(self, distance: int, entity: Actor, targeted_actor: Actor,
                          targeted_bodypart: Optional[Bodypart]):
        return actions.GunIntegratedMagAttack(distance=distance, entity=entity, targeted_actor=targeted_actor,
                                              gun=self, targeted_bodypart=targeted_bodypart)

    def loading_ap(self):

        ap_cost = 0

        entity = self.parent
        inventory = entity.parent

        proficiency = 1.0

        if not self.keep_round_chambered and self.chambered_bullet is not None:
            if isinstance(inventory, components.inventory.Inventory):
                actions.AddToInventory(item=self.chambered_bullet, amount=1, entity=inventory.parent)

                if inventory.parent.player:
                    if self.action_type == 'bolt action':
                        proficiency = inventory.parent.fighter.skill_bolt_action_proficiency
                    elif self.action_type == 'revolver':
                        proficiency = inventory.parent.fighter.skill_revolver_proficiency
                    elif self.action_type == 'semi-auto rifle':
                        proficiency = inventory.parent.fighter.skill_sa_rifle_proficiency
                    elif self.action_type == 'semi-auto pistol':
                        proficiency = inventory.parent.fighter.skill_sa_pistol_proficiency
                    elif self.action_type == 'pump action':
                        proficiency = inventory.parent.fighter.skill_pumpaction_proficiency
                    elif self.action_type == 'break action':
                        proficiency = inventory.parent.fighter.skill_breakaction_proficiency
                    elif self.action_type == 'belt fed':
                        proficiency = inventory.parent.fighter.skill_belt_fed_proficiency


            proficiency = 1 - (proficiency / 4000)

        # adds cost of cycling manual action
        if self.manual_action:
            ap_cost += proficiency * self.action_cycle_ap_cost

        load_time_modifier = self.load_time_modifier

        return ap_cost, load_time_modifier, proficiency


class GunComponent(Usable):
    def __init__(self,
                 part_type: str,
                 prevents_suppression=False,
                 is_suppressor=False,
                 is_optic=False,
                 condition_accuracy: int = 5,
                 condition_function: int = 5,
                 accuracy_part: bool = False,
                 functional_part: bool = False,
                 **kwargs,
                 ):
        self.part_type = part_type
        self.prevents_suppression = prevents_suppression
        self.is_suppressor = is_suppressor
        self.is_optic = is_optic
        self.accuracy_part = accuracy_part
        self.functional_part = functional_part

        if accuracy_part:
            self.condition_accuracy = condition_accuracy
        if functional_part:
            self.condition_function = condition_function

        self.__dict__.update(kwargs)


class RecipeUnlock(Usable):

    def __init__(self, datapack: dict):
        self.datapack = datapack

    def activate(self, action: actions.ItemAction) -> None:
        self.engine.crafting_recipes = deep_update(self.engine.crafting_recipes, self.datapack)
        self.engine.message_log.add_message(
            f"Crafting recipes unlocked - {list(self.datapack.keys())[0]}",
            colour.GREEN,
        )

        self.consume()
