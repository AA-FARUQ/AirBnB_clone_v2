#!/usr/bin/python3
"""This module instantiates a storage object based on environment variabe"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Create a storage instance based on the environment variable
storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all models.
"""
storage_instance.reload()
