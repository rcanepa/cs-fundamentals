"""Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
find the duplicate one.

Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once."""


def find_duplicate(numbers):
    """
    Time Complexity: O(N), where N = len(numbers)
    Space Complexity: O(1).
    """
    slow = numbers[0]
    fast = numbers[numbers[0]]

    while slow != fast:
        slow = numbers[slow]
        fast = numbers[numbers[fast]]

    fast = 0
    while slow != fast:
        slow = numbers[slow]
        fast = numbers[fast]

    return slow


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3, 1, 4], 1),
        ([2, 1, 3, 1], 1),
        ([2, 2, 3, 1], 2),
        ([1, 2, 1], 1),
        ([1, 1], 1)
    ]

    for test_numbers, expected_result in test_cases:
        result = find_duplicate(test_numbers)
        print(test_numbers, result)
        assert result == expected_result
