from entity import Item
from components.consumables import GunComponent
import colour

"""
OPTICS
"""

adapter_mlok_picrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="MLOK Picatinny Rail Adapter",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Rail Adapter',
                                   is_attachment_point_types=['Picrail Side Mount', 'Picrail Underbarrel',
                                                              'Picrail Top Mount'],
                                   attachment_point_required=('MLOK Side Mount', 'MLOK Underbarrel', 'MLOK Top Mount'),
                                   ),
    description='Picatinny rail adapters for MLOK attachment systems, allowing the attachment of picatinny rail '
                'mounted accessories'
)


holosun503 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Holosun HS503 Red Dot Sight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.08,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='A small unmagnified red dot optical sight by holosun designed for rifles and carbines'
)

acog_ta01 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Trijicon ACOG TA01 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=0.94,
                                   base_accuracy=1.2,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='A 4x magnification tritium illuminated scope designed by Trijicon'
)

eotech_exps3 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="EOTECH EXPS3 Holographic Sight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.09,
                                   base_accuracy=1.04,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='An unmagnefied rifle holographic sight by EOTech designed for close quarters combat'
)

aimpoint_comp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Aimpoint CompM4",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.02,
                                   base_accuracy=1.11,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='An unmagnified reflex sight by Aimpoint'
)

kobra_ekp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Kobra EKP-1S-O3M Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   close_range_accuracy=1.06,
                                   base_accuracy=1.06,
                                   attachment_point_required=('AK Side Mount',),
                                   ),
    description='An unmagnified russian red dot sight designed to mount to AK and SVD type rifles'
)

kobra_ekp_picrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Kobra EKP-1S-O3M Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.06,
                                   base_accuracy=1.06,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='An unmagnified russian red dot sight by Axion. This version mounts to a standard picatinny rail '
                'as opposed to the side mounted version'
)

amguh1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Vortex Razor AMG UH-1 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.12,
                                   base_accuracy=1.02,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='A compact, unmagnified holographic sight by vortex'
)

compactprism = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Monstrum Tactical Compact Prism Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.02,
                                   base_accuracy=1.15,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='A fixed 2x magnification scope by Monstrum Tactical'
)


pm2scope = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Schmidt and Bender PM II",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=0.83,
                                   base_accuracy=1.3,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='A popular precision scope by Schmidt and Bender capable of 1-8x magnification'
)

hensoldtff = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Hensoldt FF 4-16x56 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=0.92,
                                   base_accuracy=1.25,
                                   attachment_point_required=('Picrail Optics Mount',),
                                   ),
    description='A 4-16x magnification scope for precision shooting by Hensoldt'
)

pso1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="PSO-1 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=0.96,
                                   base_accuracy=1.17,
                                   attachment_point_required=('AK Side Mount',),
                                   ),
    description='A Russian 4x fixed magnification scope designed to mount to AK and SVD type rifles'
)


deltapoint = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Leupold DeltaPoint Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.19,
                                   base_accuracy=0.94,
                                   is_attachment_point_types=['Dovetail Optics Mount', ],
                                   ),
    description='A popular compact unmagnified reflex sight by Leupold intended for fast target aquisition'
)


okp7 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="OKP7 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   close_range_accuracy=1.12,
                                   attachment_point_required=('AK Side Mount',),
                                   ),
    description='An unmagnified russian holographic sight designed to mount to AK and SVD type rifles'
)

suppressor_obsidian_45 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Rugged Obsidian 45 Suppressor",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   fire_rate_modifier=1.1,
                                   sound_radius=0.67,
                                   recoil=0.87,
                                   close_range_accuracy=0.82,
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
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   fire_rate_modifier=1.07,
                                   sound_radius=0.6,
                                   recoil=0.84,
                                   close_range_accuracy=0.86,
                                   base_accuracy=0.95,
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
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   fire_rate_modifier=1.1,
                                   sound_radius=0.65,
                                   recoil=0.92,
                                   close_range_accuracy=0.87,
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
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   fire_rate_modifier=1.1,
                                   sound_radius=0.60,
                                   recoil=0.88,
                                   close_range_accuracy=0.85,
                                   attachment_point_required=('Barrel Thread 5/8x24',),
                                   is_suppressor=True,
                                   ),
    description='A rifle suppressor intended for 7.62mm rifles compatible with 1/2x28 barrel threading'
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