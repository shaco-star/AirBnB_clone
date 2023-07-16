#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel

"""Test BaseModel for expected behavior"""


class TestUser(unittest.TestCase):
    """Tests to check TestUser class"""

    def setUp(self):
        self.user = User()

    def test_init(self):
        """Test initialization"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.user, BaseModel)


if __name__ == '__main__':
    unittest.main()
