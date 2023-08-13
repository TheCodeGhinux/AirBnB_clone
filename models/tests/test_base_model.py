#!/usr/bin/python3
"""Unit test for base model"""
import time
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    "Defines unit test class"

    def test_init_with_kwargs(self):
        data = {
            'id': '123',
            'created_at': '2023-08-11T12:00:00.000000',
            'updated_at': '2023-08-11T14:30:00.000000',
            'name': 'Test Model'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.created_at, datetime(2023, 8, 11, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2023, 8, 11, 14, 30, 0))
        self.assertEqual(obj.name, 'Test Model')

    def test_str_method(self):
        obj = BaseModel()
        expected = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected)

    def test_save_method(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at

        # Introduce a short delay (e.g., 1 second) to ensure updated_at changes
        time.sleep(1)

        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
