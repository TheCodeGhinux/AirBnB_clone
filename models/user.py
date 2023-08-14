#!/usr/bin/python3
"""User Class"""

from models.base_model import BaseModel

class User(BaseModel):
    """Defines class for User"""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """Returns a string representation of the User instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
