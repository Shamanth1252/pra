def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if target is not found

# Example usage:
sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12  # Change this to the element you want to search
index = binary_search(sorted_list, target)
if index != -1:
    print("Element", target, "found at index:", index)
else:
    print("Element", target, "not found in the list.")
