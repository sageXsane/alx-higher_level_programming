#!/usr/bin/python3
"""2-square module
    contains the following:
    Square class with five methods
"""


class Square:
    """Square class with init method
        methods:
        __init__: initializes square object with a size
        area: returns the area of the square object
        get size: returns the value of size
        set size: sets the value of size according to some criteria
        my_print: prints the square using hashes
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialises square object with size
            which is an optional private instance attribute
            Check to see whether size is a valid integer greater than 0 else
            raise relevant errors and exception messages
        Args:
            size (int): size of the square
            position (tuple): shifts the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size method - returns the value of size

            Return: returns the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method - sets the value of size

            which is an optional private instance attribute
            Check to see whether value is a valid integer greater than 0 else
            raise relevant errors and exception messages

            Args:
                value: value of size that must be checked and set to size

            """
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Area method

            Return:
                returns the area of the square (square of its size)
        """
        return self.__size ** 2

    @property
    def position(self):
        """get position method

            Return: returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set position method
            sets the position of the square

            Args:
                value : a tuple containing two integers
        """
        if value is not None:
            if len(value) != 2:
                raise TypeError("position must be a tuple of 2 \
positive integers")
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                raise TypeError("position must be a tuple of 2 \
positive integers")
            if value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 \
positive integers")
            else:
                self.__position = value

    def my_print(self):
        """my print method
            prints the square using hashes to represnt the size of the square.
        """
        if self.__size == 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print(end="\n")
            for r in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for c in range(0, self.__size):
                    print("#", end="")
                print(end="\n")
