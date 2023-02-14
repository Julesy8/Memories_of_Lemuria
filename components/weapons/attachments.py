from entity import Item
from components.consumables import GunComponent
import colour

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
                                   ap_to_equip=1.04,
                                   optic_properties={'target_acquisition_ap': 0.9,
                                                     'ap_distance_cost_modifier': 0.83,
                                                     'spread_modifier': 0.76,
                                                     'sight_height_above_bore': 1.63,
                                                     'zero_range': 25, },
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
                                   optic_properties={'target_acquisition_ap': 1.16,
                                                     'ap_distance_cost_modifier': 0.71,
                                                     'spread_modifier': 0.65,
                                                     'sight_height_above_bore': 1.535,
                                                     'zero_range': 100, },
                                   ap_to_equip=1.07,
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
                                   optic_properties={'target_acquisition_ap': 0.84,
                                                     'ap_distance_cost_modifier': 0.89,
                                                     'spread_modifier': 0.84,
                                                     'sight_height_above_bore': 1.59,
                                                     'zero_range': 50, },
                                   ap_to_equip=1.05,
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
                                   optic_properties={'target_acquisition_ap': 0.94,
                                                     'ap_distance_cost_modifier': 0.82,
                                                     'spread_modifier': 0.69,
                                                     'sight_height_above_bore': 2.0,
                                                     'zero_range': 50, },
                                   ap_to_equip=1.07,
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
                                   optic_properties={'target_acquisition_ap': 0.8,
                                                     'ap_distance_cost_modifier': 0.92,
                                                     'spread_modifier': 0.87,
                                                     'sight_height_above_bore': 2.0,
                                                     'zero_range': 100, },
                                   ap_to_equip=1.03,
                                   attachment_point_required=('AK Side Mount', ),
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
                                   optic_properties={'target_acquisition_ap': 0.8,
                                                     'ap_distance_cost_modifier': 0.92,
                                                     'spread_modifier': 0.87,
                                                     'sight_height_above_bore': 2.0,
                                                     'zero_range': 100, },
                                   ap_to_equip=1.03,
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
                                   optic_properties={'target_acquisition_ap': 0.87,
                                                     'ap_distance_cost_modifier': 0.86,
                                                     'spread_modifier': 0.74,
                                                     'sight_height_above_bore': 1.58,
                                                     'zero_range': 25, },
                                   ap_to_equip=1.02,
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
                                   optic_properties={'target_acquisition_ap': 0.96,
                                                     'ap_distance_cost_modifier': 0.77,
                                                     'spread_modifier': 0.72,
                                                     'sight_height_above_bore': 2.19,
                                                     'zero_range': 50, },
                                   ap_to_equip=1.06,
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
                                   optic_properties={'target_acquisition_ap': 1.25,
                                                     'ap_distance_cost_modifier': 0.63,
                                                     'spread_modifier': 0.62,
                                                     'sight_height_above_bore': 1.47,
                                                     'zero_range': 200, },
                                   ap_to_equip=1.11,
                                   attachment_point_required=('Picrail Optics Mount - Long',),
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
                                   optic_properties={'target_acquisition_ap': 1.21,
                                                     'ap_distance_cost_modifier': 0.73,
                                                     'spread_modifier': 0.66,
                                                     'sight_height_above_bore': 1.39,
                                                     'zero_range': 100, },
                                   ap_to_equip=1.06,
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
                                   optic_properties={'target_acquisition_ap': 0.79,
                                                     'ap_distance_cost_modifier': 0.93,
                                                     'spread_modifier': 0.87,
                                                     'sight_height_above_bore': 0.94,
                                                     'zero_range': 25, },
                                   ap_to_equip=1.04,
                                   attachment_point_required=('AK Side Mount',),
                                   ),
    description='An unmagnified russian holographic sight designed to mount to AK and SVD type rifles'
)

""" 
Iron Sights
"""

