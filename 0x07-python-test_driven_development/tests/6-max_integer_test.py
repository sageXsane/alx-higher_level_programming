#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ TestMaxInteger class

        Tests cases for the max_integer function using unittest
    """

    def test_maxInteger(self):
        """ test_maxInteger    

            tests max_integer function with different values
        """
        "Normal case: Positive integers"
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        "Case: Mixture of positive and negative integers"
        self.assertEqual(max_integer([2, -3, -10, 10]), 10)

        "Case: Negative integers"
        self.assertEqual(max_integer([-19, -10, -1, -230]), -1)

        "Case: empty list = [] or list missing"
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)


