#!/usr/bin/python3
"""Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines class for Amenity"""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Amenity.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
