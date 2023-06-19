from entity import Item
from components.consumables import GunMagFed, GunComponent
from components.gunparts import Parts
import colour

"""
FRAMES
"""

# SEMI-AUTO

m1911_frame_gov_ss = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Frame - SS",
    weight=0.53,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                                               'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}, },
                                   ),
    description='An unramped stainless steel full-sized frame for 1911 Government/Commander type handguns.'
)

m1911_frame_gov_alloy = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Frame - Alloy",
    weight=0.332,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                                               'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}, },
                                   ),
    description='An unramped full-sized frame for 1911 Government/Commander type handguns. Made of aluminium alloy, '
                'it is considerably lighter than a steel frame.'
)

m1911_frame_gov_ss_tac = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Frame Tactical - SS",
    weight=0.578,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   is_attachment_point_types=['Picrail Underbarrel - Short', ],
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                                               'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}, },
                                   ),
    description='An unramped stainless steel full-sized frame for 1911 Government/Commander type handguns. This '
                'tactical variant also has a picatinny rail attachment point for attachment of under barrel '
                'accessories such as flash lights and lasers.'
)

m1911_frame_gov_alloy_tac = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Frame - Alloy",
    weight=0.361,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   is_attachment_point_types=['Picrail Underbarrel - Short', ],
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                                               'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}, },
                                   ),
    description='An unramped full-sized frame for 1911 Government/Commander type handguns. Made of aluminium alloy, '
                'it is considerably lighter than a steel frame. This tactical variant also has a picatinny rail '
                'attachment point for attachment of under barrel accessories such as flash lights and lasers.'
)

# FULL AUTO

m1911_frame_gov_ss_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Full-Auto Frame - SS",
    weight=0.53,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'automatic': {'fire rate': 1000, 'automatic': True}},
                                   prefix='Full-Auto',
                                   ),
    description='An unramped stainless steel full-sized frame for 1911 Government/Commander type handguns. The action '
                'and trigger group have been modified, allowing fully automatic fire.'
)

m1911_frame_gov_alloy_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Full-Auto Frame - Alloy",
    weight=0.332,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'automatic': {'fire rate': 1000, 'automatic': True}},
                                   prefix='Full-Auto',
                                   ),
    description='An unramped full-sized frame for 1911 Government/Commander type handguns. Made of aluminium alloy, '
                'it is considerably lighter than a steel frame. The action and trigger group have been modified, '
                'allowing fully automatic fire.'
)

m1911_frame_gov_ss_tac_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Full-Auto Frame Tactical - SS",
    weight=0.578,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   is_attachment_point_types=['Picrail Underbarrel - Short', ],
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'automatic': {'fire rate': 1000, 'automatic': True}},
                                   prefix='Full-Auto',
                                   ),
    description='An unramped stainless steel full-sized frame for 1911 Government/Commander type handguns. This '
                'tactical variant also has a picatinny rail attachment point for attachment of under barrel '
                'accessories such as flash lights and lasers. The action and trigger group have been modified,'
                ' allowing fully automatic fire.'
)

m1911_frame_gov_alloy_tac_auto = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 Full-Auto Frame - Alloy",
    weight=0.361,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Frame',
                                   is_attachment_point_types=['Picrail Underbarrel - Short', ],
                                   incompatibilities=(("Iron Sight",),),
                                   functional_part=True,
                                   fire_modes={'automatic': {'fire rate': 1000, 'automatic': True}},
                                   prefix='Full-Auto',
                                   ),
    description='An unramped full-sized frame for 1911 Government/Commander type handguns. Made of aluminium alloy, '
                'it is considerably lighter than a steel frame. This tactical variant also has a picatinny rail '
                'attachment point for attachment of under barrel accessories such as flash lights and lasers.'
)

"""
BARRELS
"""

""".45"""

# STANDARD

m1911_barrel_gov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 5 Inch Barrel 'Government'",
    weight=0.113,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['.45 Government Length Slide']},
                                   tags=['.45 Government Length Barrel', ],
                                   compatible_magazine_type='1911 .45 ACP',
                                   compatible_bullet_type='.45 ACP',
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type .45 ACP barrel for M1911 handguns.'
)

m1911_barrel_commander = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 4 Inch Barrel 'Commander'",
    weight=0.104,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['.45 Commander Length Slide', '.45 Government Length Slide']},
                                   tags=['.45 Commander Length Barrel', ],
                                   compatible_magazine_type='1911 .45 ACP',
                                   compatible_bullet_type='.45 ACP',
                                   velocity_modifier=0.96,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type .45 ACP barrel for M1911 handguns.'
)

