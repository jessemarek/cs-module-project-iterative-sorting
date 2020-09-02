def linear_search(arr, target):
    # Your code here
    # we need to look at each item in thelist and compare it to the target
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # keep track of the lower index and higher index
    low = 0
    high = len(arr) - 1

    while low <= high:
        # find the midpoint and compare that index value to the target
        mid = high + low // 2
        # if the index value matches the target return it
        if target == arr[mid]:
            return mid
        # otherwise decide which half to discard and repeat on the remaining half
        # if the target is less than the mid we can discard the right most half
        if target < arr[mid]:
            high = mid - 1
        # otherwise discard the left most half
        if target > arr[mid]:
            low = mid + 1

    return -1  # not found
