#!/usr/bin/python3
""" Square module """


class BaseGeometry:
    """Base Geometry classs """

    def area(self):
        """ area method:
            Currently raises an exception error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator method:
            Validates that value is an appropriate integer value

            Args:
                name: string value labeling the base geometry object
                value: integer value that is being validated

            Exceptions:
                TypeError: if value is not an integer
                ValueError: if value is not a valid integer
                            value > 0
            """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        elif value is None:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """ area method:
            Returns the area of the rectangle object
        """
        return (self.__width * self.__height)

    def __str__(self) -> str:
        """ str method:
            return, the following rectangle description:
            [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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

    def __str__(self) -> str:
        """ str method:
            return, the following square description:
            [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
