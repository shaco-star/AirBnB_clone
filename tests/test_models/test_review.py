#!/usr/bin/python3
"""Test Review for expected behavior"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests to check Review class"""

    def setUp(self):
        """Test setup"""
        self.review = Review()

    def test_init(self):
        """Test init"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.review, BaseModel)


if __name__ == '__main__':
    """Main class"""
    unittest.main()
