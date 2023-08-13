#!/usr/bin/python3                                                                                                                          
"""Test for BaseModel"""

import unittest
from datetime import datetime
from ...models.base_model import BaseModel  # Relative import                                                                               


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        model = BaseModel()

        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        model = BaseModel()
        model_str = str(model)
        expected = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model_str, expected)

    def test_save_method(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)


if __name__ == '__main__':
    unittest.main()
