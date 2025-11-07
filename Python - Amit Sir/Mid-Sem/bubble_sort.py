def bubble_sort(arr):
    n = len(arr)
    # Loop through all array elements
    for i in range (n -1):
        for j in range ( n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [5, 2, 9, 1, 5, 6]
print("Original arr: " , arr)
sorted_arr = bubble_sort(arr)
print("Sorted arr: ", sorted_arr)