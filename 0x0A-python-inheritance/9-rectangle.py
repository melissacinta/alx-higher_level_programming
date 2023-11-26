#!/usr/bin/python3

"""rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits fro BaseGeometry"""
    def __init__(self, width, height):
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
    def __str__(self):
        """ return the string version of the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
