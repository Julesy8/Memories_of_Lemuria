from entity import Item
from components.consumables import GunComponent
import colour

# TODO - ability to adjust zero range
# TODO - add new parts
# TODO - better consider muzzle break balancing

"""
OPTICS
"""

holosun503 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Holosun HS503R Red Dot Sight",
    weight=0.106,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=25,
                                   target_acquisition_ap=0.9,
                                   ap_distance_cost_modifier=0.83,
                                   ap_to_equip=1.04,
                                   spread_modifier=0.76,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='A small unmagnified red dot optical sight by holosun designed for rifles and carbines'
)

acog_ta01 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Trijicon ACOG TA01 Optic",
    weight=0.297,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=100,
                                   target_acquisition_ap=1.16,
                                   ap_distance_cost_modifier=0.71,
                                   ap_to_equip=1.07,
                                   spread_modifier=0.65,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='A 4x magnification tritium illuminated scope designed by Trijicon'
)

eotech_exps3 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="EOTECH EXPS3 Holographic Sight",
    weight=0.317,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=50,
                                   target_acquisition_ap=0.84,
                                   ap_distance_cost_modifier=0.89,
                                   ap_to_equip=1.05,
                                   spread_modifier=0.84,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='An unmagnefied rifle holographic sight by EOTech designed for close quarters combat'
)

aimpoint_comp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Aimpoint CompM4",
    weight=0.376,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=50,
                                   target_acquisition_ap=0.94,
                                   ap_distance_cost_modifier=0.82,
                                   ap_to_equip=1.07,
                                   spread_modifier=0.69,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='An unmagnified reflex sight by Aimpoint'
)

kobra_ekp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Kobra EKP-1S-O3M Optic",
    weight=0.410,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   zero_range=100,
                                   target_acquisition_ap=0.8,
                                   ap_distance_cost_modifier=0.92,
                                   ap_to_equip=1.03,
                                   spread_modifier=0.87,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='An unmagnified russian red dot sight designed to mount to AK and SVD type rifles'
)

kobra_ekp_picrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Kobra EKP-1S-O3M Optic - Picatinny Mount",
    weight=0.380,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=100,
                                   target_acquisition_ap=0.8,
                                   ap_distance_cost_modifier=0.92,
                                   ap_to_equip=1.03,
                                   spread_modifier=0.87,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='An unmagnified russian red dot sight by Axion. This version mounts to a standard picatinny rail '
                'as opposed to the side mounted version'
)

amguh1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Vortex Razor AMG UH-1 Optic",
    weight=0.33,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=25,
                                   target_acquisition_ap=0.87,
                                   ap_distance_cost_modifier=0.86,
                                   ap_to_equip=1.02,
                                   spread_modifier=0.74,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='A compact, unmagnified holographic sight by vortex'
)

compactprism = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Monstrum Tactical Compact Prism Optic",
    weight=0.48,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=50,
                                   target_acquisition_ap=0.96,
                                   ap_distance_cost_modifier=0.77,
                                   ap_to_equip=1.06,
                                   spread_modifier=0.72,
                                   attachment_point_required=('Picrail Optics Mount - Long',
                                                              'Picrail Optics Mount - Short'),
                                   ),
    description='A fixed 2x magnification scope by Monstrum Tactical'
)


pm2scope = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Schmidt and Bender PM II 5",
    weight=0.86,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=200,
                                   target_acquisition_ap=1.25,
                                   ap_distance_cost_modifier=0.63,
                                   ap_to_equip=1.11,
                                   spread_modifier=0.62,
                                   attachment_point_required=('Picrail Optics Mount - Long', ),
                                   ),
    description='A popular precision scope by Schmidt and Bender capable of 1-8x magnification'
)

pso1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="PSO-1 Optic",
    weight=0.6,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=100,
                                   target_acquisition_ap=1.21,
                                   ap_distance_cost_modifier=0.73,
                                   ap_to_equip=1.06,
                                   spread_modifier=0.66,
                                   attachment_point_required=('AK Side Mount',),
                                   ),
    description='A Russian 4x fixed magnification scope designed to mount to AK and SVD type rifles'
)

