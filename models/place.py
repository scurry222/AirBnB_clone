#!/usr/bin/python3
""" place.py - 1 class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits attributes from base model
    Args:
        BaseModel('class'): include attributes
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
