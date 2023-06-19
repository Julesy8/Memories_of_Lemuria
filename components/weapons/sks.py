from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
stocks
"""

stock_sks = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Stock",
    weight=0.70,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   felt_recoil=0.53,
                                   ap_distance_cost_modifier=0.73,
                                   spread_modifier=0.88,
                                   target_acquisition_ap=0.83,
                                   equip_time=1.25,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.88,
                                       'spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.82}),
    description='Wood SKS rifle stock'
)

stock_sks_tapco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS TAPCO Stock",
    weight=1.08,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long'],
                                   optic_mount_properties={'receiver_height_above_bore': 0.079,
                                                           'spread_modifier': 1.1,
                                                           'target_acquisition_ap': 0.86},
                                   additional_required_parts=('AR Stock',),
                                   felt_recoil=0.46,
                                   ap_distance_cost_modifier=0.75,
                                   spread_modifier=0.85,
                                   target_acquisition_ap=0.87,
                                   equip_time=1.3,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.83,
                                       'ap_distance_cost_modifier': 0.9,
                                       'spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.77}),
    description='A polymer rifle stock for the SKS by TAPCO, including a AR-15 stock adapter'
)

stock_sks_dragunov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Dragunov Stock",
    weight=1.01,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   felt_recoil=0.48,
                                   ap_distance_cost_modifier=0.69,
                                   spread_modifier=0.83,
                                   target_acquisition_ap=0.9,
                                   equip_time=1.3,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.89,
                                       'spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.79}),
    description='A polymer Dragunov rifle style stock for the SKS'
)

stock_sks_fab = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS FAB Defense Stock",
    weight=1.36,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   is_attachment_point_types=['Picrail Underbarrel - Short',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Short'],
                                   additional_required_parts=('AR Stock',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.079,
                                                           'spread_modifier': 1.1,
                                                           'target_acquisition_ap': 0.86},
                                   felt_recoil=0.52,
                                   ap_distance_cost_modifier=0.72,
                                   spread_modifier=0.81,
                                   target_acquisition_ap=0.84,
                                   equip_time=1.25,
                                   grip_properties={
                                       'felt_recoil': 0.84,
                                       'ap_distance_cost_modifier': 0.92,
                                       'spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.78}),
    description='A light weight tactical polymer stock for the SKS, including a folding AR-15 stock adapter'
)

stock_sks_sabertooth = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Sabertooth Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long'],
                                   additional_required_parts=('AR Stock', 'AR Grip'),
                                   optic_mount_properties={'receiver_height_above_bore': 0.079,
                                                           'spread_modifier': 1.1,
                                                           'target_acquisition_ap': 0.86},
                                   equip_time=1.1,
                                   grip_properties={
                                       'felt_recoil': 0.88,
                                       'ap_distance_cost_modifier': 0.92,
                                       'spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.78}),
    description='A polymer assault rifle style stock for the SKS, including a AR-15 stock adapter'
)

stock_sks_bullpup = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS SGWorks Bullpup Stock",
    weight=0.93,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long'],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.079},
                                   felt_recoil=0.51,
                                   ap_distance_cost_modifier=0.71,
                                   load_time_modified=1.3,
                                   spread_modifier=0.79,
                                   target_acquisition_ap=0.81,
                                   equip_time=0.9,
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.9,
                                       'spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.8}),
    description='A polymer assault rifle style stock for the SKS, including a AR-15 stock adapter'
)

"""
barrels
"""

barrel_sks = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'spread_modifier': 0.95, },
                                   compatible_magazine_type='SKS Magazine',
                                   barrel_length=20,
                                   is_optic=True,
                                   equip_time=1.1,
                                   velocity_modifier=0.96,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel"
)

barrel_sks_shortened = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel - Shortened",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'spread_modifier': 0.96, },
                                   compatible_magazine_type='SKS Magazine',
                                   barrel_length=17.5,
                                   is_optic=True,
                                   velocity_modifier=0.939,
                                   equip_time=0.9,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a cut down 17.5 inch SKS barrel "
)

barrel_sks_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel (Full-Auto Conversion)",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'spread_modifier': 0.95, },
                                   barrel_length=20,
                                   compatible_magazine_type='SKS Magazine',
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   equip_time=1.1,
                                   velocity_modifier=0.96,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel converted to be capable of fully automatic fire"
)

barrel_sks_shortened_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel - Shortened (Full-Auto Conversion)",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'spread_modifier': 0.96, },
                                   compatible_magazine_type='SKS Magazine',
                                   barrel_length=17.5,
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   equip_time=0.9,
                                   velocity_modifier=0.939,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a cut down 17.5 inch SKS barrel converted to be capable of fully automatic fire"
)

barrel_sks_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel (AK Mag Conversion)",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'spread_modifier': 0.95, },
                                   compatible_magazine='AK 7.62x39',
                                   is_optic=True,
                                   barrel_length=20,
                                   equip_time=1.1,
                                   velocity_modifier=0.96,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel. The magazine well has been converted to accept "
                "7.62x39 Kalashnikov type magazines."
)

barrel_sks_shortened_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel - Shortened (AK Mag Conversion)",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'spread_modifier': 0.96, },
                                   compatible_magazine_type='AK 7.62x39',
                                   is_optic=True,
                                   barrel_length=17.5,
                                   velocity_modifier=0.939,
                                   equip_time=0.9,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a cut down 17.5 inch SKS barrel. The magazine well has been converted to accept "
                "7.62x39 Kalashnikov type magazines."
)

barrel_sks_auto_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel (Full-Auto + AK Mag Conversion)",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'spread_modifier': 0.95, },
                                   compatible_magazine_type='AK 7.62x39',
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   barrel_length=20,
                                   equip_time=1.1,
                                   velocity_modifier=0.96,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel converted to be capable of fully automatic fire. "
                "The magazine well has been converted to accept 7.62x39 Kalashnikov type magazines."
)

barrel_sks_shortened_auto_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Receiver & Barrel - Shortened (Full-Auto + AK Mag Conversion)",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'spread_modifier': 0.96, },
                                   compatible_magazine_type='AK 7.62x39',
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   barrel_length=17.5,
                                   equip_time=0.9,
                                   velocity_modifier=0.939,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a cut down 17.5 inch SKS barrel converted to be capable of fully automatic fire. "
                "The magazine well has been converted to accept 7.62x39 Kalashnikov type magazines."
)

"""
other
"""

sks_integrated_mag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS 10 Round Internal Magazine",
    weight=0.185,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Internal Magazine',
                                   mag_capacity=10,
                                   ),
    description="A standard SKS 10 round internal magazine."
)

sks_optics_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Picatinny Optics Mount",
    weight=0.16,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Optics Mount',
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.5},
                                   ),
    description="Picatinny rail optics mount for the SKS by Matador arms mounting to the receiver"
)

sks = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS",
    weight=1,
    stacking=None,
    description='The SKS is a semi-automatic rifle that was developed by the Soviet Union in the late 1940s. It was '
                'designed to be a modern replacement for the Mosin-Nagant rifle and was adopted by the Soviet '
                'military in 1949 before being replaced by the AK-47 shortly after. It is still widely available '
                'today as a surplus firearm and remains a popular choice among collectors and enthusiasts.',
    usable_properties=GunMagFed(
        chambered_bullet=None,
        keep_round_chambered=False,
        ap_to_equip=75,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}},
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type='7.62x39',
        compatible_clip='SKS Clip',
        velocity_modifier=1.0,
        felt_recoil=1.0,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sound_modifier=1.0,
        zero_range=25,
        receiver_height_above_bore=0.9,
        sight_height_above_bore=0.23,
        spread_modifier=0.05,
        compatible_magazine_type='SKS Magazine',
        gun_type='rifle',
        barrel_length=20
    )
)

sksdict = {
    "guns": {
        "automatic rifles": {
            "SKS Rifle": {
                "required parts": {
                    "SKS Barrel": 1,
                    "SKS Stock": 1,
                },
                "compatible parts": {
                    "SKS Internal Magazine": 1,
                    "Attachment Adapter": 1,
                    "SKS Optics Mount": 1,
                    "Underbarrel Accessory": 1,
                    "Side Mounted Accessory": 1,
                    "Muzzle Device": 1,
                    "Optic": 1
                },
                "item": sks
            },
        }
    },
}
