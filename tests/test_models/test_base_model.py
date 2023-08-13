#!/usr/bin/python3                                                                                                                          
"""Test for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import models

class TestBaseModel(unittest.TestCase):
    """Definea the Test class"""

    def setUp(self):
        """Set up a new instance of BaseModel for each test."""
        self.base_model = BaseModel()

    def test_attributes(self):
        """Test the presence of required attributes."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        """Test if the 'id' attribute is a string."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """Test if 'created_at' attribute is a datetime object."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if 'updated_at' attribute is a datetime object."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """Test if 'save' method updates the 'updated_at' attribute."""
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """Test if 'to_dict' method returns a valid dictionary."""
        self.base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(self.base_model_dict, dict)
        self.assertEqual(self.base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(self.base_model_dict['created_at'], str)
        self.assertIsInstance(self.base_model_dict['updated_at'], str)

    def test_str(self):
        """Test if the '__str__' method returns the expected string representation."""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_all(self):
        """Test if 'all' method returns a dictionary containing instances."""
        all_instances = BaseModel.all()
        self.assertIsInstance(all_instances, dict)
        self.assertIn(self.base_model, all_instances.values())

if __name__ == '__main__':
    unittest.main()
