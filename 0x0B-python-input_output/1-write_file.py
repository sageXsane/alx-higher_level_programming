#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ write_file method:
        writes a string to a text file (UTF8)
        returns the number of characters written

        Args:
            filename - name of file
            text - text to be written to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        written_chars = f.write(text)
        return written_chars
