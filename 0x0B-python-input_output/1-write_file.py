#!/usr/bin/python3
""" write file module """


def write_file(filename="", text=""):
    """ write_file method:
        writes a string to a text file (UTF8) and
        returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num_written = f.write(text)
        return num_written
