import abc
from abc import ABC, abstractmethod


# Абстрактный класс "Геометрическая фигура"
class Figure(ABC):
    @abc.abstractmethod
    def square(self):
        pass

