#!/usr/bin/python3
"""Module provides funtion `read_file`.
"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
