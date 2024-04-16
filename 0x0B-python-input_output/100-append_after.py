#!/usr/bin/python3
""" 100-append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """ append_after method:
        inserts a line of text to a file
        after each line containing a specific string

        Args:
            filename - name of file containing text
            search_strings - specific string to which after
                            new string must be appended
            new_string - string to be appended
    """
    with open(filename, "r", encoding="utf-8") as f:
        file_data = list(f)

    with open(filename, "w", encoding="utf-8") as f:
        for line in file_data:
            f.write(line)
            if search_string in line:
                f.write(new_string)
