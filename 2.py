# 2. O => Open/Close Principle (OCP)
# Software entities (classes, modules, functions etc.) should be open for extension
# but closed for modification.
# Example

class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius ** 2)
        
    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * shape.width * shape.height
        elif shape.type == "circle":
            return 2 * 3.14 * shape.radius
        
# if we want to add support for new shape, like triangle, we would have to 
# modify the calculate_area and calculate_perimeter methods, violating 
# the Open/Close principle
# to overcome this challenges as follow 

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
# We can add now new shape like Triangle without modifying the existing code 
class Triangle(Shape):
    # Now implement your code for triangle 
    pass







