#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.
    """
    prompt = "(hbnb) "
    classes = {"BaseModel"}

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ Quit signal to exit the program """
        print("")
        return True

    def emptyline(self):
        """Doing nothing when pass empty line"""
        pass

    def do_create(self, args):
        """create instance specified by user """
        if len(args) == 0:
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
        else:
            obj = eval(args)()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """ print a class instance of a given id"""
        if len(args) == 0:
            print("** class name missing **")
            return
        arg = parse(args)
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
            return
        try:
            if arg[1]:
                obj = "{}.{}".format(arg[0], arg[1])
                if obj not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[obj])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, args):
        """" Delete a class instance of a given id"""
        if len(args) == 0:
            print("** class name missing **")
            return
        arg = parse(args)
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
            return
        try:
            if arg[1]:
                obj = "{}.{}".format(arg[0], arg[1])
                if obj not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del (storage.all()[obj])
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, args):
        """ print all instances of a given class"""
        objs = []
        if len(args) == 0 or args in HBNBCommand.classes:
            for v in storage.all().values():
                objs.append(v)
            print(objs)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ update an instance of a given id"""
        if len(args) == 0:
            print("** class name missing **")
            return
        arg = parse(args)
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist ** ")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif ("{}.{}".format(arg[0], arg[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        elif len(arg) >= 4:
            obj = storage.all()["{}.{}".format(arg[0], arg[1])]
            if arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg[2]])
                obj.__dict__[arg[2]] = valtype(arg[3])
            else:
                obj.__dict__[arg[2]] = arg[3]
        elif type(eval(arg[2])) == dict:
            obj = storage.all()["{}.{}".format(arg[0], arg[1])]
            for k, v in eval(arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


def parse(arg):
    """Helper method to parse user typed input"""
    return tuple(arg.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
