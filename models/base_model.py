#!/usr/bin/python3
"""BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines Base model class"""

    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance

        Args:
            args: Non-keyword variable-length argument list
            kwargs: Key-value variable-length argument list
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
