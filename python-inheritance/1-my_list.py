#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list"""


class MyList(list):
    """Implements a list in sorted ascending order"""

    def printed_sorted(self):
        print(sorted(self))
