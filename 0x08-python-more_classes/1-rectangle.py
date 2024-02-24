#!/usr/bin/python3
""" 1-rectangle module """


class Rectangle:
    """ Retangle class contains:
        initializing method
        set and get width methods
        get and set height methods
    """

    def __init__(self, width=0, height=0):
        """ init method
            Initialises rectangle dimensions arguments to
            related object attributes

            Args:
                width: width of the rectangle
                height: height of the rectangle

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method that returns width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method that sets the width attribute to value(if valid)"""
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """ getter method that returns height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method that sets the height attribute to value(if valid)"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
