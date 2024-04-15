#!/usr/bin/python3
""" rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class:
        inherits from BaseGeometry class
    """

    def __init__(self, width, height):
        """ init method:
            initialises private attributes to width and height
            parameters are validated using integer_validator method

            Args:
                width(int): positive width of rectangle instance
                height(int): positive height of rectangle instance
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
