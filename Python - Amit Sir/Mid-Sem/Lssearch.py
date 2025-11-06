def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"Element {key} is indexed at {i}")
            return
    print("Element not found")

arr = [10,25,30,45,50]
key = 45
linear_search(arr, key)