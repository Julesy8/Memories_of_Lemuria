from __future__ import annotations

from copy import deepcopy
from math import sin, cos, asin, floor, sqrt, pi, dist
from random import choices, uniform, choice
from random import randint
from typing import Optional, TYPE_CHECKING

from numpy import log
# import matplotlib.pyplot as plt
from shapely.geometry import LineString

import colour
from components.consumables import RecipeUnlock
from components.datapacks import datapackdict
from entity import Actor, Item
from render_order import RenderOrder

if TYPE_CHECKING:
    from engine import Engine
    from components.consumables import Wearable


def rotate(origin_x, origin_y, point_x, point_y, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """

    qx = origin_x + cos(angle) * (point_x - origin_x) - sin(angle) * (point_y - origin_y)
    qy = origin_y + sin(angle) * (point_x - origin_x) + cos(angle) * (point_y - origin_y)
    return qx, qy

# TODO - more body parts i.e. hands, feet, chest and abdomen.
#  Chest and abdomen solves problem of aiming for middle of torso


class Bodypart:
    parent: Actor

    def __init__(self,
                 hp: int,
                 protection_ballistic: float,
                 protection_physical: int,
                 connected_to: dict,  # part: (offset from centre to centre X, offset from centre to centre Y)
                 name: str,
                 width: int,  # cm
                 height: int,  # cm
                 depth: int,  # tissue depth (cm)
                 part_type: Optional[str],
                 # tissue strength and density probably don't need to be variables
                 strength_tissue: int = 1000000,  # tissue tensile strength, newtons per square metre
                 density_tissue: int = 1040,  # density of tissue, kg/m^3
                 vital: bool = False,
                 ):

        self.max_hp = hp
        self.hp_last_turn = hp
        self._hp = hp
        self.total_damage_taken = 0  # damage taken below 0 HP
        self._protection_ballistic = protection_ballistic
        self._protection_physical = protection_physical
        self.connected_to = connected_to
        self.width = width
        self.height = height
        self.depth = depth
        self.vital = vital  # whether when the body part gets destroyed, the entity should die
        self.strength_tissue = strength_tissue
        self.density_tissue = density_tissue
        self.show_splatter_message = False  # whether a splatter should show for this limb
        self.splatter_message_shown = False  # whether a splatter message has been shown for this limb. Can be set to
        self.splatter_message = None
        self.equipped: Optional[Wearable] = None  # equipped armour item
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
    def protection_ballistic(self) -> float:
        return self._protection_ballistic

    @protection_ballistic.setter
    def protection_ballistic(self, value):
        self._protection_ballistic = value

    @property
    def protection_physical(self) -> int:
        return self._protection_physical

    @protection_physical.setter
    def protection_physical(self, value):
        self._protection_physical = value

    @hp.setter
    def hp(self, value: int) -> None:

        show_cripple_message = True

        entity_name = self.parent.name.replace(' remains', '')

        # sets splatter message
        if value <= 0 and not self.parent.player and not self.splatter_message_shown:
            self.total_damage_taken += abs(value)
            thickness = min(self.width, self.height)
            limb_size = thickness * self.depth

            if self.total_damage_taken / limb_size >= 0.1:
                show_cripple_message = False
                self.show_splatter_message = True
                self.splatter_message = choice([f"The {entity_name}'s {self.name} is split open",
                                                f"The {entity_name}'s {self.name} splits into gore",
                                                ])

            if self.total_damage_taken / limb_size >= 0.2:
                self.splatter_message = choice([f"The {entity_name}'s {self.name} is blown into pieces",
                                                f"The {entity_name}'s {self.name} is mangled beyond recognition",
                                                f"Bits of {entity_name}'s {self.name} splatter on the floor",
                                                ])

            elif self.total_damage_taken / limb_size >= 0.3:
                self.splatter_message = choice([f"The {entity_name}'s {self.name} explodes into gore",
                                                f"The {entity_name}'s {self.name} is destroyed in a bloody mess",
                                                f"The {entity_name}'s {self.name} erupts into a fine red mist",
                                                ])

        self._hp = max(0, min(value, self.max_hp))

        if self._hp <= self.max_hp * 0.70 and self.parent.bleeds:
            self.engine.game_map.tiles[self.parent.x, self.parent.y][3][2] = colour.RED

        if self._hp == 0 and self.parent.ai:

            if self.vital:
                self.die()

        elif self._hp <= self.max_hp * (1 / 4) and self.functional:
            self.cripple()

            if self.parent.player:
                self.engine.message_log.add_message(f"{entity_name}'s {self.name} is crippled", fg=colour.RED)

            else:
                if show_cripple_message:
                    self.engine.message_log.add_message(f"The {entity_name}'s {self.name} is crippled!",
                                                        fg=colour.GREEN)

                # causes AI to flee
                if self.vital:
                    if self.parent.fighter.fears_death and not self.parent.fighter.has_fled_death:
                        self.parent.fighter.fleeing_turns = 5
                        self.parent.fighter.has_fled_death = True

                        # changes fight style to less accurate and more frantic
                        try:
                            self.parent.fighter.attack_style_cqc()

                        except AttributeError:
                            pass

    def die(self) -> None:

        # drops random item from list and held item
        if len(self.parent.fighter.item_drops.keys()) > 0:
            drops = list(self.parent.fighter.item_drops.keys())
            drop_weight = list(self.parent.fighter.item_drops.values())

            # chooses item to drop from list
            item_drop = deepcopy(choices(population=drops, weights=drop_weight, k=1)[0])

            # gives PDA datapack properties
            if isinstance(item_drop, Item):
                if item_drop.name == 'PDA':

                    data_pack_pop = []
                    data_pack_weight = []

                    for i in datapackdict[self.engine.current_level]:
                        data_pack_pop.append(i[0])
                        data_pack_weight.append(i[1])

                    item_drop.usable_properties = RecipeUnlock(choices(population=data_pack_pop,
                                                                       weights=data_pack_weight, k=1)[0])

            if item_drop is not None:
                item_drop.usable_properties.parent = item_drop
                item_drop.place(x=self.parent.x, y=self.parent.y, gamemap=self.engine.game_map)

        # drops held weapon
        if self.parent.inventory.held is not None:
            self.parent.inventory.held.place(x=self.parent.x, y=self.parent.y, gamemap=self.engine.game_map)
            self.parent.inventory.held = None

        if self.parent.name not in self.engine.bestiary.keys():
            if not self.parent.fighter.description == '':
                self.engine.bestiary[self.parent.name] = self.parent.fighter.description

        self.parent.ai = None
        self.parent.char = '%'
        self.parent.fg_colour = colour.WHITE
        self.parent.render_order = RenderOrder.CORPSE
        self.parent.blocks_movement = False

        # prints death message
        if self.parent.player:
            self.engine.players.remove(self.parent)
            if len(self.engine.players) > 0:
                self.engine.player = self.engine.players[0]
                return self.engine.message_log.add_message(f"{self.parent.name} is dead!", colour.LIGHT_MAGENTA)

        self.parent.name = f"{self.parent.name} remains"

    def deal_damage_melee(self, meat_damage: int, armour_damage: int, attacker: Actor):

        target_name = self.parent.name.replace(' remains', '')

        armour_protection = self.protection_physical

        if self.equipped:
            armour_protection = self.equipped.protection_physical
            # # whether attack hits armour or not
            # if self.equipped.armour_coverage < 100:
            #     # random chance whether attack hits armour based on armour coverage
            #     if choices(population=(True, False),
            #                weights=(self.equipped.armour_coverage,
            #                         100 - self.equipped.armour_coverage))[0]:
            #         armour_protection = self.equipped.protection_physical
            # else:
            #     # armour covers 100% of part
            #     armour_protection = self.equipped.protection_physical

        if armour_damage < self.protection_physical + armour_protection:
            damage = 0
        elif self.protection_physical + armour_protection == 0:
            damage = meat_damage
        else:
            damage = meat_damage - floor(((armour_protection + self.protection_physical) / armour_damage)) * meat_damage

        if damage > 0:
            self.hp -= damage

        # hit, no damage dealt
        else:
            if attacker.player:
                self.engine.message_log.add_message(f"{target_name}'s attack deals no damage.", colour.YELLOW)
            else:
                self.engine.message_log.add_message(f"{attacker.name}'s attack deals no damage.", colour.LIGHT_BLUE)

    def check_if_hit_connected(self, diameter_bullet: float, mass_bullet: int, velocity_bullet: int,
                               drag_bullet: float, config_bullet: float, bullet_length: float, bullet_expands: bool,
                               bullet_yaws: bool, bullet_fragments: bool, bullet_max_expansion: float,
                               bullet_expansion_velocity: int, attacker: Actor, hit_location_x: float,
                               hit_location_y: float):

        # checks if each connected part hit
        for part_name, location_xy in self.connected_to.items():
            for part in self.parent.bodyparts:
                if part.name == part_name:
                    part.deal_damage_gun(diameter_bullet=diameter_bullet,
                                         mass_bullet=mass_bullet,
                                         velocity_bullet=velocity_bullet,
                                         drag_bullet=drag_bullet,
                                         config_bullet=config_bullet,
                                         bullet_length=bullet_length,
                                         bullet_expands=bullet_expands,
                                         bullet_yaws=bullet_yaws,
                                         bullet_fragments=bullet_fragments,
                                         bullet_max_expansion=bullet_max_expansion,
                                         bullet_expansion_velocity=bullet_expansion_velocity,
                                         attacker=attacker,
                                         hit_location_x=hit_location_x + (location_xy[0] * 0.3937),
                                         hit_location_y=hit_location_y + (location_xy[1] * 0.3937),
                                         connected_check=True
                                         )

    def deal_damage_gun(self, diameter_bullet: float, mass_bullet: int, velocity_bullet: int,
                        drag_bullet: float, config_bullet: float, bullet_length: float, bullet_expands: bool,
                        bullet_yaws: bool, bullet_fragments: bool, bullet_max_expansion: float,
                        bullet_expansion_velocity: int, attacker: Actor, hit_location_x: float,
                        hit_location_y: float, connected_check: bool = False):

        # source for amour penetration and wound mass : Quantitative Ammunition Selection

        target_name = self.parent.name.replace(' remains', '')

        if abs(hit_location_y) > (self.height * 0.3937 / 2):

            # checks if hit a connected bodypart
            if len(self.connected_to.keys()) != 0 and not connected_check:
                self.check_if_hit_connected(diameter_bullet=diameter_bullet,
                                            mass_bullet=mass_bullet,
                                            velocity_bullet=velocity_bullet,
                                            drag_bullet=drag_bullet,
                                            config_bullet=config_bullet,
                                            bullet_length=bullet_length,
                                            bullet_expands=bullet_expands,
                                            bullet_yaws=bullet_yaws,
                                            bullet_fragments=bullet_fragments,
                                            bullet_max_expansion=bullet_max_expansion,
                                            bullet_expansion_velocity=bullet_expansion_velocity,
                                            attacker=attacker,
                                            hit_location_x=hit_location_x,
                                            hit_location_y=hit_location_y
                                            )
            else:
                if attacker.player:
                    self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.YELLOW)

                else:
                    self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.LIGHT_BLUE)
                return

        # metres to inches
        entity_x_inches = self.parent.x * 39.3701
        entity_y_inches = self.parent.y * 39.3701

        width_inches = self.width * 0.3937
        depth_inches = self.depth * 0.3937

        attacker_x_inches = attacker.x * 39.3701 + 1.0  # adding 1 inch prevents division by 0 error
        attacker_y_inches = attacker.y * 39.3701 + 1.0

        # https://www.mathworks.com/matlabcentral/answers/484422-how-to-find-the-coordinates-of-a-point-perpendicular-to-a-line-knowing-the-distance

        slope_gunshot = (entity_y_inches - attacker_y_inches) / (entity_x_inches - attacker_x_inches)

        perp_slope = -1 / slope_gunshot

        hit_cardinal_x = entity_x_inches + (hit_location_x * sqrt(1 / (1 + perp_slope ** 2)))
        hit_cardinal_y = entity_y_inches + (perp_slope * hit_location_x * sqrt(1 / (1 + perp_slope ** 2)))

        diameter_bullet_metric = diameter_bullet * 25.4  # millimitres
        mass_bullet_metric = mass_bullet * 0.0647989  # grams
        velocity_bullet_metric = velocity_bullet * 0.3048  # metres per second

        # v = ventrtal (front), d = dorsal (back), r = right, l = left
        # o = origin, p = point

        rotation_angle = self.parent.orientation
        d_xo, d_yo = rotate(entity_x_inches,
                            entity_y_inches,
                            (entity_x_inches + (depth_inches * 0.5)),
                            entity_y_inches - (width_inches * 0.5),
                            rotation_angle)
        d_xp, d_yp = rotate(entity_x_inches,
                            entity_y_inches,
                            (entity_x_inches + (depth_inches * 0.5)),
                            (entity_y_inches + (width_inches * 0.5)),
                            rotation_angle)

        v_xo, v_yo = rotate(entity_x_inches,
                            entity_y_inches,
                            entity_x_inches - (depth_inches * 0.5),
                            entity_y_inches - (width_inches * 0.5),
                            rotation_angle)
        v_xp, v_yp = rotate(entity_x_inches,
                            entity_y_inches,
                            entity_x_inches - (depth_inches * 0.5),
                            (entity_y_inches + (width_inches * 0.5)),
                            rotation_angle)

        r_xo, r_yo = rotate(entity_x_inches,
                            entity_y_inches,
                            entity_x_inches - (depth_inches * 0.5),
                            entity_y_inches - (width_inches * 0.5),
                            rotation_angle)
        r_xp, r_yp = rotate(entity_x_inches,
                            entity_y_inches,
                            (entity_x_inches + (depth_inches * 0.5)),
                            entity_y_inches - (width_inches * 0.5),
                            rotation_angle)

        l_xo, l_yo = rotate(entity_x_inches,
                            entity_y_inches,
                            entity_x_inches - (depth_inches * 0.5),
                            entity_y_inches + (width_inches * 0.5),
                            rotation_angle)
        l_xp, l_yp = rotate(entity_x_inches,
                            entity_y_inches,
                            (entity_x_inches + (depth_inches * 0.5)),
                            entity_y_inches + (width_inches * 0.5),
                            rotation_angle)

        # determines which face of the body part was first hit by the bullet to determine the armour coverage

        line_bulletpath = LineString([(attacker_x_inches, attacker_y_inches), (entity_x_inches, entity_y_inches)])
        line_v = LineString([(v_xo, v_yo), (v_xp, v_yp)])
        line_d = LineString([(d_xo, d_yo), (d_xp, d_yp)])
        line_l = LineString([(l_xo, l_yo), (l_xp, l_yp)])
        line_r = LineString([(r_xo, r_yo), (r_xp, r_yp)])

        v_int_pt = line_v.crosses(line_bulletpath)
        d_int_pt = line_d.crosses(line_bulletpath)
        l_int_pt = line_l.crosses(line_bulletpath)
        r_int_pt = line_r.crosses(line_bulletpath)

        # plt.figure(num=0, dpi=120)
        # plt.plot([d_xo, d_xp], [d_yo, d_yp], c='red')
        # plt.plot([v_xo, v_xp], [v_yo, v_yp], c='blue')
        # plt.plot([l_xo, l_xp], [l_yo, l_yp], c='green')
        # plt.plot([r_xo, r_xp], [r_yo, r_yp], c='yellow')
        # plt.plot([attacker_x_inches, hit_cardinal_x], [attacker_y_inches, hit_cardinal_y], c='pink')
        # plt.plot([attacker_x_inches, entity_x_inches], [attacker_y_inches, entity_y_inches], c='purple')
        # plt.plot([attacker_x_inches, entity_x_inches], [attacker_y_inches, entity_y_inches], c='red')
        # plt.gca().invert_yaxis()
        # plt.show()

        hit = False

        armour_coverage = 0

        if v_int_pt:
            if self.equipped is not None:
                armour_coverage = self.equipped.coverage_v
            hit = True

        if d_int_pt:
            if self.equipped is not None:
                armour_coverage = self.equipped.coverage_d
            hit = True

        if l_int_pt:
            if self.equipped is not None:
                armour_coverage = self.equipped.coverage_l
            hit = True

        if r_int_pt:
            if self.equipped is not None:
                armour_coverage = self.equipped.coverage_r
            hit = True

        # does not intersect with any body surface, miss
        if not hit:
            if not connected_check and len(self.connected_to.keys()) != 0:
                self.check_if_hit_connected(diameter_bullet=diameter_bullet,
                                            mass_bullet=mass_bullet,
                                            velocity_bullet=velocity_bullet,
                                            drag_bullet=drag_bullet,
                                            config_bullet=config_bullet,
                                            bullet_length=bullet_length,
                                            bullet_expands=bullet_expands,
                                            bullet_yaws=bullet_yaws,
                                            bullet_fragments=bullet_fragments,
                                            bullet_max_expansion=bullet_max_expansion,
                                            bullet_expansion_velocity=bullet_expansion_velocity,
                                            attacker=attacker,
                                            hit_location_x=hit_location_x,
                                            hit_location_y=hit_location_y
                                            )
            else:
                if attacker.player:
                    self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.YELLOW)

                else:
                    self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.LIGHT_BLUE)
                return

        # creates a point past the body and checks if and where line intersects with body surfaces
        slope_cardinal = (attacker_y_inches - hit_cardinal_y) / (attacker_x_inches - hit_cardinal_x)

        multiplier = 1.0

        if attacker_x_inches > hit_cardinal_x:
            multiplier = -1.0

        y_int = hit_cardinal_y - (slope_cardinal * attacker_x_inches)
        y_extended = slope_cardinal * (attacker_x_inches + (2 * attacker_x_inches * multiplier)) + y_int
        x_extended = hit_cardinal_x + (2 * attacker_x_inches * multiplier)

        line_bulletpath = LineString(
            [(attacker_x_inches, attacker_y_inches), (x_extended, y_extended)])

        v_int_pt = line_v.intersection(line_bulletpath, grid_size=0.1)
        d_int_pt = line_d.intersection(line_bulletpath, grid_size=0.1)
        l_int_pt = line_l.intersection(line_bulletpath, grid_size=0.1)
        r_int_pt = line_r.intersection(line_bulletpath, grid_size=0.1)

        intersects = []

        if hasattr(v_int_pt, 'x'):
            intersects.append((v_int_pt.x, v_int_pt.y))

        if hasattr(d_int_pt, 'x'):
            intersects.append((d_int_pt.x, d_int_pt.y))

        if hasattr(l_int_pt, 'x'):
            intersects.append((l_int_pt.x, l_int_pt.y))

        if hasattr(r_int_pt, 'x'):
            intersects.append((r_int_pt.x, r_int_pt.y))

        # calculates the maximum distance through the body the bullet can travel in cm
        if len(intersects) >= 2:
            wound_path_len = dist(intersects[0], intersects[1]) * 2.54  # converts to cm
        else:
            if attacker.player:
                self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.YELLOW)

            else:
                self.engine.message_log.add_message(f"{attacker.name}'s shot misses.", colour.LIGHT_BLUE)
            return

        armour_protection = 0

        if self.equipped:
            # whether attack hits armour or not
            if armour_coverage > 0:
                if not (hit_location_y * -1) + (self.height * 0.3937 / 2) > (self.height * 0.3937 * armour_coverage):
                    armour_protection += self.equipped.protection_ballistic

        if armour_protection > 0:

            ballistic_limit = sqrt(((diameter_bullet ** 3) / mass_bullet) *
                                   ((armour_protection / (9.35 * 10 ** -9 * diameter_bullet)) ** 1.25))
            try:
                residual_velocity = sqrt((velocity_bullet ** 2) - (ballistic_limit ** 2))
            except ValueError:
                residual_velocity = 0
            velocity_bullet = residual_velocity
            velocity_bullet_metric = residual_velocity * 0.3048

        if velocity_bullet_metric > 0:

            wound_mass = 0

            # uniaxial strain proportionality
            strain_prop = (diameter_bullet_metric ** (1.0 / 3)) * sqrt(self.strength_tissue / self.density_tissue)

            # whether or not bullet has expanded i.e. in the case of a hollow point
            bullet_expanded = False

            # changes damage based on bullet expansion
            if bullet_expands:

                bullet_expanded = True

                # bullet expansion changes the drag and bullet config to that of an expanded hollow point
                drag_bullet = 0.441511
                config_bullet = 0.819152

                # bullet begins expansion at 1 / bullet_max_expansion times velocity required for maximum expansion
                if velocity_bullet > bullet_expansion_velocity * (1 / bullet_max_expansion):

                    # expansion increases linearly with velocity between min and max expansion velocity
                    diameter_bullet_metric *= bullet_max_expansion * (velocity_bullet / bullet_expansion_velocity)

                elif velocity_bullet >= bullet_expansion_velocity:
                    diameter_bullet_metric *= bullet_max_expansion

            pen_depth = (
                    log(((velocity_bullet_metric / strain_prop) ** 2 + 1)) *
                    (mass_bullet_metric / (pi * ((0.5 * (diameter_bullet_metric / 10)) ** 2)
                                           * (self.density_tissue / 1000) * drag_bullet)))

            if pen_depth > wound_path_len:
                pen_depth = wound_path_len

            # bullet expands over 5 cm distance, so only calculates wound channel mass of area that it passed through
            # while expanded
            if bullet_expanded and pen_depth > 5:
                # wound channel mass pre expansion
                wound_mass += round(pi * (0.5 * ((diameter_bullet_metric / 10) ** 2)) * 5 *
                                    (self.density_tissue / 1000) * config_bullet)
                pen_depth -= 5

            wound_mass += round(pi * (0.5 * ((diameter_bullet_metric / 10) ** 2)) * pen_depth *
                                (self.density_tissue / 1000) * config_bullet)

            # print('wound mass from channel', wound_mass)

            if not bullet_expanded and bullet_yaws:

                # arbitrary calculation based on 5.56 bullet yaw
                # depth at which bullet yaws in body part
                yaw_depth = (0.28 / config_bullet) * (2600 / velocity_bullet) * (0.810 / bullet_length) * 12 * \
                            uniform(0.75, 1.25)

                # print('yaw depth ', yaw_depth)

                # only proceeds if bullet yaws within the body part
                if not yaw_depth > wound_path_len:

                    # bullets will only fragment at velocities above 3000
                    # bullet fragments
                    if bullet_fragments and velocity_bullet > 3000:

                        # these are completely arbitrary
                        # proportional to kinetic energy of the projectile, based on 5.56
                        multiplier = ((mass_bullet * velocity_bullet ** 2) / 526165695) * uniform(0.75, 1.25)

                        wound_len = 11.72 * multiplier
                        wound_width = 2.77 * multiplier
                        wound_len_in_body = wound_len

                        if (wound_len + yaw_depth) > wound_path_len:
                            wound_len_in_body = wound_path_len - yaw_depth

                        # volume calculations for an ellipsoid
                        # the entirety of the wound is contained within the body
                        if wound_len_in_body == wound_len:
                            vol = 1.3333 * pi * (wound_len / 2) * wound_width ** 2

                        # more than half the wound is contained within the body
                        elif wound_len_in_body > (wound_len / 2):
                            vol = 1.3333 * pi * (wound_len / 2) * wound_width ** 2
                            vol -= 0.6666 * pi * (wound_len - wound_len_in_body) * wound_width ** 2

                        # less than half the wound is contained within the body
                        else:
                            vol = 0.6666 * pi * wound_len_in_body * wound_width ** 2

                        # this is an arbitrary representation of bullet fragmentation damage. Bullet fragmentation
                        # wounds cannot be accurately modeled.
                        wound_mass += round(vol / 4)

                        # subtracts damage that would have occurred normally without fragmentation in that length of
                        # the wound channel
                        wound_mass -= round(pi * (0.5 * ((diameter_bullet_metric / 10) ** 2)) * wound_len_in_body *
                                            (self.density_tissue / 1000) * config_bullet)

                    # bullet yaws
                    else:

                        # calculates cross sectional area of a bullet (spitzer type) based on an ogive shape
                        chord = bullet_length * 1.12282  # inches
                        bearing_len = bullet_length - chord  # inches
                        radius = diameter_bullet * 6
                        theta = 2 * asin(chord / (diameter_bullet * 12))
                        area_ogive = 0.5 * (theta - sin(theta)) * radius ** 2
                        bullet_area = (area_ogive + (bearing_len * diameter_bullet)) * 6.4516  # converted to cm
                        wound_len = 11.72 * (velocity_bullet / 2800)

                        if (wound_len + yaw_depth) > wound_path_len:
                            wound_len = wound_path_len - yaw_depth

                        # this is not a realistic representation of yaw wounding, but its better to make an arbitrary
                        # representation than leaving it out entirely as this would cause rifle bullets to be woefully
                        # underpowered. Bullet yaw wounds cannot be accurately modeled. Based on 5.56 yaw.
                        wound_mass += round(wound_len * bullet_area * 0.6)

                        # subtracts damage that would have occurred normally without yawing in that length of
                        # the wound channel
                        wound_mass -= round(pi * (0.5 * ((diameter_bullet_metric / 10) ** 2)) * wound_len *
                                            (self.density_tissue / 1000) * config_bullet)

            if wound_mass > 0:

                damage = wound_mass * 0.875

                self.hp -= damage
                if attacker.player:
                    self.engine.message_log.add_message(f"{attacker.name} shoots {target_name} in the {self.name}",
                                                        colour.GREEN)
                else:
                    self.engine.message_log.add_message(f"{attacker.name} shoots {target_name} in the {self.name}",
                                                        colour.RED)

            # hit, no damage dealt
            else:
                if attacker.player:
                    self.engine.message_log.add_message(f"{attacker.name}'s shot fails to penetrate "
                                                        f"{self.parent.name}", colour.YELLOW)
                else:
                    self.engine.message_log.add_message(f"{attacker.name}'s attack is stopped by {target_name}'s "
                                                        f"armour!", colour.LIGHT_BLUE)

        # failed to penetrate armour
        else:
            if attacker.player:
                self.engine.message_log.add_message(f"{attacker.name}'s shot fails to penetrate {target_name}",
                                                    colour.YELLOW)
            else:
                self.engine.message_log.add_message(f"{attacker.name}'s attack is stopped by {target_name}'s "
                                                    f"armour!", colour.LIGHT_BLUE)

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
        self.parent.fighter.ap_per_turn_modifier = 1.0

        if hasattr(self.parent.fighter, '_felt_recoil'):
            self.parent.fighter.felt_recoil = self.parent.fighter.felt_recoil_original


class Arm(Bodypart):
    def __init__(self,
                 hp: int,
                 protection_ballistic: float,
                 protection_physical: int,
                 connected_to: dict,
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
            protection_ballistic=protection_ballistic,
            protection_physical=protection_physical,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            width=width,
            height=height,
            connected_to=connected_to
        )

    def cripple(self) -> None:
        self.functional = False

        # entity drops their gun if right arm crippled
        if self.name == "Right Arm":
            try:

                self.parent.inventory.held.place(self.parent.x, self.parent.y, self.engine.game_map)
                message_colour = colour.GREEN

                if self.parent == self.engine.player:
                    message_colour = colour.RED

                self.engine.message_log.add_message(f"{self.parent.name} drops their {self.parent.inventory.held.name}",
                                                    message_colour)

                self.parent.inventory.held = None

            except AttributeError:
                pass

        self.parent.fighter.ranged_accuracy *= 1.2
        self.parent.fighter.melee_accuracy *= 0.8
        self.parent.fighter.action_ap_modifier *= 1.3

        if hasattr(self.parent.fighter, '_felt_recoil'):
            self.parent.fighter.felt_recoil *= 1.3


class Leg(Bodypart):
    def __init__(self,
                 hp: int,
                 protection_ballistic: float,
                 protection_physical: int,
                 connected_to: dict,
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
            protection_ballistic=protection_ballistic,
            protection_physical=protection_physical,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            width=width,
            height=height,
            connected_to=connected_to
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
                 protection_ballistic: float,
                 protection_physical: int,
                 connected_to: dict,
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
            protection_ballistic=protection_ballistic,
            protection_physical=protection_physical,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            vital=True,
            width=width,
            height=height,
            connected_to=connected_to
        )

    def cripple(self) -> None:
        # crippling the head 'knocks out' the entity for a random amount of turns
        if not self.parent == self.engine.player:
            self.functional = False

            turns_inactive = randint(3, 6)
            self.parent.fighter.turns_move_inactive = turns_inactive
            self.parent.fighter.turns_attack_inactive = turns_inactive
            self.parent.fighter.ap_per_turn_modifier = 0.7

        self.parent.fighter.action_ap_modifier *= 1.4


class Body(Bodypart):
    def __init__(self,
                 hp: int,
                 protection_ballistic: float,
                 protection_physical: int,
                 connected_to: dict,
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
            protection_ballistic=protection_ballistic,
            protection_physical=protection_physical,
            name=name,
            depth=depth,
            strength_tissue=strength_tissue,
            density_tissue=density_tissue,
            part_type=part_type,
            vital=True,
            width=width,
            height=height,
            connected_to=connected_to
        )
