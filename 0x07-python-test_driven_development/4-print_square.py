#!/usr/bin/python3
""" print square module
    Has a function print_square that prints size X size square
"""


def print_square(size=0):
    """ print_square function

        prints a square depending on the dimensions of size

        Args:
            size: size of the square

        Exceptions:
            TypeError: size must be an integer
            ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print(end="\n")
    else:
        for row in range(0, size):
            for col in range(0, size):
                print("#", end="")
            print(end="\n")


if __name__ == "__main__":
    import doctest
    doctest.testmod(Verbose=True)
