"""Find the K most repeated values from an array A. In case of a tie,
return the smallest value of the tied group.

Examples:
    A = [3, 3, 1], K = 1
    Result = [3]

    A = [3, 3, 1, 2, 2, 2], K = 1
    Result = [2]

    A = [3, 3, 1, 2, 2, 2], K = 2
    Result = [2, 3]
"""

from collections import defaultdict
from heapq import heappush, heappop


def find_k_values(a, k):
    # Steps:
    # 1. create frequencies dictionary ~ O(N), where N = len(a)
    # 2. with the frequencies dictionary, load a priority queue, in which
    #    the most frequent value is on the top ~ O(M * log(M)), where M = unique elements of a
    # 3. pop K elements from the priority queue ~ O(K * log(M))
    frequencies = defaultdict(int)

    # TC: O(N), where N = len(a)
    for value in a:
        frequencies[value] += 1

    pq = []
    # TC: O(M * log(M)), where M = len(frequencies.keys()) <==> unique values of a
    for value, frequency in frequencies.items():
        heappush(pq, (frequency * -1, value))

    res = []
    # TC: O(K * log(M))
    while pq and k > 0:
        _, value = heappop(pq)
        res.append(value)
        k -= 1

    return res


if __name__ == "__main__":
    test_cases = [
        ([3], 1, [3]),
        ([3], 2, [3]),
        ([3, 3, 1], 1, [3]),
        ([3, 3, 1, 2, 2, 2], 1, [2]),
        ([3, 3, 1, 2, 2, 2], 2, [2, 3]),
        ([3, 3, 1, 2, 2, 2], 3, [2, 3, 1]),
        ([4, 2, 1, 1, 3, 2, 1, 1], 3, [1, 2, 3]),
        ([4, 2, 1, 1, 3, 2, 1, 1, 5], 3, [1, 2, 3]),
        ([4, 2, 1, 1, 3, 2, 1, 5, 1, 5], 3, [1, 2, 5]),
        ([4, -4, -4, 2, 1, 1, 3, 2, 1, 5, 1, 5, -1], 3, [1, 2, -4]),
        ([1, 2, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5, 6]),
        (range(100), 100, range(100))
    ]

    for array, k, expected_result in test_cases:
        print("a =", array, "k =", k)
        result = find_k_values(array, k)
        assert set(result) == set(expected_result)
