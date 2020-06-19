import chemical_graphs.Logic.Resources.ErrorMargin


def get_error_object(error_tuple):
    return chemical_graphs.Logic.Resources.ErrorMargin.ErrorEllipse(error_tuple[0], error_tuple[1])