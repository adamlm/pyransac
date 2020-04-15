import random

from pyransac.classes import RansacParams


def find_inliers(points, param_func, error_func, params: RansacParams):
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


def _find_supporters(points, func, params, threshold):
    supporters = []

    for point in points:
        error = func(point, params)

        if error <= threshold:
            supporters.append(point)

    return supporters
