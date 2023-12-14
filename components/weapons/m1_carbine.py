from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
Reciever
"""

m1_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1 Carbine Reciever",
    weight=0.99,
    stacking=None,
    usable_properties=GunComponent(part_type='M1 Carbine Reciever',
                                   functional_part=True,
                                   ),
    description='An unbarreled M1 carbine action'
)

m2_reciever = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M2 Carbine Reciever",
    weight=0.99,
    stacking=None,
    usable_properties=GunComponent(part_type='M2 Carbine Reciever',
                                   functional_part=True,
                                   ),
    description='An unbarreled selective fire M2 carbine action'
)


"""
STOCK
"""

m1_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine Stock",
    weight=0.795,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Stock',
                                   compatible_parts={'M1/M2 Carbine Barrel': ['M1/M2 Carbine Barrel',
                                                                              'M1/M2 Carbine Barrel - Threaded'], },
                                   felt_recoil=0.48,
                                   ap_distance_cost_modifier=0.7,
                                   spread_modifier=0.88,
                                   target_acquisition_ap=0.76,
                                   equip_time=1.25,
                                   has_stock=True,
                                   pdw_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.87,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.83},
                                   ),
    description='A standard issue walnut wood stock for the M1 and M2 carbine'
)

m1_stock_springfield = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine Choate Folding Stock",
    weight=1.021,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Stock',
                                   suffix='Tactical',
                                   compatible_parts={'M1/M2 Carbine Barrel': ['M1/M2 Carbine Barrel',
                                                                              'M1/M2 Carbine Barrel - Threaded'],},
                                   felt_recoil=0.4,
                                   ap_distance_cost_modifier=0.73,
                                   spread_modifier=0.91,
                                   target_acquisition_ap=0.73,
                                   equip_time=1.18,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.84,
                                       'ap_distance_cost_modifier': 0.85,
                                       'spread_modifier': 0.85,
                                       'target_acquisition_ap': 0.8},
                                   ),
    description='An aftermarket polymer M1/M2 carbine stock featuring a folding stock and pistol grip manufactured' \
                ' by Choate'
)

m1_stock_ebr = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine EBR Stock",
    weight=0.7,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Stock',
                                   suffix='EBR',
                                   compatible_parts={'M1/M2 Carbine Barrel': ['M1/M2 Carbine Barrel',
                                                                              'M1/M2 Carbine Barrel - Threaded'],
                                                     "M1/M2 Carbine Optic Mount": ["M1/M2 Carbine S&K Optics Mount"]},
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long'],
                                   additional_required_parts=('AR Stock', 'AR Grip', 'Optic'),
                                   optic_mount_properties={'receiver_height_above_bore': 0.84},
                                   grip_properties={
                                       'felt_recoil': 0.86,
                                       'ap_distance_cost_modifier': 0.88,
                                       'spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.84},
                                   ),
    description="An aluminium 'EBR'-style stock for the M1/M2 carbine manufactured by SAGE International. It "
                "features an AR-15 buffer tube stock adapter and grip as well as picatinny rails for optics and "
                "accesory mounting."
)

m1_stock_enforcer = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine 'Enforcer' Pistol Stock",
    weight=0.473,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Stock',
                                   suffix="'Enforcer'",
                                   compatible_parts={'M1/M2 Carbine Barrel': ["M1/M2 Carbine 'Enforcer' Barrel",
                                                                              "M1/M2 Carbine 'Enforcer' Barrel - "
                                                                              "Threaded"]},
                                   felt_recoil=0.84,
                                   ap_distance_cost_modifier=0.93,
                                   spread_modifier=0.9,
                                   target_acquisition_ap=0.7,
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.87,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.83},
                                   ),
    description="A wooden pistol-style M1/M2 carbine stock. It has been significantly shortened compared to the " \
                "regular M1 carbine stock to an overall length of roughly 18 inches. It lacks a butt stock and " \
                "features a pistol grip."
)

"""
BARREL
"""

m1_barrel = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine Barrel",
    weight=0.61,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Barrel',
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'spread_modifier': 0.94, },
                                   barrel_length=17.75,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description='A standard 18 inch M1/M2 carbine barrel chambered in .30 carbine'
)

m1_barrel_enforcer = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine 'Enforcer' Barrel",
    weight=0.347,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Barrel',
                                   compatible_parts={"M1/M2 Carbine Optic Mount": ["M1/M2 Carbine S&K Optics Mount"]},
                                   optic_properties={'target_acquisition_ap': 0.94,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.04, },
                                   barrel_length=10.25,
                                   velocity_modifier=0.83,
                                   target_acquisition_ap=0.92,
                                   short_barrel=True,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description="'A shortened 10 1/4 inch pistol barrel for the M1/M2 carbine designed for the 'Super Enforcer' M1 " \
                "carbine pistols made by Iver Johnson Arms."
)

m1_barrel_threaded = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine Barrel - Threaded",
    weight=0.61,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28'],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'spread_modifier': 0.93, },
                                   barrel_length=17.75,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description='A standard 18 inch M1/M2 carbine barrel chambered in .30 carbine. It has been threaded to accept ' \
                'muzzle devices.'
)

m1_barrel_enforcer_threaded = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine 'Enforcer' Barrel - Threaded",
    weight=0.347,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28'],
                                   optic_properties={'target_acquisition_ap': 0.94,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.04, },
                                   barrel_length=10.25,
                                   velocity_modifier=0.83,
                                   target_acquisition_ap=0.92,
                                   short_barrel=True,
                                   is_optic=True,
                                   accuracy_part=True,
                                   ),
    description="'A shortened 10 1/4 inch pistol barrel for the M1/M2 carbine designed for the 'Super Enforcer' M1 " \
                "carbine pistols made by Iver Johnson Arms. It has been threaded to accept muzzle devices."
)

"""
ACCESSORIES
"""

m1_m6b_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine M6-B Optics Mount",
    weight=0.204,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Optic Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.84},
                                   ),
    description="An aluminium forward picatinny optics mount for the M1 and M2 carbine manufactured by Ultimak. It "
                "mounts onto the barrel, replacing the top hand guard."
)

m1_sk_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M1/M2 Carbine S&K Optics Mount",
    weight=0.113,
    stacking=None,
    usable_properties=GunComponent(part_type='M1/M2 Carbine Optic Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Short', ],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.84},
                                   ),
    description="An aluminium picatinny optics mount for the M1 and M2 carbine manufactured by S&K Scope Mounts. It "
                "replaces the rear iron sight."
)

m1_carbine = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="M1 Carbine",
    weight=2.4,
    stacking=None,
    description='The M1 Carbine is a lightweight semi-automatic rifle known for its versatility and reliability. '
                'Used during World War II, it offered soldiers a compact design, detachable magazine,'
                ' and fired the small but powerful .30 Carbine cartridge, making it ideal for non-frontline troops and '
                'support personnel. It has since seen service in numerous conflicts including the Korean and Vietnam'
                ' wars and is a favourite of civilian gun owners.',
    usable_properties=GunMagFed(
        compatible_magazine_type='M1/M2 Carbine',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=80,
        current_fire_mode='single shot',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        parts=Parts(),
        compatible_bullet_type='.30 Carbine',
        velocity_modifier={'projectile': 1.0},
        felt_recoil=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0,
        sight_height_above_bore=0.53,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        spread_modifier=1.0,
        projectile_spread_modifier={'single projectile': 1.0},
        barrel_length=17.75,
        gun_type='rifle'
    )
)

m2_carbine = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="M2 Carbine",
    weight=2.4,
    stacking=None,
    description='The M2 Carbine is a selective-fire rifle developed during World War II as an upgrade to the'
                ' semi-automatic M1 Carbine. it offered soldiers a compact design, detachable magazine and fired the '
                'small but powerful .30 Carbine cartridge, making it ideal for non-frontline troops and support'
                ' personnel.',
    usable_properties=GunMagFed(
        compatible_magazine_type='M1/M2 Carbine',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=75,
        current_fire_mode='single shot',
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'automatic': {'fire rate': 750, 'automatic': True}},
        parts=Parts(),
        compatible_bullet_type='.30 Carbine',
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0,
        sight_height_above_bore=0.53,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        spread_modifier=1.0,
        projectile_spread_modifier={'single projectile': 1.0},
        barrel_length=17.75,
        gun_type='rifle'
    )
)

m1carb_dict = {
    "guns": {
        "automatic rifles": {
            "M1 Carbine": {
                "required parts": {
                    "M1 Carbine Reciever": 1,
                    "M1/M2 Carbine Stock": 1,
                    "M1/M2 Carbine Barrel": 1,
                },
                "compatible parts": {
                    "M1/M2 Carbine Optic Mount": 1,
                    "Attachment Adapter": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": m1_carbine
            },
        }
    },
}

m2carb_dict = {
    "guns": {
        "automatic rifles": {
            "M2 Carbine": {
                "required parts": {
                    "M2 Carbine Reciever": 1,
                    "M1/M2 Carbine Stock": 1,
                    "M1/M2 Carbine Barrel": 1,
                },
                "compatible parts": {
                    "M1/M2 Carbine Optic Mount": 1,
                    "Attachment Adapter": 1,
                    "Muzzle Adapter": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": m2_carbine
            },
        }
    },
}