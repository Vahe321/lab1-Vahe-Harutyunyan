def binary_search(arr, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr, x):
    n = len(arr)
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    return binary_search(arr, i // 2, min(i, n - 1), x)

