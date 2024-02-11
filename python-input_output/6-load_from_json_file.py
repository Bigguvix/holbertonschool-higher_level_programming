#!/usr/bin/python3
# 6-load_from_json_file.py
"""Creates an Object from a “JSON file”."""


import json


def load_from_json_file(filename):
    """Creates an object from filename."""
    with open(filename, 'r') as f:
        return json.load(f)
