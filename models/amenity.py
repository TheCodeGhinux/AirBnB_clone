#!/usr/bin/python3
"""Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines class for an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
