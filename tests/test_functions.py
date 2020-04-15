"""Test case for the functions module.

This module contains tests for the model and error functions.
"""

# Standard library imports
import math
import unittest

# Local application imports
from pyransac import functions


class TestRansac(unittest.TestCase):
    """Test the functions module.

    """
    def test_get_line_args(self) -> None:
        self.assertRaises(ValueError, functions.get_line, [])
        self.assertRaises(ValueError, functions.get_line, [(1, 1)])
        self.assertRaises(ValueError, functions.get_line, [(1, 1) * 3])

    def test_get_line_vertical(self) -> None:
        test_data = [(1, 0), (1, 10)]

        model = functions.get_line(test_data)
        self.assertIs(model['slope'], math.nan)
        self.assertIs(model['y_int'], math.nan)
        self.assertEqual(model['x_int'], test_data[0][0])

    def test_get_line_horizontal(self) -> None:
        test_data = [(1, 10), (10, 10)]

        model = functions.get_line(test_data)
        self.assertEqual(model['slope'], 0)
        self.assertEqual(model['y_int'], test_data[0][1])
        self.assertIs(model['x_int'], math.nan)

    def test_get_line_pos(self) -> None:
        test_data = [(0, 1), (1, 2)]

        model = functions.get_line(test_data)
        self.assertEqual(model['slope'], 1)
        self.assertEqual(model['y_int'], 1)
        self.assertEqual(model['x_int'], -1)

    def test_get_line_neg(self) -> None:
        test_data = [(0, 2), (1, 1)]

        model = functions.get_line(test_data)
        self.assertEqual(model['slope'], -1)
        self.assertEqual(model['y_int'], 2)
        self.assertEqual(model['x_int'], 2)

    def test_get_line_error_vertical(self) -> None:
        test_point = (1, 2)
        test_model = {'slope': math.nan,
                      'y_int': math.nan,
                      'x_int': 3}

        error = functions.get_line_error(test_point, test_model)

        self.assertEqual(error, 2)

    def test_get_line_error_horizontal(self) -> None:
        test_point = (2, 1)
        test_model = {'slope': 0,
                      'y_int': 5,
                      'x_int': math.nan}

        error = functions.get_line_error(test_point, test_model)

        self.assertEqual(error, 4)

    def test_get_line_error_pos(self) -> None:
        test_point = (5, 1)
        test_model = {'slope': 2,
                      'y_int': 2,
                      'x_int': -1}

        error = functions.get_line_error(test_point, test_model)

        self.assertAlmostEqual(error, 11 * math.sqrt(5) / 5)

    def test_get_line_error_neg(self) -> None:
        test_point = (6, 1)
        test_model = {'slope': -3,
                      'y_int': 3,
                      'x_int': 1}

        error = functions.get_line_error(test_point, test_model)

        self.assertAlmostEqual(error, 8 * math.sqrt(10) / 5)


if __name__ == '__main__':
    unittest.main()
