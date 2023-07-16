#!/usr/bin/python3
"""Test BaseModel for expected behavior"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests to check BaseModel class"""
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        """Test initialization"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_str(self):
        """Test str"""
        expected = "[BaseModel] ({}) {}".format(self.model.id,
                                                self.model.__dict__)
        self.assertEqual(str(self.model), expected)

    def test_save(self):
        """Test save"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test dict """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(type(model_dict["created_at"]), str)
        self.assertEqual(type(model_dict["updated_at"]), str)


if __name__ == '__main__':
    """Main class"""
    unittest.main()
