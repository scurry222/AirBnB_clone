#!/usr/bin/python3
""" place.py - 1 class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    def __init__(self,n="", c="", u="", d="", nr="", nb="", mg="", lt="",
                 lg="", ai=[""], *args, **kwargs):
        """ Initalize City as an obj
        Args:
            args: arguments from cmd line
            kwargs: Dict of obj attrs
        """
        self.name = n
        self.city_id = c
        self.user_id = u
        self.description = d
        self.number_rooms = nr
        self.number_bathrooms = nb
        self.max_guest = mg
        self.latitude = lt
        self.longitude = lg
        self.amenity_ids = ai
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        string = ""
        string += "[{}] ".format(__class__.__name__)
        string += "({}) ".format(self.id)
        string += "{}".format(self.__dict__)
        return string
