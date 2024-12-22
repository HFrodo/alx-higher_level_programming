#!/usr/bin/python3
'''
This module is responsible for creating a rectangle

It uses a Rectangle class with height and width attributes
And property setters and getters to assign values to create the obj
'''


class Rectangle:
    def __init__(self, width=0, height=0):
        '''
        This initializes the Rectangle object with height and width

        Attributes:
            __width(int): Holds the horizontal length of the rectangle
            __height(int): Holds the vertical length of rectangle
        '''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''
        Getter property for the width attribute

        Returns:
            int: __width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter property for the width attribute

        Args:
            value(int): the new width value

        Raises:
            TypeError: if width is not an integer type
            ValueError: if width < 0

        Returns:
            int: __width
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''
        Getter property for height attribute

        Returns:
            int: __height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter property for the height attribute

        Args:
            value(int): The new height value.

        Raises:
            TypeError: if height is not an integer type
            ValueError: if height < 0

        Returns:
            int: __height
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
