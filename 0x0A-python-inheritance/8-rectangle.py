#!/usr/bin/python3
""" Rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class
        Class that is the childclass of the BaseGeometry class
    """

    def __init__(self, width, height):
        """ rectangle subclass initiate method
            Sets private atrributes height and width to given values
            Validates whether height and width are valid positive integers
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
