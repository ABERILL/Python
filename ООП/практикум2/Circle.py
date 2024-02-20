class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self):
        return 3.14 * self.radius ** 2

    def calculate_circle_perimeter(self):
        return 2 * 3.14 * self.radius


for i in range(10):
    radius = int(input("Введите радиус окружности: "))
    circle1 = Circle(radius)
    area = circle1.calculate_circle_area()
    perimeter = circle1.calculate_circle_perimeter()
    print(f"Площадь окружности равна: {area}")
    print(f"Периметр окружности равен: {perimeter}")
