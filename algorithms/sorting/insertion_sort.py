def insertion_sort(array):
    """Insertion sort.

    Time Complexity:    O(n^2)
    Space Complexity:   O(1)
    """
    for i in range(1, len(array)):
        cur = array[i]
        j = i - 1
        while cur < array[j] and j >= 0:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = cur

    return array
