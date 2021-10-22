
class FColor:

    def __init__(self):
        self._color = None

    @property
    def colorprop(self):
        return self._color

    @colorprop.setter
    def colorprop(self, value):
        self._color = value