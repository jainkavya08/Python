# Program to create a dictionary and access elements

# Create a dict
student = {
    "name": "Kavya",
    "age": 20,
    "course": "BCA",
    "year": 2025
}

# Display the entire dictionary
print("Student dictionary: ", student)

# Accessing the elements
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Year:", student["year"])

# Accessing using get() method
print("Access using get():", student.get("course"))

