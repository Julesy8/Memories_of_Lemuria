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

strength_tissue = 1000000
density_tissue = 1040
#armour_protection = 0.

for bullet in bullet_list:

    print('----------------------------')
    print(bullet.name)

    for armour_protection in arange(0, 1, 0.01):

        diameter_bullet = bullet.usable_properties.diameter * 25.4
        velocity_bullet = bullet.usable_properties.velocity * 0.3048
        mass_bullet = bullet.usable_properties.mass * 0.0647989
        drag_bullet = bullet.usable_properties.drag_coefficient
        config_bullet = bullet.usable_properties.proj_config

        residual_velocity = 0

        bl_mild_steel = sqrt(((bullet.usable_properties.diameter ** 3) / bullet.usable_properties.mass) *
                                  ((armour_protection / (
                                              9.35 * 10 ** -9 * bullet.usable_properties.diameter)) ** 1.25))
        try:
            residual_velocity = sqrt((bullet.usable_properties.velocity ** 2) - (bl_mild_steel ** 2))
        except ValueError:
            pass

        # strain_prop = (diameter_bullet ** (1.0 / 3)) * sqrt(strength_tissue / density_tissue)
        #
        # pen_depth = log(((velocity_bullet / strain_prop) ** 2 + 1)) * \
        #             (mass_bullet / (pi * ((0.5 * (diameter_bullet / 10)) ** 2)
        #                             * (density_tissue / 1000) * drag_bullet))
        #
        # wound_mass = round(pi * (0.5 * ((diameter_bullet / 10) ** 2)) * pen_depth *
        #                    (density_tissue / 1000) * config_bullet)

        print('bullet residual velocity:', armour_protection,  residual_velocity)

        if residual_velocity == 0:
            break

        # print('wound penetration depth:', pen_depth)
        # print('wound mass:', wound_mass)

