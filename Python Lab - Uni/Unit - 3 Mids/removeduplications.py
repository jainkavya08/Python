# Program to remove duplicates from a list

# Create list
numbers = [10,10,20,30,30,20,30,40,50,60,60]

# Remove duplicates
unique_numbers = list(set(numbers))

# Display
print("Original list: " , numbers)
print("Removed duplicates list: ", unique_numbers)