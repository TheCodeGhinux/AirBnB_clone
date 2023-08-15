#!/usr/bin/python3
"""Unit test for FileStorage"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Defines class for file storage unit test.
    Tests the methods in file storage.
    """

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except:
            pass

    def test_all_empty(self):
        all_objs = self.storage.all()
        self.assertEqual(type(all_objs), dict)
        self.assertEqual(len(all_objs), 0)

    def test_all_non_empty(self):
        obj1 = BaseModel()
        obj2 = User()
        obj1.save()
        obj2.save()

        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)
        self.assertIn("BaseModel." + obj1.id, all_objs)
        self.assertIn("User." + obj2.id, all_objs)


if __name__ == '__main__':
    unittest.main()