okp7 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="OKP7 Optic",
    weight=0.255,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   zero_range=25,
                                   target_acquisition_ap=0.79,
                                   ap_distance_cost_modifier=0.93,
                                   ap_to_equip=1.04,
                                   spread_modifier=0.87,
                                   attachment_point_required=('AK Side Mount',),
                                   ),
    description='An unmagnified russian holographic sight designed to mount to AK and SVD type rifles'
)

"""
Suppressor
"""

suppressor_obsidian_45 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Rugged Obsidian 45 Suppressor",
    weight=0.36,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   muzzle_break_efficiency=0.31,
                                   target_acquisition_ap=1.13,
                                   fire_rate_modifier=1.09,
                                   sound_radius=0.27,
                                   attachment_point_required=('Barrel Thread .578x28',),
                                   is_suppressor=True,
                                   ),
    description='A modular suppressor compatible with .578x28 barrel threading'
)

suppressor_wolfman_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Dead Air Wolfman Suppresssor",
    weight=0.408,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   muzzle_break_efficiency=0.35,
                                   target_acquisition_ap=1.15,
                                   fire_rate_modifier=1.11,
                                   sound_radius=0.24,
                                   attachment_point_required=('Barrel Thread 1/2x28',),
                                   is_suppressor=True,
                                   ),
    description='A large, modular suppressor for firearms with 1/2x28 barrel threading '
)

suppressor_obsidian_9 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Rugged Obsidian 9 Suppressor",
    weight=0.36,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   muzzle_break_efficiency=0.30,
                                   target_acquisition_ap=1.12,
                                   fire_rate_modifier=1.08,
                                   sound_radius=0.25,
                                   attachment_point_required=('Barrel Thread 1/2x28',),
                                   is_suppressor=True,
                                   ),
    description='A modular suppressor compatible with 1/2x28 barrel threading'
)

suppressor_saker_762 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SilencerCo Saker 762 Suppressor",
    weight=0.663,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   muzzle_break_efficiency=0.31,
                                   target_acquisition_ap=1.16,
                                   fire_rate_modifier=1.12,
                                   sound_radius=0.27,
                                   attachment_point_required=('Barrel Thread 5/8x24',),
                                   is_suppressor=True,
                                   ),
    description='A rifle suppressor intended for 7.62mm rifles compatible with 1/2x28 barrel threading'
)

"""
Accessories
"""

adapter_mlok_picrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MLOK Picatinny Rail Adapter - Long Rails",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Rail Adapter',
                                   is_attachment_point_types=['Picrail Side Mount - Long', 'Picrail Underbarrel - Long',
                                                              'Picrail Top Mount - Long'],
                                   attachment_point_required=('MLOK Side Mount - Long', 'MLOK Underbarrel - Long',
                                                              'MLOK Top Mount - Long'),
                                   ),
    description='Picatinny rail adapters for MLOK attachment systems, allowing the attachment of picatinny rail '
                'mounted accessories'
)

adapter_mlok_picrail_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MLOK Picatinny Rail Adapter - Short Rails",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Rail Adapter',
                                   is_attachment_point_types=['Picrail Side Mount - Short',
                                                              'Picrail Underbarrel - Short',
                                                              'Picrail Top Mount - Short'],
                                   attachment_point_required=('MLOK Side Mount - Short',
                                                              'MLOK Underbarrel - Short',
                                                              'MLOK Top Mount - Short'),
                                   ),
    description='Picatinny rail adapters for MLOK attachment systems, allowing the attachment of picatinny rail '
                'mounted accessories'
)

laser_sight = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Laser Sight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='gun_accessory',
                                   close_range_accuracy=1.05,
                                   ),
    description='A small red laser to assist with target aquisition'
)

forward_grip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Forward Grip",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='accessory_underbarrel',
                                   recoil=0.9
                                   ),
    description='A vertical grip for easier recoil control'
)