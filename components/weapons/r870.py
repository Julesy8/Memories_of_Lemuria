from entity import Item
from components.consumables import GunIntegratedMag, GunComponent
from components.gunparts import Parts
import colour

"""
Note - barrels made for 4 rnd magazine tube do not fit those made for 6 rnd magazine tube

Overall weight for 14 inch barrel shockwave 4 rnd magazine - 5.65 lbs 
Raptor pistol grip weight - 0.625 lbs
Magpul forend weight - 0.6 lbs
Action weight w 4 rnd mag tube and 14 inch barrel - 4.42 lbs
Estimated weight for 14 inch barrel - 1.48 lbs 
Action weight 4 rnd magazine w/o barrel - 2.94 lbs

28 inch barrel weight - 3.5 lbs 
26 inch barrel weight - 2.93 lbs
weight reduction / inch - 8%

Overall weight 28 in barrel walnut stock fieldmaster, 4 round mag - 7.5 lbs
stock and forend - 1.5 kg (3.3 lbs)
action weight w 28 in barrel - 4.2 lbs 

Overall weight 870 express tactical magpul (6 rnd tube) - 7.5 lbs
Magpul forend weight - 0.6 lbs
Magpul stock weight - 1.5 lbs
Action weight w 6 rnd mag tube and 18.5 inch barrel - 5.4 lbs 
Barrel weight - 2.18 lbs
Action weight 6 rnd magazine w/o barrel - 3.22 lbs

presumably wood forend is 0.272 kg
"""

"""
RECIEVER
"""

reciever_r870_4rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 Reciever - 4 Round Mag",
    weight=1.33,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Reciever',
                                   compatible_parts={'Model 870 Barrel': ["Model 870 26 Inch Barrel",
                                                                          "Model 870 TAC-14 Barrel",
                                                                          "Model 870 TAC-14 Barrel - Blade Sight"]},
                                   is_optic=True,
                                   functional_part=True,
                                   ),
    description='Remington model 870 reciever with 4 round magazine tube'
)

reciever_r870dm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 DM Reciever",
    weight=1.46,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Reciever',
                                   compatible_parts={'Model 870 Barrel': ["Model 870 26 Inch Barrel",
                                                                          "Model 870 TAC-14 Barrel",
                                                                          "Model 870 TAC-14 Barrel - Blade Sight"]},
                                   incompatibilities=(("Model 870 Magazine Extension",),),
                                   compatible_magazine_type='R870 DM',
                                   is_optic=True,
                                   functional_part=True,
                                   ),
    description='A magazine-fed version of the classic Remington model 870 reciever.'
)

reciever_r870_6rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 Reciever - Tactical Express",
    weight=1.46,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Reciever',
                                   suffix='Tactical Express',
                                   compatible_parts={'Model 870 Barrel': [
                                           "Model 870 'Tactical Express' 18.5 Inch Barrel",
                                           "Model 870 18.5 Inch Barrel - Blade Sight", ]},
                                   mag_capacity=7,
                                   is_optic=True,
                                   functional_part=True,
                                   ),
    description='Remington model 870 reciever with 6 round magazine tube. Only compatible with Tactical Express 18.5 '
                'inch barrls.'
)

reciever_r870_shorty = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 Reciever - Super Shorty",
    weight=1.43,
    stacking=None,
    usable_properties=GunComponent(part_type='Super Shorty Reciever',
                                   suffix='Super Shorty',
                                   compatible_parts={'Model 870 Barrel': ["Model 870 Super Shorty Barrel", ]},
                                   incompatibilities=(("Model 870 Forend",),),
                                   mag_capacity=3,
                                   is_optic=True,
                                   functional_part=True,
                                   grip_properties={
                                       'felt_recoil': 0.84,
                                       'ap_distance_cost_modifier': 0.95,
                                       'spread_modifier': 0.93,
                                       'target_acquisition_ap': 0.96},
                                   ),
    description='Remington model 870 reciever with a 2 round magazine tube designed for the Serbu Super Shorty, '
                'an ultra-compact variant of the model 870. It comes pre-installed with a folding vertical forend.'
)

