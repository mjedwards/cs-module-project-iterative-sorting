def linear_search(arr, target):
    # Your code here
    for x in range(len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr) -1 
    low = 0
    mid_point = 0
    # Your code here
    while low <= high:
        mid_point = (high + low) // 2
        if arr[mid_point] < target:
            low = mid_point + 1
        elif arr[mid_point] > target:
            high = mid_point - 1
        else:
            return mid_point

    return -1  # not found
