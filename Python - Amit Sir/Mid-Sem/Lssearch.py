def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"Element {key} is indexed at {i}")
            return
    print("Element not found")

# Example
arr = [10,20,30,40,50]
key = 30
linear_search(arr,key)
