#!/usr/bin/python3
#  1-write_file.py
"""Writes to a text file"""


def write_file(filename="", text=""):
    """Function that writes to a text file"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
