#!/usr/bin/python3
""" FileStorage Module for HBNB project """
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
            self.save()

    def all(self, cls=None):
        """Return list of objects of one type of class"""
        if cls:
            return [obj for obj in self.__objects.values() if isinstance(obj, cls)]
        return list(self.__objects.values())

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    cls = models.classes.get(cls_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
