from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from exceptions import Impossible

from math import sqrt, e, pi, cos, sin
from random import uniform, choices
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
        self.amount = amount

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
                                                 healing_item=self.parent))

    def activate(self, action: actions.HealPart) -> BaseEventHandler:
        bodypart = action.part_to_heal
        bodypart.heal(self.amount)

        self.parent.stacking.stack_size -= 1

        self.engine.message_log.add_message(f"{self.parent.name}'s remaining: {self.parent.stacking.stack_size}",
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
                if item.usable_properties.condition_accuracy < 5 or item.usable_properties.condition_function < 5:
                    options.append(item)

        # returns part selection menu
        return SelectPartToRepair(engine=self.engine,
                                  options=options,
                                  callback=lambda item_to_repair:
                                  actions.RepairItem(entity=user,
                                                     item_to_repair=item_to_repair,
                                                     repair_kit_item=self.parent))

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
                weight_handling_modifier = 0.4 + 0.6 * total_weight

            else:
                weight_handling_modifier = 0.5 + 0.5 * (total_weight / 4)

        equip_time = self.ap_to_equip * inventory.parent.fighter.action_ap_modifier * weight_handling_modifier

        if hasattr(self, 'loaded_magazine'):
            if self.loaded_magazine is not None:
                equip_time *= self.loaded_magazine.equip_ap_mod

        return self.ap_to_equip
        # TODO - if weapon attack turns in full auto go over one turn, should be broken up into multiple turns

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
                                         weapon=self, targeted_bodypart=targeted_bodypart).handle_action()

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
                 mass: int,  # bullet mass in grains
                 charge_mass: float,  # mass of propellant in grains
                 diameter: float,  # inches
                 velocity: int,  # feet per second
                 proj_config: float,  # corresponds to form factor, e.g. JHP, FMJ
                 drag_coefficient: float,  # drag coeficient in 10% ballistic gel for different projectil types
                 spread_modifier: float,  # range penalty per tile to account for spread
                 ballistic_coefficient: float,
                 bullet_length: float,  # inches
                 max_expansion: float = 1.0,  # multiplier of diameter
                 max_expansion_velocity: int = 2000,  # velocity at which bullet expands to maximum diameter
                 bullet_expands=False,  # whether bullet expands (hollow point / soft point)
                 bullet_yaws=False,  # whether bullet tumbles
                 bullet_fragments=False,  # whether bullet fragments
                 load_time_modifier: int = 200,
                 projectile_no: int = 1,
                 ):
        self.bullet_type = bullet_type
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
                 compatible_bullet_type: list,  # compatible bullet i.e. 9mm
                 mag_capacity: int,
                 ):
        self.compatible_bullet_type = compatible_bullet_type
        self.mag_capacity = mag_capacity
        self.magazine: list[Bullet] = []

    def loading_ap(self):
        return 0, 1.0, 1.0

    def load_magazine(self, ammo: Bullet, load_amount: int) -> None:

        # loads bullets into magazine
        single_round = deepcopy(ammo)

        for i in range(load_amount):
            self.magazine.append(single_round)
            if len(self.magazine) == \
                    self.mag_capacity:
                break

        if isinstance(self, GunIntegratedMag):
            self.chamber_round()

    def unload_magazine(self, entity: Actor) -> None:
        # unloads bullets from magazine

        bullets_unloaded = []

        inventory = entity.inventory

        if isinstance(inventory, components.inventory.Inventory):

            if isinstance(self, GunIntegratedMag):
                if not self.keep_round_chambered:
                    self.magazine.append(self.chambered_bullet)
                    setattr(self, "chambered_bullet", None)

            if len(self.magazine) > 0:
                for bullet in self.magazine:

                    if bullet not in bullets_unloaded:
                        bullets_unloaded.append(bullet.parent)
                        bullet_counter = 0
                        for i in self.magazine:
                            if i.parent.name == bullet.parent.name:
                                bullet_counter += 1

                        bullet.parent.stacking.stack_size = bullet_counter

                        actions.AddToInventory(item=bullet.parent, amount=bullet_counter,
                                               entity=inventory.parent).perform()
                self.magazine = []

            else:
                return self.engine.message_log.add_message(f"{entity.name} is already empty", colour.RED)

