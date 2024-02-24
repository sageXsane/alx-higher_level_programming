#!/usr/bin/python3
""" 2-rectangle module """


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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            raise ValueError("heigth must be >= 0")
        self.__height = value

    def area(self):
        """ area method
            returns the area of the reactangle
            = width * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter public instance method
            returns the perimeter of the rectangle
            = 2(width + height)
        """

        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle using hash characters"""
        rectangle = ""
        if (self.__width == 0) or (self.__height == 0):
            return rectangle
        else:
            for row in range(0, self.__height):
                for col in range(0, self.__width):
                    rectangle += "#"
                if row != self.__height - 1:
                    rectangle += "\n"
        return rectangle
