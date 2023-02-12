#!/usr/bin/python3
""" Creating a BaseModel that defines all common attributes/methods
for other classes

"""

from models import storage
from datetime import datetime
import uuid


class BaseModel:
    """
    The BaseModel class is a blueprint for other classes to inherit from.
    This allows for creating classes that share common functionality
    and attributes
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())  # generate a unique id for instance
        self.created_at = datetime.now()  # sets creation time to current time
        self.updated_at = self.created_at  # sets update time to current time

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        """Returns a string repre.. of the BaseModel instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' attributes of the instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary repre.. of the BaseModel instance"""
        result = {
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat(),
                "__class__": type(self).__name__  # useful in deserializtion
            }
        result.update(self.__dict__)
        # Copying all attributes and values of BaseModel instance
        # +into 'result' dictioary
        return result
