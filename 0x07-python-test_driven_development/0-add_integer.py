#!/usr/bin/python3
"""This module provides one funtion `add_integer`.

Example:
    >>> add_interger(2, 4)
    6
"""


def add_integer(a, b=98):
    """Adds 2 numbers.

    Casts every float to an int

    Args:
        a (int):
        b (int):
    
    Returns:
        int: The sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b