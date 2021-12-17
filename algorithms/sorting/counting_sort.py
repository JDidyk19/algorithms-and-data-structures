def counting_sort(array, max_value=None):
    """Counting sort.

    Time Complexity:    O(n + k)
    Space Complexity:   O(n + k)
    """
    if not array:
        return []

    if max_value is None:
        max_value = max(array) + 1

    counts = [0] * max_value

    for item in array:
        counts[item] += 1

    idx = 0
    for item in range(max_value):
        for _ in range(counts[item]):
            array[idx] = item
            idx += 1

    return array
