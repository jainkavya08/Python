# Program to add and remove elements from a dictionary

# Creating a dictionary
student = {
    "name": "Kavya",
    "age": 20,
    "course": "BCA"
}

print("Original Dictionary:", student)

# Adding elements
student["year"] = 2025
student["grade"] = "A"
print("After Adding Elements:", student)

# Removing an element using pop()
student.pop("age")
print("After Removing 'age':", student)

# Removing last inserted item using popitem()
student.popitem()
print("After Removing Last Item:", student)

# Removing an element using del
del student["course"]
print("After Deleting 'course':", student)
