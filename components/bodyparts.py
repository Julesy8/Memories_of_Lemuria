from entity import Actor

class Bodypart:
    # a basic bodypart
    def __init__(self,
                 hp: int,
                 defence: int,
                 vital: bool,
                 walking: bool,
                 flying:bool,
                 grasping: bool,
                 name: str,
                 type: str # can be 'Body', 'Head', 'Arms' or 'Legs'
                 ):
        self.max_hp = hp
        self._hp = hp
        self._defence = defence
        self.vital = vital
        self.walking = walking
        self.flying = flying
        self.grasping = grasping
        self.name = name
        self.type = type

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def defence(self) -> int:
        return self._defence

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))

    @defence.setter
    def defence(self, value):
        self._defence = value
