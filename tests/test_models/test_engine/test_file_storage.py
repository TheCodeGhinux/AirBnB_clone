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

    def test_reload(self):
        # Create an empty file before testing reload
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write('{}')

        # Perform the reload
        self.storage.reload()

        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == '__main__':
    unittest.main()
