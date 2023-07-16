#!/usr/bin/python3
"""Test Amenity for expected behavior"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""
    def setUp(self):
        """Test setup"""
        self.amenity = Amenity()

    def test_init(self):
        """Test init"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