m1911_barrel_long = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 6 Inch Long Barrel",
    weight=0.131,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['.45 Commander Length Slide', '.45 Government Length Slide',
                                                       '.45 Long SLide']},
                                   tags=['.45 Long Barrel', ],
                                   compatible_magazine_type='1911 .45 ACP',
                                   compatible_bullet_type='.45 ACP',
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   velocity_modifier=1.049,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type .45 ACP barrel for M1911 handguns.'
)

# THREADED

m1911_barrel_gov_threaded = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 5 Inch Barrel 'Government' - Threaded",
    weight=0.113,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28', ],
                                   compatible_parts={
                                       'M1911 Slide': ['.45 Government Length Slide']},
                                   tags=['.45 Government Length Barrel', ],
                                   compatible_magazine_type='1911 .45 ACP',
                                   compatible_bullet_type='.45 ACP',
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type .45 ACP barrel for M1911 handguns. It has been threaded to'
                'accept a suppressor or other muzzle device.'
)

m1911_barrel_commander_threaded = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 4 Inch Barrel 'Commander' - Threaded",
    weight=0.104,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28', ],
                                   compatible_parts={
                                       'M1911 Slide': ['.45 Commander Length Slide', '.45 Government Length Slide']},
                                   tags=['.45 Commander Length Barrel', ],
                                   compatible_magazine_type='1911 .45 ACP',
                                   compatible_bullet_type='.45 ACP',
                                   velocity_modifier=1.049,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type .45 ACP barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)

m1911_barrel_long_threaded = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 6 Inch Long Barrel - Threaded",
    weight=0.131,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread .578x28', ],
                                   compatible_parts={
                                       'M1911 Slide': ['.45 Commander Length Slide', '.45 Government Length Slide',
                                                       '.45 Long SLide']},
                                   tags=['.45 Long Barrel', ],
                                   compatible_magazine_type='1911 .45 ACP',
                                   compatible_bullet_type='.45 ACP',
                                   velocity_modifier=1.049,
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type .45 ACP barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)


"""9mm"""

# STANDARD

m1911_barrel_gov_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 5 Inch Barrel 'Government'",
    weight=0.163,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['9mm Government Length Slide']},
                                   tags=['9mm Government Length Barrel', ],
                                   compatible_magazine_type='1911 9mm',
                                   compatible_bullet_type='9mm',
                                   barrel_length=5,
                                   velocity_modifier=1.0658,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type 9mm luger barrel for M1911 handguns.'
)

m1911_barrel_commander_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 4 Inch Barrel 'Commander'",
    weight=0.145,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['9mm Commander Length Slide', '9mm Government Length Slide']},
                                   tags=['9mm Commander Length Barrel', ],
                                   compatible_magazine_type='1911 9mm',
                                   compatible_bullet_type='9mm',
                                   barrel_length=4,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type 9mm luger barrel for M1911 handguns.'
)

m1911_barrel_long_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 6 Inch Long Barrel",
    weight=0.167,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['9mm Commander Length Slide', '9mm Government Length Slide',
                                                       '9mm Long SLide']},
                                   tags=['9mm Long Barrel', ],
                                   compatible_magazine_type='1911 9mm',
                                   compatible_bullet_type='9mm',
                                   barrel_length=6,
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   velocity_modifier=1.0859,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type 9mm luger barrel for M1911 handguns.'
)

# THREADED

m1911_barrel_gov_threaded_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 5 Inch Barrel 'Government' - Threaded",
    weight=0.163,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={
                                       'M1911 Slide': ['9mm Government Length Slide']},
                                   tags=['9mm Government Length Barrel', ],
                                   compatible_magazine_type='1911 9mm',
                                   compatible_bullet_type='9mm',
                                   barrel_length=5,
                                   velocity_modifier=1.0658,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type 9mm luger barrel for M1911 handguns. It has been '
                'threaded to accept a suppressor or other muzzle device.'
)

m1911_barrel_commander_threaded_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 4 Inch Barrel 'Commander' - Threaded",
    weight=0.145,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={
                                       'M1911 Slide': ['9mm Commander Length Slide', '9mm Government Length Slide']},
                                   tags=['9mm Commander Length Barrel', ],
                                   compatible_magazine_type='1911 9mm',
                                   compatible_bullet_type='9mm',
                                   barrel_length=4,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type  9mm luger barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)

