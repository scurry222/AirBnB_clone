#!/usr/bin/python3
""" The command console for the airbnb clone """


import cmd
import os
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand inherits from Cmd and overrides
        methods to it's own customized version

        do_methods
        ----------
        Methods that define and add a function to the class
        do_EOF:
    """
    prompt = '(hbnb) '

    def do_EOF(self, inp):
        return True

    def do_quit(self, inp):
        return True

    def do_create(self, inp):
        if not inp:
            print("** class name missing **")
        elif inp == "BaseModel" or inp == "User":
            obj = BaseModel()
            obj.save()
            print("{}".format(obj.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, inp):
        inpu = inp.split()
        storage.reload()
        objs = storage.all()
        key = ""
        if not inp:
            print("** class name missing **")
        elif inpu[0] == "BaseModel" or inpu[0] == "User":
            if len(inpu) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    obj = BaseModel(objs[key])
                    print("{}".format(obj.__str__()))
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, inp):
        inpu = inp.split()
        storage.reload()
        objs = storage.all()
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
                    insert = json.dumps(objs)
                    with open("file.json", "w", encoding='utf-8') as myFile:
                        myFile.write(insert)
                    storage.reload()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, inp):
        if inp == "BaseModel" or inp == "" or inp == "User":
            storage.reload()
            objs = storage.all()
            list_obj = []
            string = ""
            for _, value in objs.items():
                obj = BaseModel(value)
                list_obj.append(obj)
                for objest in list_obj:
                    string += obj.__str__()
            print("{}".format(string))
        else:
            print("** class doesn't exist **")


    def do_update(self, inp):
        inpu = inp.split()
        storage.reload()
        objs = storage.all()
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
                    new_dict = {inpu[2]: inpu[3]}
                    objs[key].update(new_dict)
                    insert = json.dumps(objs)
                    print(insert)
                    with open("file.json", "w", encoding='utf-8') as myFile:
                        myFile.write(insert)
                    storage.reload()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Exits the system")

    def emptyline(self):
        pass

    def help_create(self):
        print("Creates a new instance of a class")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
