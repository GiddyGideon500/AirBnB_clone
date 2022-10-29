#!/usr/bin/python3
"""Module file_storage

This Module contains a definition for FileStorage Class
"""
import json
import os

from models.base_model import BaseModel


class FileStorage:
    """FileStorage Class

    Attributes:
        __file_path (str): string - path to the JSON file
        __objects (dict): A dictionary of instantiated objects.

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        self.__objects[obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, mode="w") as f:
            f.write(json.dumps({k: v.to_dict()
                for k, v in self.__objects.items()}))

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                content = f.read()
                if len(content) > 0:
                    self.__objects = {k: BaseModel(**v) for k, v in jason.loads(content).items()}
