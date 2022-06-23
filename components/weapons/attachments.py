from entity import Item
from components.consumables import GunComponent
import colour
from components.commonitems import steel


"""
OPTICS
"""

holosun503 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Holosun HS503 Red Dot Sight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A small unmagnified red dot optical sight by holosun designed for rifles and carbines'
)

acog_ta01 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Trijicon ACOG TA01 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A 4x magnification tritium illuminated scope designed by Trijicon'
)

eotech_exps3 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="EOTECH EXPS3 Holographic Sight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='An unmagnefied rifle holographic sight by EOTech designed for close quarters combat'
)

aimpoint_comp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Aimpoint CompM4",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='An unmagnified reflex sight by Aimpoint'
)

kobra_ekp = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Kobra EKP-1S-O3M Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='An unmagnified russian red dot sight designed to mount to AK and SVD type rifles'
)

amguh1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Vortex Razor AMG UH-1 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='An unmagnified holographic sight by vortex'
)

compactprism = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Monstrum Tactical Compact Prism Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A fixed 2x magnification scope by Monstrum Tactical'
)

leaperutg = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Leapers UTG Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A compact unmagnified reflex sight by Leapers'
)

pm2scope = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Schmidt and Bender PM II",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A popular precision scope by Schmidt and Bender capable of 1-8x magnification'
)

hensoldtff = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Hensoldt FF 4-16x56 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A 4-16x magnification scope for precision shooting by Hensoldt'
)

pso1 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="PSO-1 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A Russian 4x fixed magnification scope designed to mount to AK and SVD type rifles'
)

nspum = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="NSPU-M Night Vision Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A hefty Russian fixed 3.5x magnification night vision scope designed to mount to AK and '
                'SVD type rifles'
)

deltapoint = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Leupold DeltaPoint Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='A popular compact unmagnified reflex sight by Leupold'
)


okp7 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="OKP7 Optic",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='optic',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   base_accuracy=1.1,
                                   ),
    description='An unmagnified russian holographic sight designed to mount to AK and SVD type rifles'
)

suppressor_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Suppressor 9mm",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='muzzle_device',
                                   material={steel: 1},
                                   sound_radius=0.77,
                                   recoil=0.90,
                                   close_range_accuracy=0.85,
                                   is_suppressor=True,
                                   compatible_calibres=('9mm',)
                                   ),
    description='Traps gasses as they exit the barrel, quietening the sound of shots'
)


laser_sight = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Laser Sight",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='gun_accessory',
                                   material={steel: 1},
                                   close_range_accuracy=1.05,
                                   ),
    description='A small red laser to assist with target aquisition'
)

forward_grip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Forward Grip",
    weight=0.2,
    stacking=None,
    usable_properties=GunComponent(part_type='accessory_underbarrel',
                                   material={steel: 1},
                                   recoil=0.9
                                   ),
    description='A vertical grip for easier recoil control'
)