"""
BARREL
"""

r870_barrel_26 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 26 Inch Barrel",
    weight=1.33,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Barrel',
                                   suffix='Fieldmaster',
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier={'single projectile': 1.0, 'buckshot': 1.0},
                                   is_attachment_point_types=['Remington 12 Ga Choke', ],
                                   optic_properties={'target_acquisition_ap': 0.95,
                                                     'ap_distance_cost_modifier': 1.2,
                                                     'spread_modifier': 1.1, },
                                   barrel_length=26,
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description='26 inch Remington model 870 barrel assembly. It is ribbed and vented and features a low profile '
                'bead front sight. Designed for the Fieldmaster series of shotguns.'
)

r870_barrel_18 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 'Tactical Express' 18.5 Inch Barrel",
    weight=0.98,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier={'single projectile': 0.96, 'buckshot': 0.97},
                                   is_attachment_point_types=['Remington 12 Ga Choke', ],
                                   optic_properties={'target_acquisition_ap': 0.95,
                                                     'ap_distance_cost_modifier': 1.2,
                                                     'spread_modifier': 1.1, },
                                   barrel_length=18.5,
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description=('18.5 inch Remington model 870 barrel assembly designed for the Tactical Express model. Features a '
                 'low profile bead frontight.')
)

r870_barrel_t14 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 TAC-14 Barrel",
    weight=0.67,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Barrel',
                                   suffix='TAC-14',
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier={'single projectile': 0.9, 'buckshot': 0.92},
                                   is_attachment_point_types=['Remington 12 Ga Choke', ],
                                   optic_properties={'target_acquisition_ap': 0.95,
                                                     'ap_distance_cost_modifier': 1.2,
                                                     'spread_modifier': 1.1, },
                                   barrel_length=14,
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description='14 inch Remington model 870 barrel assembly designed for the TAC-14. Features a low profile bead'
                ' front sight.'
)

r870_barrel_shorty = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 Super Shorty Barrel",
    weight=0.268,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   velocity_modifier={'single projectile': 0.62, 'buckshot': 0.77},
                                   is_attachment_point_types=['Remington 12 Ga Choke', ],
                                   optic_properties={'target_acquisition_ap': 1.1,
                                                     'ap_distance_cost_modifier': 3.0,
                                                     'spread_modifier': 3.0, },
                                   barrel_length=14,
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description='An extremely short 6.5 inch Remington 870 barrel designed by Serbu for the model 870 variant of '
                'the ultra-compact Super-Shorty shotgun'
)

r870_barrel_18_bead = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 18.5 Inch Barrel - Blade Sight",
    weight=0.98,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Barrel',
                                   tags=['Bead Front Sight', ],
                                   velocity_modifier={'single projectile': 0.96, 'buckshot': 0.97},
                                   is_attachment_point_types=['Remington 12 Ga Choke', ],
                                   optic_properties={'target_acquisition_ap': 0.97,
                                                     'ap_distance_cost_modifier': 1.0,
                                                     'spread_modifier': 1.05, },
                                   barrel_length=18.5,
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True,
                                   additional_required_parts=('Iron Sight',)
                                   ),
    description='18.5 inch Remington model 870 barrel assembly. Features a large tritium front dot sight for use with '
                'ghost ring rear sights.'
)

r870_barrel_t14_bead = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 TAC-14 Barrel - Blade Sight",
    weight=0.67,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Barrel',
                                   suffix='TAC-14',
                                   tags=['Bead Front Sight', ],
                                   velocity_modifier={'single projectile': 0.9, 'buckshot': 0.92},
                                   is_attachment_point_types=['Remington 12 Ga Choke', ],
                                   optic_properties={'target_acquisition_ap': 0.97,
                                                     'ap_distance_cost_modifier': 1.0,
                                                     'spread_modifier': 1.05, },
                                   barrel_length=14,
                                   is_optic=True,
                                   accuracy_part=True,
                                   functional_part=True,
                                   additional_required_parts=('Iron Sight',)
                                   ),
    description='14 inch Remington model 870 barrel assembly designed for the TAC-14. Features a large tritium front '
                'dot sight for use with ghost ring rear sights.')

