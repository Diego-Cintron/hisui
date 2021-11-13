import math

class circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius
