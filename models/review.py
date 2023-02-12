#!/usr/bin/python3
"""Create a review class using this module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Managing review objects here"""
    place_id = ""
    user_id = ""
    text = ""
