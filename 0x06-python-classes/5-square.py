#!/usr/bin/python3
'''
This module allows for the creation of a square from the Square class

The class has an attribute for the side length
It uses property setters & getters to validate input
Methods within it are used to calculate the area and print out the square
'''


class Square:
    '''
    This is the "Square" class which contains methods and attributes for it.

    Attributes:
        __size (int): the size of the square (private).
    '''

    def __init__(self, size=0):
        '''
        Initializes square instance with the size attribute

        Args:
            size (int): side length of a square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is negative
        '''

        self.__size = size

    @property
    def size(self):
        '''
        Property getter to retrieve side length value

        Returns:
            int: side length of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Property setter to assign a new value to the side length of square

        Args:
            __size (int): current value of side length
            value (int): new value of side length

        Raises:
            TypeError: if value is not int
            ValueError: if value is negative
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        Method for calculating area

        Returns:
            int: area of square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        Prints out the actual square using "#".
        If size is 0, it prints an empty line.

        Args:
            None
        '''
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
