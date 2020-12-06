from entity import Entity


class Fighter:  # basic class for entities that fight
    def __init__(self, power, volume_blood, energy, move_cost, attack_cost, bleeds=True, alive=True):
        self.power = power
        self.max_volume_blood = volume_blood
        self.volume_blood = volume_blood
        self.energy = energy
        self.move_cost = move_cost
        self.attack_cost = attack_cost
        self.bleeds = bleeds
        self.alive = alive

class Humanoid(Entity):  # humanoid body class
    def __init__(self, head_hp, torso_hp, limbs_hp, head_def, torso_def, arms_def, legs_def, x, y,
                 char, fg_colour, bg_colour, name, blocks_movement=True, fighter=None, ai=None):
        self.head_hp_max = head_hp
        self.torso_hp_max = torso_hp
        self.r_arm_hp_max = limbs_hp
        self.l_arm_hp_max = limbs_hp
        self.r_leg_hp_max = limbs_hp
        self.l_leg_hp_max = limbs_hp
        self.head_hp = head_hp
        self.torso_hp = torso_hp
        self.r_arm_hp = limbs_hp
        self.l_arm_hp = limbs_hp
        self.r_leg_hp = limbs_hp
        self.l_leg_hp = limbs_hp
        self.head_def = head_def
        self.torso_def = torso_def
        self.r_arm_def = arms_def
        self.l_arm_def = arms_def
        self.r_leg_def = legs_def
        self.l_leg_def = legs_def
        super().__init__(x, y, char, fg_colour, bg_colour, name,
                         blocks_movement=blocks_movement, fighter=fighter, ai=ai)
