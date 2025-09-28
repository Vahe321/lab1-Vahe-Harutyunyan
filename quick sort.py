def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    left = []
    right = []
    middle = []

    pivot = arr[n // 2]

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)

    return quick_sort(left) + middle + quick_sort(right)


numbers = [4, 5, 1, 7, 3, 9]

print("After :", quick_sort(numbers))