"""
STOCK
"""

r870_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Wood Stock",
    weight=0.476,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=0.5,
                                   ap_distance_cost_modifier=0.69,
                                   spread_modifier=0.85,
                                   target_acquisition_ap=0.77,
                                   equip_time=1.3,
                                   has_stock=True,
                                   ),
    description='A standard wooden Remington model 870 buttstock.'
)

r870_stock_polymer = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Polymer Stock",
    weight=0.476,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=0.5,
                                   ap_distance_cost_modifier=0.69,
                                   spread_modifier=0.85,
                                   target_acquisition_ap=0.77,
                                   equip_time=1.3,
                                   has_stock=True,
                                   ),
    description='A standard polymer Remington model 870 buttstock.'
)

r870_stock_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Magpul SGA Stock",
    weight=0.68,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=0.46,
                                   ap_distance_cost_modifier=0.64,
                                   spread_modifier=0.81,
                                   target_acquisition_ap=0.82,
                                   equip_time=1.3,
                                   has_stock=True,
                                   ),
    description='A modern, adjustable polymer buttstock for Remington model 870 shotguns. It features a configurable '
                'buttpad to adjust length of pull and reduce felt recoil and a cheek riser for use with optics.'
)

r870_stock_shockwave = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Raptor Grip",
    weight=0.283,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=0.89,
                                   ap_distance_cost_modifier=0.9,
                                   spread_modifier=0.89,
                                   target_acquisition_ap=0.7,
                                   ),
    description='A polymer birds head style grip for the Remington model 870 shotgun designed for use in the TAC-14 '
                'configuration designed by Shockwave Technologies. Designed to skirt US federal laws regulating '
                'minimum overall length of shotguns, it is installed in place of a traditional '
                'buttstock, making the gun more compact and practical for hip fire.'
)

r870_stock_pistol = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 ATI Pistol Grip",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=0.94,
                                   ap_distance_cost_modifier=0.87,
                                   spread_modifier=0.87,
                                   target_acquisition_ap=0.68,
                                   ),
    description='A polymer pistol grip for Remington model 870 shotguns designed by ATI Outdoors. It is installed in '
                'place of a traditional buttstock, making the gun more compact and practical to hip fire.'
)

r870_stock_maverick = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Maverick 88 Stock",
    weight=0.9,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=0.46,
                                   ap_distance_cost_modifier=0.69,
                                   spread_modifier=0.78,
                                   target_acquisition_ap=0.73,
                                   equip_time=1.26,
                                   has_stock=True,
                                   ),
    description='A polymer stock with built in pistol grip for shotguns including the Remington model 870.'
)
"""
can't find weight for this one
r870_stock_topfold = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870 Top-Folding Stock",
    weight=,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=,
                                   ap_distance_cost_modifier=,
                                   spread_modifier=,
                                   target_acquisition_ap=,
                                   equip_time=,
                                   has_stock=True,
                                   ),
    description='A polymer stock with built in pistol grip for shotguns including the Remington model 870 designed by '
                'ATI outdoors. The stock can be folded over the top of the firearm for ease of storage and tactical'
                ' situations.'
)"""

r870_stock_sterling = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Sterling Stock",
    weight=0.7,  # this is a guess
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   felt_recoil=0.44,
                                   ap_distance_cost_modifier=0.63,
                                   spread_modifier=0.82,
                                   target_acquisition_ap=0.86,
                                   equip_time=1.3,
                                   has_stock=True,
                                   ),
    description="An ergonomic wood laminate thumbhole style stock for the Remington model 870 designed by Boyd's "
                "Hardwood Gunstocks. It features a raised cheek weld and rubber recoil pad."
)

"""
FOREND
"""

r870_forend = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Wood Forend",
    weight=0.27,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Forend',
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.92,
                                       'spread_modifier': 0.91,
                                       'target_acquisition_ap': 0.8},
                                   ),
    description='A standard wooden Remington model 870 forend.'
)

r870_forend_polymer = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Polymer Forend",
    weight=0.26,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Forend',
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.92,
                                       'spread_modifier': 0.91,
                                       'target_acquisition_ap': 0.8},
                                   ),
    description='A standard polymer Remington model 870 forend.'
)

