#!/usr/bin/python3
'''
This module creates a square from the Square class

The class has an attribute for the side length
It uses property setters & getters to validate input
Methods within it are used to calculate the area and print out the square
'''


class Square:
    '''
    This class defines the square with size and position attributes.

    Attributes:
        __size(int): the side length of the square
        __position(int): The relative position of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is greater than 0
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes the square instance with
        size and position private attributes

        Args:
            size(int): side length of the square
            position(int): horizontal and vertical position of square

        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        Getter method

        Returns:
            int: side length of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Setter method to assign new length of side

        Args:
            __size(int): current side length of square
            value(int): new side length of square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''
        Getter method

        Returns:
            int: position of the square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Setter method assigns new position of square

        Args:
            __position(int): current position
            value(int): new horizontal and vertical position of square

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        '''
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''
        Method for calculating area

        Returns:
            int: area of square
        '''
        return self.__size ** 2

    def my_print(self):
        '''
        Prints out the actual square using "#" in its right position
        If size is 0, it prints an empty line.

        Args:
            None
        '''
        if (self.__size == 0):
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