m1911_barrel_long_threaded_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 6 Inch Long Barrel - Threaded",
    weight=0.167,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 1/2x28', ],
                                   compatible_parts={
                                       'M1911 Slide': ['9mm Commander Length Slide', '9mm Government Length Slide',
                                                       '9mm Long SLide']},
                                   tags=['9mm Long Barrel', ],
                                   barrel_length=6,
                                   compatible_magazine_type='1911 9mm',
                                   compatible_bullet_type='9mm',
                                   velocity_modifier=1.0859,
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type  9mm luger barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)

"""10mm"""

# STANDARD

m1911_barrel_gov_10mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm 5 Inch Barrel 'Government'",
    weight=0.163,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Government Length Slide']},
                                   tags=['10mm Government Length Barrel', ],
                                   compatible_magazine_type='1911 10mm',
                                   compatible_bullet_type='10mm',
                                   barrel_length=5,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type 10mm barrel for M1911 handguns.'
)

m1911_barrel_commander_10mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm 4 Inch Barrel 'Commander'",
    weight=0.145,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide']},
                                   tags=['10mm Commander Length Barrel', ],
                                   compatible_magazine_type='1911 10mm',
                                   compatible_bullet_type='10mm',
                                   barrel_length=4,
                                   velocity_modifier=0.94,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type 10mm barrel for M1911 handguns.'
)

m1911_barrel_long_10mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm 6 Inch Long Barrel",
    weight=0.167,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide',
                                                       '10mm/40 S&W Long SLide']},
                                   tags=['10mm Long Barrel', ],
                                   compatible_magazine_type='1911 10mm',
                                   compatible_bullet_type='10mm',
                                   barrel_length=6,
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   velocity_modifier=1.0318,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type 10mm barrel for M1911 handguns.'
)

# THREADED

m1911_barrel_gov_threaded_10mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm 5 Inch Barrel 'Government' - Threaded",
    weight=0.163,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],  # TODO - add attachments for this
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Government Length Slide']},
                                   tags=['10mm Government Length Barrel', ],
                                   compatible_magazine_type='1911 10mm',
                                   compatible_bullet_type='10mm',
                                   barrel_length=5,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type 10mm barrel for M1911 handguns. It has been '
                'threaded to accept a suppressor or other muzzle device.'
)

m1911_barrel_commander_threaded_10mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm 4 Inch Barrel 'Commander' - Threaded",
    weight=0.145,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide']},
                                   tags=['10mm Commander Length Barrel', ],
                                   compatible_magazine_type='1911 10mm',
                                   compatible_bullet_type='10mm',
                                   barrel_length=4,
                                   velocity_modifier=0.94,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type 10mm barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)

m1911_barrel_long_threaded_10mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm 6 Inch Long Barrel - Threaded",
    weight=0.167,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide',
                                                       '10mm/40 S&W Long SLide']},
                                   tags=['10mm Long Barrel', ],
                                   compatible_magazine_type='1911 10mm',
                                   compatible_bullet_type='10mm',
                                   barrel_length=6,
                                   velocity_modifier=1.0318,
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type 10mm barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)

"""40 S&W"""

# STANDARD

m1911_barrel_gov_40sw = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 40 S&W 5 Inch Barrel 'Government'",
    weight=0.163,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Government Length Slide']},
                                   tags=['40 S&W Government Length Barrel', ],
                                   compatible_magazine_type='1911 40 S&W',
                                   compatible_bullet_type='40 S&W',
                                   barrel_length=5,
                                   velocity_modifier=1.0508,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type 40 S&W barrel for M1911 handguns.'
)

m1911_barrel_commander_40sw = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 40 S&W 4 Inch Barrel 'Commander'",
    weight=0.145,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide']},
                                   tags=['40 S&W Commander Length Barrel', ],
                                   compatible_magazine_type='1911 40 S&W',
                                   compatible_bullet_type='40 S&W',
                                   barrel_length=4,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type 40 S&W barrel for M1911 handguns.'
)

m1911_barrel_long_40sw = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 40 S&W 6 Inch Long Barrel",
    weight=0.167,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide',
                                                       '10mm/40 S&W Long SLide']},
                                   tags=['40 S&W Long Barrel', ],
                                   compatible_magazine_type='1911 40 S&W',
                                   compatible_bullet_type='40 S&W',
                                   barrel_length=6,
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   velocity_modifier=1.0806,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type 40 S&W barrel for M1911 handguns.'
)

# THREADED

