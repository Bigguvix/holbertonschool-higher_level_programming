#!/usr/bin/python3
# 5-save_to_json_file.py
"""Writes an Object to a text file,"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj
    to filename."""

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
