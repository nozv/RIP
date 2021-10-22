from lab_python_oop.figure import Figure
from lab_python_oop.color import FColor
import math


class Circle(Figure):

    _type = "круг"

    @classmethod
    def gettype(cls):
        return cls._type

    def __init__(self, p_radius, p_color):
        self._radius = p_radius
        self._color = FColor()
        self._color.colorprop = p_color

    def square(self):
        return self._radius**2 * math.pi

    def __repr__(self):
        return "{} {} радиусом {} и площадью {}".format(
            self._color.colorprop,
            Circle.gettype(),
            self._radius,
            self.square()
        )