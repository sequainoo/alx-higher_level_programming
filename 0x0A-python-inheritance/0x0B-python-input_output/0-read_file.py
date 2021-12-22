#!/usr/bin/python3
"""This module presents the function read_file.
"""


def read_file(filename=""):
    """Reads the given file `filename`.

    Prints to stdout.

    Args:
        filename (str): The name of file
        text (str): The text to write to file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
