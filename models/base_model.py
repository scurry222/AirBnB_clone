#!/usr/bin/python3

import uuid
import datetime

"""
"""


class BaseModel():
    """
    """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        string = ""
        string += "[<{}>] ".format(__class__.__name__)
        string += "(<{}>) ".format(self.id)
        string += "<{}>".format(self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        tmp = ""
        tmp = self.__dict__.copy()
        tmp['__class__'] = self.__class__.__name__
        tmp['created_at'] = self.created_at.isoformat()
        tmp['updated_at'] = self.updated_at.isoformat()
        return tmp
