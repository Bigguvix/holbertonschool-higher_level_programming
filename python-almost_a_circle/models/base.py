#!/usr/bin/python3
# base.py
"""Base model class."""


class Base:
    """as the name suggest, it represents the "base"
    for all other classes in this project.

    __nb__objects (id) : it represents the number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
