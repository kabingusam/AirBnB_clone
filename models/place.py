<<<<<<< HEAD
#!/usr/bin/python3
"""The Place class"""
=======
#!/usr/bin/python3
"""The amenity class"""
from models.base_model import BaseModel
>>>>>>> da769404f09a9d798eee720bf1f1ac73d3b3c38f

<<<<<<< HEAD
class Place(BaseModel):
    """public class attributes"""
=======

class Amenity(BaseModel):
    """create public class attributes """
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
>>>>>>> da769404f09a9d798eee720bf1f1ac73d3b3c38f