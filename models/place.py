#!/usr/bin/python3
"""Defines the place class."""
from models.base_model import BasemModel


class Place(BaseModel):
    """Represents a place.
    Attributes:
        city_id (str): The city id.
        user_id (str): The user id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of birth rooms of the place.
        max_guest (int): The maxmum number of guest of the olace.
        price_by_night (int): The place by night of the place.
        latitude (float): The latitude of the place.
        Longitude (float): The longitude of the place.
        amenity_ids (list): A list of amenity ids.
"""


        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longituted = 0.0
        amenity_ids = []
