#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


# Create a single instance of DBStorage
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage after creating the instance
storage.reload()
