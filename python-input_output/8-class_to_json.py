#!/usr/bin/python3
# 8-class_to_json.py
"""returns simple data structure"""

def class_to_json(obj):
    """Creates a dict description of obj."""
    return obj.__dict__
