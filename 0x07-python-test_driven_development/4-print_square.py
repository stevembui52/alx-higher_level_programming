#!/usr/bin/python3
"""
Return a square with character #
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
