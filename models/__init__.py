#!/usr/bin/python3
""" initialization of storage """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
