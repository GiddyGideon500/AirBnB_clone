#!/usr/bin/python3
"""Module base

This Module contains a definition for Base Class
"""
from models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base model Class for the hbnb project"""

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Basemodel"""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(**kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        cdict = self.__dict__.copy()
        cdict["created_at"] = self.created_at.isoformat()
        cdict["updated_at"] = self.updated_at.isoformat()
        cdict["__class__"] = self.__class__.__name__
        return cdict

    def __str__(self):
        """should print/str representation of the BaseModel instance."""
        clasNme = self.__class__.__name__
        return "[{}] ({}) {}".format(clasNme, self.id, self.__dict__)
