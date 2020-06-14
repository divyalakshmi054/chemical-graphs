import json
import importlib.resources as pkg_resources


GRAPH_INDICES_FILE = 'GraphIndex.json'


def list_files():
    with pkg_resources.open_text(__name__, GRAPH_INDICES_FILE) as json_file:
        graph_indices = json.load(json_file)
        return graph_indices.keys()


def list_graphs(file_name):
    with pkg_resources.open_text(__name__, GRAPH_INDICES_FILE) as json_file:
        graph_indices = json.load(json_file)
        assert file_name in graph_indices.keys()
        return graph_indices[file_name]
