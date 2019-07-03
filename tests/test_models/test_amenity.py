#!/usr/bin/python3
"""
test_amenity - 1 test class

"""

import unittest
import re
import json
import os
import time
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Tests for Amenity class """

    def setUp(self):
        """ Preinitialize values go here """
        pass

    def resetStorage(self):
        """ Reset FileStorage data """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """ Test instantiation of Amenity class """
        b = Amenity()
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        """ Tests attributes of Amenity class """
        attributes = storage.attributes()["Amenity"]
        b = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)
