#!/usr/bin/python3
"""Console test"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Unit test for console"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(mock_stdout.getvalue()) > 0)

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            self.assertTrue(len(mock_stdout.getvalue()) > 0)

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), "** instance id missing **")

    def test_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("BaseModel.count()")
            self.assertTrue(len(mock_stdout.getvalue()) > 0)

if __name__ == '__main__':
    unittest.main()
