#!/usr/bin/python3
"""
base_model - the base model for any class that inherits its attributes
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Class for the models to build on

        Attributes:
        id: str
           A unique id for any initiated BaseModel object
        created_at: datetime
           The time when the class was initiated
        update_at: datetime
           The time when the class was updated
    """

    def __init__(self, *args, **kwargs):
        """ Initializer for BaseModel """
        setup = '%Y-%m-%dT%H:%M:%S.%f'
        if len(kwargs) > 0:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                                                  kwargs["created_at"], setup)
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                                                  kwargs["updated_at"], setup)
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Make string representation of the class

        Args:
            self('class'): object to represent
        """
        string = ""
        string += "[{}] ".format(self.__class__.__name__)
        string += "({}) ".format(self.id)
        string += "{}".format(self.__dict__)
        return string

    def save(self):
        """ Update the time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dict representation """
        d = ""
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
