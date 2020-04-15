"""class module tests.

This module contains tests for classes in the classes module.
"""

# Standard library imports
import unittest

# Local application imports
import pyransac


class TestRansacParams(unittest.TestCase):
    """Test RansacParams data class.

    """
    def test_init(self) -> None:
        """Test RansacParams initialization.

        :return: None
        """
        params = pyransac.RansacParams(samples=1,
                                       iterations=2,
                                       confidence=3,
                                       threshold=4)

        self.assertEqual(params.samples, 1)
        self.assertEqual(params.iterations, 2)
        self.assertEqual(params.confidence, 3)
        self.assertEqual(params.threshold, 4)


if __name__ == '__main__':
    unittest.main()
