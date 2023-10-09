#!/usr/bin/python3
"""
If the object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Inheritance of subclass"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
