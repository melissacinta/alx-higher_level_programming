#!/usr/bin/python3
"""Module housing a function that writes to a file"""


def write_file(filename="", text=""):
    """Function that writes to file and return the
    number of characters written
    """
    with open(filename, "w", encoding='UTF8') as f:
        writeNum = f.write(text)
        return writeNum
