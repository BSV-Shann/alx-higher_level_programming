#!/usr/bin/python3
"""
This module is a function that adds two numbers
"""
def add_integer(a, b=98):
    """This function returns value of a + b

    Args:
        a: should be an int. else throw an error
        b: second int. else throw an error. default is 98

    Return:
        a + b or raise a TypeError
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
