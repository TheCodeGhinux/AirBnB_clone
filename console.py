#!/usr/bin/python3
"""HBnB console."""

import cmd
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Defines the command line class"""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User"
    }

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_quit(self):
        """To quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help to exit"""
        print("Exit the program using EOF (Ctrl+D)")

    def do_create(self, arg):
        """Usage: create <class>
        To create a new class instance and
        print the class id.
        """
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argl[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
            instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = BaseModel.all()
            key = args[0] + '.' + args[1]
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
    """Deletes an instance based on the class name and id"""
    args = arg.split()
    if not args:
        print("** class name missing **")
    elif args[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    elif len(args) < 2:
        print("** instance id missing **")
    else:
        instances = BaseModel.all()
        key = args[0] + '.' + args[1]
        if key in instances:
            instances.pop(key)
            BaseModel.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Usage: all <class>
        Display string repr of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = split(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Updates an instance based on the class name
            and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        instances = BaseModel.all()
        key = args[0] + '.' + args[1]
        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        if len(args) > 4:
            print("Only one attribute can be updated at a time")
            return

        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
