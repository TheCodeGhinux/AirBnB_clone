#!/usr/bin/python3
"""BaseModel"""


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional attributes specific to User class


class Post(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional attributes specific to Post class
