#!/usr/bin/python3
""" append file module """


def append_write(filename="", text=""):
    """ append_write method:
        appends a string at the end of a text file (UTF8) and
        returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        num_written = f.write(text)
        return num_written
