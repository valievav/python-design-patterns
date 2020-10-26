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
class LineToPointAdapter:
    cache = {}  # store cache

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        print(f'\n'
              f'Generating points for line '
              f'[{line.start.x}, {line.start.y}] -> [{line.end.x}, {line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)
        top = max(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(bottom, top+1):
                points.append(Point(left, y))  # vertical line
        elif bottom - top == 0:
            for x in range(left, right+1):
                points.append(Point(x, bottom))  # horizontal line

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


def draw(figures):
    print('----Drawing figures----')
    for figure in figures:
        for line in figure:
            adapter = LineToPointAdapter(line)
            for point in adapter:
                draw_point(point)


if __name__ == "__main__":
    rectangles = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw(rectangles)
    draw(rectangles)  # this run does not generate lines - it uses cache (no line print output)
