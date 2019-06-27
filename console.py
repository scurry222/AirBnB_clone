#!/usr/bin/python3
""" The command console for the airbnb clone """


import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand inherits from Cmd and overrides
        methods to it's own customized version
    """
    prompt = '(hbnb) '

    def do_EOF(self, inp):
        return True

    def do_quit(self, inp):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Exits the system")

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
