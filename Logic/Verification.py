import Resources.GeometricEntities as Ge
import Resources.ErrorMargin as Em
from typing import List, Tuple
import math
import Resources.Constants as Constants


def get_mismatch_points(ip: Ge.Graph, tp: Ge.Graph, err: Em.ErrorInterface) -> List[Tuple[Ge.Point, Ge.Point]]:
    mismatch_points = []
    ip.sort_graph_points()
    tp.sort_graph_points()
    assert len(ip.points) == len(tp.points)
    for i in range(0, len(ip.points)):
        if not err.verify(ip.points[i], tp.points[i]):
            mismatch_points.append((ip.points[i], tp.points[i]))
    return mismatch_points


def get_recommended_points(ip: Ge.Graph, tp: Ge.Graph, err: Em.ErrorInterface, convergence: float = 0.5) -> Ge.Graph:
    assert 0 < convergence < 1
    final_graph = ip
    tp.sort_graph_points()
    while True:
        final_graph.sort_graph_points()
        mismatch_points = get_mismatch_points(final_graph, tp, err)
        if len(mismatch_points) == 0:
            return final_graph
        for i in range(0, len(final_graph.points)):
            assert final_graph.points[i].x == tp.points[i].x
            final_graph.points[i].y = convergence * tp.points[i].y + (1-convergence) * final_graph.points[i].y

