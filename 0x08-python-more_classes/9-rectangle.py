#!/usr/bin/python3
"""This is a rectangle class definition."""


class Rectangle:
    """Create a rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle object using width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of rectagle."""
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return string represenation of the instance."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            x = ""
            for i in range(self.__height):
                x += (str(self.print_symbol) * self.__width)
                if i != self.__height - 1:
                    x += "\n"
            return x

    def __repr__(self):
        """Return a string that can create an instance using "eval()"."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when a deleted object is called."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle out of the two."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a square using the rectangle class."""
        return (cls(size, size))
