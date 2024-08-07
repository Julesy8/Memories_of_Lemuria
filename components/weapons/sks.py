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
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Stock",
    weight=0.70,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   felt_recoil=0.48,
                                   ap_distance_cost_modifier=0.73,
                                   handling_spread_modifier=0.88,
                                   target_acquisition_ap=0.83,
                                   ap_to_equip=1.25,
                                   has_stock=True,
                                   accuracy_part=True,
                                   grip_properties={
                                       'felt_recoil': 0.87,
                                       'ap_distance_cost_modifier': 0.88,
                                       'handling_spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.82}),
    description='Wood SKS rifle stock'
)

stock_sks_tapco = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS TAPCO Stock",
    weight=1.08,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long'],
                                   optic_mount_properties={'receiver_height_above_bore': 0.079,
                                                           'handling_spread_modifier': 1.1,
                                                           'target_acquisition_ap': 0.86},
                                   additional_required_parts=('AR Stock',),
                                   suffix='Tactical',
                                   felt_recoil=0.9,
                                   ap_to_equip=1.3,
                                   accuracy_part=True,
                                   has_stock=True,
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.87,
                                       'handling_spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.8}),
    description='A polymer rifle stock for the SKS by TAPCO, including a AR-15 stock adapter and pistol grip'
)

stock_sks_dragunov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Dragunov Stock",
    weight=1.01,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   suffix='Tactical',
                                   felt_recoil=0.44,
                                   ap_to_equip=1.3,
                                   has_stock=True,
                                   accuracy_part=True,
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.87,
                                       'handling_spread_modifier': 0.89,
                                       'target_acquisition_ap': 0.8}),
    description='A polymer Dragunov rifle style stock for the SKS'
)

stock_sks_fab = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS FAB Defense Stock",
    weight=1.36,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   suffix='Tactical',
                                   is_attachment_point_types=['Picrail Underbarrel - Short',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Short'],
                                   additional_required_parts=('AR Stock',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.079,
                                                           'handling_spread_modifier': 1.1,
                                                           'target_acquisition_ap': 0.86},
                                   ap_to_equip=1.3,
                                   accuracy_part=True,
                                   grip_properties={
                                       'felt_recoil': 0.84,
                                       'ap_distance_cost_modifier': 0.87,
                                       'handling_spread_modifier': 0.87,
                                       'target_acquisition_ap': 0.8}),
    description='A light weight tactical polymer stock for the SKS, including a folding AR-15 stock adapter'
)

stock_sks_sabertooth = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Sabertooth Stock",
    weight=1,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   suffix='Tactical',
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long'],
                                   additional_required_parts=('AR Stock', 'AR Grip'),
                                   optic_mount_properties={'receiver_height_above_bore': 0.079,
                                                           'handling_spread_modifier': 1.1,
                                                           'target_acquisition_ap': 0.86},
                                   ap_to_equip=1.1,
                                   accuracy_part=True,
                                   grip_properties={
                                       'felt_recoil': 0.88,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.88,
                                       'target_acquisition_ap': 0.8}),
    description='A polymer assault rifle style stock for the SKS, including a AR-15 stock adapter'
)

stock_sks_bullpup = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS SGWorks Bullpup Stock",
    weight=0.93,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Stock',
                                   suffix='Bullpup',
                                   is_attachment_point_types=['Picrail Underbarrel - Long',
                                                              'Picrail Optics Mount - Long',
                                                              'Picrail Side Mount - Long'],
                                   additional_required_parts=('Optic',),
                                   optic_mount_properties={'receiver_height_above_bore': 0.079},
                                   accuracy_part=True,
                                   felt_recoil=0.45,
                                   ap_distance_cost_modifier=0.71,
                                   load_time_modified=1.3,
                                   handling_spread_modifier=0.79,
                                   target_acquisition_ap=0.81,
                                   ap_to_equip=0.9,
                                   grip_properties={
                                       'felt_recoil': 0.85,
                                       'ap_distance_cost_modifier': 0.9,
                                       'handling_spread_modifier': 0.9,
                                       'target_acquisition_ap': 0.8}),
    description='A polymer assault rifle style stock for the SKS, including a AR-15 stock adapter'
)

"""
barrels
"""

barrel_sks = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'sight_spread_modifier': 0.02, },
                                   compatible_magazine_type=('SKS Magazine', ),
                                   barrel_length=20,
                                   is_optic=True,
                                   ap_to_equip=1.1,
                                   velocity_modifier={'7.62x39': 0.96},
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel"
)

barrel_sks_shortened = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel - Shortened",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   suffix='Short Barrel',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'sight_spread_modifier': 0.02, },
                                   compatible_magazine_type=('SKS Magazine', ),
                                   barrel_length=17.5,
                                   is_optic=True,
                                   velocity_modifier={'7.62x39': 0.939},
                                   ap_to_equip=0.9,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a cut down 17.5 inch SKS barrel "
)

barrel_sks_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel (Full-Auto Conversion)",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   suffix='Full-Auto',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'sight_spread_modifier': 0.02, },
                                   barrel_length=20,
                                   compatible_magazine_type=('SKS Magazine', ),
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   ap_to_equip=1.1,
                                   velocity_modifier={'7.62x39': 0.96},
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel converted to be capable of fully automatic fire"
)

