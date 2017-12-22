"""Given a function f and a value y, which are related according to
f(x) = y, find the function f' that given y, returns x and return x.

Also, it can be assumed that for every x and y, the following will
always be true:
    if x0 <= x1, then f(x0) <= f(x1), for every x > 0.

    Examples:
        inputs: f = x^2, y = 9
        return: 3

        inputs: f = x + 1, y = 10
        return: 9
"""


def inverse(fn):
    def compute_x(y):
        start = 0
        end = y
        middle = (end + start) // 2
        approximation = fn(middle)
        while approximation != y:
            if approximation < y:
                start = middle
            else:
                end = middle
            middle = (end + start) // 2
            approximation = fn(middle)
        return middle
    return compute_x


if __name__ == "__main__":
    test_cases = [
        (
            lambda x: x**2,
            [9, 100, 81],
            [3, 10, 9]
        ),
        (
            lambda x: x + 1,
            [10, 4000],
            [9, 3999]
        ),
        (
            lambda x: x * 2,
            [12, 20, 50000],
            [6, 10, 25000]
        )
    ]

    for test_n, (input_function, ys, xs) in enumerate(test_cases, start=1):
        print("Test case #", test_n, ", function ", input_function.__name__)
        result = []
        for y in ys:
            print("\t\tTesting y =", y)
            inverse_fn = inverse(input_function)
            result.append(inverse_fn(y))
        assert result == xs
