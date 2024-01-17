#!/usr/bin/python3
"""Instance of an object of  FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from os import getenv

StorageType = getenv('HBNB_TYPE_STORAGE')
if StorageType == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
