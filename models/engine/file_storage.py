#!/usr/bin/python3
"""
This is a module contains the definition of the FileStorage class
"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serializes instances to a JSON file and desrializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State,
    }

    def all(self):
        """
        Returns: the dictionary `__objects`
        """
        return type(self).__objects

    def new(self, obj):
        """
        Sets in `__objects` the `obj` with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        type(self).__objects[key] = obj
        #
        # key = "{}.{}".format(type(obj).__name__, obj.id)
        # FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes `__objects` to the JSON file `__file_path`
        """
        objs = {
            key: value.to_dict() for key, value in type(self).__objects.items()
        }
        with open(type(self).__file_path, mode="w", encoding="utf-8") as file:
            json.dump(objs, file)
        #
        # with open(FileStorage.__file_path, "w", encoding="utf-8") as fsa:
        #             dsa = {ksa: vsa.to_dict() for ksa, vsa in FileStorage.__objects.items()}
        #             json.dump(dsa, fsa)

    def reload(self):
        """
        Deserializes the JSON file to `__objects` if `__file_path`
        exists, else nothing
        """
        if os.path.exists(type(self).__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                new_obj_dict = json.load(file)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value["__class__"]](**value)
                self.__objects[key] = obj
