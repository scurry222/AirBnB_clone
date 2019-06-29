#!/usr/bin/python3
""" review.py - 1 class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initalize City as an obj
        Args:
            args: arguments from cmd line
            kwargs: Dict of obj attrs
        """
        super().__init__(self, *args, **kwargs)
