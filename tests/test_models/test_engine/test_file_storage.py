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
        except FileNotFoundError:
            pass

    def test_save(self):
        obj1 = BaseModel()
        obj2 = User()
        obj1.save()
        obj2.save()

        self.storage.save()

        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write('{}')

        self.storage.reload()

        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == '__main__':
    unittest.main()
