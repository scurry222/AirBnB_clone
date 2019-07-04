#!/usr/bin/python3
""" city.py - 1 class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits attributes from base model
        Attributes
        ----------
        state_id: str
          the state where the city is located
        name: str
          the name of the city
        all attributes from BaseModel are inherited
    """

    state_id = ""
    name = ""
