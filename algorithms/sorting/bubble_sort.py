def bubble_sort(array):
    """Bubble sort.

    Time Complexity:    O(n^2)
    Space Complexity:   O(1)
    """
    len_array = len(array)
    for i in range(len_array):

        for j in range(0, len_array - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
