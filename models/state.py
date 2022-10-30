#!/usr/bin/python3
"""state class inherited from basemodel"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents the state of the model

    Atrribute:
        name (str): the name of the state
    """

    name = ""
