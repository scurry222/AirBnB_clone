#!/usr/bin/python3
""" city.py - 1 class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits attributes from base model
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