m1911_barrel_gov_threaded_40sw = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 40 S&W 5 Inch Barrel 'Government' - Threaded",
    weight=0.163,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Government Length Slide']},
                                   tags=['40 S&W Government Length Barrel', ],
                                   compatible_magazine_type='1911 40 S&W',
                                   compatible_bullet_type='40 S&W',
                                   barrel_length=5,
                                   velocity_modifier=1.0508,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped full length 5 inch Government type 40 S&W barrel for M1911 handguns. It has been '
                'threaded to accept a suppressor or other muzzle device.'
)

m1911_barrel_commander_threaded_40sw = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 40 S&W 4 Inch Barrel 'Commander' - Threaded",
    weight=0.145,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide']},
                                   tags=['40 S&W Commander Length Barrel', ],
                                   compatible_magazine_type='1911 40 S&W',
                                   compatible_bullet_type='40 S&W',
                                   barrel_length=4,
                                   target_acquisition_ap=0.98,
                                   equip_time=0.97,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 4 inch Commander type 10mm barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)

m1911_barrel_long_threaded_40sw = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 40 S&W 6 Inch Long Barrel - Threaded",
    weight=0.167,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Barrel',
                                   is_attachment_point_types=['Barrel Thread 9/16x24', ],
                                   compatible_parts={
                                       'M1911 Slide': ['10mm/40 S&W Commander Length Slide',
                                                       '10mm/40 S&W Government Length Slide',
                                                       '10mm/40 S&W Long SLide']},
                                   tags=['40 S&W Long Barrel', ],
                                   compatible_magazine_type='1911 40 S&W',
                                   compatible_bullet_type='40 S&W',
                                   barrel_length=6,
                                   velocity_modifier=1.0806,
                                   target_acquisition_ap=1.02,
                                   equip_time=1.03,
                                   accuracy_part=True,
                                   short_barrel=True
                                   ),
    description='A ramped 6 inch Long type 40 S&W barrel for M1911 handguns. It has been threaded to accept a '
                'suppressor or other muzzle device.'
)


"""
SLIDES
"""

""".45"""

# STANDARD

m1911_slide_gov = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Government' Slide",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['.45 Government Length Slide', ],
                                   suffix='Government',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for .45 ACP M1911 pistols.'
)

m1911_slide_commander = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Commander' Slide",
    weight=0.272,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', ],
                                   tags=['.45 Commander Length Slide', ],
                                   suffix='Commander',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel Commander type slide for .45 ACP M1911 pistols.'
)

m1911_slide_long = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP Long Slide",
    weight=0.425,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['.45 Long Slide', ],
                                   suffix='Long Slide',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for .45 ACP M1911 pistols.'
)

# LIGHTENED

m1911_slide_gov_light = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Government' Slide - Custom",
    weight=0.311,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['.45 Government Length Slide', ],
                                   suffix='Government',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for .45 ACP M1911 pistols. Sections have been '
                'milled out to make it both lighter and more aesthetically pleasing.'
)

m1911_slide_commander_light = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Commander' Slide - Custom",
    weight=0.237,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', ],
                                   tags=['.45 Commander Length Slide', ],
                                   suffix='Commander',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel shortened Commander type slide for .45 ACP M1911 pistols. Sections have '
                'been milled out to make it both lighter and more aesthetically pleasing.'
)

m1911_slide_long_light = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP Long Slide - Custom",
    weight=0.370,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['.45 Long Slide', ],
                                   suffix='Long Slide',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for .45 ACP M1911 pistols. Sections have been milled out to make it both '
                'lighter and more aesthetically pleasing.'
)


"""9mm"""

# STANDARD

m1911_slide_gov_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Government' Slide",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['9mm Government Length Slide', ],
                                   suffix='Government',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 9mm luger M1911 pistols.'
)

m1911_slide_commander_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Commander' Slide",
    weight=0.272,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', ],
                                   tags=['9mm Commander Length Slide', ],
                                   suffix='Commander',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel Commander type slide for 9mm luger M1911 pistols.'
)

m1911_slide_long_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm Long Slide",
    weight=0.425,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['9mm Long Slide', ],
                                   suffix='Long Slide',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 9mm luger M1911 pistols.'
)

# LIGHTENED

m1911_slide_gov_light_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Government' Slide - Custom",
    weight=0.311,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['9mm Government Length Slide', ],
                                   suffix='Government',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 9mm luger M1911 pistols. Sections have been '
                'milled out to make it both lighter and more aesthetically pleasing.'
)

m1911_slide_commander_light_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Commander' Slide - Custom",
    weight=0.237,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', ],
                                   tags=['9mm Commander Length Slide', ],
                                   suffix='Commander',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel shortened Commander type slide for 9mm luger M1911 pistols. Sections '
                'have been milled out to make it both lighter and more aesthetically pleasing.'
)

