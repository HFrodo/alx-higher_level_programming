#!/usr/bin/python3
'''
This module is responsible for creating a rectangle

It uses a Rectangle class with height and width attributes
And property setters and getters to assign values to create the obj
'''


class Rectangle:
    '''
    Class that defines the rectangle object (based on 0-rectangle.py).

    Attributes:
        __width(int): width of rectangle
        __height(int): height of rectangle

    '''
    def __init__(self, width=0, height=0):
        '''
        This initializes the Rectangle object with height and width

        Args:
            width(int): horizontal length of the rectangle (defaults to 0)
            height(int): vertical length of rectangle (defaults to 0)

        Raises:
            TypeError: if width/ height is not an integer
            ValueError: if width/height is less than 0
        '''
        self.height = height
        self.width = width

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
        Setter property for the private instance width attribute

        Args:
            value(int): the new width value

        Raises:
            TypeError: if width is not an integer type
            ValueError: if width is less than 0

        Returns:
            int: __width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            ValueError: if height is less than 0

        Returns:
            int: __height
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        Public instance method which calculates Area

        Returns:
            int: Area of the rectangle
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        Public instance method which computes Perimeter

        Returns:
            int: Perimeter of rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)
