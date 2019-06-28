#!/usr/bin/python3
""" state.py - 1 class """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    self.name = ""

    def __init__(self, *args, **kwargs):
        """ Initalize City as an obj
        Args:
            args: arguments from cmd line
            kwargs: Dict of obj attrs
        """
        super().__init__(self, *args, **kwargs)
