#!/usr/bin/python3
# rectangle.py
"""Define a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initlialize a new rectangle"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