m1911_slide_long_light_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm Long Slide - Custom",
    weight=0.370,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['9mm Long Slide', ],
                                   suffix='Long Slide',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 9mm luger M1911 pistols. Sections have been milled out to make it '
                'both lighter and more aesthetically pleasing.'
)

"""10mm/40s&w"""

# STANDARD

m1911_slide_gov_40 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Government' Slide",
    weight=0.363,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['10mm/40 S&W Government Length Slide', ],
                                   suffix='Government',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 10mm/40 S&W M1911 pistols.'
)

m1911_slide_commander_40 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Commander' Slide",
    weight=0.276,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', ],
                                   tags=['10mm/40 S&W Commander Length Slide', ],
                                   suffix='Commander',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel Commander type slide for 10mm/40 S&W M1911 pistols.'
)

m1911_slide_long_40 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W ACP Long Slide",
    weight=0.432,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['10mm/40 S&W Long Slide', ],
                                   suffix='Long Slide',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 10mm/40 S&W M1911 pistols.'
)

# LIGHTENED

m1911_slide_gov_light_40 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Government' Slide - Custom",
    weight=0.316,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['10mm/40 S&W Government Length Slide', ],
                                   suffix='Government',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 10mm/40 S&W M1911 pistols. Sections have been '
                'milled out to make it both lighter and more aesthetically pleasing.'
)

m1911_slide_commander_light_40 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Commander' Slide - Custom",
    weight=0.240,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', ],
                                   tags=['10mm/40 S&W Commander Length Slide', ],
                                   suffix='Commander',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel shortened Commander type slide for 10mm/40 S&W M1911 pistols. Sections '
                'have been milled out to make it both lighter and more aesthetically pleasing.'
)

m1911_slide_long_light_40 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W Long Slide - Custom",
    weight=0.376,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', ],
                                   tags=['10mm/40 S&W Long Slide', ],
                                   suffix='Long Slide',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 10mm/40 S&W M1911 pistols. Sections have been milled out to make it '
                'both lighter and more aesthetically pleasing.'
)

"""OPTICS CUT SLIDE"""


""".45"""

# STANDARD

m1911_slide_gov_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Government' Slide",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['.45 Government Length Slide', ],
                                   suffix='Government',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for .45 ACP M1911 pistols. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_commander_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Commander' Slide",
    weight=0.272,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['.45 Commander Length Slide', ],
                                   suffix='Commander',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel Commander type slide for .45 ACP M1911 pistols. Includes an optics cut '
                'for mounting of pistol optics.'
)

m1911_slide_long_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP Long Slide",
    weight=0.425,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['.45 Long Slide', ],
                                   suffix='Long Slide',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for .45 ACP M1911 pistols. Includes an optics cut for mounting of '
                'pistol optics.'
)

# LIGHTENED

m1911_slide_gov_light_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Government' Slide - Custom",
    weight=0.311,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['.45 Government Length Slide', ],
                                   suffix='Government',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for .45 ACP M1911 pistols. Sections have been '
                'milled out to make it both lighter and more aesthetically pleasing. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_commander_light_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP 'Commander' Slide - Custom",
    weight=0.237,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['.45 Commander Length Slide', ],
                                   suffix='Commander',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel shortened Commander type slide for .45 ACP M1911 pistols. Sections have '
                'been milled out to make it both lighter and more aesthetically pleasing. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_long_light_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 .45 ACP Long Slide - Custom",
    weight=0.370,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['.45 Long Slide', ],
                                   suffix='Long Slide',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for .45 ACP M1911 pistols. Sections have been milled out to make it both '
                'lighter and more aesthetically pleasing. Includes an optics cut for mounting of pistol optics.'
)


"""9mm"""

# STANDARD

m1911_slide_gov_9mm_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Government' Slide w/ Optic Cut",
    weight=0.357,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['9mm Government Length Slide', ],
                                   suffix='Government',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 9mm luger M1911 pistols. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_commander_9mm_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Commander' Slide w/ Optic Cut",
    weight=0.272,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['9mm Commander Length Slide', ],
                                   suffix='Commander',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel Commander type slide for 9mm luger M1911 pistols. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_long_9mm_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm Long Slide w/ Optic Cut",
    weight=0.425,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['9mm Long Slide', ],
                                   suffix='Long Slide',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 9mm luger M1911 pistols. '
                'Includes an optics cut for mounting of pistol optics.'
)

