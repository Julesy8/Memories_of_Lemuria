from entity import Actor
from RenderOrder import RenderOrder
from engine import Engine
from input_handlers import GameOverEventHandler

class Bodypart:
    # a basic bodypart
    entity: Actor
    def __init__(self,
                 hp: int,
                 defence: int,
                 vital: bool,
                 walking: bool,
                 flying:bool,
                 grasping: bool,
                 functional: bool,
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
        self.functional = functional
        self.name = name
        self.type = type

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def defence(self) -> int:
        return self._defence

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0:
            if self.vital:
                self.die()

            else:
                self.functional = False
                print(f"{self.entity.name}'s {self.name} is destroyed!")

    @defence.setter
    def defence(self, value):
        self._defence = value

    def die(self):

        if self.engine.player is self.entity:
            death_message = "The player has died!"
            self.engine.event_handler = GameOverEventHandler(self.engine)

        else:
            death_message = f"{self.entity.name} is dead!"

        self.entity.fg_colour = [0,0,0]
        self.entity.bg_colour = [191,0,0]
        self.entity.blocks_movement = False
        self.entity.ai = None
        self.entity.name = f"remains of {self.entity.name}"
        self.entity.render_order = RenderOrder.CORPSE

        print(death_message)