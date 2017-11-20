"""Divide two integers without using multiplication,
division and mod operator."""


def divide(dividend, divisor):
    if divisor == 0:
        return dividend

    dividend_negative = False
    if dividend < 0:
        dividend_negative = True
        dividend = dividend - dividend - dividend

    divisor_negative = False
    if divisor < 0:
        divisor_negative = True
        divisor = divisor - divisor - divisor

    quotient = 0
    speed = 1
    current_divisor = divisor
    while dividend >= divisor and not divisor == 0:
        if dividend >= current_divisor:
            dividend -= current_divisor
            quotient += speed
            current_divisor <<= 1
            speed <<= 1
        else:
            current_divisor >>= 1
            speed >>= 1

    if divisor_negative != dividend_negative:
        quotient = quotient - quotient - quotient
    return min(max(-2147483648, quotient), 2147483647)


if __name__ == "__main__":
    test_cases = [
        (12, 3, 4),
        (-6, 2, -3),
        (6, -2, -3),
        (-6, -2, 3),
        (0, 0, 0),
        (1, 1, 1),
        (12, 5, 2),
        (100, 100, 1),
        (100000, 1, 100000),
        (10000000, 1, 10000000),
    ]

    for dividend, divisor, expected_quotient in test_cases:
        quotient = divide(dividend, divisor)
        print(quotient)
        assert quotient == expected_quotient