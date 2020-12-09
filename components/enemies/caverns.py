from components.npc_templates import Fighter, Basic
from components.ai import HostileEnemy
from components.bodyparts import Bodypart

def placeholder_fighter():
    return Fighter(power= 1, bleeds = True)

def placeholder_head():
    return Bodypart(5, 5, True, False, False, False, 'Head')

def placeholder_body():
    return Bodypart(10, 5, True, False, False, False, 'Body')

def placeholder_r_arm():
    return Bodypart(5, 5, False, False, False, True, 'Right Arm')

def placeholder_l_arm():
    return Bodypart(5, 5, False, False, False, True, 'Left Arm')

def placeholder_r_leg():
    return Bodypart(5, 5, False, False, True, False, 'Right Leg')

def placeholder_l_leg():
    return Bodypart(5, 5, False, False, True, False, 'Left Leg')

placeholder_common = Basic(
    x=0, y=0,
    char = 'N',
    fg_colour = [255, 255, 255],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg(),
    ai=HostileEnemy
)

placeholder_uncommon = Basic(
    x=0, y=0,
    char = 'N',
    fg_colour = [0, 255, 0],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg(),
    ai=HostileEnemy
)

placeholder_rare = Basic(
    x=0, y=0,
    char = 'N',
    fg_colour = [0, 0, 255],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg(),
    ai=HostileEnemy
)

placeholder_v_rare = Basic(
    x=0, y=0,
    char = 'N',
    fg_colour = [255,0,255],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg(),
    ai = HostileEnemy
)

placeholder_legendary = Basic(
    x=0, y=0,
    char = 'N',
    fg_colour = [255, 128, 0],
    bg_colour = None,
    name = 'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg(),
    ai = HostileEnemy
)

