#!/usr/bin/python3
"""import FileStorage and set it equal to
   storage and call reload 
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()