class DetachableMagazine(Magazine):
    def __init__(self,
                 magazine_type: str,  # type of weapon this magazine works with i.e. glock 9mm
                 compatible_bullet_type: list,  # compatible bullet i.e. 9mm
                 mag_capacity: int,
                 magazine_size: str,  # small, medium or large
                 ap_to_load: int,  # ap it takes to load magazine into gun
                 failure_chance: int = 0,  # % chance to cause a jam
                 target_acquisition_ap_mod: float = 1.0,
                 ap_distance_cost_mod: float = 1.0,
                 equip_ap_mod: float = 1.0,
                 ):

        super().__init__(compatible_bullet_type=compatible_bullet_type, mag_capacity=mag_capacity)

        self.magazine_type = magazine_type
        self.magazine_size = magazine_size
        self.ap_to_load = ap_to_load
        self.failure_chance = failure_chance
        self.target_acquisition_ap_mod = target_acquisition_ap_mod
        self.ap_distance_cost_mod = ap_distance_cost_mod
        self.equip_ap_mod = equip_ap_mod

class Clip(Magazine):
    def __init__(self,
                 magazine_type: str,
                 compatible_bullet_type: list,
                 mag_capacity: int,
                 magazine_size: str,
                 ap_to_load: int,
                 ):

        super().__init__(compatible_bullet_type=compatible_bullet_type, mag_capacity=mag_capacity)

        self.magazine_type = magazine_type
        self.magazine_size = magazine_size
        self.ap_to_load = ap_to_load

