from chemical_graphs.Logic.Resources import ErrorMargin, GeometricEntities
from chemical_graphs.Logic import Normalization, Verification


def get_error_object(error_tuple):
    return ErrorMargin.ErrorEllipse(error_tuple[0], error_tuple[1])


def get_graph_object(points):
    new_list = []
    for pt in points:
        new_list.append(GeometricEntities.Point(pt[0], pt[1]))
    return GeometricEntities.Graph(new_list, 1.0, 1.0)


def compare_slope(template_graph, input_graph, error, rate):
    nt = Normalization.Normalize(template_graph)
    nt.fit_to_input_pos(input_graph)
    return Verification.get_recommended_points(input_graph, nt.tp, error, rate)


def compare_slope_and_pos(template_graph, input_graph, error, rate):
    nt = Normalization.Normalize(template_graph)
    nt.fit_to_input_count(input_graph)
    return Verification.get_recommended_points(input_graph, nt.tp, error, rate)