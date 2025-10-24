import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0


    while prev < n and arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1


    while prev < n and arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if prev < n and arr[prev] == x:
        return prev
    return -1
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 13
index = jump_search(arr, x)

if index != -1:
    print(f"{x} found at index {index}")
else:
    print("Not found")
