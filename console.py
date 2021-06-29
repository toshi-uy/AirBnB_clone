#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter"""
import cmd
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Holberton AirBnB clone console
    contains the entry point of the command interpreter
    quit and EOF to exit the program
    help dispays help
    an empty line + ENTER doesn't execute anything
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """Exits on EOF"""
        print()
        return True

    def do_quit(self, line):
        """exits when typing quit"""
        return True

    def emptyline(self):
        """passing emptyline do nothing"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_item = eval(line)()
            print(new_item.id)
            new_item.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name"""
        command = line.split()
        if not line:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** instance id missing **")
        if len(command) == 2:
            new_item = "{}.{}".format(command[0], command[1])
            if new_item not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_item])

    def do_destroy(self, line):
        """method to delete an instance based on the class name and id"""
        command = line.split()
        if not line:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** no instance found **")
        else:
            new_item = "{}.{}".format(command[0], command[1])
            if new_item not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(new_item)
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        list_object = []
        new_item = storage.all()
        if line and line not in self.classes:
            print("** class doesn't exist **")
        elif line in self.classes:
            for key, value in new_item.items():
                split_key = key.split(".")
                new_key = "[" + split_key[0] + "] (" + split_key[1] + ")"
                list_object.append(new_key + " " + str(value))
        else:
            for key, value in new_item.items():
                list_object.append(str(key) + " " + str(value))
        print(list_object)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        command = line.split()
        if not line:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) == 1:
            print("** no instance found **")
        elif command[0] + "." + command[1] not in storage.all():
            print("** no instance found **")
        elif len(command) == 2:
            print("** attribute name missing **")
        elif len(command) == 3:
            print("** value missing **")
        else:
            new_obj = storage.all().get(command[0] + "." + command[1])
            setattr(new_obj, command[2], command[3][1, -1])
            new_obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
