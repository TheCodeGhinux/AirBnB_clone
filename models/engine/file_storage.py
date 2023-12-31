#!/usr/bin/python3
"""Storage Engine"""

import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = {key: obj.to_dict()
                   for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    cls_name = value['__class__']
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            return
