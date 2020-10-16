import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x={self.x}, y={self.y}"


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(Line(self.start, self.end))  # use deepcopy to have separate copy of attrs (simple obj creation won't work for Point.x/y update!)

    def __str__(self):
        return f"Start: {self.start}. End: {self.end}"


line = Line(Point(1,2), Point(10,20))
print(line)
line2 = line.deep_copy()
line2.start.y = 100  # object attr can be updated separately from original object
print('---')
print(line)
print(line2)
