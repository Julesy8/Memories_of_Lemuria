from entity import Entity


class Fighter:
    def __init__(self, power, volume_blood, bleeds=True, alive=True):
        self.power = power
        self.max_volume_blood = volume_blood
        self.volume_blood = volume_blood
        self.bleeds = bleeds
        self.alive = alive


class Humanoid(Entity):
    def __init__(self, head_hp, torso_hp, limbs_hp, head_def, torso_def, arms_def, legs_def,
                 x, y, char, fg_colour, bg_colour, name, movement_phase, movement_phase_max, movements_per_turn,
                 blocks=True, fighter=None, ai=None):
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
        super().__init__(x, y, char, fg_colour, bg_colour, name, movement_phase, movement_phase_max, movements_per_turn,
                         blocks=blocks, fighter=fighter, ai=ai)