r870_forend_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Magpul Forend",
    weight=0.26,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Forend',
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.9,
                                       'spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.8},
                                   is_attachment_point_types=['MLOK Underbarrel - Long',
                                                              'MLOK Side Mount - Long'],
                                   ),
    description='A polymer forend for the Remington model 870 featuring MLOK accessory attachment points.'
)

r870_forend_tacstar = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 TacStar Forend",
    weight=0.23,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Forend',
                                   grip_properties={
                                       'felt_recoil': 0.8,
                                       'ap_distance_cost_modifier': 0.93,
                                       'spread_modifier': 0.91,
                                       'target_acquisition_ap': 0.85},
                                   ),
    description='A polymer forend for the Remington model 870 featuring an ergonomic pistol grip rather than a '
                'traditional pump grip designed by TacStar.'
)

r870_forend_voa = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 VOA Forend",
    weight=0.23,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Forend',
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.86,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.82},
                                   is_attachment_point_types=['MLOK Underbarrel - Long',
                                                              'MLOK Side Mount - Long'],
                                   ),
    description='A tactical-style aluminum forend for the Remington model 870 designed by Strike Industries. It is '
                'milled with several vents to reduce weight and features MLOK accessory attachment points.'
)

"""
CHOKE
"""

r870_choke_im = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Improved Modified Choke",
    weight=0.01,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Choke',
                                   attachment_point_required=('Remington 12 Ga Choke',),
                                   projectile_spread_modifier={'buckshot': 0.66},
                                   ),
    description="Designed for the Remington model 870, this choke attaches inside of the bore of the shotgun, "
                "restricting its diameter and allowing for tighter groups with buck and bird shot. "
                "Constricts the bore diameter significantly to a size between that of an full and modified choke."
)

r870_choke_modified = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Modified Choke",
    weight=0.01,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Choke',
                                   attachment_point_required=('Remington 12 Ga Choke',),
                                   projectile_spread_modifier={'buckshot': 0.71},
                                   ),
    description="Designed for the Remington model 870, this choke attaches inside of the bore of the shotgun, "
                "restricting its diameter and allowing for tighter groups with buck and bird shot. "
                "Less constrictive than an improved modified choke."
)

r870_choke_cylinder = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Cylinder Choke",
    weight=0.01,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Choke',
                                   attachment_point_required=('Remington 12 Ga Choke',),
                                   ),
    description="Designed for the Remington model 870, this choke tube attaches inside of the bore of the shotgun."
                "Does not constrict the diameter of the bore, making it ideal for use at close range and with slugs."
)

r870_choke_improved_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Tactical Breacher Choke",
    weight=0.023,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Choke',
                                   attachment_point_required=('Remington 12 Ga Choke',),
                                   muzzle_break_efficiency=0.54,
                                   sound_radius=1.17,
                                   projectile_spread_modifier={'buckshot': 0.83},
                                   ),
    description="Designed for the Remington model 870, this improved cyclinder pattern choke tube attaches inside of "
                "the bore of the shotgun, restricting its diameter and allowing for tighter groups with buck and "
                "bird shot. Slightly more constrictive than a clyinder choke. Includes a ported muzzle brake to reduce "
                "recoil."
)

r870_choke_cylinder_ported = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Tactical Muzzle Brake",
    weight=0.023,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Choke',
                                   attachment_point_required=('Remington 12 Ga Choke',),
                                   muzzle_break_efficiency=0.58,
                                   sound_radius=1.2,
                                   ),
    description="Designed for the Remington model 870, this choke attaches inside of the bore of the shotgun."
                "Does not constrict the diameter of the bore, making it ideal for use at close range with shot and "
                "for use with slugs. Includes a ported muzzle brake to reduce recoil."
)

"""
ACCESSORIES
"""

r870_ar_stock_adapter = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mesa Tactical LEO M870 AR-15 Stock Adapter",
    weight=0.4,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Stock',
                                   additional_required_parts=('AR Stock', 'AR Grip'),
                                   ),
    description='An AR-15 buffer tube stock and pistol grip adapter designed by Mesa Tactical for the Remington model '
                '870, replacing the stock.'
)

