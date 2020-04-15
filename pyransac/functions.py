"""Model and error functions.

This module contains different model building and
error calculation functions.
"""

# Standard library imports
import math


def get_line(points):
    if len(points) != 2:
        raise ValueError(f'Need 2 points to make line, not {len(points)}')

    point1 = points[0]
    point2 = points[1]

    try:
        slope = (point1[1] - point2[1]) / (point1[0] - point2[0])
    except ZeroDivisionError:
        return {'slope': math.nan,
                'y_int': math.nan,
                'x_int': point1[0]}

    y_int = point1[1] - slope * point1[0]
    try:
        x_int = -1 * y_int / slope
    except ZeroDivisionError:
        return {'slope': slope,
                'y_int': y_int,
                'x_int': math.nan}

    return {'slope': slope,
            'y_int': y_int,
            'x_int': x_int}


def get_line_error(point, params):
    slope = params['slope']
    y_int = params['y_int']
    x_int = params['x_int']

    if slope == 0:
        return abs(point[1] - y_int)

    if slope is math.nan:
        return abs(point[0] - x_int)

    return abs(point[1] - y_int - slope * point[0]) / math.sqrt(slope ** 2 + 1)
