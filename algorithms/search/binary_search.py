
# Iterative Binary Search Function
def binary_search_iterative(element, array):
    """TODO: Iterative search a given element in array[]

    Time Complexity: O(log(n))
    Space Complexity: O(1)
    """
    left = 0
    right = len(array) - 1

    while left < right:
        mid = (left + right) // 2
        current = array[mid]
        if current == element:
            return mid

        elif current < element:
            left = mid + 1

        elif current > element:
            right = mid - 1
    return -1


# Recursive Binary Search Function
def binary_search_recursive(element, array, left, right):
    """TODO: Recursive search a given element in array[]

        Time Complexity: O(log(n))
        Space Complexity: O(log(n))
        """
    mid = (left + right) // 2
    current = array[mid]
    if left <= right:
        if current == element:
            return mid

        elif current < element:
            return binary_search_recursive(element, array, mid + 1, right)

        elif current > element:
            return binary_search_recursive(element, array, left, mid - 1)
    return -1
