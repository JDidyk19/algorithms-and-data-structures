def binary_search_iterative(array, element):
    """Binary Search (Iterative).

    Time Complexity:    O(log(n))
    Space Complexity:   O(1)
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            left = mid + 1
        elif array[mid] > element:
            right = mid - 1
    return -1


def binary_search_recursive(array, element):
    """Binary Search (Recursive).

    Time Complexity:    O(log(n))
    Space Complexity:   O(log(n))
    """
    def binary_search_recursive_(array, element, left, right):
        if left <= right:
            mid = (left + right) // 2
            if array[mid] == element:
                return mid
            elif array[mid] < element:
                return binary_search_recursive_(array, element, mid + 1, right)
            elif array[mid] > element:
                return binary_search_recursive_(array, element, left, mid - 1)
        return -1

    return binary_search_recursive_(array, element, 0, len(array) - 1)
