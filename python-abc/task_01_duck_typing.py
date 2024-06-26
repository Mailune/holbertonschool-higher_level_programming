#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


# Define the abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Implement the Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Implement the Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Define the shape_info function that uses duck typing
def shape_info(shape):
    # Using duck typing to call area and perimeter methods
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
