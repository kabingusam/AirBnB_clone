#!/usr/bin/python3
"""The city class"""
from models.base_model import BaseModel

class City(BaseModel):
   """create public class attributes:"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Enable City to accepts attributes"""
        if(args and type(args[0]) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)   