r870_optic_picrail = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Picatinny Rail Optics Mount",
    weight=0.09,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Optics Mount',
                                   optic_mount_properties={'receiver_height_above_bore': 0.2},
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   ),
    description='An aluminium picatinny rail optics mount. Screws into the top of a drilled and tapped Remington '
                'Model 870 reciever.'
)

r870_optic_picrail_ghost = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 Ghost Sights w/ Picatinny Mount",
    weight=0.1,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Optics Mount',
                                   optic_mount_properties={'receiver_height_above_bore': 0.2},
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   additional_required_parts=('Bead Front Sight',),
                                   tags=['Iron Sight', ],
                                   sight_height_above_bore=0.35,
                                   ),
    description='An aluminium rear XS Blade ghost sight for the Remington model 870. Includes a picatinny rail for '
                'optics mounting. Screws into the top of a drilled and tapped Remington Model 870 reciever.'
)

r870_extension_2rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 +2 Magazine Extension",
    weight=0.18,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Magazine Extension',
                                   additional_magazine_capacity=2,
                                   ),
    description='A magazine tube extension for the Remington model 870. It attaches to the end of the magazine tube '
                'and gives an extra 2 shells capacity.'
)

r870_extension_4rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 +4 Magazine Extension",
    weight=0.13,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Magazine Extension',
                                   additional_magazine_capacity=4,
                                   ),
    description='A magazine tube extension for the Remington model 870. It attaches to the end of the magazine tube '
                'and gives an extra 4 shells capacity.'
)

r870_extension_6rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M870 +6 Magazine Extension",
    weight=0.368,
    stacking=None,
    usable_properties=GunComponent(part_type='Model 870 Magazine Extension',
                                   compatible_parts={'Model 870 Barrel': ['Model 870 26 Inch Barrel', ]},
                                   additional_magazine_capacity=6,
                                   ),
    description='A magazine tube extension for the Remington model 870. It attaches to the end of the magazine tube '
                'and gives an extra 6 shells capacity. ')

"""
GUN
"""

rem_870 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="Model 870",
    weight=1,
    stacking=None,
    description='',
    usable_properties=GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=False,
        ap_to_equip=75,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type='12 Gauge',
        velocity_modifier={'single projectile': 1.0, 'buckshot': 1.0},
        felt_recoil=1.0,
        mag_capacity=5,
        target_acquisition_ap=50,
        manual_action=True,
        action_cycle_ap_cost=100,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0.63,
        sight_height_above_bore=0.12,
        spread_modifier=1.0,
        projectile_spread_modifier={'single projectile': 1.0, 'buckshot': 1.0},
        gun_type='rifle',
        barrel_length=20
    )
)

r870_dict = {
    "guns": {
        "shotguns": {
            "Remington 870": {
                "required parts": {
                    "Model 870 Reciever": 1,
                    "Model 870 Barrel": 1,
                    "Model 870 Stock": 1,
                    "Model 870 Forend": 1,
                    "Model 870 Choke": 1,
                },
                "compatible parts": {
                    "Attachment Adapter": 1,
                    "Model 870 Magazine Extension": 1,
                    "Model 870 Optics Mount": 1,
                    "Underbarrel Accessory": 1,
                    "Side Mounted Accessory": 1,
                    "Optic": 1
                },
                "item": rem_870
            },
        }
    },
}

supersporty_dict = {
    "guns": {
        "shotguns": {
            "Remington 870 Super Shorty": {
                "required parts": {
                    "Super Shorty Reciever": 1,
                    "Model 870 Barrel": 1,
                    "Model 870 Stock": 1,
                    "Model 870 Choke": 1,
                },
                "compatible parts": {
                    "Attachment Adapter": 1,
                    "Model 870 Magazine Extension": 1,
                    "Model 870 Optics Mount": 1,
                    "Underbarrel Accessory": 1,
                    "Side Mounted Accessory": 1,
                    "Optic": 1
                },
                "item": rem_870
            },
        }
    },
}
