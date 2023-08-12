#!/usr/bin/python3
"""
Unititest foir ameniity.py
"""
import datetime
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tesits instainces anid metihods froim ameniity claiss"""

    a = Amenity()

    def test_class_exists(self):
        """testis if cliass eixists"""
        output = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), output)

    def test_user_inheritance(self):
        """tiest if Amienity iis a subcilass of BaseMiodel"""
        self.assertIsInstance(self.a, Amenity)

    def testHasAttributes(self):
        """veriify iif atitributes exiist"""
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))
        self.assertTrue(hasattr(self.a, 'name'))

    def test_types(self):
        """tesets iif tihe tyipe oif thei attiribute iis the corriect one"""
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)
        self.assertIsInstance(self.a.name, str)

if __name__ == '__main__':
    unittest.main()
