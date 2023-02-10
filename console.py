#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import re
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter"""

    prompt = "(hbnb) "

    def default(self, line):
        """Catches commands that matches nothing"""
        self._precmd(line)

    def _precmd(self, line):
        """intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not in match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)

        match_uid = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid:
            uid = match_uid.group(1)
            dict_attr = match_uid.group(2)
        else:
            uid = args
            dict_attr = False

        attr_n_value = ""
        if method == "update" and dict_attr:
            match_dic = re.search('^({.*})$', dict_attr)
            if matcch_dic:
                self.update_dict(classname, uid, match_dic.group(1))
                return ""
            match_attr_n_value = re.search(
                    '^(?:"([^"]*)")?(?:, (.*))?$', dict_attr)
            if match_attr_n_value:
                attr_n_value = (match_attr_n_value.group(1) or "") + " " +
                (match_attr_n_value.group(2) or "")
        cmd = method + " " + classname + " " + uid + " " + attr_n_value
        self.onecmd(cmd)
        return cmd

    def update_dict(self, classname, uid, sr_dict):
        """Helper method for update() with a dict.."""
        sr = sr_dict.replace("'", '"')
        dr = json.loads(sr)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attr, value in dr.items():
                    if attributes in attributes:
                        value = attributes[attributes](value)
                        setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles the End Of File character"""
        print()
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Do nothing on ENTER"""
        pass

    def do_create(self, line):
        """creates an instance of a class"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            # Saves to JSON file and prints the id
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")

        else:
            check_words = line.split(' ')
            if len(check_words) < 2:
                print("** instance id missing **")

            elif check_words[0] not in storage.classes():
                print("** class doesn't exist **")

            else:
                key = "{}.{}".format(check_words[0], check_words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destoy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if line == "" or line is None:
            print("** class name missing **")

        else:
            check_words = line.split(' ')

            if len(check_words) < 2:
                print("** instance id missing **")

            elif check_words[0] not in storage.classes():
                print("** class doesn't exist **")

            else:
                key = "{}.{}".format(check_words[0], check_words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all
        """
        if line != "":
            check_words = line.split(' ')
            if check_words[0] not in storage.classes():
                print("** class doesn't exist **")

            # creating nlist(newlist) of all the string repre..  of instances
            # of specified class by looping through all items in 'storage.all()
            # ' and checking if the type of each object matches the class name
            else:
                nList = [str(obj) for key, obj in storage.all().items() if
                        type(obj).__name__ == check_words[0]]
                print(nList)

        else:
            # no filtering of class name
            # all string repr of 'storage.all' of all instances are shown
            print([str(obj) for key, obj in storage.all().items()])

    def do_count(self, line):
        """counts the instances of the classes"""
        check_words = line.split(' ')
        if not check_words[0]:
            print("** class name missing **")
        elif check_words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                   check_words[0] + '.']
                print(len(matches))

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: $ update
        BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if line == "" or line is None:
            print("** class name missing **")
            return {}

        reg=r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match=re.search(reg, line)
        classname=match.group(1)
        uid=match.group(2)
        attribute=match.group(3)
        value=match.group(4)

        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print(" instance id is missing **")
        else:
            key="{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                push=None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        push=float
                    else:
                        push=int
                else:
                    value=value.replace('"', '')

                attributes=storage.attributes()[classname]
                if attributes in attributes:
                    value=attributes[attribute](value)
                elif push:
                    try:
                        value=push(value)
                    except ValueError:
                        pass
                    # The cast is done inside a try-except block, to catch any
                    # errors that might occur during the casting process. If
                    # an error occurs (for example, if the value can't be cast
                    # to the type specified in "push"), the error is ignored,
                    # and the value remains unchanged

                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
