import random


def is_sorted(array):
    for idx in range(len(array) - 1):
        if array[idx] > array[idx + 1]:
            return False
    return True


def bogosort(array):
    """Bogosort.

    Time Complexity:    O((n-1)*n!)
    Space Complexity:   O(1)
    """
    while not is_sorted(array):
        random.shuffle(array)

    return array
