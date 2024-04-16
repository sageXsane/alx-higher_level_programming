#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
    """ read_file method:
        reads a text file (UTF8) and prints it to stdout

        Args:
            filename - name of the file
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
