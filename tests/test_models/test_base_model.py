#!/usr/bin/python3                                                                                                                          
"""Test for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import models

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        self.base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(self.base_model_dict, dict)
        self.assertEqual(self.base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(self.base_model_dict['created_at'], str)
        self.assertIsInstance(self.base_model_dict['updated_at'], str)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_all(self):
        all_instances = BaseModel.all()
        self.assertIsInstance(all_instances, dict)
        self.assertIn(self.base_model, all_instances.values())

if __name__ == '__main__':
    unittest.main()
