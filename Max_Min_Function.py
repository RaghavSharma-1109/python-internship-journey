def max_value(arr):
    if not arr:
        return None
    largest = float('-inf')
    for num in arr:
        if num >largest:
            largest = num
    return largest
def min_value(arr):
    if not arr:
        return None
    smallest = float('inf')

    for num in arr:
        if num <smallest:
            smallest = num
    return smallest


arr = [1,-1, 40,-19,89]
max_val = max_value(arr)
min_val = min_value(arr)
print(f"Maximum value in arr is:{max_val}")
print(f"Minimum value in arr is:{min_val}")
