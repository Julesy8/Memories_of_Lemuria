from entity import Item
from components.consumables import GunMagFed, ComponentPart
from components.gunparts import GunParts
import colour

mac10_reciever = Item(
    x=0, y=0,
    char="?",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="MAC 10 Reciever",
    weight=1,
    stacking=None,
    usable_properties=ComponentPart(part_type='mac10_reciever'),
    description='glock barrel'
)

mac10 = Item(
    x=0, y=0,
    char="r",
    fg_colour=colour.LIGHT_GRAY,
    bg_colour=None,
    name="Mac 10",
    weight=1,
    stacking=None,
    description='Mac 10',
    usable_properties=GunMagFed(
        compatible_magazine_type='mac1045',
        chambered_bullet=None,
        keep_round_chambered=False,
        loaded_magazine=None,
        equip_time=1,
        fire_modes={'single shot': 1, 'automatic': 1090},
        current_fire_mode='single shot',
        base_meat_damage=10,
        base_armour_damage=10,
        base_accuracy=1.0,
        range_accuracy_dropoff=40,
        parts=GunParts(),
        enemy_attack_range=5,
        possible_parts=glock_parts_dict,
        sound_radius=10,
        recoil=3,
        close_range_accuracy=1.0,
    )
)