#!/usr/bin/python3

"""
"""

import re
import cmd
import os
import json
import time
import unittest
import uuid
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """  """

    def SetUp(self):
        """  """

    def tearDown(self):
        """  """
        pass

    def resetStorage(self):
        """  """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """  """
        b = BaseModel()
        self.assertEqual(str(type(b)),
                        "<class 'models.base_model.BaseModel'>")
        self. assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_instance_kwargs(self):
        """  """
        b = BaseModel()
        b.name = "scoot"
        b.age = 98
        model_json = b.to_dict()
        new_model = BaseModel(**model_json)
        self.assertEqual(new_model.to_dict(), b.to_dict())

    def test_instance_dict(self):
        """  """
        d = {"__class__": "BaseModel",
             "updated_at":
             datetime(42, 12, 6, 12, 54, 6, 12).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "char": "a",
             "str": "string time",
             "int": 42,
             "float": 3.14}
        base = BaseModel(**d)
        self.assertEqual(base.to_dict(), d)

    def test_no_arg_init(self):
        """  """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.__init__()

    def test_many_arg_init(self):
        """  """
        self.resetStorage()
        b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_attributes(self):
        """  """
        
    def test_none(self):
        """  """
        b = BaseModel()
        rec = re.compile("^\[(.*)] \((.*)\) (.*)$")
        reb = rec.match(str(b))
        self.assertIsNotNone(reb)

    def test_str_model(self):
        """  """
        b = BaseModel()
        rec = re.compile("^\[(.*)] \((.*)\) (.*)$")
        reb = rec.match(str(b))
        self.assertEqual(reb.group(1), "BaseModel")

    def test_str_id(self):
        """  """
        b = BaseModel()
        rec = re.compile("^\[(.*)] \((.*)\) (.*)$")
        reb = rec.match(str(b))
        self.assertEqual(reb.group(2), b.id)

    def test_str_datetime(self): 
        """  """
        b = BaseModel()
        rec = re.compile("^\[(.*)] \((.*)\) (.*)$")
        reb = rec.match(str(b))
        date = reb.group(3)
        date = re.match("(datetime\.datetime\(*\))", date)

    def test_to_dict_no_args(self):
        """  """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.to_dict()

    def test_to_dict_many_args(self):
        """  """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.to_dict(98, 99)

    def test_to_dict_name(self):
        """  """
        b = BaseModel()
        b.name = "scoot"
        d = b.to_dict()
        self.assertEqual(d["name"], b.name)

    def test_to_dict_class(self):
        """  """
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["__class__"], type(b).__name__)

    def test_to_dict_age(self):
        """  """
        b = BaseModel()
        b.age = 108
        d = b.to_dict()
        self.assertEqual(d["age"], b.age)

    def test_to_dict_id(self):
        """  """
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)

    def test_to_dict_created_at(self):
        """  """
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["created_at"], b.created_at.isoformat())

    def test_to_dict_updated_at(self):
        """  """
        b = BaseModel()
        b.name = "scoot"
        d = b.to_dict()
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())

    def test_save_no_args(self):
        """  """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_save_many_args(self):
        """  """
        self.resetStorage()
        with self.assertRaises(TypeError):
            BaseModel.save(4, 42)

if __name__ == '__main__':
    unittest.main()       
