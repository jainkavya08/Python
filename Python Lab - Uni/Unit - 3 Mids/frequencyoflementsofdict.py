# Program to count frequency of elements using dictionary

# Creating a list
numbers = [2, 4, 2, 8, 4, 4, 6, 2, 8]

# Creating an empty dictionary
frequency = {}

# Counting frequency of each element
for item in numbers:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

# Displaying the frequency of elements
print("List:", numbers)
print("Frequency of elements:", frequency)
