#!/usr/bin/python3
""" console """

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from os import getenv
from shlex import split as spliter


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class"""
        kargs = {}
        args = spliter(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        clname = args.pop(0)
        for s in args:
            s = s.split("=")
            if len(s) == 2 and ' ' not in s[1]:
                s[1] = s[1].replace('_', " ")
                s[1] = s[1].replace('"', '')
                kargs[s[0]] = s[1]
        if clname == "Place":
            tps = ("number_rooms", "number_bathrooms",
                   "max_guest", "price_by_night")
            cpkargs = kargs.copy()
            for key in cpkargs:
                if key in ("latitude", "longtitude"):
                    try:
                        kargs[key] = float(kargs[key])
                    except ValueError:
                        kargs.pop(key)
                elif key in tps:
                    if kargs[key].isdigit():
                        kargs[key] = int(kargs[key])
                    else:
                        kargs.pop(key)
        print(kargs)
        for key in kargs:
            print(type(kargs[key]))
        if clname in classes:
            instance = classes[clname](**kargs)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = spliter(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = spliter(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = spliter(arg)
        obj_list = []
        if len(arg) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = spliter(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
