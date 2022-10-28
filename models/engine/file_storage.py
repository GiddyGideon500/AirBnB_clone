#!/usr/bin/python3
"""Module file_storage

This Module contains a definition for FileStorage Class
"""
from models.base_model import BaseModel
import json

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
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def def save(self):
        """Serialize __objects to the JSON file __file_path."""
        
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(dictn, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        k

