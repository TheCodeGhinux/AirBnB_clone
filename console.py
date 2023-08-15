#!/usr/bin/python3
"""HBnB console."""

import cmd
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
    
    def default(self, line):
        """Override default behavior to handle <class name>.count()"""
        parts = shlex.split(line)
        if len(parts) >= 3 and parts[1] == ".count()" and parts[0] in self.__classes:
            class_name = parts[0]
            class_instances = eval(class_name).all()
            count = len(class_instances)
            print(count)
        else:
            print("*** Unknown syntax:", line)

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
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = split(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

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
        try:
            class_name = arg.split('.')[0]
            if class_name in HBNBCommand.__classes:
                class_instances = eval(class_name).all()
                count = len(class_instances)
                print(count)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print("**", str(e))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
