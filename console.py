#!/usr/bin/python3
"""HBnB console."""

import cmd
import json
from datetime import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the command line class"""
    prompt = '(hbnb) '

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
        """Create a new instance of BaseModel
        and save it to the JSON file."""
        if not arg:
            print("** class name missing **")
            return
    
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
    
        new_instance = BaseModel(storage=storage)  # Pass the storage instance
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
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = BaseModel.all()
            key = args[0] + '.' + args[1]
            if key in instances:
                instances.pop(key)
                BaseModel.save_instances()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of
            all instances based on the class name"""
        instances = BaseModel.all()
        if not arg:
            print([str(instance) for instance in instances.values()])
        elif arg != "BaseModel":
            print("** class doesn't exist **")

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
