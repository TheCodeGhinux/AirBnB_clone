#!/usr/bin/python3
"""Unit test for State"""

import unittest
import os
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """
    Defines class for State unit test.
    Tests the methods in State.
    """

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_state_name(self):
        """Test if State name attribute is initialized correctly."""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
