"""Test cases for base module.

This module contains tests for the base module definitions.
"""

# Standard library imports
import unittest

# Local application imports
from pyransac import base


class TestRansac(unittest.TestCase):
    """Tests the Model base class.

    """
    def test_model_init(self):
        """Test that instantiating Model class throws error.

        """
        self.assertRaises(TypeError, base.Model)


if __name__ == '__main__':
    unittest.main()
