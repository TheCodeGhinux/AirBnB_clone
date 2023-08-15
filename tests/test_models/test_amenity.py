#!/usr/bin/python3
"""Unit test for Amenity"""

import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    Defines class for Amenity unit test.
    Tests the methods in Amenity.
    """

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_amenity_name(self):
        """Test if Amenity name attribute is initialized correctly."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
