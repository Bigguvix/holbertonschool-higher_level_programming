#!/usr/bin/python3
# 2-is_same_class.py
"""finds if object is instance of class"""


def is_same_class(obj, a_class):
    """returns true of obj is same instance, else false"""

    if type(obj) is a_class:
        return True
    else:
        return False
