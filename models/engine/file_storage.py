#!/usr/bin/python3
import json
import os
import datetime

class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects


    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()
                }, f)

    def classes(self):
        """Returns a dictionary mapping the names of the classes to the
        classes themselves (referencing)
        """

        from models import *
        return {c.__name__: c for c in (BaseModel, User, State, City, Amenity,
            Place, Review)}

    def reload(self):
        """Reload the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return {}
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            FileStorage.__objects = {
                    k: self.classes()[v["__class__"]](**v)
                    for k, v in json.load(f).items()
                    }
            return FileStorage.__objects

    def attributes(self):
        """Valid attributes and their types for classname will be returned"""

        attributes = {
                "BaseModel":
                {
                    "id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime
                    },

                "User":
                {
                    "email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str
                    },

                "State":
                { "name": str },

                "City":
                {
                    "state_id": str,
                    "name": str
                    },

                "Amenity":
                { "name": str },

                "Place":
                {
                    "city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": str
                    },

                "Review":
                {
                    "place_id": str,
                    "user_id": str,
                    "text": str
                    }
            }
        return attributes
