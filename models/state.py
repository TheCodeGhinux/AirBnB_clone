#!/usr/bin/python3
"""State Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Defines class for State"""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
