def selection_sort(array):
    """Selection sort.

    Time Complexity:    O(n^2)
    Space Complexity:   O(1)
    """
    for i in range(0, len(array)):
        index_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_min]:
                index_min = j
        array[i], array[index_min] = array[index_min], array[i]

    return array
