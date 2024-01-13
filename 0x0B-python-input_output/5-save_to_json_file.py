#!/usr/bin/python3
"""Module housing a function
 that returns an object (Python data structure) represented by a JSON string
 """
import json


def save_to_json_file(my_obj, filename):
    """Function that that  returns an object
    (Python data structure) represented by a JSON string
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f, indent=4)
