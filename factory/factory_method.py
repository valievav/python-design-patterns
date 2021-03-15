from math import cos, sin

#
# class CoordinateSystem:
#     CARTESIAN = 1
#     POLAR = 2


class Point:
    # def __init__(self, a, b, system):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = b * sin(b)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # create separate staticmethods that will init separate point
    @staticmethod
    def new_cartesian_point(x, y):  # x, y explicit naming for cartesian coordinates
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):  # rho, theta explicit naming for polar coordinates
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f"1st coordinate: {self.x}, 2nd coordinate: {self.y}"

    # Factory method - if need to have several inits, separate inits in methods instead of having all in 1
    # better naming for args, more explicit


p = Point(0,0)
p1 = p.new_cartesian_point(2,3)
p2 = p.new_polar_point(2,3)
print(p1, p2, sep='\n')
