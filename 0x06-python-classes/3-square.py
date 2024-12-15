#!/usr/bin/python3
'''
This module contains the "Square" class

Designed to obtain area of square

'''


class Square:
    '''
    This is the "Square" class
    It holds the attributes and methods for creating a square

    Attributes:
        __size(float): The size of the square (private)
    '''


    def __init__(self, size=0):
        '''
        Initializes the square object with a "size" parameter

        Parameters:
            size(float): the size of the square

        Args:
            __size(float): is the private instance attribute representing the size of the "Square"
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

