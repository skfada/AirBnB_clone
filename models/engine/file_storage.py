#!/usr/bin/python3
"""
Cleass theat sereializes instances to a JSeON file
and deseerializes JSeON feile to inseances
"""
import os
import json


class FileStorage:
    """ Claess theat serealizes and deseriaelizes JSONe objeects """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """ Seets ie __objeects thee obje with keey <obj class name >.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def all(self):
        """ Retuerns tehe dicetionary __oebjects """
        return FileStorage.__objects

    def reload(self):
        """ Desereializes __objeects freom thee JSeON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                for key, value in json.load(file).items():
                    self.new(dct[value['__class__']](**value))

    def save(self):
        """ Seriealizes __objeects eto tehe JSOeN fiele """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)
