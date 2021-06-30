#!/usr/bin/python3
"""test the FileStorage method"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import pep8
import inspect


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_FileStorage(unittest.TestCase):
    """Test the FileStorage"""
    def test_docstring(self):
        """module docstring length"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_FileStorage_arg(self):
        """testing file storage with an argument"""
        with self.assertRaises(TypeError):
            FileStorage("Holberton")
        with self.assertRaises(TypeError):
            FileStorage("89")
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_is_an_instance(self):
        """function test_is_an_instance"""
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)

    def test_file_path(self):
        """testing file path"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_All(self):
        """Test the FileStorage method itself using example """
        object_1 = FileStorage()
        object_data = object_1.all()
        self.assertIsNotNone(object_data)
        self.assertEqual(type(object_data), dict)

    def test_FileStorage_1(self):
        """Tests the FileStorage again"""
        my_model = FileStorage()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(str(type(FileStorage)), "<class 'type'>")
        self.assertTrue(isinstance(my_model, FileStorage))
        self.assertTrue(type(my_model), object)
    
    def test_reload(self):
        """tests the reload"""

if __name__ == '__main__':
    unittest.main()
