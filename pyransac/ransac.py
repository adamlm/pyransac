"""Random sample consensus (RANSAC) module.

This module contains the core code for the RANSAC algorithm.
"""

# Standard library imports
from dataclasses import dataclass
import random


@dataclass
class RansacParams:
    """Random sample consensus (RANSAC) function parameters.

    This class contains the parameters for the RANSAC algorithm.
    """
    samples: int
    """The number of random samples to take per iteration."""

    iterations: int
    """Maximum number iterations to complete."""

    confidence: float
    """The RANSAC confidence value (0 <= confidence <= 1)."""

    threshold: float
    """The error threshold to consider a point an inlier"""


def find_inliers(points, param_func, error_func, params: RansacParams):
    """Find the inliers from a data set.

    Finds the inliers from a given data set given a model and
    an error function.

    :param points: data points to evaluate
    :param param_func: function to generate model parameters
    :param error_func: function to evaluate error between data
    point and model
    :param params: parameters for the RANSAC algorithm
    :return: inliers
    """
    inliers = []
    max_support = 0

    for _ in range(0, params.iterations):
        sample_points = random.choices(points, k=params.samples)
        func_params = param_func(sample_points)
        supporters = _find_supporters(points, error_func, func_params,
                                      params.threshold)

        if len(supporters) > max_support:
            max_support = len(supporters)
            inliers = supporters

    return inliers


def _find_supporters(points: list, func, params, threshold) -> list:
    """Find data points (supporters) that support the given hypothesis.

    :param points: data points to test against the hypothesis
    :param func: error function for evaluating data points
    :param params: error function parameters
    :param threshold: error threshold to consider data point an inlier
    :return: data points that support the hypothesis
    """
    supporters = []

    for point in points:
        error = func(point, params)

        if error <= threshold:
            supporters.append(point)

    return supporters
