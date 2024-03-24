#!/usr/bin/python3
""" read file module """


def read_file(filename=""):
    """ read_file method:
        reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
