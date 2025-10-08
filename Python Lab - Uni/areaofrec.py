# Circle
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
circle_area = pi * radius * radius
circle_perimeter = 2 * pi * radius

# Rectangle
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
rec_area = length * breadth
rec_peri = 2 * length + breadth

# Printing out
print ("Area of circle is : " , circle_area)
print ("perimeter of circle is: " , circle_perimeter)
print ("Area of rectangle: " , rec_area)
print("perimeter of rectangle: " , rec_peri)