irons_sig_rear = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Sig Sauer Flip Up Rear Sight",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', ],
                                   additional_required_parts=('Front Sight',),
                                   compatible_parts={'Front Sight': ['AR15 Height', ]},
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   optic_properties={'target_acquisition_ap': 0.98,
                                                     'ap_distance_cost_modifier': 0.97,
                                                     'spread_modifier': 0.97,
                                                     'zero_range': 25, },
                                   sight_height_above_bore=1.4,
                                   ),
    description='A flip up, standard AR-15 height aperture rear sight manufactured by Sig Sauer. Attaches to picatinny '
                'rails.')

irons_sig_front = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Sig Sauer Flip Up Front Sight",
    weight=0.08,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', 'AR15 Height'],
                                   additional_required_parts=('Front Sight',),
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   ),
    description='A flip up, standard AR-15 height front post sight manufactured by Sig Sauer. Attaches to picatinny '
                'rails.')

irons_magpul_rear = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul MBUS Pro Flip Up Rear Sight",
    weight=0.051,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', ],
                                   additional_required_parts=('Front Sight',),
                                   compatible_parts={'Front Sight': ['AR15 Height', ]},
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   optic_properties={'target_acquisition_ap': 0.98,
                                                     'ap_distance_cost_modifier': 0.97,
                                                     'spread_modifier': 0.97,
                                                     'zero_range': 25, },
                                   sight_height_above_bore=1.4,
                                   ),
    description='A flip up, standard AR-15 height slim aperture rear sight manufactured by Magpul. '
                'Attaches to picatinny rails.')

irons_magpul_front = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul MBUS Pro Flip Up Front Sight",
    weight=0.042,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', 'AR15 Height'],
                                   additional_required_parts=('Front Sight',),
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   ),
    description='A flip up, standard AR-15 height slim front post sight manufactured by Magpul. '
                'Attaches to picatinny rails.')

irons_dd_rear = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Daniel Defense A1.5 Rear Iron Sight",
    weight=0.028,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', ],
                                   additional_required_parts=('Front Sight',),
                                   compatible_parts={'Front Sight': ['AR15 Height', ]},
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   optic_properties={'target_acquisition_ap': 0.98,
                                                     'ap_distance_cost_modifier': 0.97,
                                                     'spread_modifier': 0.97,
                                                     'zero_range': 25, },
                                   sight_height_above_bore=1.4,
                                   ),
    description='A standard AR-15 height aperture rear sight manufactured by Daniel Defense. '
                'Attaches to picatinny rails.')

irons_dd_front = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Daniel Defense A1.5 Front Iron Sight",
    weight=0.042,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', 'AR15 Height'],
                                   additional_required_parts=('Front Sight',),
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   ),
    description='A flip up, standard AR-15 height front post sight manufactured by Daniel Defense. '
                'Attaches to picatinny rails.')

irons_troy_rear = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Troy M4 Rear Iron Sight",
    weight=0.048,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', ],
                                   additional_required_parts=('Front Sight',),
                                   compatible_parts={'Front Sight': ['AR15 Height', ]},
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   optic_properties={'target_acquisition_ap': 0.98,
                                                     'ap_distance_cost_modifier': 0.97,
                                                     'spread_modifier': 0.97,
                                                     'zero_range': 25, },
                                   sight_height_above_bore=1.4,
                                   ),
    description='A standard AR-15 height dioptic flip up rear sight manufactured by Troy. '
                'Attaches to picatinny rails.')

irons_troy_front = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Troy M4 Front Iron Sight",
    weight=0.042,
    stacking=None,
    usable_properties=GunComponent(part_type='Optic',
                                   is_optic=True,
                                   tags=['Iron Sight', 'AR15 Height'],
                                   additional_required_parts=('Front Sight',),
                                   prevents_attachment_of={'AR Handguard': ['Optic', ]},
                                   ),
    description='A flip up, standard AR-15 height flip up front post sight manufactured by Troy. '
                'Attaches to picatinny rails.')

"""
Grips
"""

grip_hera_cqr = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="HERA Arms CQR Front Grip",
    weight=0.14,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Long',),
                                   grip_properties={
                                       'felt_recoil': 0.82,
                                       'ap_distance_cost_modifier': 0.92,
                                       'spread_modifier': 0.91,
                                       'target_acquisition_ap': 0.8},),
    description="An ergonomic polymer front grip manufactured by HERA Arms designed for AR-type rifles"
)

