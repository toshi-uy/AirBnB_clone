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

    def test_is_an_instance(self):
        """function test_is_an_instance"""
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)

    def test_FileStorage(self):
        """Test the FileStorage method itself using example """
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        print(my_model)


if __name__ == '__main__':
    unittest.main()
