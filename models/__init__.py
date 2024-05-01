#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
#from models.engine.file_storage import FileStorage
from os import getenv
from models.engine import db_storage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()


storage.reload()
