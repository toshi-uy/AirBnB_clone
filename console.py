#!/usr/bin/python3
"""Console that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Holberton AirB&B clone console
    contains the entry point of the command interpreter
    quit and EOF to exit the program
    help dispays help
    an empty line + ENTER doesn't execute anything
    """
    prompt = '(hbnb) '
    intro = 'command line interpreter for HB&B, for more info type help'

    def do_EOF(self, line):
        """Exits on EOF"""
        return True

    def do_quit(self, line):
        """exits when typing quit"""
        if line == quit:
            return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
