import math
from chemical_graphs.Logic.Resources.GeometricEntities import Graph, Line, Point
from chemical_graphs.Logic.Resources.Constants import EPSILON


class Normalize:

    def __init__(self, tp: Graph) -> None:
        self.tp = tp

    # TODO(anishbadhri): Optimize from O(n*n) to O(n)
    def fit_to_input_count(self, ip: Graph) -> None:
        self.tp.sort_graph_points()
        ip.sort_graph_points()
        normalized_tp = Graph([], 1.0, 1.0)
        for pt in ip.points:
            new_y = 0
            if pt.x < self.tp.points[0].x:
                slope = (self.tp.points[1].y - self.tp.points[0].y)/(self.tp.points[1].x - self.tp.points[0].x)
                c = self.tp.points[1].y - slope * self.tp.points[1].x
                new_y = slope * pt.x + c
            elif pt.x > self.tp.points[-1].x:
                slope = (self.tp.points[-1].y - self.tp.points[-2].y) / (self.tp.points[-1].x - self.tp.points[-2].x)
                c = self.tp.points[-1].y - slope * self.tp.points[-1].x
                new_y = slope * pt.x + c
            else:
                for i in range(0, len(self.tp.points) - 1):
                    if self.tp.points[i].x <= pt.x < self.tp.points[i + 1].x:
                        wt1 = pt.x - self.tp.points[i].x
                        wt2 = self.tp.points[i + 1].x - pt.x
                        new_y = wt1 * self.tp.points[i].y + wt2 * self.tp.points[i + 1].y
                        new_y /= wt1 + wt2
                        break
            normalized_tp.points.append(Point(pt.x, new_y))
        assert len(normalized_tp.points) == len(ip.points)
        self.tp = normalized_tp

    def fit_to_input_pos(self, ip: Graph) -> None:
        self.tp.sort_graph_points()
        ip.sort_graph_points()
        self.fit_to_input_count(ip)
        average = {"angle": 0.0, "distance": 0.0, "distance_count": 0, "angle_count": 0}
        for i in range(0, len(self.tp.points)):
            dist = self.tp.points[i].cartesian_distance(ip.points[i])
            average["distance_count"] += 1
            average["distance"] += dist
            if dist == 0:
                continue
            average["angle_count"] += 1
            average["angle"] += Line(self.tp.points[i], ip.points[i]).angle()
        if average["distance_count"] == 0 or average["angle_count"] == 0:
            return
        average["distance"] /= average["distance_count"]
        average["angle"] /= average["angle_count"]
        for i in range(0, len(self.tp.points)):
            self.tp.points[i].x += average["distance"] * round(math.cos(average["angle"]),
                                                               -1 * int(math.log10(EPSILON)))
            self.tp.points[i].y += average["distance"] * round(math.sin(average["angle"]),
                                                               -1 * int(math.log10(EPSILON)))
