import chemical_graphs.Database


def list_all_graphs(file_name):
    if file_name is None:
        graph_names = []
        for name in chemical_graphs.Database.list_files():
            graph_names.extend(list_all_graphs(name))
        return graph_names
    else:
        return chemical_graphs.Database.list_graphs(file_name)
