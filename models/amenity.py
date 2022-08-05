#!/usr/bin/python3
"""The amenity class"""
from models.base_model import BaseModel


class  Amenity(BaseModel):
    """Represents an Amenity

    Attributes:
    (str): the name of the Amenity.
    
    """
    name = ""

    def __init__(self,*args , **kwargs):
        """Enable Amenity to accept arguments"""
        if (args and (type)is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)