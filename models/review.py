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
