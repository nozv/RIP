from lab_python_oop.figure import Figure
from lab_python_oop.color import FColor


class Rectangle(Figure):

    _type = "прямоугольник"

    @classmethod
    def gettype(cls):
        return cls._type

    def __init__(self, p_width, p_height, p_color):
        self._width = p_width
        self._height = p_height
        self._color = FColor()
        self._color.colorprop = p_color

    def square(self):
        return self._width * self._height

    def __repr__(self):
        return "{} {} шириной {}, высотой {} и площадью {}".format(
            self._color.colorprop,
            Rectangle.gettype(),
            self._width,
            self._height,
            self.square()
        )