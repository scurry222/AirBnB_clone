#!/usr/bin/python3
"""
test_city - 1 test class

"""

import unittest
import re
import json
import os
import time
from models import storage
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestCity(unittest.TestCase):
    """ Tests for City class """

    def setUp(self):
        """ Preinitialize values go here """
        pass

    def resetStorage(self):
        """ Reset FileStorage data """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """ Test instantiation of City class """
        b = City()
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        """ Tests attributes of City class """
        attributes = storage.attributes()["City"]
        b = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)
