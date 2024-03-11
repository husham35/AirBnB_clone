#!/usr/bin/python3
"""
This is the definition of the `Place class` module
"""

from models.base_model import BaseModel


class Place(BaseModel):
	"""
	Definition of the Place class
	Attributes:
		city_id: (str) id of city
		user_id: (str) id of user
		name: (str) name of place
		description: (str) description of place
		number_rooms: (int) number of rooms
		number_bathrooms: (int) number of bathrooms
		max_guest: (int) number of maximum guest
		price_by_night: (int) price per night
		latitude: (float) latitude of the place
		longitude: (float) longitude of the place
		amenity_ids: (list) a list of ids of amenities
	"""
	city_id =  ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []
