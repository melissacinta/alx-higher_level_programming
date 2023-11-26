#!/usr/bin/python3
"""Module that checks for instance"""


def is_kind_of_class(obj, a_class):
    """function that returns true
    if obj is an instance of a_class
    """
    return isinstance(obj, a_class)
