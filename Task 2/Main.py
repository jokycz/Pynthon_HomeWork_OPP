from Rectangle import Rectangle
from Circle import Circle
from RightTriangle import RightTriangle
from Trapezoid import Trapezoid


shapes = [
    Rectangle(5, 10),
    Circle(7),
    RightTriangle(3, 6),
    Trapezoid(4, 6, 5)
]

for shape in shapes:
    print(f"Obsah {shape.type} je {shape.area()}")