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


def inverse(fn, target):
    start = 0
    end = target
    middle = (end + start) // 2
    approximation = fn(middle)
    while approximation != target:
        if approximation < target:
            start = middle
        else:
            end = middle
        middle = (end + start) // 2
        approximation = fn(middle)
    return middle


if __name__ == "__main__":
    test_cases = [
        (
            lambda x: x**2,
            9,
            3
        ),
        (
            lambda x: x + 1,
            10,
            9
        ),
        (
            lambda x: x * 2,
            12,
            6
        )
    ]

    for input_function, input_y, expected_result in test_cases:
        result = inverse(input_function, input_y)
        print("# ->", input_function, input_y, expected_result, result)
        assert result == expected_result
