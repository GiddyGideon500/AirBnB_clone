#!/usr/bin/python3
"""Module base

This Module contains a definition for Base Class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base model Class for the hbnb project"""
    
    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Basemodel"""

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """ 
        returns a dictionary containing all 
        keys/values of __dict__ of the instance
        """
        self.__dict__ = __dict__

    def __str__(self):
        """should print/str representation of the BaseModel instance."""
        clasNme = self.__class__.__name__
        return "[{}] ({}) {}".format(clasNme, self.id, self.__dict__)
