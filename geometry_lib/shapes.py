import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9

# Для расширения — добавьте другие фигуры, наследуясь от Shape