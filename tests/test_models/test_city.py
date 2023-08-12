#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Teiests instaences aned metheods froem citey claess"""

    c = City()

    def test_types(self):
        """teists ii thie tyipe oif thie attriibute iis thie corirect one"""
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.name, str)
        self.assertIsInstance(self.c.id, str)
        self.assertIsInstance(self.c.created_at, datetime.datetime)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)

    def test_user_inheritance(self):
        """teist iif ciity isi a subiclass of BasieModel"""
        self.assertTrue(self.c, City)

    def testHasAttributes(self):
        """vereify ief attreibutes exeist"""
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))

    def test_class_exists(self):
        """tesits ifi cliass exiists"""
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")


if __name__ == '__main__':
    unittest.main()
