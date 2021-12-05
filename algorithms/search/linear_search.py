

def linear_search(array, element):
    """To search a given element in array[]

    Time Complexity:    O(n)
    Space Complexity:   O(1)
    """
    for idx, el in enumerate(array):
        if el == element:
            return idx
    return -1
