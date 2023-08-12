#!/usr/bin/python3
"""HBnB console."""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Exit the program using EOF (Ctrl+D)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
