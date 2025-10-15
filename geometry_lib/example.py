from shapes import Circle, Triangle

# Круг
circle = Circle(5)
print(f"Area of circle: {circle.area()}")

# Треугольник
triangle = Triangle(3, 4, 5)
print(f"Area of triangle: {triangle.area()}")
print(f"Is right triangle? {triangle.is_right_triangle()}")

# Вычисление площади без знания типа
def get_area(shape):
    return shape.area()

print(get_area(circle))
print(get_area(triangle))