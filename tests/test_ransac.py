"""Test case for the ransac module.

This module contains tests for the ransac module.
"""

# Standard library imports
import unittest

# Local application imports
from pyransac import ransac
from pyransac import line2d


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
        test_inliers = [line2d.Point2D(x, x) for x in range(0, 10)]
        test_outliers = [line2d.Point2D(5, 1),
                         line2d.Point2D(5, 2),
                         line2d.Point2D(6, 1),
                         line2d.Point2D(5, 2)]
        test_data = test_inliers + test_outliers
        ransac_params = ransac.RansacParams(samples=2,
                                            iterations=10,
                                            confidence=0.999,
                                            threshold=1)

        test_model = line2d.Line2D()

        inliers = ransac.find_inliers(points=test_data,
                                      model=test_model,
                                      params=ransac_params)

        self.assertEqual(sorted(test_inliers), sorted(inliers))


if __name__ == '__main__':
    unittest.main()
