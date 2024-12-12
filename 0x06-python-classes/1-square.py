#!/usr/bin/python3
'''
This module contains a class that defines a square
'''


class Square:
    '''
    This is the "Square" class representing a square.

    Attributes:
        __size(int): The size of the square (private).
    '''
    def __init__(self, __size):
        '''
        Initializes the Square class with private instance attribute:__size
        Args:
            __size(int): The size of the square.
        '''
        self.__size = __size