barrel_sks_shortened_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel - Shortened (Full-Auto Conversion)",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   suffix='Short Barrel Full-Auto',
                                   incompatibilities=(("Iron Sight",),),
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'sight_spread_modifier': 0.02, },
                                   compatible_magazine_type=('SKS Magazine', ),
                                   barrel_length=17.5,
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   ap_to_equip=0.9,
                                   velocity_modifier={'7.62x39': 0.939},
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a cut down 17.5 inch SKS barrel converted to be capable of fully automatic fire"
)

barrel_sks_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel (AK Mag Conversion)",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   suffix='AK Mag Conversion',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'sight_spread_modifier': 0.02, },
                                   compatible_magazine_type=('AK 7.62x39',),
                                   is_optic=True,
                                   barrel_length=20,
                                   ap_to_equip=1.1,
                                   velocity_modifier={'7.62x39': 0.96},
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel. The magazine well has been converted to accept "
                "7.62x39 Kalashnikov type magazines."
)

barrel_sks_shortened_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel - Shortened (AK Mag Conversion)",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   suffix='Short Barrel AK Mag Conversion',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'sight_spread_modifier': 0.02, },
                                   compatible_magazine_type=('AK 7.62x39',),
                                   is_optic=True,
                                   barrel_length=17.5,
                                   velocity_modifier={'7.62x39': 0.939},
                                   ap_to_equip=0.9,
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a cut down 17.5 inch SKS barrel. The magazine well has been converted to accept "
                "7.62x39 Kalashnikov type magazines."
)

barrel_sks_auto_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel (Full-Auto + AK Mag Conversion)",
    weight=2.965,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   suffix='AK Mag Conversion Full-Auto',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.09,
                                                     'ap_distance_cost_modifier': 0.94,
                                                     'sight_spread_modifier': 0.02, },
                                   compatible_magazine_type=('AK 7.62x39',),
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   barrel_length=20,
                                   ap_to_equip=1.1,
                                   velocity_modifier={'7.62x39': 0.96},
                                   accuracy_part=True,
                                   functional_part=True,
                                   ),
    description="An SKS receiver with a standard 20 inch SKS barrel converted to be capable of fully automatic fire. "
                "The magazine well has been converted to accept 7.62x39 Kalashnikov type magazines."
)

barrel_sks_shortened_auto_akmag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Receiver & Barrel - Shortened (Full-Auto + AK Mag Conversion)",
    weight=2.715,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Barrel',
                                   suffix='Short Barrel AK Mag Conversion Full-Auto',
                                   incompatibilities=(("Iron Sight",),),
                                   compatible_parts={'SKS Internal Magazine': []},
                                   is_attachment_point_types=['SKS Muzzle', ],
                                   optic_properties={'target_acquisition_ap': 1.06,
                                                     'ap_distance_cost_modifier': 0.95,
                                                     'sight_spread_modifier': 0.02, },
                                   compatible_magazine_type=('AK 7.62x39',),
                                   is_optic=True,
                                   fire_modes={'automatic': {'fire rate': 750, 'automatic': True}},
                                   barrel_length=17.5,
                                   ap_to_equip=0.9,
                                   velocity_modifier={'7.62x39': 0.939},
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
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS 10 Round Internal Magazine",
    weight=0.185,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Internal Magazine',
                                   mag_capacity=10,
                                   keep_round_chambered=False,
                                   ),
    description="A standard SKS 10 round internal magazine."
)

sks_optics_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_MAGENTA,
    name="SKS Picatinny Optics Mount",
    weight=0.16,
    stacking=None,
    usable_properties=GunComponent(part_type='SKS Optics Mount',
                                   additional_required_parts=('Optic',),
                                   is_attachment_point_types=['Picrail Optics Mount - Long', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.5},
                                   ),
    description="Picatinny rail optics mount for the SKS by Matador arms mounting to the receiver"
)

sks = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_BROWN,
    name="SKS",
    weight=1,
    stacking=None,
    description='The SKS is a semi-automatic rifle that was developed by the Soviet Union in the late 1940s. It was '
                'designed to be a modern replacement for the Mosin-Nagant rifle and was adopted by the Soviet '
                'military in 1949 before being replaced by the AK-47 shortly after. It is still widely available '
                'today as a surplus firearm and remains a popular choice among collectors and enthusiasts.',
    usable_properties=GunMagFed(
        chambered_bullet=None,
        keep_round_chambered=True,
        can_hand_load=True,
        ap_to_equip=100,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False}},
        current_fire_mode='single shot',
        parts=Parts(),
        compatible_bullet_type=('7.62x39',),
        compatible_clip='SKS Clip',
        velocity_modifier={'single projectile': 1.0},
        felt_recoil=1.0,
        target_acquisition_ap=50,
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        sound_modifier=1.0,
        zero_range=109,
        receiver_height_above_bore=0.9,
        sight_height_above_bore=0.23,
        sight_spread_modifier=1.0,
        handling_spread_modifier=4.0,
        projectile_spread_modifier={'single projectile': 1.0},
        compatible_magazine_type=('SKS Magazine',),
        gun_type='rifle',
        action_type='semi-auto rifle',
        barrel_length=20
    )
)
