#!/usr/bin/python3
'''
This module defines a Square class.

The Square class creates a square according to assigned side length.
It also has methods for calculating its area together with property getters
and setters which make it seemless to change dimensions of the square.
'''


class Square:
    '''
    This is the "Square" class which contains methods and attributes for it.

    Attributes:
        __size (int): the size of the square (private).
    '''

    def __init__(self, size=0):
        '''
        The init method initializes the Square instance with a given size.

        Args:
            size (int): side of the square

        Raises:
            TypeError: if size is not int
            ValueError: if size is not a positive number
        '''
        self.__size = size

    @property
    def size(self):
        '''
        int: Gets the size of the square.

        Returns:
            int: The length of one side of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the size of the square with validation

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not int.
            ValueError: If size is negative.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        Computes the area of a square

        Returns:
            int: area of the square
        '''
        result = self.__size ** 2
        return result
