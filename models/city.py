#!/usr/bin/python3
"""
This is the definition of the `city class` module
"""

from models.base_model import BaseModel


class City(BaseModel):
	"""
	Definition of the City class
	Attributes:
		state_id: (str) id of state
		name: (str) name of state
	"""
	state_id = ""
	name = ""
