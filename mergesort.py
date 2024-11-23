
import random

def merge(a,start,mid,end):
    comparisons = initialization = 0
    i = j = 0     

    left = a[start:mid + 1]
    right = a[mid +1 :end + 1] 
    k =start
    comparisons +=1 
    while i < len(left) and j <len(right):
        comparisons += 1
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        initialization += 1    
        k += 1
    
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    
    return comparisons, initialization


def __merge_sort(a, start, end):
    comparison = initialization = 0
    if start < end: 
        mid = (start + end) // 2
        c1, i1 = __merge_sort(a, start, mid)
        c2, i2 =  __merge_sort(a, mid+1, end)
        c3, i3 = merge(a, start, mid, end)
        comparison += c1 + c2 + c3
        initialization += i1 + i2 + i3
    return comparison, initialization

def merge_sort(a):
    return __merge_sort(a, 0 ,len(a) - 1)


arr = [43, 434,23, 2342,23 ,4,2 ,43, 43 ]
merge_sort(arr)
print(arr)

def test_cases():
    arrays = [[random.randint(-2000, 20000) for _ in range(6)] for _ in range(6)]
    passed = True
    for arr in arrays:
        print(f"Original array: {arr}")
        c, i = merge_sort(arr)
        print(f"Sorted array: {arr}")
        print(f"Comparisons: {c} \nInitialization: {i}")
test_cases()
