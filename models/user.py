#!/usr/bin/python3
"""
This is the definition of the `User class` module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Definition of User class
    Attributes:
        email: (str) user email address
        password: (str) user password
        first_name: (str) user first name
        last_name: (str) user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
