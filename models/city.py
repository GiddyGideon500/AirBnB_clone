#!/usr/bin/python3

"""implementation for the city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    implementing the city class

    Attribute:
        name (str): name of the city
        state_id (str): the state id
    """

    state_id = ""
    name = ""
