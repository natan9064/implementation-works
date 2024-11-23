def sift_down(array, size, root, swaps, checks):
    largest = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2

    if left_child < size:
        checks += 1
        if array[left_child] > array[largest]:
            largest = left_child

    if right_child < size:
        checks += 1
        if array[right_child] > array[largest]:
            largest = right_child

    if largest != root:
        array[root], array[largest] = array[largest], array[root]
        swaps += 3
        swaps, checks = sift_down(array, size, largest, swaps, checks)

    return swaps, checks


def sort_with_heap(array):
    length = len(array)
    swaps = 0
    checks = 0

    for root in range(length // 2 - 1, -1, -1):
        swaps, checks = sift_down(array, length, root, swaps, checks)

    for end in range(length - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        swaps += 3
        swaps, checks = sift_down(array, end, 0, swaps, checks)

    return swaps, checks
