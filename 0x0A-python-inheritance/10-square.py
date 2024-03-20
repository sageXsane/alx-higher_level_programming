#!/usr/bin/python3
""" Square module """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Square class"""

    def __init__(self, size):
        """ square class constructor method
            Checks whether size is a valid positive integer and
            sets it to the private attribute __size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area method:
            returns the area of square obj
        """
        return (self.__size**2)
