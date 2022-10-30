#!/usr/bin/python3
"""Module console

This Module contains a definition for HBNBCommand Class
"""

import cmd
import importlib
import json
import re
from typing import cast

from models import storage


class HBNBCommand(cmd.Cmd):
    """AirBnB clone console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Exist the console using Ctrl + D"""
        print()
        return True

    def emptyline(self):
        """prevents default behavior of cmd to ignore running command on
        empty line plus enter
        """
        pass

    def do_create(self, line):
        """creates a new object and saves it"""
        obj_cls = self.get_class_from_input(line)
        if obj_cls is not None:
            new_obj = obj_cls()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """prints the string representation of an instance based on name and id
        """
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().get(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            print(saved_obj)

    def do_destroy(self, line):
        """deletes an instance based on the class name and id and saves the
        change into the JSON file
        """
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().pop(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            storage.save()

    def do_all(self, line):
        """prints all string representation of all instances based or not on
        the class name
        """
        if len(line.split()) == 0:
            result = storage.all().values()
        else:
            obj_cls = self.get_class_from_input(line)
            if obj_cls is None:
                return
            result = list(filter(lambda item: isinstance(
                item, obj_cls), storage.all().values()))

        print([str(item) for item in result])

    def do_update(self, line):
        """updates an instance based on the class name and id by adding or
        updating attribute and saves the change into the JSON file
        """
        key = self.get_obj_key_from_input(line)
        if key is None:
            return

        saved_obj = storage.all().get(key, None)
        if saved_obj is None:
            print("** no instance found **")
        else:
            attr_name, attr_val = self.get_attribute_name_value_pair(line)
            if attr_name is None or attr_val is None:
                return

            if hasattr(saved_obj, attr_name):
                attr_type = type(getattr(saved_obj, attr_name))
                attr_val = cast(attr_type, attr_val)
            setattr(saved_obj, attr_name, attr_val)
            saved_obj.save()

    def do_count(self, line):
        """prints the count of all instances based the class name"""
        obj_cls = self.get_class_from_input(line)
        if obj_cls is None:
            return
        result = list(filter(lambda item: isinstance(
            item, obj_cls), storage.all().values()))

        print(len(result))

    def get_obj_key_from_input(self, line):
        """parses and returns object key from input"""
        obj_cls = self.get_class_from_input(line)
        if obj_cls is None:
            return None
        id = self.get_id_from_input(line)
        if id is None:
            return None
        return f"{obj_cls.__name__}.{id}"

    def get_class_from_input(self, line):
        """parses and returns class from input"""
        if line is None or len(line.strip()) == 0:
            print("** class name missing **")
            return None

        return self.get_class(line.split()[0])

    def get_id_from_input(self, line):
        """parses and returns id from input"""
        cmds = line.split()
        if len(cmds) < 2:
            print("** instance id missing **")
            return None
        return cmds[1]

    def get_attribute_name_value_pair(self, line):
        """parses and returns a tuple of attribute name and value"""
        cmds = line.split()

        attr_name = None if len(cmds) < 3 else cmds[2]
        if attr_name is None:
            print("** attribute name missing **")
            return None, None

        attr_val = None if len(cmds) < 4 else cmds[3].strip('"')
        if attr_val is None:
            print("** value missing **")
            return attr_name, None

        return attr_name, attr_val

    def get_class(self, name):
        """ returns a class from models module using its name"""
        try:
            sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
            module = importlib.import_module(f"models.{sub_module}")
            return getattr(module, name)
        except Exception:
            print("** class doesn't exist **")
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
