#!/usr/bin/python3
""" rectangle module """


class Rectangle:
    """ Rectangle class

        init method
        get and set methods for private attributes
        area method
        perimeter method
        __str__ method
        __repr__ method
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ rectangle init method:

            Args:
                width - width of rectangle object
                height - height of rectangle object
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ returns area of rectangle object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __repr__(self):
        """ repr method:
            return a string representation of the rectangle to be able
            to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __str__(self):
        """ prints the rectangle object with
            dimensions represented in hashes
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            for h in range(0, self.__height):
                for w in range(0, self.__width):
                    rectangle += "#"
                if h < self.__height - 1:
                    rectangle += "\n"
            return rectangle

    def __del__(self):
        """ del method:
            prints a message when a rectangle instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
