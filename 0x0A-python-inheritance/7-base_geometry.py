#!/usr/bin/python3
""" base_geometry module """


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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
