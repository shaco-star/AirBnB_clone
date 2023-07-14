#!/usr/bin/python3
"""
Defines the FileStorage class
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    Represent an abstracted storage engine
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Add new obj to existing dictionary of instances"""
        if obj:
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        """Save obj dictionaries to json file"""
        dict = {}
        for k, v in self.__objects.items():
            dict[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dict, f)

    def reload(self):
        """If json file exists, convert obj dicts back to instances"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.load(f)
            for v in dict.values():
                self.new(eval(v['__class__'])(**v))
        except FileNotFoundError:
            return
