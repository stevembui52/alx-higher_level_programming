#!/usr/bin/python3
"""
class Rectangle: Define set and get of width and height.
"""


class Rectangle:
    """ class Square that defines a square """

    def __init__(self, width=0, height=0):
        """ Initialize attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """set passsed private attribue of width"""
        if not(isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the width of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """set passsed private attribue of width"""
        if not(isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """magic method that printthe rectangle"""
        string = ""
        if (self.__width == 0 or self.__height == 0):
            return string
        for x in range(self.__height):
            for y in range(self.__width):
                string += "#"
            string += "\n"
        return string[:-1]
