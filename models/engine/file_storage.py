#!/usr/bin/python3
import json
import os

"""
Defines the FileStorage class
"""


class FileStorage:
    """
    Represent an abstracted storage engine
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return dictionary"""
        return self.__objects

    def new(self, obj):
        """Create new object"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Convert obj to JSON and save it to __file_path"""
        json_objects = {key: obj.to_dict() if hasattr(obj, 'to_dict') else obj for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Convert JSON to python object"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)