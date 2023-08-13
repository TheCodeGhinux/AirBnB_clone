#!/usr/bin/python3
"""Storage Engine"""

import json
from os.path import exists
from models.base_model import BaseModel  # Make sure to import your model classes here

class FileStorage:
    """Represent an abstracted storage engine"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {key: obj.to_dict() for key, obj in odict.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f, default=lambda o: o.__dict__)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
