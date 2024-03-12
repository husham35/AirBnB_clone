#!/usr/bin/python3
"""
This is the definition of the `amenity class` module
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Definition of the amenity class
    Attributes:
    name: (str) amenity name
    """
    name = ""
