![](PolygonAreaCalculatorCover.png)

### About this project

This project is from freeCodeCamp's Scientific Computing with Python Certificate. This repository contains the prompt for the project as well as my solution for the assignment. 

To run my shape_calculator code with the tests provided by freeCodeCamp for this project, feel free to visit [my replit](https://replit.com/@NataliaRosado1/polygon-area-calculator).


### Assignment

In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.

#### Rectangle class
When a Rectangle object is created, it should be initialized with `width` and `height` attributes. The class should also contain the following methods:
* `set_width`
* `set_height`
* `get_area`: Returns area (`width * height`)
* `get_perimeter`: Returns perimeter (`2 * width + 2 * height`)
* `get_diagonal`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)
* `get_picture`: Returns a string that represents the shape using lines of "\*". The number of lines should be equal to the height and the number of "\*" in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
* `get_amount_inside`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`

#### Square class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The `__init__` method should store the side length in both the `width` and `height` attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a `set_side` method. If an instance of a Square is represented as a string, it should look like: `Square(side=9)`

Additionally, the `set_width` and `set_height` methods on the Square class should set both the width and height.

#### Usage example
```py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
That code should return:
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

### My solution

```
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        rect_str = "Rectangle(width={0}, height={1})".format(self.width, self.height)
        return rect_str

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
        return self.diagonal

    def get_amount_inside(self, rectangle):
        num_w = self.width // rectangle.width
        num_h = self.height // rectangle.height
        return num_w * num_h
        

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        pic_line = "*" * self.width
        pic_rows = [pic_line] * self.height
        picture = "\n".join(pic_rows)
        picture += "\n"

        return picture


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        square_str = "Square(side={})".format(self.width)
        return square_str

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
        
```
