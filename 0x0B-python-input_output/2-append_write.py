#!/usr/bin/python3
""" append_write module """


def append_write(filename="", text=""):
    """ append_write method:
        appends a string at the end of a text file (UTF8) and
        returns the number of characters added

        Args:
            filename - name of file
            text - text to be appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        written_chars = f.write(text)
        return written_chars
