"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output:  321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:
    Assume we are dealing with an environment which could only hold integers within the 32-bit
    signed integer range. For the purpose of this problem, assume that your function returns 0
    when the reversed integer overflows.
"""


def reverse(x):
    is_negative = x < 0
    if is_negative:
        x *= -1
    digits = []
    while x != 0:
        digit = x % 10
        x //= 10
        if digit == 0 and len(digits) == 0:
            continue
        digits.append(digit)

    res = 0
    n = len(digits) - 1
    for d in digits:
        res += (d * (10 ** n))
        n -= 1
    return res if not is_negative else res * -1


if __name__ == "__main__":
    test_cases = [
        (120, 21),
        (123, 321),
        (4001, 1004),
        (-20, -2)
    ]

    for input_number, expected_result in test_cases:
        assert expected_result == reverse(input_number)
