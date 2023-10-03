#!/usr/bin/python3
"""
Class lockedclass defines a locked class
"""
class LockedClass:
    """ Allow setting the attribute if it's 'first_name' """
     __slots__ = ['first_name']

    def __init__(self, first_n=""):
        self.first_name = first_n
