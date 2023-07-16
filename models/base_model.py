#!/usr/bin/python3
"""Creating BaseModel Class"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ Base class for Airbnb clone project"""
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of an instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the data and time when object is updated"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dic = dict(self.__dict__)
        dic['__class__'] = self.__class__.__name__
        if 'created_at' in dic:
            dic['created_at'] = dic['created_at'].isoformat()
        if 'updated_at' in dic:
            dic['updated_at'] = dic['updated_at'].isoformat()
        return dic
