#!/usr/bin/python3
""" A User class that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ A subclass of BaseModel that allows it to contain more information
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
