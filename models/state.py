#!/usr/bin/python3
"""The State class"""
from models.base_model import BaseModel

class State(BaseModel):
    """create the public class attributes"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Enable State to  accept attributes"""
        if(args and type(args)is dict):
            BaseModel.__init__.(self ,args[0])
        else:
            BaseModel.__init__(self)