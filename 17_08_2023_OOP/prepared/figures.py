class Figure:
    def __init__(self, x, y, line_width):
        self.x = x
        self.y = y
        self.line_width = line_width
    
    def area(self):
        return None


class Circle(Figure):
    def __init__(self, x, y, line_width, radius):
        super().__init__(x, y, line_width)
        self.radius = radius

    @property
    def area(self):
        return 3.14 * (self.radius ** 2)


class Rectangle(Figure):
    def __init__(self, x, y, line_width, width, height):
        super().__init__(x, y, line_width)
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


# figure = Circle(10, 12, 100, 100)
# figure.area


# figures = [Circle(5), Rectangle(10, 8)]
# for figure in figures:
#     print(f"Figure on ({figure.x}, {figure.y}): {figure.area()}")



    