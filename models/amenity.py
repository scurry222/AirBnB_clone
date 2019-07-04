#!/usr/bin/python3
""" amenity.py - 1 class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits attributes from base model

        attributes
        ----------
        state_id: str
        name: str
        all attributes from BaseModel are inherited
    """

    state_id = ""
    name = ""
