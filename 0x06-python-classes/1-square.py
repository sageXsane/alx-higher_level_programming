#!/usr/bin/python3

class Square:
    """Square class with initializing method only"""
    def __init__(self, size):
        """Initializes Square class with a private size attribute

        Args:
            size (int): represents the size of the square
        """
        self.__size = size
