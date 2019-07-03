#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
import re
import json
import os
import time
from models import storage
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestState(unittest.TestCase):
    """ Tests for State class """

    def setUp(self):
        """ Preinitialize values go here """
        pass

    def resetStorage(self):
        """ Reset FileStorage data """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """ Test instantiation of State class """
        b = State()
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_attributes(self):
        """ Tests attributes of State class """
        attributes = storage.attributes()["State"]
        b = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(b, k))
            self.assertEqual(type(getattr(b, k, None)), v)
