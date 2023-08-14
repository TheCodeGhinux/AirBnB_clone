#!/usr/bin/python3
"""City Class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines class for City"""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
