from insertion_sort import insertion_sort
from mergesort import merge_sort
from quick_sort import quick_sort
from heap_sort import sort_with_heap
import matplotlib.pyplot as plt
import random


def collect_sort_statistics(sorting_function, sizes):
    comparison_counts = []
    initialization_counts = []

    for n in sizes:
        data = [random.randint(1, 1000) for _ in range(n)]
        if sorting_function.__name__ in ["merge_sort", "quick_sort"]:
            comparisons, initializations = sorting_function(data)
        else:
            initializations, comparisons = sorting_function(data)

        comparison_counts.append(comparisons)
        initialization_counts.append(initializations)

    return comparison_counts, initialization_counts


def plot_sort_comparison(array_sizes, results, title, y_axis_label):
    plt.figure(figsize=(10, 6))
    for algorithm, values in results.items():
        plt.plot(array_sizes, values, marker='o', label=algorithm)
    plt.title(title)
    plt.xlabel("Array Size")
    plt.ylabel(y_axis_label)
    plt.legend()
    plt.grid(True)
    plt.show()


test_sizes = [10, 50, 100, 200, 500]

insertion_comparisons, _ = collect_sort_statistics(insertion_sort, test_sizes)
merge_comparisons, _ = collect_sort_statistics(merge_sort, test_sizes)
quick_comparisons, _ = collect_sort_statistics(quick_sort, test_sizes)
heap_comparisons, _ = collect_sort_statistics(sort_with_heap, test_sizes)

comparison_data = {
    "Insertion Sort": insertion_comparisons,
    "Merge Sort": merge_comparisons,
    "Quick Sort": quick_comparisons,
    "Heap Sort": heap_comparisons
}

plot_sort_comparison(test_sizes, comparison_data,
                     title="Sorting Algorithm Comparison: Number of Comparisons",
                     y_axis_label="Comparison Count")
