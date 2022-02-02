from enum import auto, Enum


class RenderOrder(Enum):
    BACKGROUND = auto()
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()
    HIGHEST = auto()