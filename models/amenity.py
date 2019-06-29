#!/usr/bin/python3
""" amenity.py - 1 class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    self.state_id = ""
    self.name = ""

    def __init__(self, *args, **kwargs):
        """ Initalize City as an obj
        Args:
            args: arguments from cmd line
            kwargs: Dict of obj attrs
        """
        super().__init__(self, *args, **kwargs)
