import Resources.GeometricEntities as Ge
import Resources.ErrorMargin as Em
from typing import List, Tuple


def get_mismatch_points(ip: List[Ge.Point], tp: List[Ge.Point], err: Em.ErrorInterface) -> List[Tuple[Ge.Point, Ge.Point]]:
    mismatch_points = []
    if len(ip) == len(tp):
        for i in range(0, len(ip)):
            if not err.verify(ip[i], tp[i]):
                mismatch_points.append((ip[i], tp[i]))
    else:
        # TODO: Implement for unequal size
        print("Yet to implement")
    return mismatch_points