# LIGHTENED

m1911_slide_gov_light_9mm_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Government' Slide - Custom w/ Optic Cut",
    weight=0.311,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['9mm Government Length Slide', ],
                                   suffix='Government',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 9mm luger M1911 pistols. Sections have been '
                'milled out to make it both lighter and more aesthetically pleasing. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_commander_light_9mm_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm 'Commander' Slide - Custom w/ Optic Cut",
    weight=0.237,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['9mm Commander Length Slide', ],
                                   suffix='Commander',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel shortened Commander type slide for 9mm luger M1911 pistols. Sections '
                'have been milled out to make it both lighter and more aesthetically pleasing. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_long_light_9mm_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 9mm Long Slide - Custom w/ Optic Cut",
    weight=0.370,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['9mm Long Slide', ],
                                   suffix='Long Slide',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 9mm luger M1911 pistols. Sections have been milled out to make it '
                'both lighter and more aesthetically pleasing. Includes an optics cut for mounting of pistol optics.'
)

"""10mm/40s&w"""

# STANDARD

m1911_slide_gov_40_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Government' Slide w/ Optic Cut",
    weight=0.363,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['10mm/40 S&W Government Length Slide', ],
                                   suffix='Government',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 10mm/40 S&W M1911 pistols. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_commander_40_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Commander' Slide w/ Optic Cut",
    weight=0.276,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['10mm/40 S&W Commander Length Slide', ],
                                   suffix='Commander',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel Commander type slide for 10mm/40 S&W M1911 pistols. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_long_40_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W ACP Long Slide w/ Optic Cut",
    weight=0.432,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['10mm/40 S&W Long Slide', ],
                                   suffix='Long Slide',
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 10mm/40 S&W M1911 pistols. '
                'Includes an optics cut for mounting of pistol optics.'
)

# LIGHTENED

m1911_slide_gov_light_40_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Government' Slide - Custom w/ Optic Cut",
    weight=0.316,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.92,
                                                     'ap_distance_cost_modifier': 1.08,
                                                     'spread_modifier': 1.1, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['10mm/40 S&W Government Length Slide', ],
                                   suffix='Government',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A full length stainless steel Government type slide for 10mm/40 S&W M1911 pistols. Sections have been '
                'milled out to make it both lighter and more aesthetically pleasing. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_commander_light_40_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W 'Commander' Slide - Custom w/ Optic Cut",
    weight=0.240,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.91,
                                                     'ap_distance_cost_modifier': 1.09,
                                                     'spread_modifier': 1.12, },
                                   is_attachment_point_types=['Commander Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['10mm/40 S&W Commander Length Slide', ],
                                   suffix='Commander',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A shortened stainless steel shortened Commander type slide for 10mm/40 S&W M1911 pistols. Sections '
                'have been milled out to make it both lighter and more aesthetically pleasing. '
                'Includes an optics cut for mounting of pistol optics.'
)

m1911_slide_long_light_40_optic = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 10mm/40 S&W Long Slide - Custom w/ Optic Cut",
    weight=0.376,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Slide',
                                   optic_properties={'target_acquisition_ap': 0.93,
                                                     'ap_distance_cost_modifier': 1.07,
                                                     'spread_modifier': 1.09, },
                                   is_attachment_point_types=['Government Barrel Bushing', 'Pistol Optics Mount', ],
                                   tags=['10mm/40 S&W Long Slide', ],
                                   suffix='Long Slide',
                                   fire_rate_modifier=1.1,
                                   is_optic=True,
                                   functional_part=True,
                                   accuracy_part=True
                                   ),
    description='A stainless steel long slide for 10mm/40 S&W M1911 pistols. Sections have been milled out to make it '
                'both lighter and more aesthetically pleasing. Includes an optics cut for mounting of pistol optics.'
)


"""
Grip Panels
"""

m1911_grip_magpul = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Magpul MOE 1911 Grip Panels",
    weight=0.0311,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Grip Panels',
                                   target_acquisition_ap=0.96,
                                   ),
    description='Polymer grip panels for 1911 pistols designed by Magpul.'
)

m1911_grip_rectac = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Recover Tactica GR11l 1911 Grip Panels",
    weight=0.034,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Grip Panels',
                                   felt_recoil=0.98,
                                   spread_modifier=0.97
                                   ),
    description='Ergonomic rubber pistol grip panels for 1911 pistols designed by Recover Tactical.'
)

m1911_grip_wood = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Wooden 1911 Grip Panels",
    weight=0.0302,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Grip Panels',
                                   ),
    description='Wooden 1911 grip panels styled after those originally issued with 1911 pistols.'
)

