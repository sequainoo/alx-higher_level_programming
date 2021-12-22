#!/usr/bin/python3
"""This module presents the function write_file.
"""


def write_file(filename="", text=""):
    """Writes text given into a file `filename`.

    Creates file if does not already exists.

    Args:
        filename (str): The name of file
        text (str): The text to write to file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        if text and type(text) is str:
            return f.write(text)
