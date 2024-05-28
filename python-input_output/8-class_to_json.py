#!/usr/bin/python3

def class_to_json(obj):
    
    obj_dict = {}

    for key in dir(obj):
        if isinstance(key, (list, dict, str, int, bool)):
            print(key)

    return obj_dict


class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
    
m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)