m1911_grip_operator = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="VZ Operator II 1911 Grip Panels",
    weight=0.0618,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Grip Panels',
                                   spread_modifier=0.97,
                                   target_acquisition_ap=0.98,
                                   ),
    description='Textured G-10 laminate 1911 grip panels designed by VZ, including an ergonomic thumb notch.'
)

m1911_grip_palmswell = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="VZ Palm Swell 1911 Grip Panels",
    weight=0.0697,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Grip Panels',
                                   felt_recoil=0.97,
                                   target_acquisition_ap=0.99,
                                   ),
    description='G-10 laminate 1911 grip panels designed by VZ. The lower half of the panels are slightly raised, '
                'giving it a more ergonomic feel.'
)

m1911_grip_hogue = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Hogue Rubber 1911 Grip",
    weight=0.077,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Grip Panels',
                                   felt_recoil=0.96,
                                   ),
    description='Rubber 1911 grip designed by hogue. Includes ergonomic finger grooves which wrap around '
                'the front of the grip.'
)

m1911_rec_stock = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Recover Tactical 20/11 1911 Stabilizer Kit",
    weight=0.720,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Grip Panels',
                                   felt_recoil=0.87,
                                   equip_time=1.2,
                                   ap_distance_cost_modifier=0.7,
                                   spread_modifier=0.89,
                                   target_acquisition_ap=0.75,
                                   has_stock=True
                                   ),
    description='A polymer side folding stabilizer stock kit by Recover Tactical for 1911 pistols. It attaches by and '
                'replaces the normal 1911 grip panels and also features an under barrel picatinny rail for accessory '
                'mounting.'
)

"""
Muzzle Devices
"""

m1911_comp_tj = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 TJ's Custom Muzzle Brake",
    weight=0.198,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   incompatibilities=(('.45 Government Length Slide', '.45 Long Barrel'),
                                                      ('.45 Long Slide', '.45 Government Length Barrel'),
                                                      ('9mm Government Length Slide', '9mm Long Barrel'),
                                                      ('9mm Long Slide', '9mm Government Length Barrel'),
                                                      ('10mm/40 S&W Government Length Slide', '10mm Long Barrel'),
                                                      ('10mm/40 S&W Long Slide', '10mm Government Length Barrel'),
                                                      ('10mm/40 S&W Government Length Slide', '40S&W Long Barrel'),
                                                      ('10mm/40 S&W Long Slide', '40S&W Government Length Barrel'),),
                                   attachment_point_required=('Government Barrel Bushing',),
                                   muzzle_break_efficiency=0.4,
                                   target_acquisition_ap=1.03,
                                   sound_radius=1.11,
                                   ),
    description="A large, 3 inch steel muzzle brake for 1911 government and long slide type pistols designed by TJ's "
                "Custom gunworks. There are eight slots machined into the top to reduce muzzle climb."
)

m1911_comp_punisher = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 VD Punisher Muzzle Brake",
    weight=0.066,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   incompatibilities=(('.45 Government Length Slide', '.45 Long Barrel'),
                                                      ('.45 Long Slide', '.45 Government Length Barrel'),
                                                      ('9mm Government Length Slide', '9mm Long Barrel'),
                                                      ('9mm Long Slide', '9mm Government Length Barrel'),
                                                      ('10mm/40 S&W Government Length Slide', '10mm Long Barrel'),
                                                      ('10mm/40 S&W Long Slide', '10mm Government Length Barrel'),
                                                      ('10mm/40 S&W Government Length Slide', '40S&W Long Barrel'),
                                                      ('10mm/40 S&W Long Slide', '40S&W Government Length Barrel'),),
                                   attachment_point_required=('Government Barrel Bushing',),
                                   muzzle_break_efficiency=0.24,
                                   target_acquisition_ap=1.02,
                                   sound_radius=1.08,
                                   ),
    description='A steel muzzle brake for 1911 government and long slide type pistols designed by Valkyrie Dynamics. '
                'There are three slots machined into the top to reduce muzzle climb.'
)

