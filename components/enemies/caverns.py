from components.npc_templates import Fighter, Basic
from components.bodyparts import Bodypart

x = 1
y = 1

def placeholder_fighter():
    return Fighter(1, 100, 100, 100, 100, True, True)

def placeholder_head():
    return Bodypart(5,5,5,True,False,False,False,'Head')

def placeholder_body():
    return Bodypart(10,10,5,True,False,False,False,'Body')

def placeholder_r_arm():
    return Bodypart(5,5,5,False,False,False,True,'Right Arm')

def placeholder_l_arm():
    return Bodypart(5,5,5,False,False,False,True,'Left Arm')

def placeholder_r_leg():
    return Bodypart(5, 5, 5, False, False, True, False, 'Right Leg')

def placeholder_l_leg():
    return Bodypart(5, 5, 5, False, False, True, False, 'Left Leg')

placeholder_common = Basic(
    x, y, 'N',
    [255, 255, 255],
    None,
    'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg()
)

placeholder_uncommon = Basic(
    x, y, 'N',
    [0, 255, 0],
    None,
    'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg()
)

placeholder_rare = Basic(
    x, y, 'N',
    [0, 0, 255],
    None,
    'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg()
)

placeholder_v_rare = Basic(
    x, y, 'N',
    [255,0,255],
    None,
    'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg()
)

placeholder_legendary = Basic(
    x, y, 'N',
    [255, 128, 0],
    None,
    'Placeholder',
    fighter=placeholder_fighter(),
    head = placeholder_head(),
    body = placeholder_body(),
    limb_1 = placeholder_r_arm(),
    limb_2 = placeholder_l_arm(),
    limb_3 = placeholder_r_leg(),
    limb_4 = placeholder_l_leg()
)

