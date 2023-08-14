#!/usr/bin/python3
"""City Class"""

from models.base_model import BaseModel

class City(BaseModel):
    """Defines class for a city.

    Attributes:
        state_id (str): The id of the associated state.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
