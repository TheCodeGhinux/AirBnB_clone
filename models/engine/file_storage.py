#!/usr/bin/python3

"""File Storage."""

import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file
        and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
    """Deserializes the JSON file to __objects"""
    if exists(self.__file_path):
        with open(self.__file_path, 'r') as file:
            try:
                obj_dict = json.load(file)
            except json.JSONDecodeError:
                obj_dict = {}
            for key, value in obj_dict.items():
                class_name = value['__class__']
                cls = eval(class_name)
                self.__objects[key] = cls(**value)


storage = FileStorage()
storage.reload()
