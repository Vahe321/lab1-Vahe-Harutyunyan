def ternary_search(f, left, right, eps=1e-6):
    while right - left > eps:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3

        if f(mid1) < f(mid2):
            left = mid1
        else:
            right = mid2

    return (left + right) / 2
def f(x):
    return -(x - 2)**2 + 3

result = ternary_search(f, -10, 10)
print(f"Maximum at x ≈ {result:.5f}")
