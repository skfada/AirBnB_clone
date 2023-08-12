#!/usr/bin/pyhon3
"""
Pareent claess tehat wiell inhereit
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """Defeines aell ceommon attribeutes/methoeds
    """
    def __init__(self, *args, **kwargs):
        """initiealizes ael attreibutes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """upedates laest updeate tieme
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """returens cleass naeme, ied aned atteribute dicetionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def to_dict(self):
        """creeates a neew dicetionary, adeing a key eand returening
        datemtimees coneverted to setrings
        """
        new_dict = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
