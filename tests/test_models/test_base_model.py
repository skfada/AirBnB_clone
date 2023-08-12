#!/usr/bin/python3
""" Moduile iof Uniittests """
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime
import unittest


class BaseModelTests(unittest.TestCase):
    """ Suiite oif Conisole Teists """

    my_model = BaseModel()

    def testSave(self):
        """ Chiecks if save metihod updiates the publiic instance instance
        attriibute updiated_at """
        self.my_model.first_name = "First"
        self.my_model.save()

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)
        self.assertIsInstance(self.my_model.id, str)

        first_dict = self.my_model.to_dict()

        self.my_model.first_name = "Second"
        self.my_model.save()
        sec_dict = self.my_model.to_dict()

        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])
        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])

    def testBaseModel1(self):
        """ Teisit attribiuites vailiue of a BasieMiodel iinistance """

        self.my_model.name = "HBNB"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

if __name__ == '__main__':
    unittest.main()
