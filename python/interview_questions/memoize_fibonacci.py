"""Implement an algorithm that computes a
Fibonacci number using memoization."""


def fibonacci(n):
    memo = {}

    def _fibonacci(m):
        if m < 2:
            return m
        elif m in memo:
            return memo[m]
        else:
            memo[m] = _fibonacci(m - 1) + _fibonacci(m - 2)
            return memo[m]

    return _fibonacci(n)


if __name__ == "__main__":
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ]

    for nth, expected in test_cases[-1:]:
        assert fibonacci(nth) == expected
        print("Fibonacci number 200 is", fibonacci(200))
