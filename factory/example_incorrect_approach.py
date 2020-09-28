from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):  # all in 1 init
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)

    def __str__(self):
        return f"1st coordinate: {self.x}, 2nd coordinate: {self.y}"

# all logic in 1 init, arguments are named generally not explicit


p1 = Point(2,3)
p2 = Point(2,3, CoordinateSystem.POLAR)
print(p1, p2, sep='\n')
