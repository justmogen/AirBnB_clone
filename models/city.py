#!/usr/bin/python3
"""Using this module to create The User Class"""

from models.base_model import BaseModel


class City(BaseModel):
    """managing city objects using this class"""

    state_id = ""
    name = ""
