#!/usr/bin/python3

""" 'text indentation module'
    ==================================
    indents text with two newlines after every encounter with
    '.' '?' ':' characters
"""


def text_indentation(text=""):
    """ text_indentation function
         indents text with two newlines after every encounter with
        '.' '?' ':' characters

        Args:
            text: text containing characters that indicate indent

        Exceptions:
            TypeError: if text is not a valid string value
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    line = ""
    for char in text:
        line += char
        if char in ['.', '?', ':']:
            print("{}".format(line.strip()), end="\n\n")
            line = ""
    if line:
        print("{}".format(line.strip()))


if __name__ == "__main__":
    import doctest
    doctest.testmod(Verbose=True)
