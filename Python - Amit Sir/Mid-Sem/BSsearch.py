def binary_search(arr,key):
    low = 0
    high = len(arr) - 1

    while low <= high :
        mid = (low + high ) // 2
        if arr[mid] == key:
            print(f"Element {key} is indexed at {mid}")
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    print("Element not found")

# Example
arr = [10, 25, 30, 45, 50]
key = 25
binary_search(arr,key)