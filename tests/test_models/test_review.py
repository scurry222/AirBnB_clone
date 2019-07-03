#!/usr/bin/python3
"""
test_review - 1 test class

"""

import unittest
import re
import json
import os
import time
from models import storage
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestReview(unittest.TestCase):
    """ Tests for Review class """

    def setUp(self):
        """ Preinitialize values go here """
        pass

    def resetStorage(self):
        """ Reset FileStorage data """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """ Test instantiation of Review class """
        b = Review()
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        """ Tests attributes of Review class """
        attributes = storage.attributes()["Review"]
        b = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)
