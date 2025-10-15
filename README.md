# Geometry_Lib
Geometry_Lib - тестовый проект для ООО Mindbox

A Python library for calculating areas of geometric shapes like circles and triangles.

## Features

- Calculate area of a circle by radius.
- Calculate area of a triangle by three sides.
- Check if a triangle is right-angled.
- Extensible for more shapes.
- Unit tests included.

## Usage

```python
from geometry_lib import Circle, Triangle

circle = Circle(5)
print(circle.area())

triangle = Triangle(3, 4, 5)
print(triangle.area())
print(triangle.is_right_triangle())