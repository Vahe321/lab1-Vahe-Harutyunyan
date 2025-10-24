def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1
arr = [1, 3, 5, 7, 9, 11, 13]
x = 7
result = binary_search(arr, x)

if result != -1:
    print(f"{x} ka index {result}")
else:
    print("chi gtnvel ")

