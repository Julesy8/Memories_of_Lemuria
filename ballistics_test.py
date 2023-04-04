from components.weapons.bullets import bullet_list
from math import sqrt, log, pi
from numpy import arange

"""
Body armour standards:

VPAM 1 - 0.13 inches mild steel - 22 LR
VPAM 2 - 0.16 - 123 gr 9mm
VPAM 3 - 0.2 - 9mm +P
VPAM 4 - 0.28 - 357 / 44 mag
VPAM 5 - 0.3 - 357 +P 
VPAM 6 - 0.56 - 7.62x39
VPAM 7 - 0.83 5.56/7.62x51
VPAM 10 - 0.93 7.62x54r
"""
#
# strength_tissue = 1000000
# density_tissue = 1040
# armour_protection = 0
#
# for bullet in bullet_list:
#
#     print('----------------------------')
#     print(bullet.name)
#
#     # for armour_protection in arange(0, 1, 0.01):
#
#     diameter_bullet = bullet.usable_properties.diameter * 25.4
#     velocity_bullet = bullet.usable_properties.velocity * 0.3048
#     mass_bullet = bullet.usable_properties.mass * 0.0647989
#     drag_bullet = bullet.usable_properties.drag_coefficient
#     config_bullet = bullet.usable_properties.proj_config
#
#     bl_mild_steel = sqrt(((bullet.usable_properties.diameter ** 3) / bullet.usable_properties.mass) *
#                          ((armour_protection / (
#                                  9.35 * 10 ** -9 * bullet.usable_properties.diameter)) ** 1.25))
#
#     try:
#         velocity_bullet = sqrt((bullet.usable_properties.velocity ** 2) - (bl_mild_steel ** 2)) * 0.3048
#     except ValueError:
#         velocity_bullet = 0
#         pass
#
#     strain_prop = (diameter_bullet ** (1.0 / 3)) * sqrt(strength_tissue / density_tissue)
#
#     pen_depth = log(((velocity_bullet / strain_prop) ** 2 + 1)) * \
#                 (mass_bullet / (pi * ((0.5 * (diameter_bullet / 10)) ** 2)
#                                 * (density_tissue / 1000) * drag_bullet))
#
#     depth_part = 20
#
#     if pen_depth > depth_part:
#         pen_depth = depth_part
#
#     wound_mass = round(pi * (0.5 * ((diameter_bullet / 10) ** 2)) * pen_depth *
#                        (density_tissue / 1000) * config_bullet * velocity_bullet)
#
#     print('bullet residual velocity:', armour_protection, velocity_bullet * 3.28084)
#
#     print('wound penetration depth:', pen_depth)
#     print('wound mass:', wound_mass)

# fragmentation damage

import numpy as np
from random import uniform
from math import asin, sin


def yaw_depth_calc():

    projectile_config = 1
    bullet_length = 1  # inches
    velocity = 1  # fps

    yaw_depth = (0.28 / projectile_config) * (2600 / velocity) * (2.26 / bullet_length) * 12 * uniform(0.3, 1.3)

    print(yaw_depth)


def frag_wound_dimensions():

    bullet_mass = 1  # grains
    velocity = 1  # fps

    # proportional to kinetic energy of the projectile
    multiplier = ((0.5 * bullet_mass * velocity ** 2) / 185900000)

    wound_len = 11.72 * multiplier
    wound_radius = 2.77 * multiplier


def frag_wound_volume():
    wound_len_in_body = 11.72

    wound_len = 11.72
    wound_width = 2.77

    vol = 0

    # the entirety of the wound is contained within the body
    if wound_len_in_body == wound_len:
        vol = 1.3333 * np.pi * (wound_len / 2) * wound_width ** 2

    # more than half the wound is contained within the body
    elif wound_len_in_body > (wound_len / 2):
        vol = 1.3333 * np.pi * (wound_len / 2) * wound_width ** 2
        vol -= 0.6666 * np.pi * (wound_len - wound_len_in_body) * wound_width ** 2

    # less than half the wound is contained within the body
    else:
        vol = 0.6666 * np.pi * wound_len_in_body * wound_width ** 2

    # this is an arbitrary representation of bullet fragmentation damage. Bullet fragmentation wounds cannot be
    # accurately modeled.
    damage = vol * 0.26548

    print(damage)


def tumble_wound():

    bullet_mass = 55  # grains
    velocity = 2600  # fps

    bullet_length = 2.26

    chord = bullet_length * 1.12282  # inches
    diameter = .223  # inches

    bearing_len = bullet_length - chord # inches

    radius = diameter * 6

    theta = 2 * asin(chord/(diameter * 12))

    area_ogive = 0.5 * (theta - sin(theta)) * radius ** 2

    # bullet area should probably be pre-calculated
    bullet_area = (area_ogive + (bearing_len * diameter)) * 6.4516  # converted to cm

    # proportional to kinetic energy of the projectile
    multiplier = ((0.5 * bullet_mass * velocity ** 2) / 185900000)

    wound_len = 11.72 * multiplier

    part_depth = 20

    yaw_depth = 1

    if (wound_len + yaw_depth) > part_depth:
        wound_len = part_depth - yaw_depth

    # this is not a realistic representation of yaw wounding, but its better to make an arbitrary representation than
    # leaving it out entirely as this would cause rifle bullets to be woefully underpowered. Bullet yaw wounds cannot
    # be accurately modeled.
    vol_wound_channel = wound_len * bullet_area * 0.3

    print(vol_wound_channel)

frag_wound_volume()
tumble_wound()

sound_radius = (((mass * velocity ** 2) / (2 * ((pi * diameter / 2) ** 2) * barrel_length)) / 181039271) * 20

