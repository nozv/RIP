from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import FColor


class Square(Rectangle):

    _type = "квадрат"

    @classmethod
    def gettype(cls):
        return cls._type

    def __init__(self, p_side, p_color):
        self._side = p_side
        self._color = FColor()
        self._color.colorprop = p_color

    def square(self):
        return self._side**2

    def __repr__(self):
        return "{} {} со стороной {} и площадью {}".format(
            self._color.colorprop,
            Square.gettype(),
            self._side,
            self.square()
        )

