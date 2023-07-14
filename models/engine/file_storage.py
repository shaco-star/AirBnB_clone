#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            k = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[k] = obj

    def save(self):
        dict = {}
        for k, v in self.__objects.items():
            dict[k] = v.to_dict()
        with open (self.__file_path, 'w') as f:
            json.dump(dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.load(f)
            for v in dict.values():
                self.new(eval(v['__class__'])(**v))
        except FileNotFoundError:
            return





