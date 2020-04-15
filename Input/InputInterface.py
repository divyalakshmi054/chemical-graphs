import abc

import Resources.GeometricEntities as Ge
from typing import List


class InputInterface(abc.ABC):
    @abc.abstractmethod
    def get_points(self) -> List[Ge.Point]:
        pass


class InputFile(InputInterface):
    def __init__(self, file_name: str):
        self.file_stream = open(file_name, 'r')

    def get_points(self) -> List[Ge.Point]:
        points_list = []
        for line in self.file_stream:
            coordinates = [x.strip() for x in line.split(',')]
            assert len(coordinates) == 2
            cur_point = Ge.Point(float(coordinates[0]), float(coordinates[1]))
            points_list.append(cur_point)
        return points_list


# TODO(divyalakshmi054) : Implement Command Line Read
class InputCommandLine(InputInterface):
    def __init__(self):
        pass

    def get_points(self) -> List[Ge.Point]:
        pass
