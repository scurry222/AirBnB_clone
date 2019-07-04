#!/usr/bin/python3
""" review.py - 1 class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits attributes from base model

        Attributes
       -----------
       place_id: str
          The identification of the place
       user_id: str
          The identification of the user
       text: str
          The text
       all attributes from BaseModel are inherited
    """

    place_id = ""
    user_id = ""
    text = ""
