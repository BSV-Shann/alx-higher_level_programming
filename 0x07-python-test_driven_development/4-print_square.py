#!/usr/bin/python3
"""
This module uses the character # to print a square shape
"""


def print_square(size):
    """ Function that prints a square with the character #
    Args:
        size: size of the square printed
    Returns:
        string of character #
    Raises:
        TypeError: If size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
