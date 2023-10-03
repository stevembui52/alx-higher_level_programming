#!/usr/bin/python3
"""
Class lockedclass defines a locked class
"""
class LockedClass:
    def __setattr__(self, name, value):
        if  name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute 'last_name'")
