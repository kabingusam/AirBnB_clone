#!/usr/bin/python3
"""The Place class"""
from models.base_model import BaseModel

class Place(BaseModel):
    """public class attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities = []

    def __init__(self,*args , **kwargs):
        """Enable Amenity to accept arguments"""
        if (args and type(args)is dict):
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)