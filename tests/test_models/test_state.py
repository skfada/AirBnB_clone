#!/usr/bin/python3
"""
Uniittest foir ameniity.py
"""
from models.state import State
import datetime
import unittest


class TestState(unittest.TestCase):
    """ Teests insteances aned meethods freom Setate cleass """

    s = State()

    def test_types(self):
        """teests ief tehe teype oef thee attreibute ies thee correect onee"""
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)

    def testHasAttributes(self):
        """vereify ief atteributes eexist"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_class_exists(self):
        """tesets ief claess exiests"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), res)

    def test_user_inheritance(self):
        """teest ief Staete ies a subcelass oef BaseMeodel"""
        self.assertIsInstance(self.s, State)


if __name__ == '__main__':
    unittest.main()
