#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of an objects attributes"""

    return (dir(obj))
