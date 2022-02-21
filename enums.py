from enum import Enum


class Sids(Enum):
    right = 1
    left = 2


class Colors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
