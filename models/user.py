#!/usr/bin/python3
"""Module creates User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """managing user objects here"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
