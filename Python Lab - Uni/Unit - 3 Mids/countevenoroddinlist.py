# Program to count even and odd numbers in a list

# Create the list
numbers = [10, 23,4,5,24,53,43,2,5,43,56,78]

# Intialize counters
even_count = 0
odd_count = 0

# Traverse the list
for num in numbers :
    if num % 2 == 0 :
        even_count += 1
    else :
        odd_count += 1

# Display even odd count
print ("list: " , numbers)
print("Even count: ", even_count)
print("Odd count: " , odd_count)