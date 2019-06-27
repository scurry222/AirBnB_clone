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
        self.__objects[key] = obj.to_dict()

    def save(self):
        insert = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding="utf-8") as myFile:
            myFile.write(insert)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as myFile:
                self.__objects = json.load(myFile)
