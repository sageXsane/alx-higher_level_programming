#!/usr/bin/python3
"""2-square module
    contains only initialing method for square class
"""


class Square:
    """Square class with init method"""
    def __init__(self, size=0):
        """Initialises square object with size
            which is an optional private instance attribute
            Check to see whether size is a valid integer greater than 0 else
            raise relevant errors and exception messages
        Args:
            size (int): size of the square
        """
        if size is not None:
            try:
                if not isinstance(size, int):
                    raise TypeError("size must be an integer")
                elif size < 0:
                    raise ValueError("size must be >= 0")
                else:
                    self.__size = size
            except TypeError as e:
                print(e)
            except ValueError as e:
                print(e)
