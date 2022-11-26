#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


from os.path import exists

# classes = {
#             "BaseModel": BaseModel,
#             "User": User, "State": State,
#             "City": City, "Place": Place,
#             "Amenity": Amenity, "Review": Review
#             }


class FileStorage:
    """
    Storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """
        add a new object
        """
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Save object to json file path"""
        json_object = {}
        for k in self.__objects:
            json_object[k] = self.__objects[k].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_object, f)

    def reload(self):
        """Deserialize from json to python object"""
        file_exists = exists(self.__file_path)
        if file_exists:
            with open(self.__file_path, "r") as f:
                obj = json.load(f)
            for k, v in obj.items():
                self.__objects[k] = self.classes()[v["__class__"]](**v)

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        classes = {
            "BaseModel": BaseModel,
            "User": User, "State": State,
            "City": City, "Place": Place,
            "Amenity": Amenity, "Review": Review
            }
        return classes
