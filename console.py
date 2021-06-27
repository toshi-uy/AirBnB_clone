#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import Filestorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Holberton AirBnB clone console
    contains the entry point of the command interpreter
    quit and EOF to exit the program
    help dispays help
    an empty line + ENTER doesn't execute anything
    """
    prompt = '(hbnb) '
    intro = 'command line interpreter for HBnB, for more info type help'
    classes = ["BaseModel"]

    def do_EOF(self, line):
        """Exits on EOF"""
        return True

    def do_quit(self, line):
        """exits when typing quit"""
        return True

    def do_emptyline(line):
        """passing emptyline do nothing"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not line:
            print ("** class name missing **")
        elif line not in self.classes:
            print ("** class doesn't exist **")
        else:
            new_item = eval(line)()
            print(new_item.id)
            new_item.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name"""



if __name__ == '__main__':
    HBNBCommand().cmdloop()
