#!/usr/bin/python3
"""
Base module containing the base class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Basemodel class
    """
    def __init__(self, *args, **kwargs):
        """Initalizing the base model"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """String representation of the class"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Save the instance created"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Save the instance to a dictionary"""
        obj_dic = self.__dict__.copy()
        obj_dic["__class__"] = type(self).__name__
        obj_dic["created_at"] = obj_dic["created_at"].isoformat()
        obj_dic["updated_at"] = obj_dic["updated_at"].isoformat()
        return obj_dic
