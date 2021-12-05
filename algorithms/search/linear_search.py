def linear_search(array, element):
    """Linear Search.

    Time Complexity:    O(n)
    Space Complexity:   O(1)
    """
    for idx, el in enumerate(array):
        if el == element:
            return idx
    return -1
