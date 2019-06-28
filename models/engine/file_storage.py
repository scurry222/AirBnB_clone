#!/usr/bin/python3

import json
import os

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if obj.__class__.__name__ == "User":
            new_dict = {'email': obj.email, 'password': obj.password}
            new = {'first_name': obj.first_name, 'last_name': obj.last_name}
            new.update(new_dict)
            new.update(obj.to_dict())
        self.__objects[key] = obj.to_dict()

    def save(self):
        insert = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as myFile:
            myFile.write(insert)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as myFile:
                self.__objects = json.load(myFile)
