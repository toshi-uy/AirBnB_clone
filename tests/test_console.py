#!/usr/bin/python3
"""test the Console itself"""
import unittest
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import pep8
from unittest.mock import patch
from io import StringIO
import cmd


class Test_pep8(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_Console(unittest.TestCase):
    """Tests the entire console"""

    def test_prompt(self):
        """tests the prompt"""
        with patch('sys.stdout', new=StringIO()) as f:
            expected = HBNBCommand.prompt
            self.assertEqual(expected, "(hbnb) ")

    def test_help_EOF(self):
        out = "Exits on EOF"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(out, f.getvalue().strip())

    def test_help_quit(self):
        """tests the help quit"""
        out = "exits when typing quit"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(out, salida.getvalue().strip())

    def test_help_emptyline(self):
        """Test empty line"""
        out = ""
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual(out, salida.getvalue().strip())   


    def setUp(self):
        """Set up tests."""
        storage.reload()

    def test_exit(self):
        """Tests the exit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
