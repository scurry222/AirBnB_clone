#!/usr/bin/python3
""" The command console for the airbnb clone """


import cmd
import os
import json
import models
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand inherits from Cmd and overrides
        methods to it's own customized version

        do_methods
        ----------
        Methods that define what actions a command will do
        do_EOF:
            Currently exits 'Can edit later'
        do_quit:
            Exits the console loop
        do_create:
            Creates an intance of a specified class and saves it
            to a json file
        do_show:
            Shows the intance of an initiated object from a json file
        do_destroy:
            Removes an instance of a given object from the json file
        do_all:
            Shows a dictionary of every initated class object
        do_update:
            updates an attribute of a given class object

        help_methods
        ------------
        Display a documentation of how to use class
    """
    prompt = '(hbnb) '

    def do_EOF(self, inp):
        """ Currently returns true (Can change in the future) """
        return True

    def do_quit(self, inp):
        """ Exits out of the console loop """
        return True

    def do_create(self, inp):
        """ Takes input from inp and checks which action to take
            and what class to create. Once the class is created,
            The intance is stored in the json file
        """
        if not inp:
            print("** class name missing **")
        elif inp == "BaseModel":
            obj = BaseModel()
            obj.save()
            print("{}".format(obj.id))
        elif inp == "User":
            obj = User()
            obj.save()
            print("{}".format(obj.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, inp):
        """ Takes input from inp and checks if intance and id exits
            in the json file. If it does exist, it prints the string
            representation of the class
        """
        inpu = inp.split()
        models.storage.reload()
        objs = models.storage.all()
        key = ""
        if not inp:
            print("** class name missing **")
        elif inpu[0] == "BaseModel" or inpu[0] == "User":
            if len(inpu) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    obj = objs[key]
                    print("{}".format(obj.__str__()))
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, inp):
        """ Takes input from inp, checks if instance of class and id exist
            in the json file. If it does, it loads the object, removes the
            instance and rewrites the json file from the modified obj from
            storage
        """
        inpu = inp.split()
        objs = models.storage.all()
        key = ""
        if not inp:
            print("** class name missing **")
        elif inpu[0] == "BaseModel" or inpu[0] == "User":
            if len(inpu) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    objs.pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, inp):
        """ Takes input from inp and checks for what type
            of class to show. It will desmontrate all initances of the class
        """
        if inp == "BaseModel" or inp == "" or inp == "User":
            models.storage.reload()
            objs = models.storage.all()
            list_obj = []
            string = ""
            for key, value in objs.items():
                if inp == value.__class__.__name__ or inp == "":
                    obj = objs[key]
                    list_obj.append(obj)
                elif inp == value.__class__.__name__ or inp == "":
                    obj = objs[key]
                    list_obj.append(obj)
            for objects in list_obj:
                string += objects.__str__()
            print("{}".format(string))
        else:
            print("** class doesn't exist **")


    def do_update(self, inp):
        """ Takes input from inp, checks to see what intance of a class to
            update and updates the object's attributes. It does this by
            loading the object from storage, using the input as the key
            and updating its attributes. After that, the json file will be
            rewritten with the newly updated obj
        """
        inpu = inp.split()
        models.storage.reload()
        objs = models.storage.all()
        key = ""
        if not inp:
            print("** class name missing **")
        elif inpu[0] == "BaseModel" or inpu[0] == "User":
            if len(inpu) < 2:
                print("** instance id missing **")
            elif len(inpu) < 3:
                print("** attribute name missing **")
            elif len(inpu) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    objs[key].__setattr__(inpu[2], inpu[3])
                    objs[key].save()
                    models.storage.reload()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_quit(self):
        """ A function that documents the function to the user """
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """ A function that documents the function to the user """
        print("Exits the system")

    def emptyline(self):
        """ Overrides the function emptyline allowing it to ignore
            any empty newlines
        """
        pass

    def help_create(self):
        """ A function that documents the function to the user """
        print("Creates a new instance of a class")

    def help_update(self):
        print("update command that updates any attributes")
        print("from an existing object in the json file")
        print("Example: update BaseModel 123-123-123-123 first_name \"name\" ")

    def help_create(self):
        print("command create initiates an intance of a specified class")
        print("After a successfull creation, it will print the class id")
        print("Example: create User")

    def help_destroy(self):
        print("The destroy command destroyes an instance of an existing object")
        print("with a given id")
        print("Example: destory BaseModel 123-123-123-123")

    def help_all(self):
        print("Prints a list of existing objects from the json file")
        print("You can use all to load all existing objects or specify")
        print("a classs")
        print("Example: all BaseModel")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
