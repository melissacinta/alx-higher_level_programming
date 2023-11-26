#!/usr/bin/python3
"""Module that checks for inheritance"""


def inherits_from(obj, a_class):
    """function that returns true
    if obj inherits from a_class
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
