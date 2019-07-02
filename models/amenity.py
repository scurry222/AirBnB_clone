#!/usr/bin/python3
""" amenity.py - 1 class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    state_id = ""
    name = ""