grip_promag_vertical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Pro Mag Vertical Grip",
    weight=0.09,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Short',),
                                   grip_properties={
                                       'felt_recoil': 0.94,
                                       'ap_distance_cost_modifier': 0.78,
                                       'spread_modifier': 0.75,
                                       'target_acquisition_ap': 0.95},),
    description="A simple polymer front vertical grip designed by Pro Mag"
)

grip_jem_vertical = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="JE Machine Tech Vertical Grip",
    weight=0.181,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Short',),
                                   grip_properties={
                                       'felt_recoil': 0.75,
                                       'ap_distance_cost_modifier': 0.96,
                                       'spread_modifier': 0.92,
                                       'target_acquisition_ap': 0.79},),
    description="An ergonomic polymer pistol grip style vertical grip designed by JE Machine Tech"
)

grip_magpul_angled = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul AFG2 Angled Foregrip",
    weight=0.072,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Long',),
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.89,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.81},),
    description="An angled polymer foregrip designed by Magpul"
)

grip_magpul_mvg = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul M-LOK MVG Vertical Grip",
    weight=0.039,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Short',),
                                   grip_properties={
                                       'felt_recoil': 0.79,
                                       'ap_distance_cost_modifier': 0.93,
                                       'spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.78},),
    description="A short polymer vertical fore grip designed by Magpul"
)

grip_aimtac_short = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AIM Sports Tactical Vertical Grip",
    weight=0.085,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Short',),
                                   grip_properties={
                                       'felt_recoil': 0.77,
                                       'ap_distance_cost_modifier': 0.94,
                                       'spread_modifier': 0.91,
                                       'target_acquisition_ap': 0.76},),
    description="A short polymer vertical fore grip designed by AIM Sports Tactical"
)

grip_magpul_handstop = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul M-LOK Hand Stop",
    weight=0.025,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Long',),
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.87,
                                       'spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.75},),
    description="A polymer hand stop designed by Magpul"
)

grip_hipoint_folding = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="HI Point Folding Vertical Grip",
    weight=0.18,
    stacking=None,
    usable_properties=GunComponent(part_type='Underbarrel Accessory',
                                   attachment_point_required=('Picrail Underbarrel - Short',),
                                   grip_properties={
                                       'felt_recoil': 0.91,
                                       'ap_distance_cost_modifier': 0.81,
                                       'spread_modifier': 0.75,
                                       'target_acquisition_ap': 0.93},),
    description="A slim, polymer folding vertical grip designed by HI Point"
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
                                   muzzle_break_efficiency=0.35,
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
                                   muzzle_break_efficiency=0.38,
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
                                   muzzle_break_efficiency=0.33,
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
                                   muzzle_break_efficiency=0.4,
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
    weight=0.09,
    stacking=None,
    usable_properties=GunComponent(part_type='Attachment Adapter',
                                   tags=['Handguard', ],
                                   converts_attachment_points={'MLOK Side Mount - Long': 'Picrail Side Mount - Long',
                                                               'MLOK Underbarrel - Long': 'Picrail Underbarrel - Long',
                                                               'MLOK Top Mount - Long': 'Picrail Top Mount - Long'},
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
    weight=0.048,
    stacking=None,
    usable_properties=GunComponent(part_type='Attachment Adapter',
                                   tags=['Handguard', ],
                                   converts_attachment_points={
                                       'MLOK Side Mount - Short': 'Picrail Side Mount - Short',
                                       'MLOK Underbarrel - Short': 'Picrail Underbarrel - Short',
                                       'MLOK Top Mount - Short': 'Picrail Top Mount - Short'},
                                   attachment_point_required=('MLOK Side Mount - Short', 'MLOK Underbarrel - Short',
                                                              'MLOK Top Mount - Short'),
                                   ),
    description='Picatinny rail adapters for MLOK attachment systems, allowing the attachment of picatinny rail '
                'mounted accessories'
)
