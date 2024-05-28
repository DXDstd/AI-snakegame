# to cope with forward declaration for type annotation
# the following works for Python 3.7+
# expect to become a default in Python 3.10
from __future__ import annotations
import math

class VecInt2:

    def __init__(self, x:int=0, y:int=0):
        self.x: int = x
        self.y: int = y

    def __add__(self, other):
        return VecInt2(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return VecInt2(self.x-other.x, self.y-other.y)

    def set_xy(self, x:int, y:int):
        self.x = x
        self.y = y

    def set_to(self, other:VecInt2):
        self.x = other.x
        self.y = other.y

    def move(self, other:VecInt2):
        self.x += other.x
        self.y += other.y

    def distance_to(self, other:VecInt2) -> float:
        p2: VecInt2 = self - other
        return float(math.sqrt(p2.x**2 + p2.y**2))

    def xy(self):
        return (self.x,self.y)

    def is_same_loc_as(self, other:VecInt2) -> bool:
        if self.x==other.x and self.y==other.y:
            return True
        return False
