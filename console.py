#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import json
import re

class HBNBCommand(cmd.Cmd):
    prompt = "(mkbnb) "

    def do_quit(self, line):
        """ type (quit) to exis the program """
        return True

    def do_EOF(self, line):
        """ Deals with EOF char """
        print() # to handle newline 
        return True

    def emptyline(self):
        """ Do nothing on Empty line """
        pass

    def do_create(self, cln):
        if cln == "" or cln is None:
            print("** class name missing **")
        elif cln not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes()[cln]()
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
        HBNBCommand().cmdloop()
