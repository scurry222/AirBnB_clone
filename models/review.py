#!/usr/bin/python3
""" review.py - 1 class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    def __init__(self, place_id_="", user_id_="", text="", *args, **kwargs):
        """ Initalize City as an obj
        Args:
            args: arguments from cmd line
            kwargs: Dict of obj attrs
        """
        self.place_id = place_id_
        self.user_id = user_id_
        self.text = text
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        string = ""
        string += "[{}] ".format(__class__.__name__)
        string += "({}) ".format(self.id)
        string += "{}".format(self.__dict__)
        return string
