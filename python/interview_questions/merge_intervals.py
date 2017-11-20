"""Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Create a function called find_free_intervals that given a list of
intervals, returns the list of free intervals.

For example:
Given [[1, 2], [5, 6], [1, 3], [4, 10]]
return [[3, 4]]
"""

from heapq import heappop, heappush


def merge(intervals):
    # O(N * log(N)), where N = len(intervals)
    local_id = 0
    pq = []
    for interval in intervals:
        heappush(pq, (interval[0], interval[1], local_id, interval))
        local_id += 1

    res = []

    # O(N * log(N)), where N = len(intervals)
    while len(pq) > 1:
        start1, end1, local_id1, interval1 = heappop(pq)
        start2, end2, local_id2, interval2 = pq[0]

        overlap = start2 - end1
        if overlap <= 0:
            # Drop interval 2
            heappop(pq)
            # Add the merged interval
            heappush(pq, (
                start1,
                max(end1, end2),
                local_id,
                [start1, max(end1, end2)]
            ))
        else:
            res.append(interval1)

    while pq:
        _, _, _, interval = heappop(pq)
        res.append(interval)
    return res


def find_free_intervals(intervals):
    # O(N * log(N)), where N = len(intervals)
    merged_intervals = merge(intervals)

    # O(M), where M = len(merged_intervals)
    res = []
    for i in range(1, len(merged_intervals)):
        _, end1 = merged_intervals[i - 1]
        start2, _ = merged_intervals[i]
        res.append([end1, start2])
    return res


if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 2],
                [5, 6],
                [1, 3],
                [4, 10]
            ],
            [
                [1, 3],
                [4, 10]
            ]
        ),
        (
            [
                [2, 3],
                [4, 5],
                [6, 7],
                [8, 9],
                [1, 10]
            ],
            [
                [1, 10]
            ]
        ),
        (
            [
                [1, 4],
                [2, 3]
            ],
            [
                [1, 4]
            ]

        ),
        (
            [
                [1, 3],
                [8, 10],
                [2, 6],
                [15, 18]
            ],
            [
                [1, 6],
                [8, 10],
                [15, 18]
            ]
        ),
        (
            [
                [1, 10]
            ],
            [
                [1, 10]
            ]
        ),
        (
            [
                [2, 2],
                [2, 2],
                [2, 3]
            ],
            [
                [2, 3]
            ]
        ),
        (
            [
                [2, 2],
                [2, 2]
            ],
            [
                [2, 2]
            ]
        ),
        (
            [
                [2, 2],
                [2, 2],
                [2, 10],
                [9, 12],
                [11, 20],
                [21, 22]
            ],
            [
                [2, 20],
                [21, 22]
            ]
        )
    ]

    for test_intervals, expected_result in test_cases:
        result = merge(test_intervals)
        print(test_intervals, "->", result)
        assert expected_result == result

    assert find_free_intervals([[1, 3], [8, 10], [2, 6], [15, 18]]) == [[6, 8], [10, 15]]
    assert find_free_intervals([[1, 2], [5, 6], [1, 3], [4, 10]]) == [[3, 4]]
