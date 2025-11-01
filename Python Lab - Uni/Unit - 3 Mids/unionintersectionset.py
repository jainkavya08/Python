# Program to demonstrate union, intersection, and difference of sets

# Create set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Perform set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

# Display
print("Set 1:", set1)
print("Set 2:", set2)
print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)
print("Difference of sets (Set1 - Set2):", difference_set)