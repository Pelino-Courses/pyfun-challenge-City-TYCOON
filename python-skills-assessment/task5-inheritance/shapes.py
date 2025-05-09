from math import pi

class Shape:
    """
    A basic shape class. Other shapes will inherit from this.

    """

    def area(self):
        raise NotImplementedError("Area method must be defined in the child class.")
    
    def perimeter(self):
        raise NotImplementedError("Perimeter method must be defined in the child class.")
    def __str__(self):
        return "generic Shape"
    

class Circle(Shape):
    """

    Represents a circle with a given radius.
    """
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"
    @classmethod
    def from_diameter(cls, diameter):
        """
        Create a circle using the diameter instead of radius.
        """
        return cls(diameter / 2)
    

class Rectangle(Shape):
        """

        Represents a rectangle with width and height.
        """
        def __init__(self, width, height):
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive numbers.")
            self.width = width
            self.height = height

        def perimeter(self):
            return 2 * (self.width + self.height)  
        
        def area(self):
            return self.width * self.height
        
        def __str__(self):
            return f"Rectangle {self.width} * {self.height}"
        
class Square(Rectangle):
        """

        A square is a special case of a rectangle where  all sides are equal.
        """

        def __init__(self, side):
            if  side <= 0:
                raise ValueError("Side must be a positive number.")
            super().__init__(side, side)

        def __str__(self):
            return f"Square with side {self.width}"

class Triangle(Shape): 
        """

        Represents a triangle with three side.
        """
        def __init__(self, a, b, c):
             if a <= 0 or b <= 0 or c <= 0:
                  raise ValueError("Sides must be positive numbers.")
             if a + b <= c or a + c <= b or b + c <= a:
                  raise ValueError("These sides do not form  a valid triangle .")
             self.a = a
             self.b = b
             self.c = c
        def perimeter(self):
            return self.a + self.b + self.c

        def area(self):
            # Using Heron's formula
            s = self.perimeter() / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

        def __str__(self):
            return f"Triangle with sides {self.a}, {self.b}, {self.c}"   
