#!/usr/bin/python3
"""User Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines class for User
    Attrs:
        email (string): User's email.
        first_name (string): User's first_name.
        last_name (string): User's last_name.
        password (string): User's password.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
