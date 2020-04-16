"""Base definitions module.

This module contains definitions for base classes.
"""

# Standard library imports
import abc
from typing import List


class Model(abc.ABC):
    """ABC class for data models.

    Derivative classes should extend this class and implement its
    interface.
    """
    @abc.abstractmethod
    def make_model(self, points: List) -> None:
        """Makes a model from given data points.

        :param points: list of data points with which to make model
        """

    @abc.abstractmethod
    def calc_error(self, point) -> float:
        """Calculates error between data point and model.

        :param point: data point to test against
        """
