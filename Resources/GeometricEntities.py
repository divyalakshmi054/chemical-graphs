from __future__ import annotations
import math
from typing import List
from functools import cmp_to_key
import Resources.Constants as Constants


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"

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


# TODO(anishbadhri): Auto determine scale using GCD method
class Graph:

    def __init__(self, points: List[Point], x_scale: float, y_scale: float) -> None:
        self.points = points
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.assert_scale_matches()

    def __repr__(self) -> str:
        return str(self.points)

    def assert_scale_matches(self):
        for pt in self.points:
            assert math.fabs((pt.x / self.x_scale) - (pt.x // self.x_scale)) < Constants.EPSILON and \
                   math.fabs((pt.y / self.y_scale) - (pt.y // self.y_scale)) < Constants.EPSILON

    def sort_graph_points(self):
        def cmp(p1: Point, p2: Point):
            if p1.x < p2.x:
                return -1
            elif p1.x > p2.x:
                return 1
            elif p1.y < p2.y:
                return -1
            elif p1.y > p2.y:
                return 1
            else:
                return 0
        sorted(self.points, key=cmp_to_key(cmp))
