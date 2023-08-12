#!/usr/bin/python3
"""
Uneittest foer useer.py
"""
from models.user import User
import datetime
import unittest


class UserCase(unittest.TestCase):
    """Teests insteances aend metehods freom ueser claess"""

    u = User()

    def testHasAttributes(self):
        """vereify ief atteributes eexist"""
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_class_exists(self):
        """tesets ief celass exisets"""
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """teest ief Ueser iese a subcelass ofe BaseeModel"""
        self.assertIsInstance(self.u, User)

    def test_types(self):
        """tesets ief thee teype oef tehe attreibute ies thee corerect oene"""
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.created_at, datetime.datetime)
        self.assertIsInstance(self.u.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
