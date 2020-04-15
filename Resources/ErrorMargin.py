import abc
import Resources.GeometricEntities as Ge


# TODO(anishbadhri): Rename self x, y to xmargin, ymargin
class ErrorInterface(abc.ABC):

    def __init__(self, x: float, y: float) -> None:
        assert x >= 0 and y >= 0
        self.x = x
        self.y = y

    @abc.abstractmethod
    def verify(self, p1: Ge.Point, p2: Ge.Point) -> bool:
        pass


class ErrorRectangle(ErrorInterface):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def verify(self, p1: Ge.Point, p2: Ge.Point) -> bool:
        if abs(p2.x - p1.x) <= self.x and abs(p2.y - p1.y) <= self.y:
            return True
        return False


class ErrorEllipse(ErrorInterface):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y)

    def verify(self, p1: Ge.Point, p2: Ge.Point) -> bool:
        result = ((p2.x - p1.x) ** 2) / (self.x ** 2) + ((p2.y - p1.y) ** 2) / (self.y ** 2)
        if result <= 1:
            return True
        return False
