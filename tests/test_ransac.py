import unittest

import ransac


class TestRansac(unittest.TestCase):
    def setUp(self) -> None:
        self.params = ransac.RansacParams(samples=1,
                                          iterations=2,
                                          confidence=3,
                                          threshold=4)

    def test_ransac_params(self) -> None:
        self.assertEqual(self.params.samples, 1)
        self.assertEqual(self.params.iterations, 2)
        self.assertEqual(self.params.confidence, 3)
        self.assertEqual(self.params.threshold, 4)

    def test_find_inliers(self) -> None:
        def param_func(points):
            return {'slope': 1, 'intercept': 0}

        def error_func(point, params):
            return 0

        data = [(1, 1), (2, 2), (3, 3), (4, 4)]
        ransac_params = ransac.RansacParams(samples=1,
                                            iterations=1,
                                            confidence=0.5,
                                            threshold=1)

        inliers = ransac.find_inliers(points=data,
                                      param_func=param_func,
                                      error_func=error_func,
                                      params=ransac_params)


if __name__ == '__main__':
    unittest.main()
