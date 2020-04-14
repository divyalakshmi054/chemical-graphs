from __future__ import annotations
import math


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def cartesian_distance(self, p: Point) -> float:
        return math.sqrt((self.x - p.x) ** 2.0 + (self.y - p.y) ** 2.0)


class Line:
    def __init__(self, p1: Point = Point(), p2: Point = Point()):
        self.p1 = p1
        self.p2 = p2

    def slope(self) -> float:
        p_inf = float("inf")
        n_inf = float("-inf")
        if self.p1.x == self.p2.x:
            if self.p2.y > self.p1.y:
                return p_inf
            else:
                return n_inf
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def angle(self) -> float:
        return math.atan(self.slope())
