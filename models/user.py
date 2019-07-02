#!/usr/bin/python3
""" A User class that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ A subclass of BaseModel that allows it to contain more information
    """

    def __init__(self, email="", passw="", first="", last="", *args, **kwargs):
        """ Initializes the baseModel and its own attributes"""
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = passw
        self.first_name = first
        self.last_name = last
