#!/usr/bin/python3
"""HBnB console."""

import cmd
from shlex import split
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the command line class"""
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "Amenity",
        "Review",
        "City"
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"^(.*?)\.(.*?)\(\)$", arg)
        if match:
            class_name = match.group(1)
            if class_name in self.__classes and match.group(2) in argdict:
                command = match.group(2)
                return argdict[command](class_name)
        print("*** Unknown syntax:", arg)
        return False

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

    def do_create(self, arg):
        """Usage: create <class>
        To create a new class instance and
        print the class id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Usage: <class name>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        args = shlex.split(arg)
        if len(args) >= 2 and args[1] == ".show()" and args[0] in self.__classes:
            class_name = args[0]
            instance_id = args[1][:-8]  # Remove ".show()"
            obj_key = "{}.{}".format(class_name, instance_id)
            objdict = storage.all()
            if obj_key in objdict:
                print(objdict[obj_key])
            else:
                print("** no instance found **")
        else:
            print("*** Unknown syntax:", arg)

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argl = split(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all [class]
        Display string repr of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            if len(args) == 0:
                obj_list = [str(obj) for obj in instances.values()]
            else:
                class_name = args[0]
                if class_name in HBNBCommand.__classes:
                    class_instances = eval(class_name).all()
                    obj_list = [str(obj) for obj in class_instances.values()]
                else:
                    print("** class doesn't exist **")
                    return
            print(obj_list)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> "<attribute_value>"
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
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

        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, arg):
        """Usage: <class name>.count()
        Retrieve the number of instances of a given class."""
        class_name = arg
        if class_name in self.__classes:
            class_instances = eval(class_name).all()
            count = len(class_instances)
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
