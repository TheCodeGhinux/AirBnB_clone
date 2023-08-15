#!/usr/bin/python3
"""Unit test for Review"""

import unittest
import os
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """
    Defines class for Review unit test.
    Tests the methods in Review.
    """

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_review_place_id(self):
        """Test if Review place_id attribute is initialized correctly."""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_review_user_id(self):
        """Test if Review user_id attribute is initialized correctly."""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_review_text(self):
        """Test if Review text attribute is initialized correctly."""
        review = Review()
        self.assertEqual(review.text, "")

    # Add more test methods here


if __name__ == '__main__':
    unittest.main()
