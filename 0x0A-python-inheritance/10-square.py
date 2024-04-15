#!/usr/bin/python3
""" square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class
        inherits from Rectangle class
    """

    def __init__(self, size):
        """ init method:
            initialises private size atrrtibute to size parameter
            parameter is first validated using integer_validator

            Args:
                size: side dimension of square object
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area method:
            returns area of square object
        """
        return (self.__size**2)
