

def linear_search(element, array):
    """TODO: To search a given element in arr[]

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for idx in range(len(array)):
        current = array[idx]
        if current == element:
            return idx
    return -1
