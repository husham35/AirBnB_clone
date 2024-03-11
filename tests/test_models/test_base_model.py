#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel
"""

import os
import contextlib
import unittest
from time import sleep
from datetime import datetime
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for instantiation of the BaseModel class."""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_diff_ids(self):
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_two_models_diff_created_at(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.created_at, base_model_2.created_at)

    def test_two_models_diff_updated_at(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.updated_at, base_model_2.updated_at)

    def test_str_representation(self):
        dt_obj = datetime.now()
        dt_repr = repr(dt_obj)
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = dt_obj
        base_model_str = str(base)
        self.assertIn("[BaseModel] (123456)", base_model_str)
        self.assertIn("'id': '123456'", base_model_str)
        self.assertIn(f"'created_at': {dt_repr}", base_model_str)
        self.assertIn(f"'updated_at': {dt_repr}", base_model_str)

    def test_unused_args(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_instantiate_with_kwargs(self):
        dt_obj = datetime.now()
        dt_iso = dt_obj.isoformat()
        base = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, dt_obj)
        self.assertEqual(base.updated_at, dt_obj)

    def test_instantiate_with_no_kwargs(self):
        with self.assertRaises(ValueError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiate_with_args_and_kwargs(self):
        dt_obj = datetime.now()
        dt_iso = dt_obj.isoformat()
        base = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, dt_obj)
        self.assertEqual(base.updated_at, dt_obj)

    """Unittests for the `save` method of the BaseModel class."""

    def setUp(self):
        with contextlib.suppress(IOError):
            os.rename("file.json", "tmp")

    def tearDown(self):
        with contextlib.suppress(IOError):
            os.remove("file.json")
        with contextlib.suppress(IOError):
            os.rename("tmp", "file.json")

    def test_one_save(self):
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        self.assertLess(first_updated_at, base.updated_at)

    def test_two_saves(self):
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        second_updated_at = base.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base.save()
        self.assertLess(second_updated_at, base.updated_at)

    def test_save_with_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

    def test_save_updates_file(self):
        base = BaseModel()
        base.save()
        base_model_id = "BaseModel.{}".format(base.id)
        with open("file.json", mode="r", encoding="utf-8") as file:
            self.assertIn(base_model_id, file.read())

    """Unittests for `to_dict` method of the BaseModel class."""

    def test_to_dict_type(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dict_with_correct_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_to_dict_with_added_attrs(self):
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 98
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict_datetime_attrs_are_strs(self):
        base = BaseModel()
        base_model_dict = base.to_dict()
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))

    def test_to_dict_output(self):
        dt_obj = datetime.now()
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = dt_obj
        todict = {
            "id": "123456",
            "__class__": "BaseModel",
            "created_at": dt_obj.isoformat(),
            "updated_at": dt_obj.isoformat(),
        }
        self.assertDictEqual(base.to_dict(), todict)

    def test_to_dict__dict(self):
        base = BaseModel()
        self.assertNotEqual(base.to_dict(), base.__dict__)

    def test_to_dict_with_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)


if __name__ == "__main__":
    unittest.main()
