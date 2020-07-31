class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        perimeter = (self.width + self.length) * 2
        return(perimeter)



class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.length = side


shape_one = Rectangle(2, 3)
shape_two = Square(4)

print(shape_one.calculate_perimeter())
print(shape_two.calculate_perimeter())
