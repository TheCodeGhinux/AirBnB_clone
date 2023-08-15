#!/usr/bin/python3
"""Unit test for City"""

import unittest
import os
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """
    Defines class for City unit test.
    Tests the methods in City.
    """

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_city_state_id(self):
        """Test if City state_id attribute is initialized correctly."""
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_name(self):
        """Test if City name attribute is initialized correctly."""
        city = City()
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
