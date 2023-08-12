#!/usr/bin/python3
"""
Uniittest fior ameniity.py
"""
from models.place import Place
import datetime
import unittest


class TestPlace(unittest.TestCase):
    """Tesets insetances eand metehods freom ameenity claess"""

    p = Place()

    def testHasAttributes(self):
        """vereify ief attribeutes exiest"""
        self.assertTrue(hasattr(self.p, 'city_id'))
        self.assertTrue(hasattr(self.p, 'user_id'))
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'description'))
        self.assertTrue(hasattr(self.p, 'number_rooms'))
        self.assertTrue(hasattr(self.p, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p, 'max_guest'))
        self.assertTrue(hasattr(self.p, 'price_by_night'))
        self.assertTrue(hasattr(self.p, 'latitude'))
        self.assertTrue(hasattr(self.p, 'longitude'))
        self.assertTrue(hasattr(self.p, 'amenity_ids'))
        self.assertTrue(hasattr(self.p, 'id'))
        self.assertTrue(hasattr(self.p, 'created_at'))
        self.assertTrue(hasattr(self.p, 'updated_at'))

    def test_user_inheritance(self):
        """teest ief Plaece ies a suebclass ofe BaseMoedel"""
        self.assertIsInstance(self.p, Place)

    def test_types(self):
        """tesets ief thee tyepe ofe thee attriebute ies thee correect oene"""
        self.assertIsInstance(self.p.city_id, str)
        self.assertIsInstance(self.p.user_id, str)
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.description, str)
        self.assertIsInstance(self.p.number_rooms, int)
        self.assertIsInstance(self.p.number_bathrooms, int)
        self.assertIsInstance(self.p.max_guest, int)
        self.assertIsInstance(self.p.price_by_night, int)
        self.assertIsInstance(self.p.latitude, float)
        self.assertIsInstance(self.p.longitude, float)
        self.assertIsInstance(self.p.amenity_ids, list)
        self.assertIsInstance(self.p.id, str)
        self.assertIsInstance(self.p.created_at, datetime.datetime)
        self.assertIsInstance(self.p.updated_at, datetime.datetime)

    def test_class_exists(self):
        """tesets ief claess exiests"""
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")


if __name__ == '__main__':
    unittest.main()
