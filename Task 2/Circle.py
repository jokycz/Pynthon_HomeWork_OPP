import math

from Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    @property
    def type(self):
        return "kružnice"
