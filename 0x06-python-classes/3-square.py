#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents  a square"""
    
    def ___init__(self, size=0):
        """initialize a new square
        
        Args:
            size (int): The size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
        
    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
