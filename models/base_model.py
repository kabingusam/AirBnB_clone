#!/usr/bin/python3
'''Define the BaseModel class'''
import from models
from uuid import uuid4
from datetime import datetime

Class BaseModel:
    '''Represents the BaseModel of the AirBnB project'''
    def __init__(self, *args, **kwargs):
        '''initialize a new BaseModel

        Args:
            args : unused
            kwargs(dict) : keys/value pairs of attributes
        '''
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
