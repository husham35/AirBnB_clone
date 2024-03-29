#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview
"""

import contextlib
import os
import unittest
from datetime import datetime
from time import sleep

import models
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_text_is_public_class_attribute(self):
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_two_reviews_diff_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    def test_two_reviews_diff_updated_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    def test_str_representation(self):
        date = datetime.now()
        dt_repr = repr(date)
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = date
        rvstr = str(rev)
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn(f"'created_at': {dt_repr}", rvstr)
        self.assertIn(f"'updated_at': {dt_repr}", rvstr)

    def test_args_unused(self):
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_instantiate_with_kwargs(self):
        date = datetime.now()
        dt_iso = date.isoformat()
        rev = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rev.id, "345")
        self.assertEqual(rev.created_at, date)
        self.assertEqual(rev.updated_at, date)

    def test_instantiate_with_None_kwargs(self):
        with self.assertRaises(ValueError):
            Review(id=None, created_at=None, updated_at=None)

    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUpClass(cls):
        with contextlib.suppress(IOError):
            os.rename("file.json", "tmp")

    def tearDown(self):
        with contextlib.suppress(IOError):
            os.remove("file.json")
        with contextlib.suppress(IOError):
            os.rename("tmp", "file.json")

    def test_one_save(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)

    def test_two_saves(self):
        rev = Review()
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        second_updated_at = rev.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rev.save()
        self.assertLess(second_updated_at, rev.updated_at)

    def test_save_with_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_save_updates_file(self):
        rev = Review()
        rev.save()
        rvid = f"Review.{rev.id}"
        with open("file.json", "r", encoding="utf-8") as file:
            self.assertIn(rvid, file.read())

    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_has_correct_keys(self):
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_to_dict_has_added_attrs(self):
        rev = Review()
        rev.middle_name = "Holberton"
        rev.my_number = 98
        self.assertEqual("Holberton", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def test_to_dict_datetime_attrs_are_strs(self):
        rev = Review()
        rv_dict = rev.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.now()
        rev = Review()
        rev.id = "123456"
        rev.created_at = rev.updated_at = date
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), tdict)

    def test_contrast_to_dict__dict(self):
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def test_to_dict_with_arg(self):
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)


if __name__ == "__main__":
    unittest.main()
