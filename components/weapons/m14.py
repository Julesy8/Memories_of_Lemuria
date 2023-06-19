from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
RECIEVERS
"""

m14_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14 Reciever",
    weight=1.719,
    stacking=None,
    usable_properties=GunComponent(part_type='M14 Reciever',
                                   functional_part=True,
                                   ),
    description='An unbarreled M14 action with gas system'
)

m1a_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1A Reciever",
    weight=1.719,
    stacking=None,
    usable_properties=GunComponent(part_type='M1A Reciever',
                                   functional_part=True,
                                   ),
    description='An unbarreled M1A action with gas system'
)

"""
BARRELS
"""

m14_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A Standard Barrel",
    weight=0.91,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Barrel',
                                   optic_properties={'target_acquisition_ap': 1.1,
                                                     'ap_distance_cost_modifier': 0.93,
                                                     'spread_modifier': 0.93, },
                                   is_attachment_point_types=['Barrel Thread .595"x32 tpi', ],
                                   barrel_length=22,
                                   velocity_modifier=0.98,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description='A standard 22 inch M14/M1A barrel chambered in 7.62x51 NATO'
)

m14_barrel_18in = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A 18.5 Inch Barrel",
    weight=0.82,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Barrel',
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'spread_modifier': 0.94, },
                                   is_attachment_point_types=['Barrel Thread .595"x32 tpi', ],
                                   barrel_length=18.5,
                                   velocity_modifier=0.938,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.95,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description='An 18.5 inch M14/M1A barrel chambered in 7.62x51 NATO'
)

m14_barrel_socom = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A SOCOM Barrel",
    weight=0.77,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Barrel',
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'spread_modifier': 0.96, },
                                   suffix='SOCOM',
                                   muzzle_break_efficiency=0.36,
                                   sound_radius=1.06,
                                   barrel_length=16,
                                   velocity_modifier=0.925,
                                   target_acquisition_ap=0.95,
                                   equip_time=0.9,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description='A short 16 inch M14/M1A barrel chambered in 7.62x51 NATO. Features a proprietary muzzle brake which '
                'attaches to the gas block.'
)

"""
STOCKS
"""

m14_stock_fiberglass = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A USGI Fiberglass Stock",
    weight=1.449,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Stock',
                                   felt_recoil=0.5,
                                   ap_distance_cost_modifier=0.69,
                                   spread_modifier=0.85,
                                   target_acquisition_ap=0.77,
                                   equip_time=1.3,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.87,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.83},
                                   ),
    description='A standard issue fiberglass stock for the M14 and M1A rifles'
)

m14_stock_wood = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A USGI Birch Wood Stock",
    weight=1.662,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Stock',
                                   felt_recoil=0.5,
                                   ap_distance_cost_modifier=0.69,
                                   spread_modifier=0.85,
                                   target_acquisition_ap=0.77,
                                   equip_time=1.3,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.87,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.83},
                                   ),
    description='A standard issue birch wood stock for the M14 and M1A rifles'
)

m14_stock_archangel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A 'Archangel' Stock",
    weight=1.974,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Stock',
                                   felt_recoil=0.46,
                                   ap_distance_cost_modifier=0.66,
                                   spread_modifier=0.82,
                                   target_acquisition_ap=0.79,
                                   equip_time=1.33,
                                   suffix='Tactical',
                                   has_stock=True,
                                   is_attachment_point_types=['Picrail Underbarrel - Long'],
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.85,
                                       'spread_modifier': 0.86,
                                       'target_acquisition_ap': 0.83},
                                   ),
    description='An aftermarket ergonomic polymer stock for the M14 and M1A rifles manufactured by ProMag featuring a '
                'picatinny rail accessory attachment points, a large rubber butt stock and an adjustable cheek riser '
                'for precision shooting'

)

m14_stock_vltor = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A VLTOR M1-S Stock",
    weight=0.874,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Stock',
                                   additional_required_parts=('AR Stock', 'AR Grip'),
                                   has_stock=True,
                                   suffix='Tactical',
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.87,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.83},
                                   ),
    description='An aftermarket polymer stock for the M14 and M1A rifles manufactured by VLTOR featuring a AR-15 type '
                'stock adapter and pistol grip'
)

m14_stock_ebr = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A M14ALCS/CV Stock",
    weight=1.33,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Stock',
                                   additional_required_parts=('AR Stock', 'AR Grip'),
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long'],
                                   has_stock=True,
                                   suffix='EBR',
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.88,
                                       'spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.82},
                                   optic_mount_properties={'receiver_height_above_bore': 0.216,
                                                           'spread_modifier': 1.06,
                                                           'target_acquisition_ap': 0.9},
                                   ),
    description='An aluminium stock for M14 and M1A rifles manufactured by SAGE International intended to modernize '
                'the M14 with features such as picatinny rail accessory and optics mounting poitns and a pistol grip. '
                'This model also features an AR-15 type butt stock adapter.'
)

m14_stock_bullpup = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A 'Rogue' Bullpup Stock",
    weight=2.85,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Stock',
                                   additional_required_parts=('AR Stock', 'AR Grip', 'Optic'),
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long'],
                                   compatible_parts={'M14/M1A Optic Mount': []},
                                   suffix='Bullpup',
                                   has_stock=True,
                                   felt_recoil=0.45,
                                   ap_distance_cost_modifier=0.7,
                                   load_time_modified=1.18,
                                   spread_modifier=0.76,
                                   target_acquisition_ap=0.81,
                                   equip_time=0.93,
                                   grip_properties={
                                       'felt_recoil': 0.86,
                                       'ap_distance_cost_modifier': 0.88,
                                       'spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.84},
                                   optic_mount_properties={'receiver_height_above_bore': 0.216},
                                   ),
    description='An aftermarket aluminium chassis manufactured by Juggernaut Tactical for M14 and M1A rifles. Its '
                'bullpup form factor significantly shortens the rifle making it more suited to CQB. It also features '
                'picatinny rail optics and accessory attachment points.'
)

"""
MUZZLE DEVICES
"""

m14_muzzle_usgi = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A USGI Flash Suppressor",
    weight=0.12,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('.595"x32 tpi',),
                                   muzzle_break_efficiency=0.14,
                                   sound_radius=1.09,
                                   ),
    description="Flash suppressor designed for M14 and M1A rifles"
)

m14_muzzle_uscg_brake = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A USCG Muzzle Brake",
    weight=0.148,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('.595"x32 tpi',),
                                   muzzle_break_efficiency=0.51,
                                   sound_radius=1.6,
                                   ),
    description="Muzzle brake designed for the US military for M14 and M1A rifles"
)

m14_muzzle_vais_brake = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A Vais Muzzle Brake",
    weight=0.11,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('.595"x32 tpi',),
                                   muzzle_break_efficiency=0.43,
                                   sound_radius=1.12,
                                   ),
    description="A small compensator/muzzle brake for M14 and M1A rifles manufactured by Vais"
)

m14_muzzle_synergy_brake = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A SLR Synergy Muzzle Brake",
    weight=0.12,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   attachment_point_required=('.595"x32 tpi',),
                                   muzzle_break_efficiency=0.47,
                                   sound_radius=1.14,
                                   ),
    description="A muzzle brake for M14 and M1A rifles manufactured by SLR"
)

"""
ACCESSORIES
"""

m14_optic_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M14/M1A Picatinny Rail Optic Mount",
    weight=0.18,
    stacking=None,
    usable_properties=GunComponent(part_type='M14/M1A Optic Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.216},
                                   ),
    description="An aluminium picatinny rail optics mount for M14 and M1A rifles manufactured by BadAce Tactical that"
                " mounts above the reciever and replaces the rear sight"
)

m14 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="M1A",
    weight=4.18,
    stacking=None,
    description='The M1A rifle is a semi-automatic only civilian derivative of the military M14 rifle. '
                'Its design pays homage to the M1 garand. It features detachable magazines and fires the '
                'powerful 7.62x51mm NATO cartridge.',
    usable_properties=GunMagFed(
        compatible_magazine_type='M14/M1A',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=75,
        current_fire_mode='single shot',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False},
                    'automatic': {'fire rate': 750, 'automatic': True}},
        parts=Parts(),
        compatible_bullet_type='7.62x51',
        velocity_modifier=1.0,
        felt_recoil=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=1.03,
        sight_height_above_bore=0.22,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        spread_modifier=0.05,
        barrel_length=22,
        gun_type='rifle'
    )
)

m1a = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="M1A",
    weight=4.18,
    stacking=None,
    description='The M1A rifle is a semi-automatic only civilian derivative of the military M14 rifle. Its design '
                'pays homage to the M1 garand. It features detachable magazines and fires the powerful 7.62x51mm '
                'NATO cartridge.',
    usable_properties=GunMagFed(
        compatible_magazine_type='M14/M1A',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=75,
        current_fire_mode='single shot',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False},},
        parts=Parts(),
        compatible_bullet_type='7.62x51',
        velocity_modifier=1.0,
        felt_recoil=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=1.03,
        sight_height_above_bore=0.22,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        spread_modifier=0.05,
        barrel_length=22,
        gun_type='rifle'
    )
)

m14_dict = {
    "guns": {
        "automatic rifles": {
            "M14": {
                "required parts": {
                    "M14 Reciever": 1,
                    "M14/M1A Stock": 1,
                    "M14/M1A Barrel": 1,
                },
                "compatible parts": {
                    "M14/M1A Picatinny Rail Optic Mount": 1,
                    "Attachment Adapter": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": m14
            },
        }
    },
}

m1a_dict = {
    "guns": {
        "automatic rifles": {
            "M1A": {
                "required parts": {
                    "M1A Reciever": 1,
                    "M14/M1A Stock": 1,
                    "M14/M1A Barrel": 1,
                },
                "compatible parts": {
                    "M14/M1A Picatinny Rail Optic Mount": 1,
                    "Attachment Adapter": 1,
                    "Muzzle Adapter": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": m1a
            },
        }
    },
}
