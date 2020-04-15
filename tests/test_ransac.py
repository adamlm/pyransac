"""Test case for the ransac module.

This module contains tests for the ransac module.
"""

# Standard library imports
import math
import unittest

# Local application imports
from pyransac import ransac


class TestRansac(unittest.TestCase):
    """Test the ransac module.

    """
    def test_ransac_params(self) -> None:
        """Test RansacParams initialization.

        :return: None
        """
        params = ransac.RansacParams(samples=1,
                                     iterations=2,
                                     confidence=3,
                                     threshold=4)

        self.assertEqual(params.samples, 1)
        self.assertEqual(params.iterations, 2)
        self.assertEqual(params.confidence, 3)
        self.assertEqual(params.threshold, 4)

    def test_find_inliers(self) -> None:
        """Test the ransac find_inliers function.

        :return: None
        """
        def param_func(points):
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
                x_int = (point1[1] - y_int) / slope
            except ZeroDivisionError:
                return {'slope': slope,
                        'y_int': y_int,
                        'x_int': math.nan}

            return {'slope': slope,
                    'y_int': y_int,
                    'x_int': x_int}

        def error_func(point, params):
            b = 1

            if params['slope'] == 0:
                return abs(b * point[1]) / abs(b)

            a = -1 * params['slope'] / b
            c = -1 * params['y_int'] / b

            if params['slope'] is math.nan:
                return abs(a * point[0]) / abs(a)

            return abs(a * point[0] + b * point[1] + c) / math.sqrt(
                a ** 2 + b ** 2)

        test_inliers = [(x, x) for x in range(0, 10)]
        test_outliers = [(5, 1), (5, 2), (6, 1), (5, 2)]
        test_data = test_inliers + test_outliers
        ransac_params = ransac.RansacParams(samples=2,
                                            iterations=10,
                                            confidence=0.5,
                                            threshold=1)

        inliers = ransac.find_inliers(points=test_data,
                                      param_func=param_func,
                                      error_func=error_func,
                                      params=ransac_params)

        self.assertEqual(sorted(test_inliers), sorted(inliers))


if __name__ == '__main__':
    unittest.main()
