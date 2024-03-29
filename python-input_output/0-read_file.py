#!/usr/bin/python3
# 0-read_file.py
"""Reads from a file and prints"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout"""
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
