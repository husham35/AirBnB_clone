#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import datetime
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test instances for the amenity class"""

    amenity = Amenity()

    def test_class_exists(self):
        """test if class exists"""
        result = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amenity)), result)

    def test_has_attrs(self):
        """test if attributes exist"""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_user_inheritance(self):
        """test if the Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_types(self):
        """tests the type of the attribute is the correct one"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.name, str)
        self.assertIsInstance(self.amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
