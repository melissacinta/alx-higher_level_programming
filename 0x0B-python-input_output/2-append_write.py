#!/usr/bin/python3
"""Module housing a function that appends writes to a file"""


def append_write(filename="", text=""):
    """Function that appends writes to file and return the
    number of characters written
    """
    with open(filename, "a", encoding='utf-8') as f:
        writeNum = f.write(text)
        return writeNum
