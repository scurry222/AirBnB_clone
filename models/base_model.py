#!/usr/bin/python3

import uuid
import datetime

"""
base_model - 1 class
"""


class BaseModel():
    """
    Class for the models to build on
    """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Make string representation of the class

        Args:
            self('class'): object to represent
        """
        string = ""
        string += "[<{}>] ".format(__class__.__name__)
        string += "(<{}>) ".format(self.id)
        string += "<{}>".format(self.__dict__)
        return string

    def save(self):
        """ Update the time """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Return a dict representation """
        d = ""
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
