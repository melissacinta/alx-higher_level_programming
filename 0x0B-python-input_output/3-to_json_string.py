#!/usr/bin/python3
"""Module housing a function
 that returns the JSON representation of an object (string)
 """
import json


def to_json_string(my_obj):
    """Function that that returns the JSON representation of an
    object (string)
    """
    return json.dumps(my_obj)
