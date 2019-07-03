#!/usr/bin/python3
"""
test_file_storage - 1 test_class

"""

import unittest
import time
import os
import json
import re
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage class """

    def SetUp(self):
        """ Initialize values go here """
        pass

    def resetStorage(self):
        """ Reset FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """ Test initialiation """
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_initialize_no_args(self):
        """ Test no arg input """
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.__init__()

    def test_initialize_many_args(self):
        """ Test too many arg input """
        self.resetStorage()
        with self.assertRaises(TypeError):
            f = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_all_no_args(self):
        """ Test all() against no args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.all()

    def test_all_many_args(self):
        """ Test all() against too many args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.all(98, 99)

    def all_helper(self, inp):
        """ Do all assertions on all() class inputs """
        self.resetStorage()
        self.assertEqual(storage.all(), {})
        s = storage.references()[inp]()
        storage.new(s)
        k = "{}.{}".format(type(s).__name__, s.id)
        self.assertTrue(k in storage.all())
        self.assertEqual(storage.all()[k], s)

    def test_all_base_model(self):
        """ Test all method on BaseModel """
        self.all_helper("BaseModel")

    def test_all_user(self):
        """ Test all method on User """
        self.all_helper("BaseModel")

    def test_all_state(self):
        """ Test all method on State """
        self.all_helper("BaseModel")

    def test_all_city(self):
        """ Test all method on City """
        self.all_helper("BaseModel")

    def test_all_place(self):
        """ Test all method on Place """
        self.all_helper("BaseModel")

    def test_all_amenity(self):
        """ Test all method on Amenity """
        self.all_helper("BaseModel")

    def test_all_review(self):
        """ Test all method on Review """
        self.all_helper("BaseModel")

    def test_new_no_args(self):
        """ Test new() against no args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_many_args(self):
        """ Test new() against too many args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            storage.new(98, 99)

    def new_helper(self, inp):
        """ Do all assertions for new() class inputs """
        self.resetStorage()
        s = storage.references()[inp]()
        storage.new(s)
        k = "{}.{}".format(type(s).__name__, s.id)
        self.assertTrue(k in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[k], s)

    def test_new_base_model(self):
        """ Test new method on BaseModel """
        self.new_helper("BaseModel")

    def test_new_user(self):
        """ Test new method on User """
        self.new_helper("User")

    def test_new_state(self):
        """ Test new method on State """
        self.new_helper("State")

    def test_new_city(self):
        """ Test new method on City """
        self.new_helper("City")

    def test_new_place(self):
        """ Test new method on Place """
        self.new_helper("Place")

    def test_new_base_amenity(self):
        """ Test new method on Amenity """
        self.new_helper("Amenity")

    def test_new_review(self):
        """ Test new method on Review """
        self.new_helper("Review")

    def test_save_no_args(self):
        """ Test save() against no args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.save()

    def test_save_many_args(self):
        """ Test save() against too many args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.save(98, 99)

    def save_helper(self, inp):
        """ Do all assertions for save() class inputs """
        self.resetStorage()
        s = storage.references()[inp]()
        storage.new(s)
        k = "{}.{}".format(type(s).__name__, s.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {k: s.to_dict()}
        with open(FileStorage._FileStorage__file_path, "r",
                  encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_base_model(self):
        """ Tests save method on BaseModel """
        self.save_helper("BaseModel")

    def test_save_user(self):
        """ Tests save method on User """
        self.save_helper("User")

    def test_save_state(self):
        """ Tests save method on State """
        self.save_helper("State")

    def test_save_city(self):
        """ Tests save method on City """
        self.save_helper("City")

    def test_save_place(self):
        """ Tests save method on Place """
        self.save_helper("Place")

    def test_save_base_amenity(self):
        """ Tests save method on Amenity """
        self.save_helper("Amenity")

    def test_save_base_review(self):
        """ Tests save method on Review """
        self.save_helper("Review")

    def reload_no_args(self):
        """ Test reload() against no args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            FileStorage.reload()

    def reload_many_args(self):
        """ Test reload() against too many args """
        self.resetStorage()
        with self.assertRaises(TypeError):
            fileStorage.reload(98, 99)

    def reload_helper(self, inp):
        """ Do all assertions for reload() class inputs """
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        s = storage.references()[inp]()
        storage.new(s)
        k = "{}.{}".format(type(s).__name__, s.id)
        storage.save()
        storage.reload()
        self.assertEqual(s.to_dict(), storage.all()[k].to_dict())

    def test_reload_base_model(self):
        """ Tests reload method on BaseModel """
        self.reload_helper("BaseModel")

    def test_reload_user(self):
        """ Tests reload method on User """
        self.reload_helper("User")

    def test_reload_state(self):
        """ Tests reload method on State """
        self.reload_helper("State")

    def test_reload_city(self):
        """ Tests reload method on City """
        self.reload_helper("City")

    def test_reload_place(self):
        """ Tests reload method on Place """
        self.reload_helper("Place")

    def test_reload_amenity(self):
        """ Tests reload method on Amenity """
        self.reload_helper("Amenity")

    def test_reload_review(self):
        """ Tests reload method on Review """
        self.reload_helper("Review")


if __name__ == '__main__':
    unittest.main()
