#!/usr/bin/python3
"""Contains the rectangle class that inherits from the Base."""
from models.base import Base


class Rectangle(Base):
    """This is a Rectangle class inheriting from base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle class."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Return area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using #."""
        for col in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + '#' * self.__width, end='')
            print()

    def __str__(self):
        """Return string representation of the class."""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle instance."""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for att, val in kwargs.items():
                self.__setattr__(att, val)
            return

    def to_dictionary(self):
        """Return a dictionary representation of a Rectangle."""
        return ({'x':self.__x, 'y':self.__y, 'id':self.id, 'height':self.__height, 'width':self.__width})
