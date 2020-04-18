"""2D line module.

This module contains the model for a 2-dimensional line.
"""

# Standard library imports
from dataclasses import dataclass
import math
from typing import List

# Local application imports
from pyransac.base import Model


@dataclass(order=True)
class Point2D:
    """2-dimensional point class.

    This is a simple class to contain Cartesian coordinates of 2D point.
    """
    x: float  # pylint: disable=invalid-name
    """x coordinate of point."""
    y: float  # pylint: disable=invalid-name
    """y coordinate of point"""


class Line2D(Model):
    """Model for a 2-dimensional line.

    """
    def __init__(self, slope=None, y_int=None, x_int=None):
        self._slope = slope
        self._y_int = y_int
        self._x_int = x_int

    @property
    def slope(self):
        """Gets the slope of the model.

        :return: slope of line (None if model not made).
        """
        return self._slope

    @property
    def y_int(self):
        """Gets the y intercept of the model.

        :return: y intercept of line (None if model not made).
        """
        return self._y_int

    @property
    def x_int(self):
        """Gets the x intercept of the model.

        :return: x intercept of line (None if model not made).
        """
        return self._x_int

    def make_model(self, points: List[Point2D]) -> None:
        """Makes equation for 2D line given two data points.

        Model parameters are stored internally.

        :param points: list of data points to make model
            (length must be 2)
        :return: None
        """
        if len(points) != 2:
            raise ValueError(f'Need 2 points to make line, not {len(points)}')

        try:
            self._slope = (points[0].y - points[1].y) / (points[0].x -
                                                         points[1].x)
        except ZeroDivisionError:
            self._slope = math.nan
            self._y_int = math.nan
            self._x_int = points[0].x
            return

        self._y_int = points[0].y - self._slope * points[0].x

        try:
            self._x_int = -1 * self._y_int / self._slope
        except ZeroDivisionError:
            self._x_int = math.nan

    def calc_error(self, point: Point2D) -> float:
        """Calculate error between data point and 2D model.

        :param point: data point to calculate error with
        :return: calculated error
        """
        if self._slope == 0:
            return abs(point.y - self._y_int)

        if self._slope is math.nan:
            return abs(point.x - self._x_int)

        return abs(point.y - self._y_int - self._slope * point.x) / math.sqrt(
            self._slope ** 2 + 1)
