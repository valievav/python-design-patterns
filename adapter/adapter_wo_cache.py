class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print('.', end='')


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# need to represent a Line as a series of Points
class LineToPointAdapter(list):

    def __init__(self, line):
        super().__init__()

        print(f'\n'
              f'Generating points for line '
              f'[{line.start.x}, {line.start.y}] -> [{line.end.x}, {line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)
        top = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(bottom, top+1):
                self.append(Point(left, y))  # vertical line
        elif bottom - top == 0:
            for x in range(left, right+1):
                self.append(Point(x, bottom))  # horizontal line


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


def draw(figures):
    print('\n----Drawing figures----')
    for figure in figures:
        for line in figure:
            adapter = LineToPointAdapter(line)
            for point in adapter:
                draw_point(point)


# objects are not cached - created new ones on each run - causes too many temp objects
if __name__ == "__main__":
    rectangles = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw(rectangles)
    draw(rectangles)  # no cache, so data is re-generated anew
