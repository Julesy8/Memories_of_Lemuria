class Bodypart:
    # a basic bodypart
    def __init__(self,
                 max_hp: int,
                 hp: int,
                 defence: int,
                 vital: bool,
                 walking: bool,
                 flying:bool,
                 grasping: bool,
                 name: str
                 ):
        self.max_hp = max_hp
        self.hp = hp
        self.defence = defence
        self.vital = vital
        self.walking = walking
        self.flying = flying
        self.grasping = grasping
        self.name = name

    @property
    def hp(self) -> int:
        return self.hp

    @property
    def defence(self) -> int:
        return self.defence

    @hp.setter
    def hp(self, value: int) -> None:
        self.hp = max(0, min(value, self.max_hp))

    @defence.setter
    def defence(self, value):
        self.defence = value
