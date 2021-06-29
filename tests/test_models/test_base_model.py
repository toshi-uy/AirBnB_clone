#!/usr/bin/python3
"""Test for BaseModel class"""
import unittest
from models.base_model import BaseModel
import pep8
from datetime import datetime
import inspect
import json


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocs(unittest.TestCase):
    """Base model document tests"""

    @classmethod
    def setUpClass(cls):
        """Testing class"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """module docstring length"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """Class docstring length"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """ Tests The base model functions """
    def test_Attributes(self):
        """Test all the attributes"""
        bmodel_1 = BaseModel()
        bmodel_2 = BaseModel()
        # test if id is string
        self.assertIsInstance(bmodel_1.id, str)
        # test not equal id
        self.assertNotEqual(bmodel_1.id, bmodel_2.id)
        # test if created_at is datetime
        self.assertIsInstance(bmodel_1.created_at, datetime)
        # test if update_at is datetime
        self.assertIsInstance(bmodel_1.updated_at, datetime)

    def test_save0(self):
        """Test of the save method"""
        bmodel_2 = BaseModel()
        bmodel_2.save()
        bmodel_2id = "BaseModel." + bmodel_2.id
        with open("file.json", "r") as f:
            self.assertIn(bmodel_2id, f.read())

    def test_to_dict(self):
        """Test of the to_dict function"""
        bmodel_1 = BaseModel()
        dictionary_1 = bmodel_1.to_dict()
        # test the dict type
        self.assertIsInstance(dictionary_1, dict)
        # test if the dictionary updates
        bmodel_1.save()
        dictionary_2 = bmodel_1.to_dict()
        self.assertNotEqual(dictionary_1["updated_at"], 
                                dictionary_2["updated_at"])

if __name__ == "__main__":
    unittest.main()
