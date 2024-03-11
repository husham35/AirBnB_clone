#!/usr/bin/python3
"""
This is the definition of the `Review class` module
"""

from models.base_model import BaseModel


class Review(BaseModel):
	"""
	Definition of Review class
	Attributes:
		place_id: (str) id of place
		user_id: (str) id of user
		text: (str) content of review
	"""
	place_id = ""
	user_id = ""
	text = ""
