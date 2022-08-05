#!/usr/bin/python3
"""The Review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """create the public class attributes"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Enable Review to accept attributes"""
        if(args and type(args)is dict):
            BaseModel.__init__.(self ,args[0])
        else:
            BaseModel.__init__(self)