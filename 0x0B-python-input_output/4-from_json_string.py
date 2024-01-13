#!/usr/bin/python3
"""Module housing a function
 that returns an object (Python data structure) represented by a JSON string
 """
import json


def from_json_string(my_str):
    """Function that that  returns an object
    (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
