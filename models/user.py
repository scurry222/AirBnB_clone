#!/usr/bin/python3
""" A User class that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ A subclass of BaseModel that allows it to contain more information

        Attributes
        ----------
        email: str
           The email of the user
        password: str
           The password of the user
        first_name: str
           The first name of the user
        last_name: str
           The last name of the user
        all attributes from BaseModel are inherited
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
