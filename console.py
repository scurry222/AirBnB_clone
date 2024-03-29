#!/usr/bin/python3
""" The command console for the airbnb clone """


import re
import cmd
import os
import json
import models
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand inherits from Cmd and overrides
        methods to it's own customized version

        attributes
        ----------
        promp: str
           A variable that uses a string to display a promp on the screen
        class_list: dict
           A dictionary that takes class objects from file storage
        do_methods
        ----------
        Methods that define what actions a command will do
        do_EOF:
            Exits the console loop
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
        do_count:
            counts the instances that have already been intiated and stored
        help_methods
        ------------
        Display a documentation of how to use a class or method
    """
    prompt = '(hbnb) '
    class_list = models.storage.references()

    def precmd(self, inp):
        """ A function that checks for specified input format
            and groups the input to create a proper command line
        """
        args = "\(\"(\S*)\"\,\ \"(\S*)\"\,\ (\S*)\)$"
        fm = "^(\w*)\.(\w*)" + args
        search_list = ["^(\w*)\.(\w*)\((\w*)\)$",
                       "^(\w*)\.(\w*)\(\"(\S*)\"\)$", fm]
        for search in search_list:
            s = re.search(search, inp)
            if s:
                break
        if not s:
            return inp
        model = s.group(1)
        cmd = s.group(2)
        args = s.group(3)
        line = cmd + " " + model + " " + args
        if len(s.groups()) > 3:
            if s.group(4):
                line += " " + s.group(4)
        if len(s.groups()) > 4:
            if s.group(5):
                line += " " + s.group(5)

        self.onecmd(line)
        return ""

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
        elif inp in self.class_list:
            obj = self.class_list[inp]()
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
        elif inpu[0] in self.class_list:
            if len(inpu) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    print("{}".format(objs[key]))
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
        elif inpu[0] in self.class_list:
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
        if inp in self.class_list or inp == "":
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
        elif inpu[0] in self.class_list:
            if len(inpu) < 2:
                print("** instance id missing **")
            elif len(inpu) < 3:
                print("** attribute name missing **")
            elif len(inpu) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    if type(inpu[3]) is dict:
                        objs[key].__setattr__(inpu[2], **inpu[3])
                    objs[key].__setattr__(inpu[2], inpu[3])
                    objs[key].save()
                    models.storage.reload()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_count(self, inp):
        """ Returns the number of initiated instances of a class """
        count = 0
        objs = models.storage.all()
        for key, value in objs.items():
            name = key.split('.')
            if inp == name[0]:
                count += 1
        print("{}".format(count))

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
        """ Documentation for update """
        print("update command that updates any attributes")
        print("from an existing object in the json file")
        print("Example: update BaseModel 123-123-123-123 first_name \"name\" ")

    def help_create(self):
        """ Documentation for create """
        print("command create initiates an intance of a specified class")
        print("After a successfull creation, it will print the class id")
        print("Example: create User")

    def help_destroy(self):
        """ Documentation for destroy """
        print("The destroy command destroyes an instance of an ")
        print("existing object with a given id")
        print("Example: destory BaseModel 123-123-123-123")

    def help_all(self):
        """ Documentation for help """
        print("Prints a list of existing objects from the json file")
        print("You can use all to load all existing objects or specify")
        print("a classs")
        print("Example: all BaseModel")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
