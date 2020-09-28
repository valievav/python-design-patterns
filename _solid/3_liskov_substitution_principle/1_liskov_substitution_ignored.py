class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def area(self):
        return self._width * self._height

    def str(self):
        return f"Width: {self.width}, height: {self.height}"


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_rectangle(rect: Rectangle):
    w = rect.width
    rect.height = 10  # changes square width and height, so 'w' param is invalid for square
    exp_area = w * 10
    print(f"Expected {exp_area}, got {rect.area}")

    # violates the Liskov substitution principle because results for Rectangle and Square will be different


if __name__ == "__main__":
    rect = Rectangle(5,20)
    use_rectangle(rect)

    square = Square(5)
    use_rectangle(square)

    # Expected 50, got 50
    # Expected 50, got 100 - because w value become invalid after rect.height set to 10
