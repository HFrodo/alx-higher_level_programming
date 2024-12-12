#!/usr/bin/python3
'''
This Module contains program for rendering a square
'''


class Square:
    '''
    This is the "Square" class for the square.

    Attributes:
        __size (int): The size of the square (private).
    '''
    def __init__(self, size=0):
        '''
        Initializes the Square class with private instance attribute: __size
        
        Args:
            __size (int): The size of the square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
