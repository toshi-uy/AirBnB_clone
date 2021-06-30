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

    def test_quit_message(self):
        """ Test quit message """
        outputexpected = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_EOF_message(self):
        """ Test EOF message """
        outputexpected = "Exits on EOF"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_all(self):
        """ Test help all message """
        outputexpected = "Prints all the str representation of the instances"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_count(self):
        """ Test help count message """
        outputexpected = "Prints amount of instances of a class"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_create(self):
        """ Test help create message """
        outputexpected = "Creates a new instance of BaseModel,\
        saves it (to the JSON file) and prints the id.\
        Ex: $ create BaseModel"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_help(self):
        """ Test help help message """
        out1 = "List available commands with \""
        out2 = "help\" or detailed help with \"help cmd\"."
        outputexpected = out1 + out2
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_show(self):
        """ Test help show message """
        outputexpected = "Prints the string representation of an instance\
        based on the class name"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_destroy(self):
        """ Test help destroy message """
        outputexpected = "method to delete an instance based on the class name\
                and id"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_update(self):
        """ Test help update message """
        out1 = "Updates an instance based on the class name"
        out2 = " and\n        id by adding or updating attribute"
        outputexpected = out1 + out2
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_message(self):
        """ Test only help message """
        out1 = "Documented commands (type help <topic>):\n="
        out2 = "=======================================\n"
        out3 = "EOF  all  count  create  destroy  help  quit  show  update"
        outputexpected = out1 + out2 + out3
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_empty_line_and_enter(self):
        """ Test empty line """
        outputexpected = ""
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual(outputexpected, salida.getvalue().strip())


    def setUp(self):
        """Set up tests."""
        storage.reload()

    def test_exit(self):
        """Tests the exit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
    