m1911_comp_predator = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 VD Predator Muzzle Brake",
    weight=0.066,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   incompatibilities=(('.45 Commander Length Slide', '.45 Government Length Barrel'),
                                                      ('.45 Commander Length Slide', '.45 Long Barrel'),
                                                      ('9mm Commander Length Slide', '9mm Government Length Barrel'),
                                                      ('9mm Commander Length Slide', '9mm Long Barrel'),
                                                      ('10mm/40 S&W Commander Length Slide',
                                                       '10mm Government Length Barrel'),
                                                      ('10mm/40 S&W Commander Length Slide', '10mm Long Barrel'),
                                                      ('10mm/40 S&W Commander Length Slide',
                                                       '40S&W Government Length Barrel'),
                                                      ('10mm/40 S&W Commander Length Slide', '40S&W Long Barrel'),),
                                   attachment_point_required=('Commander Barrel Bushing',),
                                   muzzle_break_efficiency=0.24,
                                   target_acquisition_ap=1.02,
                                   sound_radius=1.08,
                                   ),
    description='A steel muzzle brake for 1911 commander type pistols designed by Valkyrie Dynamics. '
                'There are three slots machined into the top to reduce muzzle climb.')

m1911_comp_castle = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="1911 VD Castle Muzzle Brake",
    weight=0.0297,
    stacking=None,
    usable_properties=GunComponent(part_type='Muzzle Device',
                                   incompatibilities=(('.45 Government Length Slide', '.45 Commander Length Barrel'),
                                                      ('.45 Government Length Slide', '.45 Long Barrel'),
                                                      ('.45 Long Slide', '.45 Government Length Barrel'),
                                                      ('.45 Long Slide', '.45 Commander Length Barrel'),
                                                      ('10mm/40 S&W Government Length Slide', '10mm Long Barrel'),
                                                      ('10mm/40 S&W Long Slide', '10mm Government Length Barrel'),
                                                      ('10mm/40 S&W Government Length Slide', '40S&W Long Barrel'),
                                                      ('10mm/40 S&W Long Slide', '40S&W Government Length Barrel'),),
                                   attachment_point_required=('Government Barrel Bushing',),
                                   muzzle_break_efficiency=0.21,
                                   sound_radius=1.05,
                                   ),
    description='A cage-style steel muzzle brake for 1911 government and long slide type pistols designed by Valkyrie '
                'Dynamics.'
)

"""
Accessories
"""

# FAB defense GIS
m1911_bridge_mount = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="GSG 1911 Bridge Mount",
    weight=0.077,
    stacking=None,
    usable_properties=GunComponent(part_type='M1911 Optics Mount',
                                   attachment_point_required=('Picrail Underbarrel - Short',
                                                              'Picrail Underbarrel - Long'),
                                   is_attachment_point_types=['Picrail Optics Mount - Short', ],
                                   additional_required_parts=['Optic', ],
                                   optic_mount_properties={'receiver_height_above_bore': 0.263},
                                   ),
    description='An aluminium aftermarket picatinny rail sight mount for 1911 pistols'
)

"""
Gun
"""

m1911 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    name="M1911",
    weight=1.1,
    stacking=None,
    description='The 1911 is a semi-automatic handgun that was designed by John Browning and first introduced in 1911. '
                'It was the standard-issue sidearm for the United States Armed Forces from 1911 to 1985 and remains a '
                'popular firearm to this day.',
    usable_properties=GunMagFed(
        compatible_magazine_type='1911 .45 ACP',
        chambered_bullet=None,
        keep_round_chambered=True,
        loaded_magazine=None,
        ap_to_equip=75,
        fire_modes={'single shot': {'fire rate': 1, 'automatic': False},
                    'rapid fire (semi-auto)': {'fire rate': 3, 'automatic': False}, },
        current_fire_mode='single shot',
        parts=Parts(),
        velocity_modifier=1.0,
        compatible_bullet_type='1911 .45 ACP',
        felt_recoil=1.1,
        load_time_modifier=1.1,
        receiver_height_above_bore=0.45,
        sight_height_above_bore=0.067,
        sound_modifier=1.0,
        zero_range=25,
        target_acquisition_ap=30,  # TODO - maybe increase this, atleast as a modifier for enemies
        firing_ap_cost=50,
        ap_distance_cost_modifier=1.0,
        spread_modifier=0.055,
        gun_type='pistol',
        barrel_length=5
    )
)

m1911dict = {
    "guns": {
        "pistols": {
            "1911": {
                "required parts": {
                    "M1911 Frame": 1,
                    "M1911 Barrel": 1,
                    "M1911 Slide": 1,
                    "M1911 Grip Panels": 1,
                },
                "compatible parts": {
                    "M1911 Optics Mount": 1,
                    "Side Mounted Accessory": 1,
                    "Underbarrel Accessory": 1,
                    "Optic": 1,
                    "Muzzle Device": 1,
                },
                "item": m1911
            },
        }
    },
}
