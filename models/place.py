#!/usr/bin/python3
""" place.py - 1 class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits attributes from base model

        attributes
        -----------
        name: str
           name of the place
        city_id: str
           city identification
        user_id: str
           user identification
        description: str
           description of the place
        number_rooms: int
           number of rooms
        number_bathrooms: int
           number of bathrooms
        max_guest: int
           max number of guest
        price_by_night: int
           the cost of a place by night
        latitude: double
           latitude of map location
        longitude: double
           longitude of the map location
        amenity_ids: list
           A list of amenities
        all attributes from BaseModel are inherited
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
