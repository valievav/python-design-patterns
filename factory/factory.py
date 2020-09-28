from math import cos, sin


class Point:
    """
    Use PointFactory for cartesian or polar coordinates.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"1st coordinate: {self.x}, 2nd coordinate: {self.y}"


# create separate class with staticmethods for initialization
class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):  # x, y explicit naming for cartesian coordinates
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):  # rho, theta explicit naming for polar coordinates
        return Point(rho * cos(theta), rho * sin(theta))

# discoverability is a question here, better to specify that Point factory exists in Point desc


pf = PointFactory()

p1 = pf.new_cartesian_point(2,3)
p2 = pf.new_polar_point(2,3)
print(p1, p2, sep='\n')
