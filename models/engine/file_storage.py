#!/usr/bin/python3
""" Main program that stores information about the class """

import json
import os

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

    def all(self):
        """ Returns the __objects dictionary """
        return self.__objects

    def new(self, obj):
        """ Creates a dictionary from the obj dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if obj.__class__.__name__ == "User":
            new_dict = {'email': obj.email, 'password': obj.password}
            new = {'first_name': obj.first_name, 'last_name': obj.last_name}
            new.update(new_dict)
            new.update(obj.to_dict())
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ Saves the __objects dictionary on a json file """
        insert = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as myFile:
            myFile.write(insert)

    def reload(self):
        """ Loads the dictionary from a json file and stores it in __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as myFile:
                self.__objects = json.load(myFile)
