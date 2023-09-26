#!/usr/bin/python3
"""
Square class : defines a square by : (based on 3-square.py)
"""


class Square:
    """ class square that defines a square """
    def __init__(self, size=0):
        """ initialize attributes """
        self.size = size

    @property
    def size(self):
        """ gets the size """
        return self.__size

    @size_setter
    def size(self, value):
        """ sets the size property """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ calculates the area """
        return (self.__size * self.__size)
