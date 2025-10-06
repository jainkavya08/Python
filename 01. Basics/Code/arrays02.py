import array

# Create an integer array
arr = array.array('i', [1,2,3,4,5])     # Here i is to denote integer array

# Access element
print (arr[2])

# Add element
arr.append(6)

# remove element
arr.remove(3)

print(arr)