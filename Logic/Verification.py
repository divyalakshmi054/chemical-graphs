import Resources.GeometricEntities as Ge
import Resources.ErrorMargin as Em
from typing import List, Tuple
import math
import Resources.Constants as Constants


def get_mismatch_points(ip: Ge.Graph, tp: Ge.Graph, err: Em.ErrorInterface) -> List[Tuple[Ge.Point, Ge.Point]]:
    mismatch_points = []
    assert len(ip.points) == len(tp.points)
    for i in range(0, len(ip.points)):
        if not err.verify(ip.points[i], tp.points[i]):
            mismatch_points.append((ip.points[i], tp.points[i]))
    return mismatch_points


class Normalize:

    def __init__(self, tp: Ge.Graph) -> None:
        self.tp = tp

    # TODO(anishbadhri): Optimize from O(n*n) to O(n)
    def fit_to_input_count(self, ip: Ge.Graph) -> None:
        self.tp.sort_graph_points()
        ip.sort_graph_points()
        if ip.points[0].x < self.tp.points[0].x or ip.points[-1].x > self.tp.points[-1].x:
            print("Input outside Template graph range")
            assert False
        normalized_tp = Ge.Graph([], 1.0, 1.0)
        for pt in ip.points:
            for i in range(0, len(self.tp.points) - 1):
                if self.tp.points[i].x <= pt.x < self.tp.points[i + 1].x:
                    wt1 = pt.x - self.tp.points[i].x
                    wt2 = self.tp.points[i + 1].x - pt.x
                    new_y = wt1 * self.tp.points[i].y + wt2 * self.tp.points[i + 1].y
                    new_y /= wt1 + wt2
                    normalized_tp.points.append(Ge.Point(pt.x, new_y))
        assert len(normalized_tp.points) == len(ip.points)
        self.tp = normalized_tp

    def fit_to_input_pos(self, ip: Ge.Graph) -> None:
        self.tp.sort_graph_points()
        ip.sort_graph_points()
        if len(self.tp.points) != len(ip.points):
            self.fit_to_input_count(ip)
        average = {"angle": 0.0, "distance": 0.0, "count": 0}
        for i in range(0, len(self.tp.points)):
            dist = self.tp.points[i].cartesian_distance(ip.points[i])
            if dist == 0:
                continue
            average["count"] += 1
            average["distance"] += dist
            average["angle"] += Ge.Line(self.tp.points[i], ip.points[i]).angle()
        if average["count"] == 0:
            return
        average["distance"] /= average["count"]
        average["angle"] /= average["count"]
        print(average["distance"], average["angle"])
        for i in range(0, len(self.tp.points)):
            self.tp.points[i].x += average["distance"] * round(math.cos(average["angle"]), -1*int(math.log10(Constants.EPSILON)))
            self.tp.points[i].y += average["distance"] * round(math.sin(average["angle"]), -1*int(math.log10(Constants.EPSILON)))
