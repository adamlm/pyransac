"""Test cases for the line2d module.

This module contains tests for the 2D line model and error functions.
"""

# Standard library imports
import math
import unittest

# Local application imports
from pyransac import line2d


class TestLine2D(unittest.TestCase):
    """Test the 2D line module.

    """
    def test_point2d(self) -> None:
        """Test Point2D class initialization.

        """
        test_point = line2d.Point2D(1, 2)

        self.assertEqual(test_point.x, 1)
        self.assertEqual(test_point.y, 2)

    def test_line2d_init_none(self) -> None:
        """Test 2D line model initialization without parameters.

        """
        test_model = line2d.Line2D()

        self.assertIs(test_model.slope, None)
        self.assertIs(test_model.y_int, None)
        self.assertIs(test_model.x_int, None)

    def test_line2d_init_args(self) -> None:
        """Test 2D line model initialization with parameters.

                """
        test_model = line2d.Line2D(slope=1, y_int=2, x_int=3)

        self.assertEqual(test_model.slope, 1)
        self.assertEqual(test_model.y_int, 2)
        self.assertEqual(test_model.x_int, 3)

    def test_make_model_args(self) -> None:
        """Test 2D line model make_model with args != 2.

        """
        test_model = line2d.Line2D()

        self.assertRaises(ValueError, test_model.make_model, [])
        self.assertRaises(ValueError, test_model.make_model, [(1, 1)])
        self.assertRaises(ValueError, test_model.make_model, [(1, 1) * 3])

    def test_make_model_vertical(self) -> None:
        """Test 2D line model against vertical line.

        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=1, y=0), line2d.Point2D(x=1, y=10)]

        test_model.make_model(test_data)

        self.assertIs(test_model.slope, math.nan)
        self.assertIs(test_model.y_int, math.nan)
        self.assertEqual(test_model.x_int, 1)

    def test_make_model_horizontal(self) -> None:
        """Test 2D line model against horizontal line.

        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=1, y=10), line2d.Point2D(x=10, y=10)]

        test_model.make_model(test_data)

        self.assertEqual(test_model.slope, 0)
        self.assertEqual(test_model.y_int, 10)
        self.assertIs(test_model.x_int, math.nan)

    def test_make_model_positive(self) -> None:
        """Test 2D line model against line with positive slope.

        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=0, y=1), line2d.Point2D(x=1, y=2)]

        test_model.make_model(test_data)

        self.assertEqual(test_model.slope, 1)
        self.assertEqual(test_model.y_int, 1)
        self.assertEqual(test_model.x_int, -1)

    def test_make_model_negative(self) -> None:
        """Test 2D line model against line with negative slope.

        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=0, y=2), line2d.Point2D(x=1, y=1)]

        test_model.make_model(test_data)

        self.assertEqual(test_model.slope, -1)
        self.assertEqual(test_model.y_int, 2)
        self.assertEqual(test_model.x_int, 2)

    def test_get_error_vertical(self) -> None:
        """Test 2D line point distance with vertical line.

        """
        test_model = line2d.Line2D(slope=math.nan, y_int=math.nan, x_int=3)
        test_point = line2d.Point2D(1, 2)

        error = test_model.calc_error(point=test_point)

        self.assertEqual(error, 2)

    def test_get_error_horizontal(self) -> None:
        """Test 2D line point distance with horizontal line.

        """
        test_model = line2d.Line2D(slope=0, y_int=5, x_int=math.nan)
        test_point = line2d.Point2D(2, 1)

        error = test_model.calc_error(point=test_point)

        self.assertEqual(error, 4)

    def test_get_error_positive(self) -> None:
        """Test 2D line point distance with line with positive slope.

        """
        test_model = line2d.Line2D(slope=2, y_int=2, x_int=-1)
        test_point = line2d.Point2D(5, 1)

        error = test_model.calc_error(point=test_point)

        self.assertAlmostEqual(error, 11 * math.sqrt(5) / 5)

    def test_get_line_error_neg(self) -> None:
        """Test 2D line point distance with line with negative slope.

        """
        test_model = line2d.Line2D(slope=-3, y_int=3, x_int=1)
        test_point = line2d.Point2D(6, 1)

        error = test_model.calc_error(point=test_point)

        self.assertAlmostEqual(error, 8 * math.sqrt(10) / 5)


if __name__ == '__main__':
    unittest.main()
