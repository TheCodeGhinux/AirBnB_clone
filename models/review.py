"""Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines class for Review

    Attributes:
        place_id (str): The id of the associated place.
        user_id (str): The id of the associated user.
        text (str): The review text.
    """

    place_id = ""
    user_id = ""
    text = ""
