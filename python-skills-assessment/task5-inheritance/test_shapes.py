from shapes import Circle, Rectangle, Triangle

options = """

    Options:
            1. To calculate are of circle
            2. To calculate are of rectange
            3. To calculate are of Triangle

      """
print(options)
opt = int(input("Choose shape you want: "))

if  opt == 1:
    input_radius = float(input("Enter radius: "))
    circle = Circle(input_radius)

    print(f"Area of circle with radius {input_radius} is {circle.area()}")
elif opt == 2:
    length  = float(input("Lenght of rectangle: "))    
    width = float(input("Width of rectangle: "))
    rectangle = Rectangle(width, length)
    print(rectangle.area())
elif opt == 3:
    side1 = float(input("Size of size1: "))
    side2 = float(input("Size of side2: ")) 
    side3 = float(input("Size of side 3: "))
    triangle = Triangle(side1, side2, side3)   
    print(triangle.area())
else:
    print("Invalid option")