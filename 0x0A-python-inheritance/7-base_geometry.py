#!/usr/bin/python3
""" Base geometry module """


class BaseGeometry:
    """ empty class """
    pass

    def area(self):
        """ area method:
            not implemented

            Exceptions:
                Exception: area() not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator method:
            validates value

            Args:
                name - name of value
                value - integer value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value is None:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
