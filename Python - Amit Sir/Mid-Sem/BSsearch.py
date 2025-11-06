def binary_sort(arr,key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = ( low + high ) // 2
        if arr[mid] == key:
            print(f"Element {key} is indexed at {mid}")
            return
        elif arr[mid] < key :
            low = mid + 1
        else:
            high = mid - 1
    print("Element not found")

arr = [10, 20, 30, 40, 50, 60]
key = 40
binary_sort(arr, key)

