class Shape:

    def calculate_area(self):
        pass

    def calculate_perimetr(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimetr(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width

    def calculate_perimetr(self):
        return 2*(self.length+self.width)

class Triangle(Shape):
    
    def __init__(self,base,height,side1,side2,side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5*self.base*self.height

    def calculate_perimetr(self):
        return self.side1+self.side2+self.side3


radius = 3
circle = Circle(radius)
circle_area= circle.calculate_area()
circle_perimeter = circle.calculate_perimetr()
print("Радиус окружности:", radius)
print("Площадь окружности:", circle_area)
print("Периметр окружности:", circle_perimeter)

length = 6
width = 4
rectangle = Rectangle(length, width)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimetr()
print("Длинна прямоугольника:", length)
print("Ширина прямоугольника:", width)
print("Площадь прямоугольника:", rectangle_area)
print("Периметр прямоугольника:", rectangle_perimeter)

base = 3
height = 4
side1 = 4
side2 = 5
side3 = 6
triangle = Triangle(base, height, side1, side2, side3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimetr()
print("Площадь треугольника:", triangle_area)
print("Периметр треугольника:", triangle_perimeter)
