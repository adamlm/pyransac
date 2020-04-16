import abc
from typing import List


class Model(abc.ABC):
    @abc.abstractmethod
    def make_model(self, points: List) -> None:
        pass

    @abc.abstractmethod
    def calc_error(self, point) -> float:
        pass
