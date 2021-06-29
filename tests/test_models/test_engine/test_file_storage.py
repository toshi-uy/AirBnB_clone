#!/usr/bin/python3
"""test the Amenity method"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
import pep8
import inspect


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_FileStorage(unittest.TestCase):
    def test_docstring(self):
        """module docstring length"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
