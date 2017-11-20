"""You are given two non-empty lists representing two non-negative integers.
The digits are stored in reverse order and each of their buckets contain a single
digit. Add the two numbers and return it as a list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: [2, 4, 3] + [5, 6, 4]
Output: [7, 0, 8]
"""


def list_to_int(l):
    n = p = 0
    for digit in l:
        n += digit * (10 ** p)
        p += 1
    return n


def int_to_list(n):
    if n < 10:
        return [n]
    int_list = []
    while n > 0:
        int_list.append(n % 10)
        n //= 10
    return int_list


def add_two_numbers(l1, l2):
    if not l1 or not l2:
        raise Exception("you must provide to list of integers")
    return int_to_list(list_to_int(l1) + list_to_int(l2))


if __name__ == "__main__":
    test_cases = [
        ([1], [2], [3]),
        ([0, 0, 1], [2], [2, 0, 1]),
        ([0, 0, 1], [0, 2], [0, 2, 1]),
        ([0], [0], [0]),
        ([1], [0], [1]),
        ([2, 1], [0], [2, 1]),
    ]

    for number1, number2, expected_result in test_cases:
        result = add_two_numbers(number1, number2)
        assert result == expected_result
