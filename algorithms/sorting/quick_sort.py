def quick_sort(array):
    """Quick sort.

    Time Complexity:    O(n*log n)
    Space Complexity:   O(1)
    """
    low, high = 0, len(array) - 1

    def quick_sort_(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quick_sort_(array, low, pi - 1)
            quick_sort_(array, pi + 1, high)

    quick_sort_(array, low, high)

    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1