class Gun(Weapon):
    def __init__(self,
                 parts: Parts,
                 gun_type: str,
                 compatible_bullet_type: str,
                 velocity_modifier: float,
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
                 spread_modifier: float,  # MoA / 100 - for M16A2 2-3 MoA, so 0.03
                 manual_action: bool = False,
                 action_cycle_ap_cost: int = 100,
                 condition_accuracy: int = 5,
                 condition_function: int = 5,
                 firing_ap_cost: int = 25,  # additional AP cost for firing
                 muzzle_break_efficiency: float = 0.0,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 compatible_clip: str = None,
                 chambered_bullet: Optional[Bullet] = None,
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
        self.spread_modifier = spread_modifier  # MoA / 100
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


    def attack_ranged(self, distance: int, target: Actor, attacker: Actor, part_index: int, hit_location_x: int,
                      hit_location_y: int, proficiency: float, skill_range_modifier: float) -> None:

        if self.jammed:
            self.engine.message_log.add_message("Attack failed: gun jammed. Press ENTER to clear.", colour.RED)

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

        spread_angle = uniform(0, 1) * 2 * pi
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

                ammo_weight = len(magazine) * self.chambered_bullet.parent.weight
                total_weight = self.parent.weight + mag_weight + ammo_weight

                # if attacker is player, jams the gun depending on its functional condition
                if attacker.player:

                    mag_fail_chance = 0

                    if isinstance(self, GunMagFed):
                        if self.loaded_magazine:
                            if isinstance(self.loaded_magazine, DetachableMagazine):
                                mag_fail_chance = self.loaded_magazine.failure_chance

                    if choices(population=(True, False), weights=(round(25 - ((self.condition_function / 5) * 25) +
                                                                        mag_fail_chance), 100))[0]:
                        self.engine.message_log.add_message("Your gun is jammed! Press ENTER to clear.", colour.RED)
                        self.jammed = True
                        return

                muzzle_velocity = self.chambered_bullet.velocity * self.velocity_modifier

                # calculates 'sound radius' based on barrel pressure relative to that of a glock 17 firing 115 gr
                # bullets, which has an arbitrary sound radius of 20 when unsuppressed
                sound_radius = ((self.chambered_bullet.mass * muzzle_velocity ** 2) /
                                (2 * (pi * (self.chambered_bullet.diameter / 2) ** 2)
                                 * self.barrel_length) / 181039271) * 20 * self.sound_modifier

                # if the sound radius of the fired round is not already in the list, appends it to the list for
                sound_radius_list.append(sound_radius)

                # calculates AP modifier based on weight and weapon type
                if self.gun_type == 'pistol':
                    weight_handling_modifier = 0.75 + 0.25 * (self.parent.weight + total_weight)

                else:
                    weight_handling_modifier = 0.85 + 0.15 * ((self.parent.weight + total_weight) / 4)

                # gives projectile spread in MoA
                spread_diameter = \
                    self.chambered_bullet.spread_modifier * self.spread_modifier * \
                    dist_yards * attacker.fighter.ranged_accuracy * min((5 / self.condition_accuracy), 2) \
                    * proficiency * skill_range_modifier * weight_handling_modifier

                # bullet spread hit location coordinates
                radius = (spread_diameter * 0.523) * sqrt(uniform(0, 1))
                spread_x = radius * cos(spread_angle)
                spread_y = radius * sin(spread_angle)

                # Pejsa's projectile drop formula

                retardation_coefficient = \
                    self.chambered_bullet.ballistic_coefficient * 246 * muzzle_velocity ** 0.45

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

                for i in range(self.chambered_bullet.projectile_no):

                    # checks if hit
                    hit_location_x += spread_x
                    hit_location_y += (recoil_penalty * dist_yards) + projectile_path + spread_y

                    if not hit_location_x > (target.bodyparts[part_index].width * 0.3937 / 2) or hit_location_x < 0 or \
                            hit_location_y > (target.bodyparts[part_index].height * 0.3937 / 2) or hit_location_y < 0:
                        # does damage to given bodypart
                        target.bodyparts[part_index].deal_damage_gun(
                            diameter_bullet=self.chambered_bullet.diameter,
                            mass_bullet=self.chambered_bullet.mass,
                            velocity_bullet=velocity_at_distance,
                            drag_bullet=self.chambered_bullet.drag_coefficient,
                            config_bullet=self.chambered_bullet.proj_config,
                            bullet_length=self.chambered_bullet.bullet_length,
                            bullet_expands=self.chambered_bullet.bullet_expands,
                            bullet_yaws=self.chambered_bullet.bullet_yaws,
                            bullet_fragments=self.chambered_bullet.bullet_fragments,
                            bullet_max_expansion=self.chambered_bullet.max_expansion,
                            bullet_expansion_velocity=self.chambered_bullet.max_expansion_velocity,
                            attacker=attacker
                        )

                    # miss
                    else:
                        if attacker.player:
                            self.engine.message_log.add_message("Your shot misses.", colour.YELLOW)

                        else:
                            self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.LIGHT_BLUE)

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
                        bullet_momentum = self.chambered_bullet.mass * 0.000142857 * muzzle_velocity
                        gas_momentum = \
                            self.chambered_bullet.charge_mass * 0.000142857 * muzzle_velocity / 2
                        momentum_jet = \
                            self.chambered_bullet.charge_mass * 0.000142857 * gas_velocity * \
                            ((1 - muzzle_break) ** (1 / sqrt(e)))
                        self.momentum_gun = bullet_momentum + gas_momentum + momentum_jet

                    # potentailly better equation found in ADA561571 equation 7 - 8
                    velocity_gun = (self.momentum_gun / total_weight)
                    # recoil spread (MoA) based assuming M4 recoil spread is 2 MoA with stock, handguard,
                    # and pistol grip reducing felt recoil by 70% shooting 55gr bullets.
                    # arbitrary but almost impossible to calculate actual muzzle rise for all guns and conifgurations
                    recoil_spread = \
                        velocity_gun * self.felt_recoil * attacker.fighter.felt_recoil * 0.0019634 * proficiency

                    recoil_spread_list.append(recoil_spread)

                    rounds_per_quarter_sec = \
                        round((self.fire_modes[self.current_fire_mode]['fire rate'] /
                               60 * self.fire_rate_modifier) * 0.25)

                    if rounds_fired > rounds_per_quarter_sec:
                        rounds = recoil_spread_list[-rounds_per_quarter_sec:]
                        recoil_penalty = sum(rounds)
                    else:
                        recoil_penalty = sum(recoil_spread_list)

            else:
                self.shot_sound_activation(sound_radius=max(sound_radius_list), attacker=attacker)
                if attacker.player:
                    self.engine.message_log.add_message(f"Out of ammo.", colour.RED)
                break

        self.shot_sound_activation(sound_radius=max(sound_radius_list), attacker=attacker)

    def shot_sound_activation(self, sound_radius: float, attacker: Actor) -> None:
        # shot sound alert enemies in the vicinity of where the shot was fired from
        # only needs to be computed once for the 'loudest' shot fired

        for x in set(self.gamemap.actors) - {attacker}:

            if not attacker.fighter.responds_to_sound:
                continue

            dx = x.x - attacker.x
            dy = x.y - attacker.y
            distance = max(abs(dx), abs(dy))  # Chebyshev distance.

            if distance <= sound_radius:
                try:
                    path = x.ai.get_path_to(attacker.x, attacker.y)
                except AttributeError:
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

    # TODO - make it so that AI can reload from clips
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
                    actions.AddToInventory(item=self.chambered_bullet.parent, amount=1, entity=inventory.parent)
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
                self.engine.message_log.add_message(f"{inventory.parent.name}: cannot load from stripper clip",
                                                    colour.RED)

        elif inventory.parent.player:
            self.engine.message_log.add_message(f"{inventory.parent.name}: cannot load from stripper clip",
                                                colour.RED)

        return False

    def chamber_round(self):
        return NotImplementedError


