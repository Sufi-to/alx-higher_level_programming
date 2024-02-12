#!/usr/bin/python3
"""Contains the square class that inherits from rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a square class that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of square."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square instance."""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for att, val in kwargs.items():
                self.__setattr__(att, val)
            return

    def to_dictionary(self):
        """Return a dictionary representation of a Rectangle."""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        """Return a string for the square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
