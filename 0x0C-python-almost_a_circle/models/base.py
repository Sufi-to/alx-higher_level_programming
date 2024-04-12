#!/usr/bin/python3
"""Contains the base class."""
import json
import turtle
import csv

class Base:
    """This is the Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string repr of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string repr of list_objects to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON representation."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a base instance with all the attributes set."""
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(2, 3)
            else:
                dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as file:
                dict_list = Base.from_json_string(file.read())
                return [cls.create(**i) for i in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to a csv file."""
        csv_file_name = cls.__name__ + ".csv"
        with open(csv_file_name, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            if list_objs is None:
                csv_writer.write("[]")
            else:
                if cls.__name__ == "Square":
                    csv_writer.writerow("id", "size", "x", "y")
                    for square in list_objs:
                        csv_writer.writerow(square.id, square.size, square.x, square.y)
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow("id", "width", "height", "x", "y")
                    for rect in list_objs:
                        csv_writer.writerow(rect.id, rect.width, rect.height, rect.x, rect.y)

    @classmethod
    def load_from_file_csv(cls):
        """Returns objects from a csv file or empty list if not found."""
        csv_name = str(cls.__name__) + ".csv"
        try:
            with open(csv_name, 'r') as file:
                if cls.__name__ == "Rectangle":
                    f_names = ["id", "width", "height", "x", "y"]
                else:
                    f_names = ["id", "size", "x", "y"]
                reader = csv.DictReader(file, field_names=f_names)
                objs = []
                for row in reader:
                    x = row.to_dictionary()
                    objs.append(x)
                return 

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open the window and draw all the rectangles and Squares."""
        turtle.title("0x0C-python_almost_full_circle draw function")
        turtle.bgcolor("cyan")
        draw = turtle.Turtle()
        draw.shape("turtle")
        draw.shapesize(1, 1, 1)
        draw.pen(pencolor="purple", fillcolor="orange", pensize=3, speed=1)
        for r in list_rectangles:
            draw.penup()
            draw.goto(r.x, r.y)
            draw.pendown()
            for i in range(2):
                draw.fd(r.width)
                draw.lt(90)
                draw.fd(r.height)
                draw.lt(90)

        for s in list_squares:
            draw.penup()
            draw.goto(s.x, s.y)
            draw.pendown()
            for i in range(2):
                draw.fd(s.width)
                draw.lt(90)
                draw.fd(s.height)
                draw.lt(90)

        turtle.exitonclick()
