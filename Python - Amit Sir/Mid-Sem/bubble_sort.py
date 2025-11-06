def bubble_sort(arr):
    n = len(arr)
    # Loop through all array elements
    for i in range( n - 1):
        # Ladt i elements are already sorted
        for j in range ( n - i - 1):
            # Swap if the element is greater than next
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

arr = [5, 2, 9, 1, 5, 6]
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array: ", sorted_arr)