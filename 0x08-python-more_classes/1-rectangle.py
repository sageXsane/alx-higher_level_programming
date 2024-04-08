#!/usr/bin/python3
""" rectangle module """


class Rectangle:
    """ Rectangle class

        init method
        get and set methods for private attributes
    """
    def __init__(self, width=0, height=0):
        """ rectangle init method:

            Args:
                width - width of rectangle object
                height - height of rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method that gets width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width
            Args:
                value : integer value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter method that gets height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height
            Args:
                value : integer value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
