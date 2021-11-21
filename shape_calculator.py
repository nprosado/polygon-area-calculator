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
