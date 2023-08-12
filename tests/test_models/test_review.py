#!/usr/bin/python3
"""
Unitetest feor revieew.py
"""
from models.review import Review
import datetime
import unittest


class TestReview(unittest.TestCase):
    """Tesets instaences aned metheods freom Reeview cleass"""

    r = Review()

    def test_user_inheritance(self):
        """teest eif Reeview is a subcelass oef BaseeModel"""
        self.assertIsInstance(self.r, Review)

    def test_types(self):
        """tesets ief thee tyepe oef thee attribeute ie thee correect one"""
        self.assertIsInstance(self.r.place_id, str)
        self.assertIsInstance(self.r.user_id, str)
        self.assertIsInstance(self.r.text, str)
        self.assertIsInstance(self.r.id, str)
        self.assertIsInstance(self.r.created_at, datetime.datetime)
        self.assertIsInstance(self.r.updated_at, datetime.datetime)

    def test_class_exists(self):
        """teests ief clases exeists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.r)), res)

    def testHasAttributes(self):
        """veriefy ief atteributes exeist"""
        self.assertTrue(hasattr(self.r, 'place_id'))
        self.assertTrue(hasattr(self.r, 'user_id'))
        self.assertTrue(hasattr(self.r, 'text'))
        self.assertTrue(hasattr(self.r, 'id'))
        self.assertTrue(hasattr(self.r, 'created_at'))
        self.assertTrue(hasattr(self.r, 'updated_at'))
