"""Write methods to implement the multiply, subtract, and divide operations
for integer. Use only the add operator."""


def negate(a):
    one = 1 if a < 0 else -1
    res = 0
    while a != 0:
        a += one
        res += one
    return res


def subtract(a, b):
    return a + negate(b)


def multiply(a, b):
    res = 0
    pos_a = a if a >= 0 else negate(a)
    neg_b = b if b < 0 else negate(b)
    while neg_b != 0:
        res += pos_a
        neg_b += 1

    return res if (a > 0 and b > 0) or (a < 0 and b < 0) else negate(res)


def divide(a, b):
    if b == 0:
        raise Exception("you cannot divide", a, "by 0")

    pos_a = a if a >= 0 else negate(a)
    pos_b = b if b >= 0 else negate(b)
    neg_b = b if b < 0 else negate(b)
    res = 0
    while pos_a >= pos_b:
        res += 1
        pos_a += neg_b

    return res if (a > 0 and b > 0) or (a < 0 and b < 0) else negate(res)


if __name__ == "__main__":
    assert negate(-10) == 10
    assert negate(20) == -20
    assert negate(0) == 0

    test_cases = [
        (subtract, 20, 10, 10),
        (subtract, 2, 10, -8),
        (subtract, 2, 0, 2),
        (subtract, -2, 4, -6),
        (subtract, -2, -4, 2),
        (subtract, 2, -4, 6),
        (multiply, 10, 2, 20),
        (multiply, 10, -2, -20),
        (multiply, -10, 2, -20),
        (multiply, -10, -2, 20),
        (multiply, 10, 1, 10),
        (multiply, 10, 0, 0),
        (divide, 10, 1, 10),
        (divide, 5, 2, 2),
        (divide, 4, 2, 2),
        (divide, 4, 1, 4),
        (divide, 4, -2, -2),
        (divide, -4, 2, -2),
        (divide, -4, -2, 2),
    ]
    for operation, a, b, expected_result in test_cases:
        print("Running", operation.__name__, "on", a, "and", b, ".")
        assert operation(a, b) == expected_result