class Wearable(Usable):
    def __init__(self,
                 protection_ballistic: int,  # equivalent to inches of mild steel
                 armour_coverage: int,  # chance that when an attack occurs, the armour will be hit
                 protection_physical: int,
                 fits_bodypart_type: str,
                 small_mag_slots: int,
                 medium_mag_slots: int,
                 large_mag_slots: int,
                 equip_ap_cost: int,
                 ):

        self.protection_ballistic = protection_ballistic
        self.armour_coverage = armour_coverage
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
                 compatible_magazine_type: str,
                 compatible_bullet_type: str,
                 velocity_modifier: float,
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
                 spread_modifier: float,  # MoA / 100
                 manual_action: bool = False,
                 action_cycle_ap_cost: int = 100,
                 condition_accuracy: int = 5,
                 condition_function: int = 5,
                 firing_ap_cost: int = 25,  # additional AP cost for firing
                 muzzle_break_efficiency: float = 0.0,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
                 chambered_bullet: Optional[Bullet] = None,
                 loaded_magazine: Optional[DetachableMagazine] = None,
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
            spread_modifier=spread_modifier,
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
            pdw_stock=pdw_stock
        )

    def load_gun(self,  user: Actor, magazine: DetachableMagazine):
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
                if self.loaded_magazine.magazine[-1].bullet_type in \
                        self.compatible_bullet_type:
                    self.chambered_bullet = self.loaded_magazine.magazine.pop()
                else:
                    self.engine.message_log.add_message(f"{inventory.parent.name} failed to chamber a new round",
                                                        colour.RED)

    def get_attack_action(self, distance: int, entity: Actor, targeted_actor: Actor,
                          targeted_bodypart: Optional[Bodypart]):
        return actions.GunMagFedAttack(distance=distance, entity=entity, targeted_actor=targeted_actor,
                                       gun=self, targeted_bodypart=targeted_bodypart).handle_action()

class GunIntegratedMag(Gun, Magazine):
    def __init__(self,
                 parts: Parts,
                 gun_type: str,
                 velocity_modifier: float,
                 ap_to_equip: int,
                 fire_modes: dict,
                 current_fire_mode: str,
                 compatible_bullet_type: str,
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
                 spread_modifier: float,  # MoA / 100
                 manual_action: bool = False,
                 action_cycle_ap_cost: int = 100,
                 condition_accuracy: int = 5,
                 condition_function: int = 5,
                 firing_ap_cost: int = 25,  # additional AP cost for firing
                 muzzle_break_efficiency: float = 0.0,
                 fire_rate_modifier: float = 1.0,
                 load_time_modifier: float = 1.0,
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
            spread_modifier=spread_modifier,
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
            pdw_stock=pdw_stock
        )

    def chamber_round(self):
        if len(self.magazine) > 0:
            self.chambered_bullet = self.magazine.pop()

    def get_attack_action(self, distance: int, entity: Actor, targeted_actor: Actor,
                          targeted_bodypart: Optional[Bodypart]):
        return actions.GunIntegratedMagAttack(distance=distance, entity=entity, targeted_actor=targeted_actor,
                                              gun=self, targeted_bodypart=targeted_bodypart).handle_action()

    def loading_ap(self):

        ap_cost = 0

        entity = self.parent
        inventory = entity.parent

        proficiency = 1.0

        if not self.keep_round_chambered and self.chambered_bullet is not None:
            if isinstance(inventory, components.inventory.Inventory):
                actions.AddToInventory(item=self.chambered_bullet.parent, amount=1, entity=inventory.parent)

                if inventory.parent.player:
                    if self.gun_type == 'pistol':
                        proficiency = inventory.parent.fighter.skill_pistol_proficiency
                    elif self.gun_type == 'pdw':
                        proficiency = inventory.parent.fighter.skill_smg_proficiency
                    elif self.gun_type == 'rifle':
                        proficiency = inventory.parent.fighter.skill_rifle_proficiency
                    elif self.gun_type == 'bolt action':
                        proficiency = inventory.parent.fighter.skill_bolt_action_proficiency

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
