#!/usr/bin/python3
# 4-inherits_from.py
"""find if the object is an istance of a
class that inherited from specified class"""


def inherits_from(obj, a_class):
    """determines if obj is an instance of a class
    that inherited from a_class"""
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
