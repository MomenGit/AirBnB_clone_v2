#!/usr/bin/python3
"""
This module instantiates an object for storage
if it is a database storage the object is of type DBStorage
otherwise type FileStorage
"""
from os import getenv

storage = None

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
