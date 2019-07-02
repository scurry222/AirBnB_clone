#!/usr/bin/python3
""" city.py - 1 class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    state_id = state_id_
    name = name_
