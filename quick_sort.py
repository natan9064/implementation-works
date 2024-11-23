import random

def partition(a, start, end):
    comparisons = initialization = 0
    
    x = random.randint(start, end)
    a[x], a[end] = a[end], a[x]
    i = start - 1
    for j in range(start, end):
        comparisons += 1
        if a[j] <= a[end]:
            initialization += 2
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i + 1], a[end] = a[end], a[i + 1]
    initialization += 2
    return i + 1, comparisons, initialization


def __quick_sort(a, start, end):
    comparisons = initialization = 0
    if start < end:
        q, c, i = partition(a, start, end)
        left_comparisons, left_initialization = __quick_sort(a, start, q - 1)
        right_comparisons, right_initialization = __quick_sort(a, q + 1, end)
        comparisons = c + left_comparisons + right_comparisons
        initialization = i + left_initialization + right_initialization
    return comparisons, initialization


def quick_sort(a):
    comparisons, initialization = __quick_sort(a, 0, len(a) - 1)
    return comparisons, initialization


a = [43, 23, 23, 54, 65, 76, 332, 12]
comparisons, initialization = quick_sort(a)
print(f"Sorted array: {a}")
print(f"Comparisons: {comparisons}")
print(f"Initialization: {initialization}")
