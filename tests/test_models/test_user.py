#!/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""

import contextlib
import os
import unittest
from datetime import datetime
from time import sleep

import models
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for the cdinstantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_diff_created_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_diff_updated_at(self):
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        dt_inst = datetime.now()
        dt_repr = repr(dt_inst)
        usr = User()
        usr.id = "123456"
        usr.created_at = usr.updated_at = dt_inst
        usstr = str(usr)
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn(f"'created_at': {dt_repr}", usstr)
        self.assertIn(f"'updated_at': {dt_repr}", usstr)

    def test_unused_args(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiate_with_kwargs(self):
        dt_inst = datetime.now()
        dt_iso = dt_inst.isoformat()
        usr = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(usr.id, "345")
        self.assertEqual(usr.created_at, dt_inst)
        self.assertEqual(usr.updated_at, dt_inst)

    def test_instantiate_with_none_kwargs(self):
        with self.assertRaises(ValueError):
            User(id=None, created_at=None, updated_at=None)

    """Unittests for testing save method of the  class."""

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
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)

    def test_two_saves(self):
        usr = User()
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        second_updated_at = usr.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        usr.save()
        self.assertLess(second_updated_at, usr.updated_at)

    def test_save_with_arg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        usid = f"User.{user.id}"
        with open("file.json", "r", encoding="utf-8") as file:
            self.assertIn(usid, file.read())

    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_has_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_has_added_attributes(self):
        user = User()
        user.middle_name = "Holberton"
        user.my_number = 98
        self.assertEqual("Holberton", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        us_dict = user.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.now()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = date
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), tdict)

    def test_contrast_to_dict__dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
