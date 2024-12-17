#!/usr/bin/python3
'''
This module contains the "Square" class

Designed to obtain area of square

'''


class Square:
    '''
    A class that represents a Square
    It holds the attributes and methods for creating a square

    Attributes:
        __size(float): The size of one side of the square (private)
    '''
    def __init__(self, size=0):
        '''
        Initializes a square object with a given size

        Args:
            size(float): the size of one side of the square. Must be
                        a non-negative integer. Defaults to 0.

        Raises:
            TypeError: If "size" does not match a float type
            ValueError: If "size" is a negative number
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        '''
        area = self.__size * self.__size
        return area
