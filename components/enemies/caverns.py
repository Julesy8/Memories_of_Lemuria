from components.npc_templates import Fighter
from entity import Actor, Item, Stacking
from components.ai import HostileEnemy
from components.bodyparts import Bodypart, Arm, Leg
from components import consumables
from components.inventory import Inventory
import colour


def placeholder_fighter():
    return Fighter(unarmed_meat_damage=10, unarmed_armour_damage=5)


Head = Bodypart(hp=10, defence=5,  vital=True, name='head', part_type='Head', base_chance_to_hit=80)
Body = Bodypart(hp=10, defence=5, vital=True, name='body', part_type='Body', base_chance_to_hit=90, destroyable=False)
R_Arm = Arm(hp=10, defence=5, name='right arm', base_chance_to_hit=80)
L_Arm = Arm(hp=10, defence=5, name='left arm', base_chance_to_hit=80)
R_Leg = Leg(hp=10, defence=5, name='right leg', base_chance_to_hit=80)
L_Leg = Leg(hp=10, defence=5, name='left leg', base_chance_to_hit=80)

body_parts = (Body, Head, R_Arm, L_Arm, R_Leg, L_Leg)

placeholder_common = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.WHITE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
)

placeholder_uncommon = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.JADE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
)

placeholder_rare = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.BLUE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
)

placeholder_v_rare = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.PURPLE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
)

placeholder_legendary = Actor(
    x=0, y=0,
    char='N',
    fg_colour=colour.ORANGE,
    bg_colour=None,
    name='Placeholder',
    fighter=placeholder_fighter(),
    ai=HostileEnemy,
    bodyparts=body_parts,
    inventory=Inventory(capacity=0),
)

placeholder_item = Item(
    x=0, y=0,
    char="?",
    fg_colour=colour.MAGENTA,
    bg_colour=None,
    name="Placeholder Item",
    weight=1,
    stacking=None,
    usable_properties=None,
)

helmet = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Helmet",
    weight=1,
    stacking=None,
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Head',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

pauldron = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Pauldrons",
    weight=1,
    stacking=None,
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Arms',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

greaves = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Greaves",
    weight=1,
    stacking=None,
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Legs',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

chestplate = Item(
    x=0, y=0,
    char="/",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Chestplate",
    weight=1,
    stacking=None,
    usable_properties=(consumables.Wearable(
        protection=2,
        fits_bodypart_type='Body',
        large_mag_slots=1,
        medium_mag_slots=1,
        small_mag_slots=1
    ))
)

medkit = Item(
    x=0, y=0,
    char="+",
    fg_colour=colour.GREEN,
    bg_colour=None,
    name="Medkit",
    weight=1,
    stacking=Stacking(stack_size=1),
    usable_properties=consumables.HealingConsumable(amount=20),
)

glock_17 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock 17",
    weight=1,
    stacking=None,
    usable_properties=consumables.GunMagFed(
        compatible_magazine_type='glock9mm',
        chambered_bullet=None,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'automatic': 1200},
        current_fire_mode='single shot',
        base_meat_damage=10,
        base_armour_damage=10,
        base_accuracy=1.0,
        range_accuracy_dropoff=40,
    )
)

kar_98k = Item(
    x=0, y=0,
    char="k",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Kar 98K",
    weight=1,
    stacking=None,
    usable_properties=consumables.GunIntegratedMag(
        chambered_bullet=None,
        keep_round_chambered=False,
        equip_time=1,
        fire_modes={'single shot': 1},
        current_fire_mode='single shot',
        base_meat_damage=10,
        base_armour_damage=10,
        base_accuracy=1.0,
        range_accuracy_dropoff=40,
        compatible_bullet_type='8mm mauser',
        mag_capacity=5,
    )
)


glock_mag = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Glock Magazine 9mm",
    weight=1,
    stacking=None,
    usable_properties=consumables.Magazine(
        magazine_type='glock9mm',
        compatible_bullet_type='9mm',
        mag_capacity=17,
        turns_to_load=1,
        magazine_size='small',
    )
)

bullet_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='9mm Bullet',
    weight=1,
    stacking=Stacking(stack_size=10),
    usable_properties=consumables.Bullet(
        bullet_type='9mm',
        meat_damage_factor=1.0,
        armour_damage_factor=1.0,
        accuracy_factor=1.0,
        recoil_modifier=4,
    )
)

bullet_8mm_mauser = Item(
    x=0, y=0,
    char="m",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name='8mm Mauser',
    weight=1,
    stacking=Stacking(stack_size=10),
    usable_properties=consumables.Bullet(
        bullet_type='8mm mauser',
        meat_damage_factor=1.0,
        armour_damage_factor=1.0,
        accuracy_factor=1.0,
        recoil_modifier=4,
    )
)