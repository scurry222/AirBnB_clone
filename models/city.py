#!/usr/bin/python3
""" city.py - 1 class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    def __init__(self, state_id_="", name_="", *args, **kwargs):
        """ Initalize City as an obj
        Args:
            args: arguments from cmd line
            kwargs: Dict of obj attrs
        """
        self.state_id = state_id_
        self.name = name_
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        string = ""
        string += "[{}] ".format(__class__.__name__)
        string += "({}) ".format(self.id)
        string += "{}".format(self.__dict__)
        return string
