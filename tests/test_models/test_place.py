#!/usr/bin/python3
"""Unit test for Place"""

import unittest
import os
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """
    Defines class for Place unit test.
    Tests the methods in Place.
    """

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_place_city_id(self):
        """Test if Place city_id attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_place_user_id(self):
        """Test if Place user_id attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_place_name(self):
        """Test if Place name attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.name, "")

    def test_place_description(self):
        """Test if Place description attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.description, "")

    def test_place_number_rooms(self):
        """Test if Place number_rooms attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """Test if Place number_bathrooms attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_place_max_guest(self):
        """Test if Place max_guest attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_place_price_by_night(self):
        """Test if Place price_by_night attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_place_latitude(self):
        """Test if Place latitude attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_place_longitude(self):
        """Test if Place longitude attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_place_amenity_ids(self):
        """Test if Place amenity_ids attribute is initialized correctly."""
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
