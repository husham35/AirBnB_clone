#!/usr/bin/python3
"""
This is a module that contains the BaseModel class,
it contains all the definitions for methods/attributes of
the BaseModel class that will be inherited by other classes
"""

import uuid
from datetime import datetime
import models

class BaseModel:
	"""Definition for the BaseModel class"""

	def __init__(self, *args, **kwargs):
		"""Initializes the BaseModel class"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = self.created_at

		# checks if kwargs has items
		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				if key in ["created_at", "updated_at"]:
					val = datetime.strptime(str(value), "%Y-%m-%dT%H:%M:%S.%f")
					setattr(self, key, val)
				else:
					setattr(self, key, value)
		else:
			models.storage.new(self)


	def __str__(self):
		"""Prints the details of the BaseModel class"""
		classname = self.__class__.__name__
		return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

	def save(self):
		"""
		Updates the public instance attribute updated_at
		with the current datetime
		"""
		self.updated_at =  datetime.now()
		models.storage.save()

	def to_dict(self):
		"""
		Makes a dictionary containing all the key/values of __dict__ of the instance:
			-by using `self.__dict__`, only instance attributes set will be returned
			-a key __class__ must be added to this dictionary with the
				of the object
			-created_at/updated_at must be converted to string object in ISO formatr
			-
		Returns:
			a dictionary containing all keys/values of __dict__ of the instance
		"""
		dict = self.__dict__.copy()
		# dict["__class__"] = self.__class__.__name__
		# dict["created_at"] = self.created_at.isoformat()
		# dict["updated_at"] = self.updated_at.isoformat()
		#
		dict["__class__"] = self.__class__.__name__
		dict["created_at"] = self.created_at.isoformat()
		dict["updated_at"] = self.updated_at.isoformat()

		return dict
