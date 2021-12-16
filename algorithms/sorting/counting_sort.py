def counting_sort(array):
    """Counting sort.

    Time Complexity:    O(n + k)
    Space Complexity:   O(n + k)
    """
    max_value = max(array)
    counts = [0] * max_value + 1

    for item in array:
        counts[item] += 1

    idx = 0
    for item in range(max_value):
        for _ in range(counts[item]):
            array[idx] = item
            idx += 1

    return array