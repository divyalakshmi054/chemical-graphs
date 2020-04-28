import abc
from .GeometricEntities import *


class ErrorInterface(abc.ABC):

    def __init__(self, x: float, y: float) -> None:
        assert x >= 0 and y >= 0
        self.x_margin = x
        self.y_margin = y

    @abc.abstractmethod
    def verify(self, p1: Point, p2: Point) -> bool:
        pass


class ErrorRectangle(ErrorInterface):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def verify(self, p1: Point, p2: Point) -> bool:
        if abs(p2.x - p1.x) <= self.x_margin and abs(p2.y - p1.y) <= self.y_margin:
            return True
        return False


class ErrorEllipse(ErrorInterface):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def verify(self, p1: Point, p2: Point) -> bool:
        result = ((p2.x - p1.x) ** 2) / (self.x_margin ** 2) + ((p2.y - p1.y) ** 2) / (self.y_margin ** 2)
        if result <= 1:
            return True
        return False
