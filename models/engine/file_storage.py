#!/usr/bin/python3
""" Main program that stores information about the class """

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
import json
import os
import datetime


class FileStorage():
    """ This class stores information about the object in a json file
        Attributes
        -----------
        __file_path:
            contains the path to the file
        __objects:
            The dictionary that will store a dictionary of object attributes
        Methods
       ---------
         all(self):
            returns a dictionary of objects
         new(self, obj):
            Creates a key of the object cass and id. It then takes
            in the object dictionary representation and stores it in the key
            It then returns the entire dictionary
         save(self):
            Stores the __objects dictionary in a json file
         reload(self):
             Reads the json file and loads the dictioanry back to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def references(self):
        from models.user import User
        from models.amenity import Amenity
        from models.review import Review
        from models.state import State
        from models.place import Place
        from models.base_model import BaseModel
        from models.city import City

        class_list = {"BaseModel": BaseModel, "User": User,
                      "State": State, "City": City,
                      "Amenity": Amenity, "Place": Place,
                      "Review": Review}
        return class_list

    def attributes(self):
        attributes = {
            "BaseModel":
            {
                "updated_at": datetime.datetime,
                "created_at": datetime.datetime,
                "id": str
            },
            "User":
            {
                "email": str,
                "last_name": str,
                "password": str,
                "first_name": str
            },
            "State":
            {
                "name": str
            },
            "City":
            {
                "state_id": str,
                "name": str
            },
            "Amenity":
            {
                "name": str
            },
            "Place":
            {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "max_guest": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            },
            "Review": {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes

    def all(self):
        """ Returns the __objects dictionary """
        return self.__objects

    def new(self, obj):
        """ Creates a dictionary from the obj dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Saves the __objects dictionary on a json file """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary.update({key: value.to_dict()})
        insert = json.dumps(dictionary)
        with open(self.__file_path, "w", encoding="utf-8") as myFile:
            myFile.write(insert)

    def reload(self):
        """ Loads the dictionary from a json file and stores it in __objects"""
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding='utf-8') as myFile:
                    obj_dict = {}
                    obj_dict = json.load(myFile)
                    for key, value in obj_dict.items():
                        inp = key.split(".")
                        if "BaseModel" == inp[0]:
                            self.__objects[key] = BaseModel(**value)
                        elif "User" == inp[0]:
                            self.__objects[key] = User(**value)
            except Exception:
                pass

    @property
    def objects(self):
        """ Getter for objects """
        return self.__class__.__objects

    @objects.setter
    def objects(self):
        """ Setter for objects """
        obj = {}
        self.__class__.__objects = obj
