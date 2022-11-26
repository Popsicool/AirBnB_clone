#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def default(self, line: str) -> None:
        args = [
            "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"
            ]
        com = line.split(".")
        if com[0] not in args:
            return super().default(line)
        else:
            if com[1] == "User":
                pass
        return super().default(line)

    def do_EOF(self, line):
        """
        handles the end of file
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if line is None or line == "":
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            ins = storage.classes()[line]()
            ins.save()
            print(ins.id)

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based on the class name and id.
        """
        if line is None or line == "":
            print("** class name missing **")
        else:
            line = line.split(" ")
            if line[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(line) < 2:
                print("** instance id missing **")
            else:
                inst = "{}.{}".format(line[0], line[1])
                if inst not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[inst])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)

        """
        if line is None or line == "":
            print("** class name missing **")
        else:
            line = line.split(" ")
            if line[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(line) < 2:
                print("** instance id missing **")
            else:
                inst = "{}.{}".format(line[0], line[1])
                if inst not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[inst]
                    storage.save()

    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        if line is not None and line != "":
            line = line.split(" ")
            if line[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj = []
                for k, v in storage.all().items():
                    if type(v).__name__ == line[0]:
                        obj.append(str(v))
                print(obj)

    def do_update(self, line):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        if line is None or line == "":
            print("** class name missing **")
            return False
        line = line.split(" ")

        if line[0] not in storage.classes():
            print("** class doesn't exist **")
            return False
        if len(line) < 2:
            print("** instance id missing **")
            return False
        if "{}.{}".format(line[0], line[1]) not in storage.all():
            print("** no instance found **")
            return False
        if len(line) == 2:
            print("** attribute name missing **")
            return False
        if len(line) == 3:
            try:
                type(eval(line[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(line) == 4:
            obj = storage.all()["{}.{}".format(line[0], line[1])]
            if line[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[line[2]])
                obj.__dict__[line[2]] = valtype(line[3])
            else:
                obj.__dict__[line[2]] = line[3]
        elif type(eval(line[2])) == dict:
            obj = storage.all["{}.{}".format(line[0], line[1])]
            for k, v in eval(line[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
