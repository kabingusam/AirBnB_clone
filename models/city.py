#!/usr/bin/python3
"""The city class"""
from models.base_model import BaseModel

class City(BaseModel):
<<<<<<< HEAD
    """create public class attributes:
    """
    
=======
   """create public class attributes:"""
>>>>>>> da769404f09a9d798eee720bf1f1ac73d3b3c38f
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Enable City to accepts attributes"""
        if(args and type(args[0]) is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)   