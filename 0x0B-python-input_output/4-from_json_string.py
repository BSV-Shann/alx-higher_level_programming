#!/usr/bin/python3
"""A function for JSON to object"""

import json

def from_json_string(my_str):
    """Return a python object of a JSON string"""
    return json.loads(my_str)
