# This program is in Python

# class Shape is used as ADT (Abstract Data Type)
class Shape:
    def __init__(self, type):
        self.type = type
        
    def get_area(self):
        pass
    
# Inheritance: Triangle, Rectangle, Square, Circle, Parallelogram inherit from Shape
# Polymorphism: get_area() method implemented differently for each shape class
class Triangle(Shape): # Class for Triangle (Inherits class Shape)
    def __init__(self, b, h):
        self.b = b
        self.h = h
    
    def area(self): # Polymorphism
        return 0.5 * self.b * self.h
    
class Rectangle(Shape): # Class for Rectangle (Inherits class Shape)
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self): # Polymorphism
        return self.l * self.w
    
class Square(Shape): # Class for Square (Inherits class Shape)
    def __init__(self, s):
        self.s = s

    def area(self): # Polymorphism
        return self.s * self.s
    
class Circle(Shape): # Class for Circle (Inherits class Shape)
    def __init__(self, r):
        self.r = r

    def area(self): # Polymorphism
        return 3.14159 * self.r ** 2
    
class Parallelogram(Shape): # Class for Parallelogram (Inherits class Shape)
    def __init__(self, b, h):
        self.b = b
        self.h = h
    
    def area(self): # Polymorphism
        return self.b * self.h
    
def number_input(message):
    while True:
        try:
            parameter = float(input(message))
            if parameter <= 0:
                print("Your inputs are not valid! Please enter non-zero positive numbers.")
            else:    
                return parameter
        except ValueError:
            print("Invalid input!!! Please enter a number.")

                    
def triangle():
    print("Your choice was: Triangle")
    b = number_input("Enter base of the triangle (feet): ")
    h = number_input("Enter height of the triangle (feet): ")
    shape = Triangle(b, h)
    area = shape.area()
    print(f"The area of triangle with base {b} feet and height {h} feet is {area} sq.feet")
    
def rectangle():
    print("Your choice was: Rectangle")
    l = number_input("Enter length of the rectangle (in feet): ")
    w = number_input("Enter width of the rectangle (in feet): ")
    shape = Rectangle(l, w)
    area = shape.area()
    print(f"The area of rectangle with length {l} feet and width {w} feet is {area} sq.feet")
    
def square():
    print("Your choice was: Square")
    s = number_input("Enter side of the square (feet): ")
    shape = Square(s)
    area = shape.area()
    print(f"The area of square with side {s} feet is {area} sq.feet")
    
def circle():
    print("Your choice was: Circle")
    r = number_input("Enter radius of the circle (feet): ")
    shape = Circle(r)
    area = shape.area()
    print(f"The area of circle with radius {r} feet is {area} sq.feet")
    
def parallelogram():
    print("Your choice was: Parallelogram")
    b = number_input("Enter base of the parallelogram (feet): ")
    h = number_input("Enter height of the parallelogram (feet): ")
    shape = Parallelogram(b, h)
    area = shape.area()
    print(f"The area of parallelogram with base {b} feet and height {h} feet is {area} sq.feet")
    
                    
# Function for user to select shape
def input_type():
    while True:
        print("\n -- Main Menu (Select an option): -- ")
        print("a. Triangle")
        print("b. Rectangle")
        print("c. Square")
        print("d. Circle")
        print("e. Parallelogram")
        print("f. Exit")

        input_choice = input("Enter your choice: ").strip().lower()

        if input_choice == 'a':
            triangle()
        elif input_choice == 'b':
            rectangle()
        elif input_choice == 'c':
            square()
        elif input_choice == 'd':
            circle()
        elif input_choice == 'e':
            parallelogram()
        elif input_choice == 'f':
            print(" -- You choose exit, Program is ending... -- ")
            break
        else:
            print("Invalid! (Please select one of a, b, c, d, e or f)")


try:
    input_type() # function to take input type from the user (integer or string)
except RuntimeError as e:
    print("Error:", e)